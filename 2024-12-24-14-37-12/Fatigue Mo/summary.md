# Fatigue Monitoring Using Wearables and AI: Trends, Challenges, and Future Opportunities

**URL**: http://arxiv.org/pdf/2412.16847v1
**Date**: 2024-12-22
**Authors**: Kourosh Kakhi, Senthil Kumar Jagatheesaperumal, Abbas Khosravi, Roohallah Alizadehsani, U Rajendra Acharya

---

## ABSTRACT

## 배경
- 피로 모니터링은 특히 장시간 근무하거나 고소민적인 환경에서 일하는 사람들의 안전을 개선하는 데 필수적입니다.
- 피트니스 트래커 및 스마트워치와 같은 웨어러블 기술의 발전으로 개인의 피로 수준을 실시간으로 분석하여 생리적 신호를 지속적으로 모니터링 할 수 있게 되었습니다.
- 이는 피로와 관련된 위험을 예방할 수 있는 시기적절한 통찰력을 제공할 수 있습니다.

## 방법
- 이 리뷰는 피로 감지를 위한 웨어러블 기술과 인공지능(AI)의 통합에 초점을 맞추며, PRISMA 원칙에 따라 진행되었습니다.
- ECG, EMG 및 EEG와 같은 생리적 데이터에서 관련된 정보를 추출하는 신호 처리 방법을 사용한 연구들을 체계적으로 분석했습니다.
- 이후, 이러한 특징들을 머신러닝 및 딥러닝 모델을 통해 피로의 패턴 및 임박한 피로의 지표를 찾기 위해 분석했습니다.

## 결과
- 웨어러블 기술과 최첨단 AI 방법이 다중 모달 데이터 분석을 통해 피로를 정확하게 식별할 수 있음을 입증했습니다.
- 여러 출처의 데이터를 융합함으로써 정보 융합 기술이 피로 평가의 정확성과 신뢰성을 향상시켰습니다.
- 평가에서 AI 기반 신호 분석의 중요한 발전이 관찰되었으며, 이는 실시간 피로 모니터링을 개선하고 개입을 줄이는 데 기여할 것으로 예상됩니다.

## 결론
- AI 및 다중 원천 데이터 융합에 기반한 웨어러블 솔루션은 업무 및 기타 중요한 환경에서 실시간 피로 모니터링을 위한 강력한 옵션을 제공합니다.
- 이러한 발전은 이 분야의 추가적인 개선 가능성을 열어주며, 안전성을 향상하고 피로 관련 위험을 줄이는 데 유용한 도구를 제공합니다.

*키워드:* Fatigue, Physiological fatigue, Artificial intelligence, Machine learning, Deep learning.

---

## INTRODUCTION

## 요약

### 피로의 정의 및 영향
- 피로는 일반적으로 신체 활동 감소 또는 작업 수행의 어려움과 관련이 있습니다.
- 스포츠 선수 및 노동자들은 이러한 신체적 활동으로 인해 피로 문제에 직면합니다.
- 심리적 상태는 피로의 인지를 유도하며, 이는 중추 신경계에 직접적으로 영향을 미치고 기분에 영향을 줍니다.

### 피로 감지 및 모니터링
- 고도로 활동적인 개인의 피로 증상을 모니터링하는 것은 도전적입니다.
- 웨어러블 장치가 신체 활동을 관찰하고 데이터를 분석하기 위한 AI 프레임워크를 통해 도움을 줄 수 있는 가능성이 큽니다.
- 다양한 연구에서 머신러닝 기법을 활용하여 건설 및 제조업에서 피로를 발견하는 방법을 조사했습니다.

### 현재 연구 동향
- 여러 연구들은 다양한 환경에서의 피로 모니터링을 위한 여러 접근 방식을 제안했습니다. 예를 들어:
  - Lambay et al.는 건설 및 제조업에서 피로를 발견하기 위한 머신러닝 기법을 살펴보았습니다.
  - Zong et al.는 건설 근로자의 피로에 대한 체계적인 리뷰를 실행하였으며, 다양한 원인과 평가 방법을 식별했습니다.
  - Li et al.는 얼굴 이미지를 이용해 건설 장비 운영자의 피로를 모니터링하는 분산 접근 방식을 소개했습니다.

### 항공 및 운전 산업
- 항공 산업에서는 피로 위험 관리 시스템에서 AI의 역할이 논의되었습니다.
- Ziakkas et al.는 웨어러블 장치에서 수집된 데이터를 활용하여 실시간 피로 감지를 위한 FRMS의 활용 가능성을 언급했습니다.

### 웨어러블 및 AI 기술의 최근 발전
- AI와 웨어러블 기술은 피로 모니터링을 혁신하고 있으며, 다양한 физиological 신호를 기반으로 비침습적 진단이 가능해졌습니다.
- 여러 연구에서 AI 기반 전술을 채택하여 피로를 감지하는 방법을 제안하고 있습니다.

### 현재 방법의 문제점
- 현재의 피로 모니터링 방법들은 주관적이며 측정의 신뢰성에 문제가 있습니다.
- 표준화된 피로 정의 부족으로 인해 연구 결과를 비교하기 어렵습니다.
- 여러 증상과 요소가 피로를 영향을 미치므로 이를 단일 장치로 모니터링하기가 어렵습니다.

### 결론 및 미래 연구 방향
- 이 연구는 웨어러블 기술과 AI 사용의 피로 모니터링에 대한 포괄적인 문헌 리뷰를 제공합니다.
- 피로 측정 접근 방법, 사용할 수 있는 다양한 웨어러블 유형, 데이터 분석 방법, 산업별 응용을 다루고 있습니다.
- 다양한 생리학적 신호, 턴 현상, AI 및 웨어러블 기술의 결합을 논의하며 futur research opportunities를 제안합니다.

## KEYWORDS
- Fatigue
- Wearables
- AI
- Machine Learning (ML)
- Deep Learning (DL)
- Physiological Signals
- Real-time Monitoring
- Non-invasive Diagnosis
- Predictive Accuracy
- Explainable AI (XAI)

(표 및 그림은 제공된 형식에 맞추어 원본 그대로 포함되어야 하지만 각각의 그림 및 표 데이터는 여기에 명시되지 않았습니다. 원본 내용을 참조하세요.)

---

## METHODOLOGY

## 2.1. Fatigue Background

- 피로(fatigue)는 신체적, 인지적 또는 정신적 수행이 장기적 활동이나 스트레스로 인해 저하되는 다면적인 상태입니다(그림 2 참조).
- 피로는 수면 부족, 높은 정신적 또는 신체적 강도의 장시간 작업, 반복적인 단조로운 업무로 인해 발생합니다.
- 피로를 공정하게 진단할 수 있는 경우, 사고를 줄일 수 있습니다. 예를 들어, 호주 교통사고위원회에 따르면 피로는 호주의 치명적인 도로 사고의 20%-30%에 기여하는 주요 요인입니다.
- 피로의 두 가지 주요 유형은 신체적 피로와 인지적 피로입니다. 각 유형은 급성, 규범적, 만성의 세 가지 수준으로 나뉩니다(그림 3 참조).
- 급성 피로는 일반적인 신체적 또는 정신적 활동에 대한 정상적인 반응이며, 일반적으로 짧은 기간 동안 지속됩니다.
- 만성 피로는 지속적인 탈진 감정으로, 휴식으로 완화되지 않습니다.
- 규범적 피로는 정상적이고 수용 가능한 피로 상태로, 나이가 들면서 발생하는 자연스러운 현상입니다.

- 최근에는 웨어러블 기기와 인공지능(AI)을 이용한 정신적 및 신체적 피로 감지에 대한 관심이 증가하고 있습니다.
- 공학적 데이터를 기반으로 한 피로 측정 및 검출에 대한 2015년부터 2024년 사이에 8,000편 이상의 논문이 발표되었습니다(그림 4 참조).
- 피로는 주관적이기 때문에 신뢰성 있게 측정하기 어려우나, 많은 다른 신체적, 정신적, 환경적 요인에 의존합니다.
- 피로 감지 기술은 다양한 생리적 신호를 평가하는 데 있어 상당한 발전을 이루었습니다.
- 피로를 신뢰성 있게 측정하기 위해 여러 측정과 접근 방식을 고려하는 것이 중요합니다.

![](_page_3_Figure_1.jpeg)

그림 2: 확인된 두 가지 주요 피로 유형

![](_page_3_Figure_7.jpeg)

그림 3: 확인된 세 가지 형태의 피로

---

## 2.2. Literature Search Strategy

### 2.2.1. Search Methods

- 본 연구에서는 피로 모니터링 관련 연구를 찾기 위해 Google Scholar, IEEE Xplore Digital Library, Web of Science(WoS), Scopus의 네 가지 주요 데이터베이스를 활용했습니다.
- 주제 키워드는 "Fatigue Monitoring", "Wearable Technology", "Artificial Intelligence", "Machine Learning", "Deep Learning", "Physiological Signals", "ECG", "EEG", "EMG", "PPG", "EOG" 등이었습니다.

### 2.2.2. Inclusion and Exclusion Criteria

- 원본 연구 기사를 포함했으며, 컴퓨터 과학, 공학, 의료 분야에 중점을 두었습니다.
- 문헌 검토는 논문 제목과 초록을 포함하여 사전 스크리닝을 통해 수행하였습니다.

### 2.2.3. Data Extraction and Structured Meta-analysis

- 스크리닝을 통해 선택된 각 논문의 방법론적 데이터를 정리하고, 체계적 메타 분석을 통해 결과를 발표했습니다.

![](_page_5_Figure_0.jpeg)

그림 5: 체계적인 리뷰에 사용된 PRISMA 흐름도

---

## 3. Datasets Availability for Fatigue Monitoring

### 3.1. Physiological Signal-Based Datasets

- Physiological Signal 기반 데이터셋은 피로를 식별하고 신체의 반응을 조사하기 위한 주요 신호를 수집하는 데 중점을 두고 있습니다.

#### 3.1.1. PhysioNet
- PhysioNet에는 ECG, EEG 및 PPG 신호에 대한 다양한 데이터셋에 대한 접근이 제공됩니다.

#### 3.1.2. DREAMER
- DREAMER 데이터셋은 EEG 및 ECG 신호를 포함합니다.

#### 3.1.3. SEED
- SEED 데이터셋은 인지 작업 중에 수집된 EEG 데이터로 구성됩니다.

#### 3.1.4. SPhysio
- SPhysio는 ECG 및 PPG와 같은 다양한 생리적 신호를 포함합니다.

### 3.2. Behavioral and Video-Based Datasets

#### 3.2.1. YawDD
- YawDD 데이터셋은 운전자의 피로를 감지하기 위해 설계된 비디오 녹화 시리즈입니다.

#### 3.2.2. CEW
- CEW 데이터셋은 열린 눈과 닫힌 눈을 보여주는 이미지를 포함하여 졸림을 감지하는 데 사용됩니다.

### 3.3. Multi-Modal Datasets

#### 3.3.1. Driver Fatigue
- Driver Fatigue 데이터셋은 운전 중 피로 상태 감지를 위해 EEG, EOG 및 행동 데이터를 포함합니다.

#### 3.3.2. DROZY
- DROZY 데이터셋은 수면 유도 방식으로 수집된 다양한 형태의 데이터로 구성됩니다.

---

## 4. Fatigue Measurement Methods

- 피로를 측정하는 다양한 방법에 대해 설명하며, 주관적 자기보고, 성능 관련 테스트, 생물수학적 모델, 행동 관찰 및 생리적 신호 기반 접근법을 포함합니다.

### 4.1. Subjective Measure

- 주관적 피로 측정은 개인의 피로 인식을 분석합니다.

### 4.2. Performance Related Methods

- 성능 기반 방법은 사람들이 수행하는 활동이 피로 수준을 반영한다고 합니다.

### 4.3. Bio-mathematical Models

- 생물수학적 모델은 수면-각성 주기, 작업-휴식 패턴, 일주기 리듬 등의 데이터를 기반으로 피로 수준을 예측합니다.

### 4.4. Behavioural-Based Methods

- 행동 기반 방법은 개인의 행동을 관찰하여 피로의 징후를 감지합니다.

### 4.5. Physiological Signal-based Methods

- 생리적 신호 기반 방법은 개인의 생리적 반응을 측정하여 피로의 징후를 감지합니다.

---

## 5. Physiological Signals for Fatigue Monitoring

- 생리적 신호는 피로 수준을 결정하는 신뢰할 수 있는 비침습적 방법으로 널리 사용됩니다.

### 5.1. Data-driven (objective vs subjective)

- 생리적 데이터 기반 방법은 피로를 보다 정확하고 객관적으로 평가하는 데 기여합니다.

### 5.2. Real-Time Monitoring

- 생리적 신호의 수집은 피로를 실시간으로 모니터링하는 이점을 제공합니다.

### 5.3. Edge Processing

- 엣지 컴퓨팅은 생리적 데이터를 처리하는 속도와 정확성을 개선합니다.

### 5.4. Using Advanced AI and DL

- AI/ML 기술의 발전은 생리적 신호 처리에서 시사점을 제공합니다.

---

## 7. Research Challenges

### 7.1. Access to Real-Time Data

- Wearable devices는 효과적인 피로 관리를 위해 실시간 데이터 액세스가 필요합니다.

### 7.2. Ergonomics and Portability

- Wearable devices의 디자인은 사용자에게 편안함을 제공해야 합니다.

### 7.3. Unobtrusiveness

- 피로 모니터링을 위한 장치는 사용자 일상에 방해가 없어야 합니다.

### 7.4. Continuous Monitoring

- 지속적인 모니터링 시스템은 개인의 피로 상태를 모니터링합니다.

### 7.5. Data Quality

- 피로 측정에 사용되는 데이터의 품질은 정확한 진단에 필수적입니다.

---

## 8. Research Gaps and Future Opportunities

### 8.1. Predictive Accuracy

- AI 기술 적용에서 피로 모니터링의 정밀성을 높일 필요가 있습니다.

### 8.2. Multimodal Information Fusion

- 다양한 출처의 데이터를 융합하여 피로를 정확하게 감지해야 합니다.

### 8.3. Explainable AI for Fatigue Measurements

- AI 모델은 사용하기 쉬우며 이해가 가능해야 합니다.

### 8.4. Uncertainty Quantification and Trust

- AI 모델의 신뢰성을 평가하기 위한 불확실성 quantification이 필요합니다.

### 8.5. Edge Computing

- 데이터 처리의 효율성을 맷도록 엣지 컴퓨팅을 통해 접근해야 합니다.

- 이 논문에서는 피로 모니터링 시스템을 설계하고 구현할 때 고려해야 할 여러 측면에 대해 심층적으로 다루고 있습니다. signal, data comes from patient self-reports, the quality of which directly affects diagnostic accuracy.
  
---

## KEYWORDS
- Fatigue
- Wearable Technology
- Artificial Intelligence
- Machine Learning
- Deep Learning
- Physiological Signals
- ECG
- EEG
- EMG
- PPG
- EOG
- Bio-mathematical Models
- Data-driven Analysis
- Real-Time Monitoring
- Ergonomics
- Continuous Monitoring
- Predictive Accuracy
- Multimodal Information Fusion
- Explainable AI
- Edge Computing

---

## CONCLUSION

## 개요  
이 리뷰는 wearable과 AI 기술을 활용한 피로 모니터링의 전반적인 풍경을 철저히 조사하며, 다양한 분야에서 피로를 평가하고 해결하기 위해 만들어진 다양한 방법론과 기술을 보여줍니다. 전통적인 주관적 측정 방법부터 고급 생리학적 신호 기반 방법까지 여러 접근 방식이 피로를 탐지하고 이해하는 데 있어 귀중한 통찰을 제공합니다. AI와 wearable 장치의 결합은 피로 감지 시스템의 정확성, 실시간 모니터링 능력 및 전반적인 효율성을 크게 향상시켰음을 요약에서 분명히 알 수 있습니다. 

## 주요 내용  
- 피로 모니터링을 위한 다양한 접근 방식이 존재하며, 주관적 측정 방법부터 생리학적 신호 기반의 고급 방법론까지 폭넓게 활용되고 있음.
- AI와 wearable의 결합이 피로 탐지 시스템의 정밀성 및 효율성을 향상시키는데 기여하고 있음.
- 머신러닝과 딥러닝 알고리즘의 발전이 실시간 데이터 접근을 가능하게 함.
- 여전히 해결해야 할 여러 도전 과제가 존재함:
  - 즉각적인 데이터 접근 필요성
  - 사용자 친화적이고 눈에 띄지 않는 장치 디자인 개발
  - 데이터 품질과 신뢰성 확보
- 피로 감지의 예측 정확성을 향상시키고, 다중 모달 정보 융합에서의 발전과 쉽게 설명 가능한 AI 모델 개발이 필요함.
- 이러한 연구의 공백은 미래 탐색에 대해 흥미로운 전망을 제공함.
- 엣지 컴퓨팅과 새로운 센서 기술의 출현으로 이러한 도전 과제를 극복할 잠재력이 큼.
- 이러한 발전은 피로 모니터링 분야의 신뢰성 및 견고성을 높일 가능성을 지니고 있음.

## 협력과 혁신의 중요성  
현재의 방법론을 발전시키기 위한 협력의 중요성을 강조하며, 이는 의료, 항공, 스포츠, 직장 안전과 같은 중요한 분야에서의 안전성 및 효율성을 높이는 데 기여할 것임.

## KEYWORDS  
- AI  
- wearable  
- fatigue monitoring  
- machine learning  
- deep learning  
- physiological signals  
- real-time monitoring  
- multimodal information  
- edge computing  
- data reliability

---

## REFERENCES

### 요약

**A. Frasie et al. (2024): "Validation of the borg cr10 scale for the evaluation of shoulder perceived fatigue during work-related tasks"**
- 목적: 작업 관련 작업 중 어깨에 경험하는 피로를 평가하기 위해 borg CR10 스케일을 검증하는 것.
- 연구 결과: 일반화된 추정 방정식(Generalized estimating equations)을 사용했으며, 어깨 피로에 대한 로드 효과와 최대 자발적 수축(Maximal voluntary contractions)에서의 피로를 측정.
- 주요 발견: 반복 측정 및 과업 효과(Task effects)가 어깨 피로에 미치는 영향이 관찰됨.
- 중요성: 어깨 피로는 근골격계 질환(Work-related disorders)의 위험을 증가시킬 수 있음.

**B. Corcelle et al. (2024): "Immediate but not prolonged effects of submaximal eccentric vs concentric fatiguing protocols on the etiology of hamstrings' motor performance fatigue"**
- 연구 목적: 비극적 근육(hamstrings)의 운동 수행 피로의 원인을 분석하기 위해 두 가지 피로화 프로토콜의 즉각적 효과를 비교.
- 결과: 아랫무릎을 최대한 높이는 동작과 같은 부분적 근육 사용이 피로를 증가시키는 것으로 나타남.
- 결론: 에너지 소모와 피로 메커니즘에 대해 더 심층적인 분석이 필요함을 강조.

**C. Lambay et al. (2021): "A data-driven fatigue prediction using recurrent neural networks"**
- 연구 배경: 근로자의 피로도 예측을 위한 데이터 기반 접근법.
- 기술 방법: Recurrent Neural Network (RNN)을 사용하여 피로를 예측하며, 데이터를 기반으로 한 사용자 맞춤형 솔루션 제시.
- 응용: 제작 산업과 같은 영역에서 근로자의 피로도를 효과적으로 관리할 수 있는 알고리즘 제공.

**D. Zong et al. (2024): "Fatigue in construction workers: A systematic review of causes, evaluation methods, and interventions"**
- 연구의 필요성: 건설 산업에서 피로의 원인과 평가 방법에 대한 체계적인 검토 필요.
- 발견: 정신적 피로, 신체적 피로, 및 작업 환경에 대한 개입이 다루어짐.
- 함의: 보다 효과적인 피로 관리 전략을 위한 유의미한 통계적 데이터 수집이 필요함.

**E. Li et al. (2023): "Smart work package learning for decentralized fatigue monitoring through facial images"**
- 목표: 얼굴 이미지를 통한 비분산 피로 모니터링의 기술 효율성 높이기.
- 방법론: 블록체인 기술을 활용한 실시간 피로 모니터링 시스템 포함.
- 결과: 피로 평가의 정확도 및 응답 시간 개선.

**KEYWORDS**
- borg CR10 Scale
- Generalized estimating equations
- Maximal voluntary contractions
- Hamstrings
- Recurrent Neural Network (RNN)
- Work-related musculoskeletal disorders
- Block-chain
- Fatigue monitoring

---

