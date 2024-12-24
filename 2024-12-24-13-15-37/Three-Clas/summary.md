# Three-Class Text Sentiment Analysis Based on LSTM

**URL**: http://arxiv.org/pdf/2412.17347v1
**Date**: 2024-12-23
**Authors**: Yin Qixuan

---

## RELATED WORK

# 연구 동향 및 방법론 요약

최근 몇 년 동안 인터넷의 급속한 발전으로 웹에서 감정적으로 기울어진 텍스트의 빈도가 점차 증가하고 있으며, 이로 인해 텍스트 감정 분석이 자연어 처리(NLP) 분야에서 핫한 연구 방향이 되고 있습니다. 텍스트 감정 분석을 위해 연구 방법론은 주로 세 가지 범주로 나뉩니다: 감정 사전/규칙 기반 방법, 전통적인 머신 러닝 기반 방법, 심층 학습 기반 방법입니다.

## 2.1 감정 분석 방법론 기반 감정 사전/규칙

- 감정 사전을 기반으로 하는 방법은 감정 분석 분야의 초기 기술입니다.
- 정해진 감정 사전을 사용하여 입력 텍스트의 감정 단어를 분석하고 비교하여 문장 감정 극성을 예측합니다.
- 예를 들어, 중국어 사전 HowNet과 영어 사전 WordNet이 종종 사용됩니다.
- 감정 사전의 품질은 모델의 정확성과 안정성에 직접적인 영향을 미칩니다.
- 연구자들은 대규모 텍스트 데이터를 통해 감정 사전을 설계하여 분류 성능을 개선하고자 합니다.
- 감정 사전의 적용 가능성에는 중요한 한계가 있으며, 다른 맥락에서 감정 단어의 의미가 변경될 수 있습니다.
- 이러한 문제를 해결하기 위해 연구자들은 감정 사전 방법을 감독 학습과 결합하려고 시도했습니다.

## 2.2 전통적인 머신 러닝 기반 감정 분석 방법

- 전통적인 머신 러닝 방법은 알고리즘을 통해 텍스트 기능을 학습하고 추출하여 텍스트의 감정 극성을 결정합니다.
- 이러한 방법은 감정 사전 기반 접근 방식의 일부 단점을 효과적으로 피할 수 있습니다.
- 일반적으로 사용되는 머신 러닝 알고리즘으로는 Support Vector Machine (SVM), Naive Bayes, Decision Trees, K-Nearest Neighbors (KNN), Random Forest 등이 있습니다.
- 연구에서 Weibo 데이터를 기반으로 한 멀티모달 결합 감정 주제 모델(MJST)은 이모지와 사용자 성향 특성을 도입합니다.
- 전통적인 머신 러닝 방법은 성능에서 감정 사전 접근 방식을 초과하지만, 높은 의존성과 도메인 지식 요구로 인해 고전적 한계가 있습니다.

## 2.3 심층 학습 기반 감정 분석 방법

- Deep learning은 다층 신경망을 통해 데이터에서 기능 추출 및 학습을 수행합니다.
- 대표적인 모델은 Convolutional Neural Networks (CNN)과 Recurrent Neural Networks (RNN)입니다.
- Attention 메커니즘을 도입하여 모델의 감정 정보 식별 능력을 향상시키는 연구들이 있습니다.
- 최근 BERT와 같은 사전 훈련된 모델이 감정 분석 성능을 높입니다.

## 3. 모델 설계 및 구성

### 3.1 LSTM 모델 아키텍처

- Long Short-Term Memory (LSTM) 네트워크는 시퀀스 데이터를 잘 처리할 수 있는 반복 신경망(RNN)입니다.
- LSTM 모델은 입력층, LSTM층, 출력층으로 구성되어 있습니다.

### 3.2 입력층 구조

- 입력층은 원시 텍스트 데이터를 숫자 벡터 표현으로 변환합니다.
- 텍스트 전처리 → 단어 임베딩 표현 → 입력 시퀀스 구성 세 가지 주요 단계가 포함됩니다.

### 3.3 LSTM층

- LSTM 또는 RNN에서 기울기 소실 및 폭주 문제를 방지하는 저장 및 기억 기능을 도입합니다.
- LSTM 단위는 입력 게이트, 망각 게이트, 출력 게이트, 메모리 셀로 구성됩니다.

### 3.4 출력층

- 출력층은 LSTM 모델에서 생성된 특징 벡터를 완전 연결층에 전달하여 차원 축소를 처리합니다.

## 4. 실험 및 결과 분석

### 4.1 데이터 준비

- 본 연구에서는 웹 스크래핑을 통해 수집된 Weibo 댓글 텍스트 데이터셋을 사용하였습니다.
- 데이터의 유효성을 보장하기 위해 전처리 단계가 수행되었습니다.

### 4.2 실험 환경 설정

- PyTorch 오픈소스 딥러닝 프레임워크를 사용하여 실험을 수행하였습니다.

| Table 1: Experimental environment |  |
| --- | --- |
| 운영 체제 | Windows 10 64bit |
| CPU | 14 vCPU Intel(R) Xeon(R) Platinum 8362 CPU @ 2.80GHz |
| GPU | RTX 3090 (24GB) × 1 |

### 4.3 매개변수 설정

- vocab dim = 100: 단어 벡터의 차원수 설정
- n iterations = 10: 모델 훈련을 위한 반복 횟수
- n exposures = 10: 단어 빈도 임계값
- window size = 7: 문맥 윈도우 크기
- n epoch = 4: 모델 훈련 에폭 수
- input length = 100: 입력 시퀀스 길이

### 4.4 평가 메트릭

- 정확도, 정밀도, 재현율, F1 점수로 평가하였습니다.

| Table 2: Confusion Matrix |  |  |
| --- | --- | --- |
| 실제 결과 양수 | 음수 |  |
| 양수 TP |  | FN |
| 음수 FP |  | TN |

### 4.5 결과 분석

- 딥 러닝 모델이 수작업 피처 설계 없이 자율적으로 피처 표현을 학습할 수 있음을 보여주었습니다.
  
| Model | Accuracy (%) | Precision (%) | Recall (%) | F1 Score (%) |
| --- | --- | --- | --- | --- |
| KNN | 55.07 | 55.65 | 69.46 | 45.75 |
| Random Forest | 74.44 | 86.96 | 57.51 | 69.23 |
| Logistic Regression | 83.23 | 83.12 | 83.38 | 83.26 |
| Naive Bayes | 83.13 | 83.10 | 83.24 | 83.10 |
| CNN | 84.80 | — | 84.90 | 84.90 |
| RNN | 86.56 | 86.53 | 86.63 | 86.58 |
| LSTM | 98.31 | 99.98 | 96.63 | 98.28 |

## 5. 결론

본 논문은 LSTM 모델을 사용한 중국어 감정 분석의 적용을 철저히 조사하였습니다. 실험 결과, LSTM 모델은 샘플의 맥락 정보를 캡처하여 감정 분류 성능을 크게 향상시킵니다. 향후 연구는 다중 감정을 포함하는 혼합 댓글에 대해 다중 레이블 분류 접근 방식을 사용할 수 있습니다.

## KEYWORDS
- Sentiment Analysis
- Natural Language Processing (NLP)
- Support Vector Machine (SVM)
- Convolutional Neural Networks (CNN)
- Recurrent Neural Networks (RNN)
- Long Short-Term Memory (LSTM)
- Bidirectional Gated Recurrent Units (BiGRU)
- TF-IDF
- Word2Vec
- GloVe
- Attention Mechanism
- BERT
- Softmax

---

