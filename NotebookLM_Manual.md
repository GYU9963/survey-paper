# NotebookLM을 활용한 서베이 논문 작성 매뉴얼

**Last Updated:** 2026-01-29
**Version:** 2.1
**Total Papers:** 88편 (2020-2026)

---

## **논문 정보**

| 항목 | 내용 |
|------|------|
| **제목 (영문)** | Intelligent Robotic 3D Concrete Printing: From Computational Design to Process Control |
| **제목 (한글)** | 지능형 로봇 3D 콘크리트 프린팅: 계산적 설계에서 공정 제어까지 |
| **핵심 키워드** | Robotic 3DCP, Computational Design, Path Planning, AI Diagnosis, Process Control, Shotcrete |
| **차별점** | 기존 서베이와 달리 "설계 → 진단 → 제어" 전체 파이프라인을 통합적으로 다룸 |
| **관련 분석** | [Related_Surveys_Analysis.md](./Related_Surveys_Analysis.md) 참조 |

---

## **Step 0. 사전 준비: '설계도' 파일 만들기 (필수)**

AI가 방향을 잃지 않게 하려면 '지시서(Blueprint)'가 필요합니다.

- **필수 파일:**
    1. `Master_Structure_Plan.txt` - 전체 논문 구조 및 섹션별 가이드
    2. `Paper_Placement_Plan_Final.csv` - 논문 배치 현황

- **포함 내용:**
    1. **논문 제목:** Intelligent Process Control in 3DCP...
    2. **전체 목차:** (확정된 1장~6장 상세 목차)
    3. **섹션별 핵심 목표:** (예: "4장은 Design→Diagnosis 흐름을 따라야 함")
    4. **작성 톤앤매너:** (예: "학술적이고 객관적인 어조, 수동태 사용, 비판적 분석 포함")

---

## **현재 확정 목차 (2026-01-29 기준)**

```
1. Introduction & Background (10 papers)
   └── 1.1 Overview of 3D Concrete Printing
       └── 1.1.1 3DCP Overview & Trends: 10

2. Robotic Platforms and Material Characterization (17 papers)
   ├── 2.1 Hardware Systems & Kinematics (11 papers)
   │   ├── 2.1.1 Cable-Driven & Parallel Robots: 2
   │   ├── 2.1.2 Mobile & Autonomous Robots: 5
   │   └── 2.1.3 Manipulators & Kinematics: 4
   └── 2.2 Process Parameters & Rheology (6 papers)
       ├── 2.2.1 Rheology & Flow Properties: 5
       └── 2.2.2 Printability & Buildability: 1

3. Sensing and Digital Integration (6 papers)
   └── 3.1 Sensing & Monitoring Systems (6 papers)
       ├── 3.1.1 Vision & Camera Systems: 2
       └── 3.1.2 Digital Twin & Virtual Monitoring: 4

4. Computational Intelligence: From Design to Diagnosis (28 papers)
   ├── 4.1 Intelligent Path Planning & Slicing (19 papers)  ← [설계/계획]
   │   ├── 4.1.1 Toolpath Generation & G-code: 10
   │   ├── 4.1.2 Non-planar & 3D Toolpaths: 1
   │   ├── 4.1.3 Trajectory Optimization: 2
   │   └── 4.1.4 Geometric & Structural Design: 6
   └── 4.2 AI-based Defect Diagnosis (9 papers)  ← [진단/모니터링]
       ├── 4.2.1 Deep Learning & Neural Networks: 1
       ├── 4.2.2 Machine Learning Methods: 5
       ├── 4.2.3 Defect Detection & Classification: 1
       └── 4.2.4 Predictive Modeling & Diagnosis: 2

5. Process Optimization and Advanced Fabrication Techniques (27 papers)
   ├── 5.1 Real-time Feedback Control (8 papers)
   │   ├── 5.1.1 Closed-loop Process Control: 2
   │   ├── 5.1.2 Extrusion & Flow Control: 2
   │   ├── 5.1.3 Real-time Adaptation & Compensation: 1
   │   └── 5.1.4 Quality Assurance & Inline Inspection: 3
   └── 5.2 Shotcrete 3D Printing & Process Optimization (19 papers)
       ├── 5.2.1 Shotcrete 3D Printing (SC3DP): 9
       ├── 5.2.2 Surface Finishing & Troweling: 5
       └── 5.2.3 Hybrid Manufacturing & Integration: 5

6. Conclusion
   └── 6.1 Summary & Future Directions
```

---

## **현재 확정 목차 (한글)**

```
1. 서론 및 배경 (10편)
   └── 1.1 3D 콘크리트 프린팅 개요
       └── 1.1.1 3DCP 개요 및 동향: 10편

2. 로봇 플랫폼 및 재료 특성화 (17편)
   ├── 2.1 하드웨어 시스템 및 기구학 (11편)
   │   ├── 2.1.1 케이블 구동 및 병렬 로봇: 2편
   │   ├── 2.1.2 이동형 및 자율 로봇: 5편
   │   └── 2.1.3 매니퓰레이터 및 기구학: 4편
   └── 2.2 공정 파라미터 및 레올로지 (6편)
       ├── 2.2.1 레올로지 및 유동 특성: 5편
       └── 2.2.2 프린터빌리티 및 빌더빌리티: 1편

3. 센싱 및 디지털 통합 (6편)
   └── 3.1 센싱 및 모니터링 시스템 (6편)
       ├── 3.1.1 비전 및 카메라 시스템: 2편
       └── 3.1.2 디지털 트윈 및 가상 모니터링: 4편

4. 계산 지능: 설계에서 진단까지 (28편)
   ├── 4.1 지능형 경로 계획 및 슬라이싱 (19편)  ← [설계/계획 단계]
   │   ├── 4.1.1 툴패스 생성 및 G-code: 10편
   │   ├── 4.1.2 비평면 및 3D 툴패스: 1편
   │   ├── 4.1.3 궤적 최적화: 2편
   │   └── 4.1.4 기하학적 및 구조적 설계: 6편
   └── 4.2 AI 기반 결함 진단 (9편)  ← [진단/모니터링 단계]
       ├── 4.2.1 딥러닝 및 신경망: 1편
       ├── 4.2.2 머신러닝 기법: 5편
       ├── 4.2.3 결함 탐지 및 분류: 1편
       └── 4.2.4 예측 모델링 및 진단: 2편

5. 공정 최적화 및 고급 제조 기술 (27편)
   ├── 5.1 실시간 피드백 제어 (8편)
   │   ├── 5.1.1 폐루프 공정 제어: 2편
   │   ├── 5.1.2 압출 및 유량 제어: 2편
   │   ├── 5.1.3 실시간 적응 및 보정: 1편
   │   └── 5.1.4 품질 보증 및 인라인 검사: 3편
   └── 5.2 숏크리트 3D 프린팅 및 공정 최적화 (19편)
       ├── 5.2.1 숏크리트 3D 프린팅 (SC3DP): 9편
       ├── 5.2.2 표면 마감 및 트로웰링: 5편
       └── 5.2.3 하이브리드 제조 및 통합: 5편

6. 결론
   └── 6.1 요약 및 향후 연구 방향
```

### 논문 수 요약

| 섹션 | 주제 | 논문 수 |
|------|------|---------|
| 1장 | 서론 및 배경 | 10편 |
| 2장 | 로봇 플랫폼 및 재료 특성화 | 17편 |
| 3장 | 센싱 및 디지털 통합 | 6편 |
| 4장 | 계산 지능: 설계에서 진단까지 | 28편 |
| 5장 | 공정 최적화 및 고급 제조 기술 | 27편 |
| **총계** | | **88편** |

---

## **Step 1. NotebookLM 환경 구축**

- **전략:** 하나의 거대한 노트북이 아니라, **"서브-서브섹션별 개별 노트북"** 전략을 사용합니다.
- **행동:**
    1. NotebookLM 메인 화면에서 **'새 노트북'** 클릭.
    2. 제목을 **`4.1.1 Toolpath Generation`** 처럼 섹션 번호와 이름으로 설정.
    3. **업로드:** `Master_Structure_Plan.txt` (필수) + 해당 섹션용 논문들만 업로드.
    4. 영어 프롬프트 사용 권장.
    5. 모든 sub-sub section에 대해 Step 2 완료 후 Step 3 진행 권장.

---

## **Step 1.5. 논문 사전 요약 (Pre-Analysis) [NEW]**

> 💡 **목적:** 각 논문이 무엇을 다루는지 빠르게 파악하여 배치 오류를 조기에 발견합니다.

- **프롬프트:**

```markdown
[Role]
You are a research assistant.

[Task]
For each uploaded paper, provide a 2-sentence summary:
1. What is the main contribution/focus of this paper?
2. What specific technology or method does it present?

[Output Format]
| Paper Title | Main Focus | Key Technology |
|-------------|------------|----------------|
| ... | ... | ... |

Please respond in **Korean**.
```

- **활용:** 이 요약을 보고 명백히 다른 섹션에 속해야 할 논문을 조기에 발견합니다.

---

## **Step 2. 논문 적합성 검증 (Relevance Check)**

- **검증용 프롬프트:**

```markdown
[Role]
You are a strict academic reviewer.

[Task]
Evaluate if the uploaded source papers are suitable for writing **"[Section Number & Title]"** of our survey paper.

[Criteria]
1. Check if each paper focuses on **[Insert Step 2 Keyword from Table]**.
2. If a paper is irrelevant, mark it as "Recommended for Exclusion" and explain why.
3. Summarize in one sentence how each paper contributes to **"[Section Number]"**.

[Cross-Section Check] ← [NEW]
4. If any paper seems MORE suitable for another section, suggest the alternative placement.
   (Refer to the Master_Structure_Plan for section definitions)

[Output Format]
Please respond in **Korean**.
```

---

## **Step 3. 구조 제안 받기 (Structure Proposal) [NEW]**

> 💡 **목적:** 바로 초안을 쓰기 전에, 논문들을 어떤 순서와 구조로 배열할지 AI의 제안을 받습니다.

- **프롬프트:**

```markdown
[Context]
We are about to write **"[Section Number & Title]"** using the uploaded papers.

[Task]
Before drafting, propose an outline for this subsection:
1. Suggest a logical order to discuss the papers.
2. Group papers into 2-3 themes if applicable.
3. Identify which paper should be the "anchor" (most important/cited).

[Output Format]
- **Theme 1:** [Description] → Papers: [list]
- **Theme 2:** [Description] → Papers: [list]
- **Anchor Paper:** [Name] - Reason: [why it's central]

Please respond in **Korean**.
```

---

## **Step 4. 섹션별 초안 작성 (Drafting)**

### 4.1 카테고리별 초안 작성 구조

각 sub-sub-section은 다음 **5단계 구조**를 따릅니다 (섹션 특성에 따라 강조점 조정):

#### **카테고리 A: 하드웨어/시스템 (2.1, 2.2)**
```
[1] 기술 기초 & 맥락 (Technical Foundation & Context)
   └─ 상위 섹션에서의 위치, 왜 이것이 중요한가?

[2] 시스템 분류 & 특성 (System Classification & Characteristics)
   └─ 주요 유형 분류 (3-4가지), 각각의 원리, 구체적 예시

[3] 성능 비교 분석 (Comparative Performance Analysis)
   └─ 정량적/정성적 성능 지표, 장단점 표, 적합 응용 추천

[4] 제약조건 & 고려사항 (Limitations & Considerations)
   └─ 근본적 제약, 트레이드오프, 미해결 과제

[5] 통합 및 다음 단계 (Integration & Next Steps)
   └─ 상위 섹션 기여도, 다음 섹션과의 연결고리
```

#### **카테고리 B: 센싱/모니터링 (3.1)**
```
[1] 모니터링 필요성 (Monitoring Necessity)
   └─ 3DCP에서 뭐가 감시되어야 하는가? 센싱 없이 놓치는 것?

[2] 센싱 기술 & 구현 (Sensing Technologies & Implementations)
   └─ 센서 유형, 원리, 공간해상도, 시간해상도, 데이터 스트림

[3] 데이터 처리 & 해석 (Data Processing & Interpretation)
   └─ 센서 데이터 → 의미있는 정보 변환, 영상처리 기법

[4] 현재 한계 & 도전 (Current Limitations & Challenges)
   └─ 악조건에서의 신뢰성, 계산 부하, 비용과 복잡성

[5] 다운스트림 시스템과의 통합 (Integration with Downstream)
   └─ 센싱 데이터의 흐름 (4.2 진단, 5.1 제어로 활용)
```

#### **카테고리 C: 설계/계획 (4.1)**
```
[1] 설계 문제 & 목표 (Design Problem & Objectives)
   └─ 해결할 문제 (경로 생성, 궤적 최적화), 제약조건, 목표

[2] 계산 방법 & 알고리즘 (Computational Methods & Algorithms)
   └─ 주요 알고리즘 분류, 원리, 처리 시간 vs 결과 품질 비교

[3] 최적화 & 개선 전략 (Optimization & Refinement Strategies)
   └─ 초기 해 생성 → 최적화 프로세스, 다중 목표 최적화

[4] 실제 응용 & 사례 연구 (Practical Applications & Case Studies)
   └─ 실제 프로젝트 적용 사례, 성과 지표, 상황별 최적 전략

[5] 설계 유연성 & 미래 전망 (Design Flexibility & Future Outlook)
   └─ 다양한 요구에 대한 확장성, 다음 섹션(진단, 제어)과의 피드백
```

#### **카테고리 D: 진단/분석 (4.2)**
```
[1] 진단 목표 & 결함 분류 (Diagnosis Objective & Defect Taxonomy)
   └─ 어떤 결함이 발생하나? 원인, 영향, 진단의 필요성

[2] ML/DL 접근법 (Machine Learning & Deep Learning Approaches)
   └─ 전통 ML vs 딥러닝, 알고리즘 원리, 입력 데이터 형식

[3] 분류 성능 & 지표 (Classification Performance & Metrics)
   └─ Accuracy, Precision, Recall, F1-score, 클래스 불균형 처리

[4] 필드 적용 & 배포 (Field Application & Deployment)
   └─ 실제 3DCP 공정 적용 사례, 전처리, 추론 시간, 대응 방안

[5] 신뢰성 & 견고성 (Reliability & Robustness)
   └─ 새로운 데이터에 대한 강건성, 거짓 양성 위험, 피드백 루프
```

#### **카테고리 E: 제어/최적화 (5.1, 5.2)**
```
[1] 제어 목표 & 프로세스 제약 (Control Objective & Constraints)
   └─ 제어할 대상 (압력, 속도, 온도), 동역학, 목표의 균형

[2] 피드백 아키텍처 & 센서 (Feedback Architecture & Sensors)
   └─ 폐루프 구조: 센서 → 제어기 → 액추에이터, 피드백 신호

[3] 제어 알고리즘 & 전략 (Control Algorithms & Strategies)
   └─ PID, MPC, 적응제어 등, 알고리즘 선택 기준

[4] 실험 결과 & 성능 (Experimental Results & Performance)
   └─ 시뮬레이션 vs 실제 구현, 정량적 개선 지표, 사례 결과

[5] 고급 기법 & 통합 (Advanced Techniques & Integration)
   └─ 특수 기술, 하이브리드 제조, 전체 시스템 폐루프 통합
```

### 4.2 교차 섹션 연결 (Inter-section Flow)

각 sub-sub-section 말미에 다음을 명시:

1. **상위 섹션 기여도**: "이 기술은 [부모 섹션]의 핵심을 이루며..."
2. **수평적 연관성**: "유사 접근법은 [다른 sub-sub-section]에서..."
3. **하위 섹션 영향**: "이 결과는 [다음 섹션]의 [특정 주제]에 직접 활용되며..."

### 4.3 작성용 프롬프트 템플릿

**[섹션 카테고리 구분 후 해당 구조 선택]**

```markdown
[Context]
We are writing a survey paper on "Intelligent Process Control in 3DCP".
We are currently drafting **"[Section Number & Title]"** (Category: [A/B/C/D/E]).

[Section Category & Structure]
Follow the **5-stage structure for Category [X]**:
  [1] [Stage Name] → [Specific Content for this section]
  [2] [Stage Name] → [Specific Content for this section]
  [3] [Stage Name] → [Specific Content for this section]
  [4] [Stage Name] → [Specific Content for this section]
  [5] [Stage Name] → [Specific Content for this section]

[Source & Synthesis]
Synthesize the uploaded papers to create a cohesive, high-quality academic draft.

[Requirements]
1. **Language:** Write the main draft in **Academic English**. (Do NOT use bold text).
2. **Structure:** Follow the 5-stage structure above strictly.
3. **Analysis:** Critically analyze pros/cons and link to 'Intelligent Process Control'.
4. **Citations:** Cite strictly as [Author, Year] at the end of sentences.
5. **No Self-Reference:** Do NOT mention 'Master_Structure_Plan' directly. Use natural transitions.
6. **Length:** About 1.5-2 pages (600-800 words).
7. **Flow:** Include at least one table/figure. End with Inter-section Connection.

[Inter-section Connection (Ending)]
In the final paragraph, explicitly state:
- How this subsection contributes to [Parent Section]
- How it relates to other subsections (horizontal)
- How it enables or informs [Next Section] (vertical)

[Special Request for Review]
After the English draft, add a **"Korean Summary for Review"** (about 100-150 words):
- Key technologies covered
- Main arguments and findings
- Why this structure/flow was chosen
```

### 4.4 작성 팁

| 항목 | 가이드 |
|------|--------|
| **일관된 용어** | 같은 개념을 다양하게 표현하지 말 것. 용어집 유지 |
| **시각적 요소** | 각 sub-sub-section에 최소 1개 이상 표/그림/플로우차트 |
| **논문 인용** | 해당 섹션 할당 논문 70-80% 인용, 관련 섹션 보조 인용 |
| **분량** | 각 sub-sub-section 1.5-2 페이지 (약 600-800 단어) |
| **결론 통일** | 각 sub-sub-section은 "이를 통해 [다음 수준의 지능형 제어]가 가능해진다"로 귀결 |
| **표 형식** | 기술 비교는 항상 표로 제시 (정량적 비교 용이) |
| **한글 요약** | 각 섹션의 핵심을 50-100단어로 정리 |

- **결과물 저장:** 답변을 복사해서, NotebookLM 우측의 '새 노트'에 붙여넣고 제목을 `Draft_Sec_4.1.1` 등으로 저장합니다.

---

## **Step 4.5. 인용 커버리지 체크 (Citation Coverage) [NEW]**

> 💡 **목적:** 모든 업로드된 논문이 초안에서 인용되었는지 확인합니다.

- **프롬프트:**

```markdown
[Task]
Compare the draft against the uploaded source papers.

[Check]
1. List all papers that were CITED in the draft.
2. List all papers that were NOT cited (if any).
3. For uncited papers, briefly explain why they might have been excluded or how they could be incorporated.

[Output Format]
**Cited Papers:** [list with citation count]
**Uncited Papers:** [list with suggestion]

Please respond in **Korean**.
```

---

## **Step 5. 내용 교차 검증 (Fact Check & Refinement)**

- **팩트 체크 프롬프트:**

```markdown
[Role]
You are a strict academic reviewer.

[Task]
Review the drafted text against the original source papers.
Check for any **"Hallucinations"** regarding:
1. Numerical data (percentages, measurements, experimental results)
2. Experimental conditions (materials, parameters, setup)
3. Specific claims or conclusions

[Action]
- If accurate, say "Pass".
- If there are errors, provide:
  - **Problematic Sentence:** [exact quote]
  - **Issue:** [what's wrong]
  - **Correction:** [suggested fix with source reference]

[Output Format]
Please respond in **Korean**.
```

---

## **Step 5.5. 오류 수정 및 재검증 (Correction Loop)**

- **상황:** Step 5에서 AI가 오류를 지적했을 경우 실행합니다.
- **행동:**
    1. AI가 제안한 수정 문장을 참고하여 초안을 수정합니다.
    2. 수정된 초안을 소스에 추가한 후 아래 프롬프트로 재검증합니다.

- **재검증 프롬프트:**

```markdown
[Context]
The selected note 'Draft_Sec_XXX' has been revised based on your previous feedback.

[Task]
Verify if the revised content now perfectly matches the facts in the source papers.
Specifically check if the previously flagged error has been corrected.

[Output Format]
Please respond in **Korean**.
```

---

## **Step 6. Overleaf 변환 및 통합 (Coding & Merging)**

- **변환용 프롬프트:**

```markdown
[Task]
Convert the drafted text into LaTeX code.

[Formatting Rules]
1. Use `\subsubsection{Title}` for headers.
2. Format citations as `\cite{FirstAuthor_Year}` (e.g., `\cite{Zhang_2023}`).
3. Use correct LaTeX syntax for math and units (e.g., `$50 \sim 200$ N`).
4. Keep the content in **English**.
5. Do NOT use bold or italic formatting in the body text.
```

- **Overleaf 작업:** 변환된 코드를 Overleaf의 메인 파일에 순서대로 붙여넣기 합니다.

---

## **Step 7. 전체 논리 흐름 검사 (Grand Final Check)**

> 🚨 **중요:** 개별 노트북들은 서로의 존재를 모릅니다. '합체(Merge)' 후 검사가 필수입니다.

### 7.1 검토용 통합 노트북 생성

1. Step 6까지 완료해서 Overleaf에 모든 섹션이 모이면, **PDF로 저장** (`Full_Draft.pdf`)
2. NotebookLM에서 **새 노트북** 생성 (`Final_Review`)
3. `Full_Draft.pdf` + `Master_Structure_Plan.txt` 업로드

### 7.2 전체 흐름 검사 프롬프트

```markdown
[Role]
You are a journal editor-in-chief.

[Task]
Read the uploaded `Full_Draft.pdf` covering the entire paper.
Evaluate the following points:

[Checklist]
1. **Logical Flow (Design → Diagnosis → Control):**
   - Does Section 4.1 (Path Planning) naturally lead to Section 4.2 (Defect Diagnosis)?
   - Is there a seamless connection between Section 3 (Sensing) and Section 5 (Control)?

2. **Redundancy Check:**
   - Are there repetitive definitions between Section 2 (Materials) and Section 4?
   - Is any concept explained twice unnecessarily?

3. **Consistency:**
   - Is the tone and writing style consistent across all sections?
   - Are citation formats uniform?

4. **Gap Analysis:** ← [NEW]
   - Are there important topics that SHOULD be covered but are missing?
   - Does any section feel incomplete or underdeveloped?

[Output Format]
Please provide the feedback in **Korean**, citing specific section numbers.
```

---

## **🚨 작성 시 주의사항 (Pro Tips)**

1. **인용 환각(Citation Hallucination) 주의:**
   - NotebookLM은 소스 내에 있는 것만 인용하지만, 가끔 *페이지 수*나 *구체적 수치*를 틀릴 때가 있습니다.
   - 중요 데이터는 반드시 원본 PDF를 열어 눈으로 확인하세요.

2. **섹션 간 중복 방지:**
   - 프롬프트에 **"앞서 섹션 X에서 [토픽]은 다루었으니, 여기서는 [다른 측면]에만 집중해"**라고 제약을 걸어주세요.
   - 예: "Section 3에서 센싱 하드웨어는 다루었으니, Section 4.2에서는 AI 알고리즘에만 집중해"

3. **Section 4 작성 시 주의:**
   - **4.1 (Path Planning)을 먼저** 작성 → "설계/계획" 단계
   - **4.2 (Defect Diagnosis)를 나중에** 작성 → "진단/모니터링" 단계
   - 이 순서가 "From Design to Diagnosis" 흐름을 만듭니다.

4. **마스터 파일 업데이트:**
   - 글을 쓰다가 구조가 바뀌면 `Master_Structure_Plan.txt`를 수정해서 **다시 업로드**하세요.

---

## **부록: 서브-서브섹션별 프롬프트 키워드 (Master Table)**

*(이 표를 보고, 각 섹션을 작업할 때 해당 내용을 복사해서 프롬프트에 붙여넣으세요.)*

### **Section 2: Robotic Platforms and Material Characterization**

| Section | Topic | Papers | Step 2 Keywords | Step 4 Writing Guide |
|---------|-------|--------|-----------------|---------------------|
| **2.1.1** | Cable-Driven & Parallel Robots | 4 | cable-driven parallel robots, CDPR, tension-based systems, large workspace, kinematics | Focus on the advantages of CDPRs for large-scale construction (workspace, weight) and their control challenges (tension, vibration). |
| **2.1.2** | Mobile & Autonomous Robots | 5 | mobile manipulator, swarm robotics, autonomous navigation, omnidirectional, aerial 3D printing | Discuss the unlimited workspace advantage of mobile/swarm robots and the coordination challenges in multi-robot systems. |
| **2.1.3** | Manipulators & Kinematics | 4 | 6-axis robot arm, industrial manipulator, gantry system, kinematics, redundancy resolution | Explain the precision and versatility of 6-axis arms vs. the stability of gantry systems, focusing on kinematic optimization. |
| **2.2.1** | Rheology & Flow Properties | 5 | rheology, yield stress, viscosity, thixotropy, flow behavior, pumpability | Define key rheological parameters (yield stress, viscosity) and explain how they influence the pumping and extrusion process. |
| **2.2.2** | Printability & Buildability | 3 | printability, buildability, shape retention, deformation, structural stability, slump | Analyze the trade-off between pumpability and buildability, and how material stiffness affects layer stability. |

### **Section 3: Sensing and Digital Integration**

| Section | Topic | Papers | Step 2 Keywords | Step 4 Writing Guide |
|---------|-------|--------|-----------------|---------------------|
| **3.1.1** | Vision & Camera Systems | 2 | computer vision, RGB camera, depth camera, RGB-D, real-time monitoring, image processing | List vision-based monitoring techniques (2D/3D) and analyze their effectiveness in detecting geometric deviations. |
| **3.1.2** | Digital Twin & Virtual Monitoring | 4 | digital twin, BIM integration, virtual monitoring, IoT, cyber-physical systems | Describe the role of Digital Twins in synchronizing physical printing with virtual models for real-time process monitoring. |

### **Section 4: Computational Intelligence - From Design to Diagnosis**

| Section | Topic | Papers | Step 2 Keywords | Step 4 Writing Guide |
|---------|-------|--------|-----------------|---------------------|
| **4.1.1** | Toolpath Generation & G-code | 10 | toolpath generation, slicing algorithm, G-code, layer deposition path, BIM integration | Explain the workflow from 3D model to G-code, focusing on slicing algorithms specific to concrete printing constraints. |
| **4.1.2** | Non-planar & 3D Toolpaths | 1 | non-planar slicing, curved layers, conformal printing, 3D toolpath, support-free | Discuss the benefits of non-planar (curved) slicing for structural strength and surface quality compared to flat slicing. |
| **4.1.3** | Trajectory Optimization | 2 | trajectory optimization, speed planning, cornering, smoothing, energy efficiency | Analyze optimization techniques for robot movement (speed, acceleration) to minimize print time and vibration. |
| **4.1.4** | Geometric & Structural Design | 6 | topology optimization, DfAM, structural efficiency, reinforcement strategies, parametric design | Explain how Topology Optimization and DfAM principles are applied to create material-efficient 3DCP structures. |
| **4.2.1** | Deep Learning & Neural Networks | 1 | deep learning, CNN, convolutional neural network, transfer learning, advanced architecture | Explain how Deep Learning models (CNNs) are applied to image-based defect detection and their advantages over traditional methods. |
| **4.2.2** | Machine Learning Methods | 5 | machine learning, SVM, random forest, classification algorithms, data-driven modeling | Discuss traditional ML approaches (SVM, RF) for process classification and compare their data requirements with DL. |
| **4.2.3** | Defect Detection & Classification | 1 | defect classification, surface defects, cracking, voids, automated inspection | Categorize common 3DCP defects (cracks, deformation) and describe automated systems for their detection and classification. |
| **4.2.4** | Predictive Modeling & Diagnosis | 2 | predictive modeling, diagnosis, process-property relationship, quality prediction, regression | Describe how AI models predict final print quality based on process parameters and diagnose root causes of defects. |

### **Section 5: Process Optimization and Advanced Fabrication Techniques**

| Section | Topic | Papers | Step 2 Keywords | Step 4 Writing Guide |
|---------|-------|--------|-----------------|---------------------|
| **5.1.1** | Closed-loop Process Control | 2 | closed-loop control, PID controller, feedback loop, MPC, process regulation | Compare control strategies (PID vs. MPC) for maintaining process stability against disturbances in real-time. |
| **5.1.2** | Extrusion & Flow Control | 1 | extrusion control, flow rate regulation, pump control, nozzle pressure, material flow | Focus on techniques to precisely control material flow rate and synchronize it with robot movement. |
| **5.1.3** | Real-time Adaptation & Compensation | 1 | adaptive control, geometric compensation, real-time adjustment, disturbance rejection | Describe adaptive control systems that compensate for geometric deviations or material inconsistencies on the fly. |
| **5.1.4** | Quality Assurance & Inline Inspection | 3 | quality assurance, inline inspection, tolerance checking, automated QC, verification | Discuss integrated systems for continuous quality verification during the printing process. |
| **5.2.1** | Shotcrete 3D Printing (SC3DP) | 9 | shotcrete 3D printing, SC3DP, spraying, high velocity deposition, reinforcement | Explain the SC3DP process (spraying vs. extrusion) and its advantages for reinforcement integration and surface quality. |
| **5.2.2** | Surface Finishing & Troweling | 5 | automated troweling, surface smoothing, post-processing, surface roughness, finishing tool | Describe automated troweling and smoothing mechanisms integrated into the printing head or as a separate step. |
| **5.2.3** | Hybrid Manufacturing & Integration | 4 | hybrid manufacturing, additive-subtractive, milling, machining, integrated reinforcement | Discuss hybrid systems that combine additive (printing) and subtractive (milling) processes for high-precision finishing. |

---

## **작업 진행 체크리스트**

| Section | Step 1.5 | Step 2 | Step 3 | Step 4 | Step 4.5 | Step 5 | Step 6 | Status |
|---------|----------|--------|--------|--------|----------|--------|--------|--------|
| 2.1.1 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| 2.1.2 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| 2.1.3 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| 2.2.1 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| 2.2.2 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| 3.1.1 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| 3.1.2 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| 4.1.1 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| 4.1.2 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| 4.1.3 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| 4.1.4 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| 4.2.1 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| 4.2.2 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| 4.2.3 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| 4.2.4 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| 5.1.1 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| 5.1.2 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| 5.1.3 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| 5.1.4 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| 5.2.1 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| 5.2.2 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| 5.2.3 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | - |
| **Step 7** | - | - | - | - | - | - | ☐ | Final Review |

---

## **Version History**

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-26 | Initial manual |
| 2.0 | 2026-01-29 | Updated section titles, swapped 4.1↔4.2, added Steps 1.5/3/4.5, added Gap Analysis, added progress checklist |
| 2.1 | 2026-01-29 | Updated paper title, added Korean TOC, created Related_Surveys_Analysis.md |

---

*END OF MANUAL*
