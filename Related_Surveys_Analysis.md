# 기존 서베이 논문 분석 및 차별화 전략

**조사일:** 2026-01-29
**목적:** 우리 논문과 유사한 주제의 기존 서베이 확인 및 차별점 도출

---

## 우리 논문 정보

**제목:** Intelligent Robotic 3D Concrete Printing: From Computational Design to Process Control

**핵심 키워드:** Robotic 3DCP, Computational Design, Path Planning, AI Diagnosis, Process Control, Shotcrete

---

## 기존 서베이 논문 현황

### 1. 재료/물성 중심 리뷰

| 논문 | 저널 | 연도 | 주요 초점 | URL |
|------|------|------|----------|-----|
| 3D Concrete Printing Review: Equipment, Materials, Mix Design, and Properties | MDPI Buildings | 2025 | 장비, 재료, 배합 설계, 물성 | https://www.mdpi.com/2075-5309/15/12/2049 |
| Comprehensive review of 3D printed concrete, life cycle assessment, AI and ML models | ScienceDirect | 2024 | 재료, LCA, AI/ML 모델 (물성 예측 중심) | https://www.sciencedirect.com/science/article/abs/pii/S2214993724003440 |
| Recycled Waste Materials Utilised in 3D Concrete Printing | MDPI Buildings | 2025 | 재활용 재료, 지속가능성 | https://www.mdpi.com/2075-5309/15/19/3572 |

### 2. AI/ML 중심 리뷰

| 논문 | 저널 | 연도 | 주요 초점 | URL |
|------|------|------|----------|-----|
| A Review of Current Progress and Application of Machine Learning on 3D-Printed Concrete | Springer | 2023 | ML 기반 재료 최적화, 물성 예측 | https://link.springer.com/chapter/10.1007/978-981-99-7434-4_71 |
| Machine learning-driven 3D printing: A Review | ScienceDirect | 2024 | ML 기반 공정 모니터링 (일반 3D 프린팅) | https://www.sciencedirect.com/science/article/abs/pii/S2352940724002518 |
| A review on machine learning in 3D printing: applications, potential, and challenges | Artificial Intelligence Review | 2021 | ML 응용 전반 (콘크리트 특화 X) | https://dl.acm.org/doi/abs/10.1007/s10462-020-09876-9 |
| Tailoring 3D printed concrete through explainable artificial intelligence | ScienceDirect | 2023 | XAI, 물성 예측 | https://www.sciencedirect.com/science/article/abs/pii/S2352012423009402 |

### 3. 로봇/자동화 중심 리뷰

| 논문 | 저널 | 연도 | 주요 초점 | URL |
|------|------|------|----------|-----|
| Frontiers in construction 3D printing: self-monitoring, multi-robot, drone-assisted processes | Progress in Additive Manufacturing | 2024 | 멀티로봇, 드론, 모니터링 | https://link.springer.com/article/10.1007/s40964-024-00794-8 |
| Large-Scale 3D Printing for Construction by Robotic Arm and Gantry 3D Printer: A Review | MDPI Buildings | 2022 | 갠트리 vs 로봇암 비교 | https://www.mdpi.com/2075-5309/12/11/2023 |
| Mobile robotics and 3D printing: addressing challenges in path planning and scalability | Taylor & Francis | 2024 | 모바일 로봇, 경로 계획 | https://www.tandfonline.com/doi/full/10.1080/17452759.2024.2433588 |
| Robotics technologies aided for 3D printing in construction: a review | Int J Adv Manuf Technol | 2021 | 로봇 기술 전반 | https://link.springer.com/article/10.1007/s00170-021-08067-2 |

### 4. 경로 계획/공정 제어 관련

| 논문 | 저널 | 연도 | 주요 초점 | URL |
|------|------|------|----------|-----|
| Adaptive Toolpath: Enhanced Design and Process Control for Robotic 3DCP | ResearchGate | 2022 | 적응형 툴패스, 공정 제어 | https://www.researchgate.net/publication/359464178 |
| Adaptable Tool-Path Planning Method for 3D Concrete Printing Based on the Mapping Method | Springer | 2021 | 툴패스 계획 방법론 | https://link.springer.com/chapter/10.1007/978-981-33-4400-6_24 |

### 5. 일반/종합 리뷰

| 논문 | 저널 | 연도 | 주요 초점 | URL |
|------|------|------|----------|-----|
| Systematic review on 3D concrete printing technology: breakthroughs and challenges | Discover Civil Engineering | 2025 | 기술 전반, 도전과제 | https://link.springer.com/article/10.1007/s44290-025-00399-2 |
| 3D printing in construction: sustainable technology for building industry | Progress in Additive Manufacturing | 2025 | 지속가능성, 건설 응용 | https://link.springer.com/article/10.1007/s40964-025-01314-y |
| Recent Developments and Challenges of 3D-Printed Construction | MDPI Buildings | 2022 | 최근 발전, 도전과제 | https://www.mdpi.com/2075-5309/12/2/229 |

---

## 차별화 분석

### 기존 서베이들의 커버리지

```
┌─────────────────────────────────────────────────────────────────┐
│                     기존 서베이 커버리지                          │
├─────────────────────────────────────────────────────────────────┤
│  서베이 A (재료)     : [재료] [물성] [배합]                        │
│  서베이 B (AI/ML)    : [AI] [물성예측]                            │
│  서베이 C (로봇)     : [로봇 플랫폼] [하드웨어]                     │
│  서베이 D (경로계획) : [경로 계획] [모바일 로봇]                    │
│  서베이 E (종합)     : [전반적 개요] [도전과제]                     │
└─────────────────────────────────────────────────────────────────┘
```

### 우리 논문의 고유한 포지션

```
┌─────────────────────────────────────────────────────────────────┐
│                     우리 논문 커버리지                            │
├─────────────────────────────────────────────────────────────────┤
│  [로봇 플랫폼] → [센싱] → [설계/계획] → [AI 진단] → [제어] → [제조] │
│       ↑            ↑          ↑            ↑          ↑       ↑  │
│    Section 2   Section 3  Section 4.1  Section 4.2  Section 5.1  5.2│
│                                                                   │
│  ★ 핵심 차별점: "설계 → 진단 → 제어" 전체 파이프라인 통합          │
└─────────────────────────────────────────────────────────────────┘
```

### 상세 차별점

| 측면 | 기존 서베이 | 우리 논문 |
|------|------------|----------|
| **초점** | 개별 기술 영역 (재료 OR 로봇 OR AI) | 전체 시스템 통합 관점 |
| **AI 활용** | 물성 예측 중심 | 결함 진단 + 경로 최적화 |
| **로봇** | 하드웨어 비교 | 하드웨어 + 소프트웨어 + 제어 통합 |
| **경로 계획** | 단독 주제 | 설계 → 제조 흐름의 일부로 통합 |
| **서술 구조** | 기술 나열 | "Design to Control" 논리적 흐름 |
| **Shotcrete 3DP** | 거의 다루지 않음 | 별도 섹션으로 심층 분석 |

---

## 가장 유사한 기존 서베이

**"Frontiers in construction 3D printing: self-monitoring, multi-robot, drone-assisted processes"** (2024)

### 유사점:
- 멀티로봇 시스템 다룸
- 모니터링/피드백 제어 언급
- 건설 3DP 전반 커버

### 차이점:
| 항목 | 해당 서베이 | 우리 논문 |
|------|------------|----------|
| 경로 계획/슬라이싱 | 간략히 언급 | 4.1에서 심층 분석 (19편) |
| AI/ML 진단 | 간략히 언급 | 4.2에서 체계적 분류 (9편) |
| Shotcrete 3DP | 미포함 | 5.2에서 상세 분석 (18편) |
| 구조적 설계 | 미포함 | 4.1.4에서 다룸 (6편) |
| 서술 흐름 | 기술 나열식 | Design → Diagnosis → Control |

---

## 결론

**동일한 주제의 서베이 없음 - 진행 가능**

### Introduction에서 강조할 차별점:
1. **통합적 관점:** 기존 서베이들이 개별 기술(재료, 로봇, AI)을 다룬 반면, 우리는 전체 파이프라인 통합
2. **Computational Intelligence 강조:** 경로 계획 + AI 진단을 핵심 축으로 설정
3. **"Design to Control" 프레임워크:** 논리적 서술 흐름 제공
4. **Shotcrete 3DP 포함:** 기존 서베이에서 다루지 않은 고급 제조 기술

---

## 참고: 검색 키워드

```
1. "3D concrete printing" survey review 2024 2025
2. "robotic 3D printing" concrete survey review intelligent control
3. "3DCP" "path planning" OR "process control" survey review
4. "3D concrete printing" "machine learning" OR "artificial intelligence" review
5. "construction 3D printing" robotic systems automation survey review
```

---

*Last Updated: 2026-01-29*
