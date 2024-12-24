# Knowledge Editing through Chain-of-Thought

**URL**: http://arxiv.org/pdf/2412.17347v1
**Date**: 2024-12-23
**Authors**: Changyue Wang, Weihang Su, Qingyao Ai, Yiqun Liu

---

## ABSTRACT

### 요약

- **감정 분석**은 자연어 처리(NLP)에서 중요한 작업으로, 공공 여론 모니터링 및 시장 조사 등 다양한 분야에 널리 활용됨.
- 본 논문은 Long Short-Term Memory (LSTM) 네트워크에基한 세 가지 감정 분석 방법을 제안함. 이 방법은 Weibo 댓글 텍스트의 감정 극성(긍정적, 중립적, 부정적)을 분석하는 데 목표를 둠.
- LSTM은 딥러닝 모델로서 텍스트 내에서 긴 거리의 의존성을 효과적으로 처리할 수 있어, 전통적인 기계 학습 모델에 비해 장점을 제공함.
- Weibo 댓글 텍스트에서 특징을 전처리 및 학습함으로써 LSTM 모델은 댓글의 감정 범주를 정확하게 예측할 수 있음.

### 실험 결과

- 실험 결과, LSTM 모델은 Weibo 댓글에 대한 감정 분석 작업에서 98.31%의 정확도와 98.28%의 F1 점수를 기록하였으며, 이는 전통적인 모델 및 다른 딥러닝 접근 방식보다 훨씬 뛰어남.
- 이러한 결과는 LSTM이 텍스트 내 감정 정보를 더 잘 포착하여 감정 분류의 정확성을 크게 향상시킬 수 있음을 시사함.

### 제한 사항

- 그러나 LSTM 모델은 높은 계산 복잡성과 긴 텍스트 처리 속도의 저하와 같은 몇 가지 제한 사항을 여전히 가지고 있음.
- 또한, 풍자 및 유머와 같은 복잡한 감정 표현은 모델의 성능에 영향을 줄 수 있음.

### 향후 연구 방향

- 향후 연구에서는 사전 훈련된 모델과의 결합이나 특징 공학 개선 등을 통해 모델의 정확성과 실용성을 더욱 향상시킬 수 있을 것임.
- 전반적으로, LSTM 모델은 Weibo 댓글의 감정 분석에 효과적인 해결책을 제공함.

### Keywords

- Sentiment Classification
- Natural Language Processing
- LSTM
- Deep Learning
- Machine Learning

---

## INTRODUCTION

## 요약

- 컴퓨터 기술과 인터넷의 빠른 발전으로 정보 전파는 점점 인터넷에 의해 지배되고 있으며, 소셜 네트워크는 사용자가 의견과 감정을 표현하는 주요 플랫폼으로 자리잡고 있음.
- 2023년 1분기 말까지 Weibo의 월간 활성 사용자 수는 5억 9300만 명에 달하며, 일일 활성 사용자 수는 2억 5500만 명에 도달함.
- 갑작스러운 공공 사건 발생 시 Weibo에서 사용자 간의 상호작용 빈도가 크게 증가하여 짧은 시간 안에 공공 의견 영역을 형성함.
- Weibo는 정보 전파의 증폭기로서 온라인 공공 의견의 영향력을 강화함.

- 그러나 방대한 댓글 데이터로 인해 현재의 공공 의견 방향 및 영향 분석은 점점 더 어려워지고 있음.
- 수십억 개의 댓글 텍스트에서 핵심 정보를 추출하고 사용자의 감정 동향을 정확히 분석하여 세분화된 공공 의견 지침을 제공하는 것은 현재 연구 분야에서 중요한 도전이 되고 있음.

### 텍스트 감정 분석 기술
- 텍스트 감정 분석 기술은 대량의 소셜 미디어 데이터에서 귀중한 정보를 추출하여 사용자 감정 분석의 효율성을 크게 향상시킴.
- 최근 몇 년 간 심층 학습을 결합한 감정 분석 연구에서 상당한 발전이 있었음에도 불구하고 소셜 미디어 댓글 데이터의 감정 분석은 여전히 다음의 세 가지 주요 도전에 직면해 있음:
  1. 댓글 양식의 다양성: 서로 다른 소셜 플랫폼의 댓글은 종종 다중 모드 형식으로 제공되므로 다양한 모드 특성의 융합을 고려해야 함.
  2. 비격식적인 문장과 새로운 단어의 빠른 업데이트: 사용자 댓글은 종종 비격식적이고 문법 표준이 낮으며, 신흥 인기 용어를 자주 사용하여, 사전 기반 혹은 규칙 기반 감정 분석 방법으로는 처리하기 어려움.
  3. 감정 단어 품사의 복잡성: 중국어 말뭉치에서는 감정 단어의 상당 부분이 동사와 명사에 포함되지만, 저빈도 핵심 명사 감정 단어는 종종 간과되어 감정 단어 추출 또는 특성 추출 모델이 문장에서 핵심 감정 정보를 포착하는 데 어려움을 겪음.

### 연구 방법
- 본 논문은 Weibo 댓글 텍스트에 대한 실험을 진행하여 사용자의 핫 공공 의견 사건에 대한 주의도와 감정 태도를 분석함.
- 위의 도전 과제를 효과적으로 다루기 위해 본 논문에서는 Long Short-Term Memory (LSTM)를 기반으로 한 3분류 감정 분석 방법을 제안함.
- LSTM은 텍스트의 컨텍스트 의미를 포착하고 감정 분류 작업을 수행함.
- 동시에 LSTM 모델은 댓글 감정 분류 작업에서 높은 정확성과 안정성을 나타냄.
- 이 연구는 다중 모드 특성을 결합하는 것의 효과성을 검증할 뿐만 아니라 감정 분석 분야에서의 추가 탐색을 위한 참고 자료를 제공함.

## 키워드
- Long Short-Term Memory (LSTM)
- sentimento analysis
- multimodal features
- sentiment words
- Chinese corpora 
- Weibo
- active users
- public opinion events

---

## RELATED WORK

## 1. 서론  
- 최근 인터넷의 발전으로 인하여 감정이 담긴 텍스트의 빈도가 증가하고 있으며, 이는 Natural Language Processing (NLP) 분야에서 텍스트 감정 분석이 주목받는 연구 주제가 되고 있음을 나타냅니다.  
- 텍스트 감정 분석 연구 방법은 주로 세 가지 범주로 나뉩니다: sentiment dictionaries/rules 기반 방법, 전통 기계 학습 기반 방법, 그리고 딥 러닝 기반 방법입니다.

## 2. 감정 분석 방법  
### 2.1. Sentiment Analysis Methods Based on Sentiment Dictionaries/Rules  
- 감정 사전 기반 감정 분석 방법은 감정 분석 분야에서 초기 기술입니다.  
- 기본 아이디어는 정의된 감정 사전을 사용하여 입력 텍스트 내의 감정 단어를 분석하고 비교하여 문장의 감정 극성을 예측하는 것입니다. 예를 들어, HowNet(중국어 사전)와 WordNet(영어 사전)이 자주 사용됩니다.  
- 그러나 감정 사전의 품질은 모델의 정확도와 안정성에 직접적인 영향을 미칩니다.  
- 일부 연구에서는 대규모 텍스트 데이터를 바탕으로 감정 사전을 설계하여 분류 성능을 개선하고자 했습니다.  
- 그럼에도 불구하고 감정 사전의 적용 가능성은 매우 제한적이며, 문맥에 따라 감정 단어의 의미가 다를 수 있습니다.  
- 이러한 문제를 해결하기 위해 연구자들은 감정 사전 방법과 감독 학습을 결합하려고 노력하고 있습니다.  

### 2.2. Sentiment Analysis Methods Based on Traditional Machine Learning  
- 전통적인 기계 학습 방법은 알고리즘을 통해 텍스트 특성을 학습하고 추출하여 텍스트의 감정 극성을 결정합니다.  
- 일반적으로 사용되는 기계 학습 알고리즘에는 Support Vector Machine (SVM), Naive Bayes, Decision Trees, K-Nearest Neighbors (KNN), Random Forest 등이 포함됩니다.  
- 연구에서는 Weibo 데이터를 기반으로 한 다중 모달 공동 감정 주제 모델( MJST )을 도입하였고, 이는 Latent Dirichlet Allocation (LDA) 모델을 사용하여 숨겨진 감정 특성을 분석합니다.  
- 전통적인 기계 학습 방법은 성능 면에서는 감정 사전 접근 방식보다 우수하지만, 전이 가능성 부족과 도메인 지식 및 수동 라벨링 의존도가 높은 단점이 있습니다.  
- 딥 러닝 기술의 발전과 함께 감정 분석은 점차 딥 러닝 방법으로 이동해왔습니다.  

### 2.3. Sentiment Analysis Methods Based on Deep Learning  
- 딥 러닝은 다층 신경망을 통해 데이터에서 feature extraction 및 learning을 수행하며, 최근 텍스트 감정 분석에서 두드러진 장점을 보여주고 있습니다.  
- 대표적인 모델에는 Convolutional Neural Networks (CNN)과 Recurrent Neural Networks (RNN)이 포함됩니다.  
- 연구 결과, 딥 러닝 모델에 attention mechanism을 도입하면 텍스트 내 핵심 감정 정보를 인식하는 능력이 크게 향상됩니다.  
- 최근에는 BERT와 같은 pre-trained model이 텍스트 감정 분석의 발전을 이끌고 있으며, 이들 모델은 대규모 비라벨 코퍼스를 사전 학습하고 세부 작업을 위해 fine-tuning함으로써 성능을 개선합니다.  
- 딥 러닝 기반 감정 분석 방법은 점차 주류가 되었으며, pre-trained models의 도입으로 감정 분석 기술의 경계가 확장되었습니다.

## 3. 모델 설계 및 구성  
### 3.1. LSTM 모델 구조  
- Long Short-Term Memory (LSTM) 네트워크는 순차적 데이터 처리를 잘 수행하며, 긴 의존성 및 시퀀스 정보를 캡처할 수 있습니다.  
- 본 연구에서는 텍스트 데이터의 feature extraction 및 감정 분석을 위해 독립적으로 LSTM 모델을 사용합니다.  
- LSTM 모델은 입력층, LSTM 층, 출력층 등으로 구성됩니다.  
- 처리된 텍스트 시퀀스는 LSTM 네트워크로 전송되며, LSTM은 그 Unique gating mechanisms을 통해 시퀀스 데이터를 처리합니다.

### 3.2. 입력층 구조  
- LSTM 모델의 입력층은 원시 텍스트 데이터를 숫자 벡터 표현으로 변환하는 역할을 합니다.  
- 이 과정은 텍스트 전처리, 단어 표현, 입력 시퀀스 구성의 세 가지 주요 단계로 나뉩니다.  
- 텍스트 전처리 과정에서는 불용어 및 특수문자를 제거하고, 인덱스를 매겨 정수 인덱스로 변환합니다.  
- Word Embedding 기술을 통해 각 단어는 고정된 차원의 연속 벡터 표현으로 매핑됩니다.  
- 입력 시퀀스는 정규화된 길이를 갖도록 패딩 및 자르기를 수행합니다.

### 3.3. LSTM 층  
- RNN은 선형 시퀀스 데이터 처리에 적합하며, 재귀 구조를 통해 현재 은닉층은 이전 시간 단계와 입력층의 영향을 받습니다.  
- LSTM 유닛은 입력 게이트, 망각 게이트, 출력 게이트 및 메모리 셀로 구성됩니다.  
- 망각 게이트는 현재 메모리 셀에서 무엇을 버릴지를 결정하며, 입력 게이트는 새 정보를 저장할지를 결정합니다.

### 3.4. 출력층  
- 출력층은 LSTM 모델에서 생성된 feature vectors를 fully connected layer를 통해 차원 축소를 수행합니다.  
- 최종적으로 Softmax 함수를 사용하여 출력의 정규화를 수행하고 감정 극성을 예측합니다.

## 4. 실험 및 결과 분석  
### 4.1. 데이터 준비  
- 본 연구에서 사용된 데이터셋은 웹 스크래핑을 통해 수집된 Weibo 댓글 텍스트로, 총 21,091개의 샘플이 포함됩니다.  
- 데이터의 유효성을 높이기 위해 전처리 작업을 수행합니다.

### 4.2. 실험 환경 설정  
- 실험은 PyTorch 오픈 소스 딥 러닝 프레임워크를 사용하여 AutoDL 클라우드 환경에서 진행되었으며, 구체적인 설정 사항은 아래의 표와 같습니다.  
| Table 1: Experimental environment |  |
| --- | --- |
| Hardware environment |  |
| Operating system | Windows 10 64bit |
| CPU | 14 vCPU Intel(R) Xeon(R) Platinum 8362 CPU @ 2.80GHz |
| GPU | RTX 3090 (24GB) × 1 |
| Software environment |  |
| PyTorch | 1.11.0 (CUDA 11.3) |
| Python | 3.8 (Ubuntu 20.04) |
| Pandas | 2.0.3 |
| NumPy | 1.23.1 |
| scikit-learn | 1.3.2 |
| Gensim | 4.3.3 |
| TensorFlow | 2.9.0 |
| Jieba | 0.42.1 |

### 4.3. 파라미터 설정  
- vocab dim = 100
- n iterations = 10
- n exposures = 10
- window size = 7
- n epoch = 4
- input length = 100 and maxlen = 100

### 4.4. 평가 메트릭  
- 정확도, 정밀도, 재현율, F1 점수 등의 평가 메트릭을 사용하였고, 예측 결과의 confusion matrix는 아래와 같습니다.  
| Table 2: Confusion Matrix |  |  |
| --- | --- | --- |
| Predicted Result |  |  |
| Actual Result Positive | Negative |  |
| Positive TP |  | FN |
| Negative FP |  | TN |

### 4.5. 결과 분석  
- 비교 실험에서 본 연구는 네 가지 전통적인 기계 학습 기반 모델과 두 가지 딥 러닝 기반 모델을 LSTM 모델과 비교하였습니다.  
| Model | Accuracy (%) | Precision (%) | Recall (%) | F1 Score (%) |
| --- | --- | --- | --- | --- |
| KNN | 55.07 | 55.65 | 69.46 | 45.75 |
| Random Forest | 74.44 | 86.96 | 57.51 | 69.23 |
| Logistic Regression | 83.23 | 83.12 | 83.38 | 83.26 |
| Naive Bayes | 83.13 | 83.10 | 83.24 | 83.10 |
| CNN | 84.80 | — | 84.90 | 84.90 |
| RNN | 86.56 | 86.53 | 86.63 | 86.58 |
| LSTM | 98.31 | 99.98 | 96.63 | 98.28 |  
- 딥 러닝 모델이 감정 분석에서 우수한 성능을 보였습니다.

## KEYWORD  
- Natural Language Processing  
- sentiment analysis  
- sentiment dictionaries  
- machine learning  
- deep learning  
- Support Vector Machine (SVM)  
- Naive Bayes  
- Decision Tree  
- K-Nearest Neighbors (KNN)  
- Random Forest  
- Convolutional Neural Networks (CNN)  
- Recurrent Neural Networks (RNN)  
- Long Short-Term Memory (LSTM)  
- attention mechanisms  
- pre-trained models  
- BERT  
- Latent Dirichlet Allocation (LDA)  
- TF-IDF

---

## CONCLUSION

### 요약

- 이 논문은 LSTM (Long Short-Term Memory) 모델의 중국어 감정 분석에서의 적용을 철저히 조사합니다.
- 실험 결과는 샘플의 맥락 정보를 캡처함으로써 LSTM 모델이 감정 분류 성능을 크게 향상시킨다는 것을 보여줍니다.
- 비교 실험을 통해 제안된 모델이 다양한 고전 전통 기계 학습 모델보다 우수함을 입증 하였으며, 이를 통해 모델의 효과성과 실행 가능성을 어느 정도 검증하였습니다.

### 미래 연구 방향

- 미래 연구는 애매한 댓글을 더욱 심도 있게 다룰 수 있습니다.
- 여러 감정을 포함하는 댓글의 경우, 다중 레이블 분류 접근 방식을 사용하여 이러한 댓글 내의 복잡한 감정 구성을 설명할 수 있습니다.
- 맥락 정보를 통합함으로써, 이 방법은 다양한 감정적 맥락을 더 잘 이해할 수 있어 모델의 성능과 일반화 능력을 향상시킬 수 있습니다.

### KEYWORDS
- LSTM (Long Short-Term Memory)
- Sentiment Analysis
- Contextual Information
- Multi-label Classification
- Emotional Composition
- Model Performance
- Generalization Capability

---

## REFERENCES

## 연구 요약

### 1. Z. Zhang 외 (2010)의 연구
- 연구 제목: 인터넷 제품 리뷰에 대한 감정 분석 연구의 리뷰
- 주제: 인터넷 제품 리뷰에서의 감정 분석 기법에 대한 종합적인 검토
- 결론: 다양한 기법들이 적용되었으나, 데이터의 다양성과 감정 분류의 정확성이 향후 연구의 주요 도전 과제가 될 것임

### 2. J. Liang 외 (2014)의 연구
- 연구 제목: 딥러닝 기반의 웨이보 감정 분석
- 주제: 딥러닝 기법을 적용하여 웨이보에서의 사용자의 감정을 분석
- 결론: 딥러닝 기법이 기존 방법보다 높은 정확도를 보여주며, 자연어 처리 분야에서의 가능성을 제시함

### 3. G. Wang 외 (2007)의 연구
- 연구 제목: 다중 중복 라벨링 CRFs에 기반한 문장 수준 감정 분석 연구
- 주제: CRF (Conditional Random Fields)를 활용하여 문장 수준의 감정 분석을 수행
- 결론: 중복 라벨링이 감정 분석의 정확성을 향상시키는 데 기여함

### 4. X. Liu 외 (2017)의 연구
- 연구 제목: 신경망 모델에 기반한 제품 속성 감정 분석
- 주제: 신경망 모델을 사용하여 제품의 속성에 대한 감정을 분석
- 결론: 신경망은 복잡한 제품 감정 정보를 효과적으로 캡처할 수 있는 잠재력을 가지고 있음

### 5. S. Media의 연구 (2013)
- 연구 제목: 인터넷 사용자들의 감정 분석을 기반으로 한 예측 방법 연구
- 주제: 감정 분석을 통한 사용자 행동 예측
- 결론: 감정 분석이 사용자의 행동 예측에 실질적인 기여를 할 수 있음

### 6. Z. Wang 외 (2014)의 연구
- 연구 제목: 온라인 리뷰 감정 분석에서 고정 결합 특징 추출 방법 연구
- 주제: 고정 결합 특징 추출 방법을 통한 온라인 리뷰의 감정 분석
- 결론: 특정 패턴을 추출함으로써 감정 분석의 성능을 향상시킬 수 있음

### 7. L. Xie 외 (2012)의 연구
- 연구 제목: 계층 구조에 기반한 다전략 중국 웨이보 감정 분석 및 특징 추출
- 주제: 다양한 전략을 사용하여 중국 웨이보의 감정을 분석하고 특징을 추출
- 결론: 계층적 접근법이 감정 분석의 정확성을 높이는 데 기여함

## KEYWORDS
- Sentiment Analysis
- Deep Learning
- CRF (Conditional Random Fields)
- Neural Network
- Feature Extraction
- Product Attributes
- User Behavior Prediction

---

