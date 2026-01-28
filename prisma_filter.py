"""
PRISMA 2020 기반 문헌 병합, 필터링 및 분류 스크립트
주제: Intelligent Process Control in 3D Concrete Printing: From Extrusion to Finishing
"""

import pandas as pd
import re
import unicodedata

# ===== 1. 데이터 로드 및 병합 =====
print("=" * 60)
print("1. 데이터 로드 및 병합")
print("=" * 60)

# CSV 파일 로드
files = {
    'group A.csv': 'Control focus',
    'group B.csv': 'Finishing focus', 
    'group C.csv': 'Path planning focus'
}

dfs = []
for filename, description in files.items():
    try:
        df = pd.read_csv(filename, encoding='utf-8')
        df['Source_File'] = filename
        dfs.append(df)
        print(f"  - {filename} ({description}): {len(df)} 논문 로드")
    except Exception as e:
        print(f"  - {filename} 로드 실패: {e}")

# 데이터 병합
df_merged = pd.concat(dfs, ignore_index=True)
print(f"\n전체 병합된 논문 수: {len(df_merged)}")

# ===== 2. PRISMA 스크리닝 (필터링) =====
print("\n" + "=" * 60)
print("2. PRISMA 스크리닝 (필터링)")
print("=" * 60)

# 2.1 연도 필터링 (2020-2026)
df_filtered = df_merged.copy()

# Year 열을 숫자로 변환 (비어있거나 변환 불가능한 값 처리)
df_filtered['Year'] = pd.to_numeric(df_filtered['Year'], errors='coerce')

# 연도 필터링 전 개수
before_year = len(df_filtered)
df_filtered = df_filtered[(df_filtered['Year'] >= 2020) & (df_filtered['Year'] <= 2026)]
print(f"  - 연도 필터링 (2020-2026): {before_year} → {len(df_filtered)} (-{before_year - len(df_filtered)})")

# 2.2 비영어 제목 제거
def is_non_english(text):
    """비영어 문자(한국어, 중국어, 키릴 문자 등) 포함 여부 확인"""
    if pd.isna(text):
        return False
    
    for char in str(text):
        # ASCII가 아닌 문자의 카테고리 확인
        cat = unicodedata.category(char)
        name = unicodedata.name(char, '')
        
        # CJK (중국어, 일본어, 한국어) 또는 키릴 문자 확인
        if 'CJK' in name or 'HANGUL' in name or 'CYRILLIC' in name or 'ARABIC' in name:
            return True
    return False

before_lang = len(df_filtered)
df_filtered = df_filtered[~df_filtered['Title'].apply(is_non_english)]
print(f"  - 비영어 제목 제거: {before_lang} → {len(df_filtered)} (-{before_lang - len(df_filtered)})")

# 2.3 비논문 항목 제거 (Proceedings, Conference, Lecture Notes, Book, Vol.)
exclude_patterns = [
    r'^Proceedings of',
    r'^Conference on',
    r'^Lecture Notes in',
    r'^Book',
    r'^Vol\.',
]

def is_excluded_type(title):
    """제외 대상 항목 확인"""
    if pd.isna(title):
        return False
    title_str = str(title).strip()
    for pattern in exclude_patterns:
        if re.match(pattern, title_str, re.IGNORECASE):
            return True
    return False

before_type = len(df_filtered)
df_filtered = df_filtered[~df_filtered['Title'].apply(is_excluded_type)]
print(f"  - 비논문 항목 제거: {before_type} → {len(df_filtered)} (-{before_type - len(df_filtered)})")

# 2.4 중복 제거 (Title 기준, 대소문자 무시)
df_filtered['Title_lower'] = df_filtered['Title'].str.lower().str.strip()
before_dup = len(df_filtered)
df_filtered = df_filtered.drop_duplicates(subset='Title_lower', keep='first')
df_filtered = df_filtered.drop(columns=['Title_lower'])
print(f"  - 중복 제거: {before_dup} → {len(df_filtered)} (-{before_dup - len(df_filtered)})")

print(f"\n필터링 후 최종 논문 수: {len(df_filtered)}")

# ===== 3. 분류 (섹션 할당) =====
print("\n" + "=" * 60)
print("3. 섹션 분류 (키워드 기반)")
print("=" * 60)

# 섹션별 키워드 정의 (우선순위 순서: 5.2 > 5.1 > 4.2 > 4.1 > 3 > 2.2 > 2.1)
sections = {
    '5.2': {
        'name': 'Finishing',
        'keywords': ['finishing', 'troweling', 'grinding', 'surface treatment', 
                     'shotcrete', 'spraying', 'post-processing', 'smoothing']
    },
    '5.1': {
        'name': 'Feedback Control',
        'keywords': ['closed-loop', 'feedback', 'real-time control', 'adaptive control',
                     'pid', 'flow rate control', 'pressure control']
    },
    '4.2': {
        'name': 'Path Planning',
        'keywords': ['path planning', 'slicing', 'toolpath', 'trajectory', 
                     'coverage', 'optimization', 'non-planar', 'collision', 'g-code']
    },
    '4.1': {
        'name': 'Diagnosis (AI)',
        'keywords': ['defect detection', 'classification', 'deep learning', 
                     'neural network', 'cnn', 'diagnosis', 'prediction', 'machine learning']
    },
    '3': {
        'name': 'Sensing',
        'keywords': ['vision', 'camera', 'lidar', 'monitoring', 'sensing', 
                     'sensor', 'image processing', 'digital twin', 'scanner', 'ultrasonic']
    },
    '2.2': {
        'name': 'Parameters',
        'keywords': ['rheology', 'yield stress', 'viscosity', 'printability', 
                     'process parameter', 'layer height', 'flow rate', 'bond strength']
    },
    '2.1': {
        'name': 'Hardware',
        'keywords': ['cable robot', 'cable-driven', 'parallel robot', 'kinematics',
                     'manipulator', 'mobile robot', 'gantry', 'robot arm', 'wall-climbing']
    }
}

# 우선순위 순서대로 섹션 리스트
priority_order = ['5.2', '5.1', '4.2', '4.1', '3', '2.2', '2.1']

def classify_paper(row):
    """논문을 섹션으로 분류 (Title과 Abstract 기준)"""
    title = str(row['Title']).lower() if pd.notna(row['Title']) else ''
    abstract = str(row['Abstract']).lower() if pd.notna(row['Abstract']) else ''
    text = title + ' ' + abstract
    
    # 우선순위 순서대로 확인
    for section_id in priority_order:
        section_info = sections[section_id]
        for keyword in section_info['keywords']:
            if keyword.lower() in text:
                return section_id
    
    return 'Unclassified'

df_filtered['Section'] = df_filtered.apply(classify_paper, axis=1)

# 분류 결과 출력
print("\n섹션별 논문 수:")
section_counts = df_filtered['Section'].value_counts()
for section_id in priority_order + ['Unclassified']:
    if section_id in section_counts.index:
        section_name = sections.get(section_id, {}).get('name', 'Manual Review Needed')
        print(f"  - {section_id} ({section_name}): {section_counts[section_id]}")

# ===== 4. 출력 =====
print("\n" + "=" * 60)
print("4. 결과 저장")
print("=" * 60)

# 필요한 열만 선택
output_columns = ['Section', 'Title', 'Authors', 'Year', 'Cites', 'Source_File']

# 데이터 정리
df_output = df_filtered[output_columns].copy()

# Year를 정수로 변환
df_output['Year'] = df_output['Year'].astype(int)

# Cites를 정수로 변환 (NaN은 0으로)
df_output['Cites'] = pd.to_numeric(df_output['Cites'], errors='coerce').fillna(0).astype(int)

# 정렬: Section (2.1 -> 5.2), Cites (내림차순)
section_order = {'2.1': 1, '2.2': 2, '3': 3, '4.1': 4, '4.2': 5, '5.1': 6, '5.2': 7, 'Unclassified': 8}
df_output['Section_order'] = df_output['Section'].map(section_order)
df_output = df_output.sort_values(by=['Section_order', 'Cites'], ascending=[True, False])
df_output = df_output.drop(columns=['Section_order'])

# CSV 저장
output_file = 'Final_Selected_Papers.csv'
df_output.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"\n결과 파일 저장 완료: {output_file}")
print(f"최종 선정된 논문 수: {len(df_output)}")

# 상위 10개 논문 미리보기
print("\n" + "=" * 60)
print("상위 10개 논문 미리보기:")
print("=" * 60)
pd.set_option('display.max_colwidth', 60)
print(df_output.head(10).to_string(index=False))

# 통계 요약
print("\n" + "=" * 60)
print("통계 요약")
print("=" * 60)
print(f"  - 원본 논문 수: {len(df_merged)}")
print(f"  - 필터링 후 논문 수: {len(df_output)}")
print(f"  - 제거된 논문 수: {len(df_merged) - len(df_output)}")
print(f"\n섹션별 분포:")
for section_id in ['2.1', '2.2', '3', '4.1', '4.2', '5.1', '5.2', 'Unclassified']:
    count = len(df_output[df_output['Section'] == section_id])
    if count > 0:
        section_name = sections.get(section_id, {}).get('name', 'Manual Review')
        print(f"    {section_id} ({section_name}): {count}개")
