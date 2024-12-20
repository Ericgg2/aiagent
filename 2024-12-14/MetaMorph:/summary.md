## RELATED_WORK

# Instruction tuning 및 시각적 Instruction tuning

## 주요 내용
- Instruction tuning (Wei et al., 2022a; Taori et al., 2023)는 pretrained LLM을 조정하여 상호작용의 형식 및 스타일을 학습합니다. 
- 이 과정은 모델이 pretraining 동안 습득한 지식과 능력을 효과적으로 전달하는 데 도움을 줍니다 (Zhou et al., 2024a).
- LLaVA (Liu et al., 2023)는 instruction tuning을 다중모드 영역으로 확장합니다. 
- 이후 다양한 연구들이 데이터 큐레이션 (Chen et al., 2023; Laurençon et al., 2024a,b), 시각적 표현 (Tong et al., 2024a; Kar et al., 2025; Chen et al., 2024b), 그리고 instruction tuning 전략 (Gao et al., 2024; Liu et al., 2024b)의 개선에 집중하고 있습니다. 
- 몇 백만 개의 다중 모드 instruction tuning 데이터만 사용하여, 이 연구 라인은 오픈 소스 MLLMs가 여러 벤치마크 (Liu et al., 2024d; Yue et al., 2024a,b)와 애플리케이션 (Zhai et al., 2024; Pan et al., 2024a)에서 상용 모델 (OpenAI, 2024; Anthropic, 2024)과 유사한 성능에 도달하게 해주었습니다.

## 다중 모드 LLM에서 통합 모델로
- 최근 통합 모델을 구축하기 위한 노력은 주로 대규모 사전 훈련 또는 수십억 규모 데이터셋에 대한 집중적 미세 조정에 의존하고 있습니다. 
- 일부 연구는 시각적 토큰 예측을 위해 연속적 임베딩을 사용하거나 시각적 회귀 손실 (Sun et al., 2024b,a)을 통합하고, 또는 확산 기반 방법을 활용합니다 (Dong et al., 2024). 
- 다른 접근법 (Lu et al., 2022a; Aghajanyan et al., 2022; Team, 2024; Wu et al., 2024b; Liu et al., 2024c; Wang et al., 2024b; Lu et al., 2024)은 다중 모드 데이터를 개별 토큰으로 분할하여, 자율 회귀 변환기를 사용하여 학습합니다. 
- 최근 연구는 자율 회귀 및 확산 목표를 결합한 하이브리드 전략을 탐구하기도 했습니다 (Zhou et al., 2024b; Xie et al., 2024).
- 이전 연구와는 달리, 우리는 instruction tuning 동안 적은 데이터 환경에서도 통합 모델을 효과적으로 훈련할 수 있음을 보여주며, 시각적 이해와 시각적 생성 사이의 상호 관계에 대한 통찰력을 제공합니다.

## KEYWORD
- Instruction tuning
- LLM (Large Language Model)
- Pretrained
- LLaVA
- Multimodal
- Data curation
- Visual representation
- Fine-tuning
- Unified models
- Continuous embeddings
- Visual tokens
- Autoregressive transformers
- Diffusion-based methods
- Hybrid strategies

---

## DISCUSSION

## 연구 요약

- 본 연구에서는 VPiT를 제안하는데, 이는 LLMs(대형 언어 모델)가 멀티모달 토큰을 예측할 수 있도록 하는 간단하면서도 효과적인 비주얼 인스트럭션 튜닝 확장 방식이다.
- VPiT는 비주얼 질문 응답(VQA)뿐만 아니라 텍스트-투-이미지(text-to-image), 순수 이미지 및 비디오 데이터를 포함하여 더 다양한 범위의 인스트럭션 튜닝 데이터를 활용 가능하게 한다.
- 통제된 실험을 통해, 비주얼 생성 능력은 향상된 비주얼 이해의 자연스러운 부가 산물로 나타나며, 약간의 추가 생성 데이터가 필요하다는 것을 발견하였다.
- 비주얼 이해와 생성은 서로 유익하게 작용하지만, 비주얼 이해 데이터를 추가하는 것이 전체 성능을 향상시키는 데 더 큰 효과가 있음.
- 이러한 통찰을 바탕으로, 우리는 VPiT와 함께 LLaMA-3.1 8B를 미세 조정(finetuning)하여 MetaMorph를 훈련하였다. 
- 간단한 훈련 과정을 통해, MetaMorph는 비주얼 이해와 생성 모두에서 경쟁력 있는 성능을 달성하였다.
- 모델의 정성적 평가 결과, MetaMorph는 비주얼 생성 시 기본 LLM의 세계 지식 및 추론 능력을 활용할 수 있음을 보여주었다.
- 예를 들어, 전문적 고유명사("Chhogori")로 된 이미지 생성이나 시각 퍼즐 해결("monarch caterpillar의 메타모르포시스 결과 동물의 이미지 생성")과 같이 여러 단계의 추론을 요구하는 멀티모달 작업을 수행할 수 있다.
- 이는 LLMs가 최소한의 인스트럭션 튜닝만으로 활성화될 수 있는 '사전' 비주얼 지식을 이미 어느 정도 보유하고 있음을 나타낸다.
- 전체적으로, LLMs는 통합적이고 다기능적인 모델과 유사한 표현 공간을 가질 수 있다(Huh et al., 2024). 
- 우리는 이 연구의 통찰이 일반 지능을 위한 LLM 개발을 위한 더 많은 탐구를 자극하길 희망한다.

## KEYWORD
- VPiT
- LLMs
- visual instruction tuning
- multimodal tokens
- visual question answering
- text-to-image
- visual understanding
- generation data
- MetaMorph
- LLaMA-3.1 8B
- qualitative evaluation
- world knowledge
- reasoning abilities
- multimodal tasks
- prior visual knowledge
- unified and multi-functional models

---

## INTRODUCTION

## 연구 요약

### 소개
- 멀티모달 대형 언어 모델(Multimodal Large Language Models, MLLMs)은 이미지 캡션 생성에서 복잡한 시각적 추론으로 발전하였음.
- 이러한 모델은 주로 이미지와 언어의 멀티모달 입력을 처리하고 텍스트 토큰을 생성함.

### MLLM 구조와 훈련 방법
- MLLM은 사전 훈련된 비전 인코더와 사전 훈련된 언어 모델을 활용하며 MLP나 크로스 어텐션 모듈과 같은 연결기를 통해 이 두 가지 모달리티를 정렬함.
- 시각적 지시 튜닝(Visual Instruction Tuning)이 많이 사용되며, 이는 사전 훈련된 비전 인코더의 출력 임베딩을 연속적인 “시각적 토큰”으로 취급하여 사전 훈련된 LLM에 입력으로 직접 제공함.

### 효율성과 효과성
- 시각적 지시 튜닝은 데이터와 계산 효율성이 있으며, 사전 훈련된 LLM은 적당한 계산과 수백만 개의 이미지-텍스트 질문-응답 쌍으로 멀티모달 LLM로 재사용될 수 있음.
- LLM은 이미 상당량의 내재적 시각적 지식을 보유하고 있어 지시 튜닝 과정에서 시각적 이해를 효과적으로 학습하고 개발할 수 있음.

### 연구 동기 및 VPiT 제안
- 우리는 LLM을 시각적 정보를 생성할 수 있도록 효율적으로 미세 조정할 수 있는지 조사함.
- VPiT(Visual-Predictive Instruction Tuning)를 제안하고, 연속적인 시각적 토큰과 이산 텍스트 토큰을 모두 출력하도록 LLM을 훈련시킴.

### VPiT 아키텍처 및 훈련 프로세스
1. **모달 데이터 토큰화**: 텍스트와 이미지 데이터를 함께 포함하여 훈련에 사용함.
2. **모델 아키텍처**: LLM의 원래 헤드 외에 시각적 토큰을 예측하기 위한 별도의 비전 헤드를 추가함.
3. **손실 함수**: LLM의 언어 헤드는 다음 토큰 예측을 위한 크로스 엔트로피 손실을 사용하고, 시각 예측에서는 코사인 유사도 손실을 사용함.

### 데이터 유형
- **시각적 이해 데이터**: 이미지나 비디오를 입력으로 사용하여 텍스트 응답을 출력함.
- **시각적 생성 데이터**: 이미지 설명을 기반으로 시각적 토큰을 예측함.
- **기타 시각 데이터**: 교차 입력 토큰으로부터 시각적 토큰 예측.

### 시각적 생성 유도
- VPiT 프레임워크를 통해 우리는 시각적 이해와 생성 간의 시너지 효과를 연구함.
- 시각적 토큰 예측 능력은 시각적 입력 이해에서 결과하며 추가 훈련이 최소화됨.

### 실험 결과 및 분석
1. **시각 생성 유도**: 
   - 시각적 이해 데이터를 함께 훈련함으로써, 적은 양의 시각 생성 데이터로 높은 질의 비주얼 토큰 생성 가능.
   - 서로의 능력은 상호 유익하며 서로 강화하는 관계에 있음.
  
2. **MetaMorph 모델**:
   - LLaMA-3.1 8B 기반으로훈련된 MetaMorph는 시각적 이해와 생성에서 경쟁력 있는 성능을 나타냄.
   - MetaMorph는 LLM의 지식을 활용하여 전문 용어에 대한 정확한 시각 토큰을 생성함.
   - 모델이 문제를 해결하기 위해 암묵적인 추론 단계를 수행할 수 있다는 증거도 있음.

### 결론
- LLM과 비전 인코더 간의 충분한 협동을 통해 시각적 생성 능력과 이해 능력 모두를 향상시킬 수 있음을 시사함.

## KEYWORD
- Multimodal Large Language Models (MLLMs)
- Visual Instruction Tuning
- Visual-Predictive Instruction Tuning (VPiT)
- Pretrained Vision Encoder
- Pretrained Language Model
- Cross-Attention Modules
- MLP
- Image-Text Question-Answer Pairs
- Diffusion Model

### Table 1. MetaMorph 성능 비교
|   Method   | Base LLM       | MMBenchEN | SEED  | RealworldQA | ... | COCO (FID) |
|------------|----------------|-----------|-------|-------------|-----|------------|
| Visual Understanding Only | GPT-4V*      | 75.8     | 69.1  | 61.4        | ... | -          |
| Visual Generation Only     | Stable Diffusion 1.5* | -         | -     | -          | ... | 9.6        |
| Unified Models            | MetaMorph (ours) | LLaMA-3.1 8B | 75.2     | 71.8  | 58.3        | ... | 11.8       |

### Figure 1
- VPiT 훈련, 추론 및 MetaMorph 예제.
- 데이터 수집 과정과 비주얼 생성 단계의 상호 작용 설명.

---

## REFERENCES

# 연구 요약

이 논문에서는 LLM과 비주얼 태스크를 결합하기 위해 MetaMorph라는 새로운 모델을 제안합니다. 이 모델은 다양한 멀티모달 태스크를 수행할 수 있는 능력을 갖추고 있으며, 비주얼 이해 및 생성의 상호작용을 검토합니다.

## A 훈련 세부사항 및 하이퍼파라미터

- **MetaMorph 훈련**
  - 이전 연구에서 기술한 2단계 훈련 방식을 따릅니다.
  - 첫 단계에서는 두 개의 레이어 MLP를 사용하여 비주얼 토큰과 LLM 간의 어댑터를 사전 훈련합니다.
  - 두 번째 단계에서 비전 백본을 제외한 전체 모델을 미세 조정합니다.
  
- **확산 비주얼라이저 훈련**
  - Stable Diffusion 1.5와 같은 사전 훈련된 확산 모델을 활용합니다.
  - 입력 차원을 2048로 매핑하여 교차 주의 차원과 정렬합니다.
  
## B 벤치마크 평가

- **MMBench**: 멀티모달 능력의 기준.
- **Seed**: 시각적 태스크 중심의 기준.
- **V*STAR**: 고해상 이미지의 세부 사항 테스트를 위한 VQA 기준.
  
## C 데이터

- **데이터 구성**
  - 다양한 출처에서 데이터 수집하여 LLM이 여러 태스크를 통해 미세 조정될 수 있도록 함.
  
- **데이터 전처리**
  - 다양한 포맷으로 전처리하여 훈련에 적합하게 변환합니다.

## D 시각적 토큰 생성

- **visual generation 성능을 발휘하기 위한 샘플 수 요구 사항**
  - 훈련 성능이 서로 다른 결합 수행의 영향을 탐구했습니다.
  
- **다양한 LLM에서 훈련 결과**
  - LLaMA-3, LLaMA-3.1 및 LLaMA-3 70B의 성능을 측정하여 비주얼 이해와 생성에서의 개선을 도출하였습니다.

## 표 및 그림

- **표 2**: 모든 실험에 대한 구현 세부사항과 하이퍼파라미터.
- **표 3**: 서로 다른 손실 함수 비교.
- **표 4**: 생성 데이터 단독 훈련 vs 추가 데이터와의 공동 훈련 결과.

## 키워드

- LLM
- MetaMorph
- MLP
- GELU
- Vision-Language Models
- ImageQA
- VideoQA
- Instruction Tuning
- Diffusion Models
- VQA
- CLIP Score
- FID Score

이 정보를 바탕으로 논문의 깊은 이해를 도와주기 위한 기술적 세부 사항을 요약하였습니다.

---

