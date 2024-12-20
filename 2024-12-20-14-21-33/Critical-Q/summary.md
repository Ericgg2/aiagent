## CONCLUSION

# 요약

- **Large Language models (LLMs)**는 고급 추론 도구를 나타내지만, 여전히 논리적 및 수학적 문제에 직면했을 때 여러 가지 문제에 직면한다.
- 이러한 문제를 해결하기 위해 **argumentation theories**와 **test-time compute inference** 패러다임을 결합한 솔루션을 제안한다. 후자는 모델이 출력하기 전에 '생각할 시간'을 더 주는 아이디어로 요약될 수 있다.
- 전자는 **Toulmin’s tradition**의 주장의 패턴 구성 요소와 주장의 유효성을 검증하기 위한 **critical questions** 개념을 의미한다. 
- 우리의 솔루션은 이러한 모든 요소를 **Critical-Questions-of-Thought (CQoT)**라는 파이프라인으로 통합하여 LLM의 추론 성능을 향상시킬 수 있다.
- CQoT는 **MT-Bench Reasoning** 및 수학 문제에서 평가되었으며, 다섯 개의 다른 모델, 독점 및 오픈 소스를 사용하여 테스트되었다.
- 평가 결과 CQoT는 기본 모델과 **Chain-of-Thought**로 증강된 버전 모두를 능가하며, 응답의 정확성과 유용성에서 평균 5% 향상을 보였다.

# 감사의 글
UK Materials and Molecular Modelling Hub의 계산 자원에 감사드리며, 이는 부분적으로 EPSRC의 지원을 받는다 (EP/T022213/1, EP/W032260/1 및 EP/P020194/1).

# KEYWORDS
- Large Language models (LLMs)
- argumentation theories
- test-time compute inference
- Toulmin’s tradition
- critical questions
- Critical-Questions-of-Thought (CQoT)
- MT-Bench Reasoning
- Chain-of-Thought

---

## METHODOLOGY

## 연구 요약

### CQoT 접근 방식
- CQoT 접근 방식은 Figure 2에서 설명된 네 가지 단계로 요약된다.
- 이 방법의 주요 요소인 '비판적 질문(CQ)'는 파이프라인의 2단계에서 사용된다.
- 각 CQ는 Toulmin의 모델에서 어떤 요소를 목표로 하는지 식별한다.
- LLM이 Toulmin의 논증 모델을 따르지 않는다고 주장하지 않지만, LLM은 추정적 추론을 사용하며, Toulmin의 일반적인 스키마를 포함하는 CQ 세트를 통해 LLM이 도출한 결론에 대해 테스트할 수 있다.

### 사용된 비판적 질문
1. 사고 과정이 명확하게 정의된 전제로 시작되는가? (Data)
2. 전제가 증거 또는 인정된 사실에 의해 지지되는가? (Data)
3. 논리적 연결이 전제와 결론 사이에서 사용되는가? (Warrant)
4. 사고 과정에서 사용된 논리적 연결이 유효한가? (Warrant)
5. 사고 과정에서 오류나 논리적 오류를 피하는가? (Warrant, Backing)
6. 결론이 전제에서 논리적으로 도출되는가? (Claim)
7. 사고 과정이 확립된 지식 또는 원칙과 일관되는가? (Backing)
8. 사고 과정이 그럴듯하고 합리적인 결론으로 이어지는가? (Claim, Qualifier, Rebuttal)

- 응답은 이러한 질문에 비판적으로 평가되며, 대부분의 CQ에 대해 긍정적으로 응답해야 결론에 도달할 수 있다.

### 실험 설계
- 우리 접근 방식을 테스트하기 위해 오픈 소스 LLM만 사용했다.
- 특히, 최고의 성능을 보여준 Gemini 1.5-pro-001을 선택했다.
- GPT-4o와 Claude Sonnet 3.5도 선택하였다. 
- 여러 회사의 다양한 모델을 선택하여 폭넓은 샘플에서 접근 방식을 테스트하였다.

### CQoT 파이프라인
- CQoT는 모든 LLM 위에 구현할 수 있는 간단한 접근 방식이다.
- 각각의 네 단계는 아래와 같이 설명된다.
  1. LLM에 입력 쿼리에 대해 논리적으로 추론하도록 유도하고 계획을 작성하도록 요청한다.
  2. 모델이 비판적 질문에 의거하여 이전의 추론 단계를 평가하도록 한다.
  3. 모델이 비판적 질문에 대한 응답을 평가한다. 7/8 이상의 질문에 긍정적인 응답이 있을 경우 4단계로 진행된다.
  4. LLM이 최종 응답을 제공하기 위해 사고 과정을 엄격하게 따르도록 요구한다.

### 평가
- 실험은 CQoT 파이프라인을 기준 모델과 CoT 증가 모델과 비교하여 평가하였다.
- Llama 3.1 70b-Instruct와 Nemotron-51b-Instruct를 사용하여 제거 연구(ablation study)를 수행하였다.
- CQoT 접근 방식은 패러미터 조정과 함께 LLMs의 성능을 향상시킨다는 결과를 보였다.

### 실험 결과
- 연구 결과, CQoT를 통한 모델의 성능이 기준 성능 및 CoT 접근 방식에 비해 향상되었다.
- 결과는 다음과 같다:

| 모델                     | MT-Bench (Reasoning) | MT-Bench (Math) |
|--------------------------|-----------------------|------------------|
| Claude Sonnet 3.5       | 8.6                   | 9.25             |
| GPT-4o                   | 8.3                   | 9.5              |
| Gemini 1.5-pro-001       | 8.45                  | 8.75             |
| Llama 3.1-70b-Instruct   | 8.05                  | 8.95             |
| Nemotron-51b-Instruct    | 6.75                  | 8.75             |

- CQoT 성능에서 평균 약 5%의 향상을 보였다.

### 결론
- CQoT 접근 방식은 LLM의 논리적 응답성을 향상시키는 비판적 질문의 역할이 중요함을 강조하였다. 이를 통해 CQoT가 향상된 추론 결과를 도출한다는 것을 보여주었다.

## KEYWORD
- Critical-Questions-of-Thought (CQoT)
- LLM (Large Language Model)
- Toulmin’s model
- Data
- Warrant
- Claim
- Backing
- Qualifier
- Rebuttal

---

## DISCUSSION

## 요약

이 연구는 LLMs(대형 언어 모델)의 문제 해결 능력을 향상시키기 위해 '사고할 시간을 더 주는 것'이 효과적이라는 가설을 검증합니다. LLMs가 인퍼런스 중에 더 많은 시간을 갖게 되면, 복잡한 추론 문제를 해결하는 능력이 증가한다고 주장합니다. 또한, 인간의 사고의 주된 특징 중 하나인 논쟁적 본질의 중요성을 강조하며, 이는 지식의 응집을 위해 특정 정보를 도전(또는 지지)하는 주장 형성의 기초가 됩니다. 이 연구는 CQoT 접근 방식이 CQs(비판적 질문)를 활용하여 LLMs의 논리 및 수학적 기술을 향상시키는 파이프라인을 제안합니다.

### 1. CQoT 파이프라인의 구동 엔진
- CQoT 파이프라인의 주된 엔진은 Step 1에서 생성된 reasoning protocol로, 이는 LLM의 사고 과정을 이끌어 냅니다.
- LLM의 응답은 이 프로토콜에 의존하며, 제공된 reasoning plan에 오류가 있을 경우 잘못된 응답을 초래할 수 있습니다.

### 2. CQs의 역할
- Step 2 및 Step 3에서 구현된 CQs는 잘못 설계된 프로토콜을 걸러내는 데 도움을 줍니다.
- 그러나 덜 성능이 뛰어난 모델은 여전히 테스트를 회피할 수 있습니다.

### 3. CQoT의 효과
- CQoT 덕분에 LLM은 잠재적 응답 중에 올바른 답변이 최소한 한 번 나타날 경우, 올바른 응답을 출력할 가능성이 높아집니다.
- CQoT를 통해 완전히 '새로운' 응답을 생성하는 능력은 관찰되지 않았습니다.

### 4. 모델 평가에서의 발견
- 모델 평가 중 대부분의 기본 모델은 CoT 없이 더 나은 성능을 보이는 것으로 나타났습니다.
- 이는 training 또는 post-processing 단계에서 이미 전략적 사고 방식을 결합했기 때문일 수 있습니다.

### 5. 장점
- CQoT 접근 방식은 언급한 바와 같이, 작은 오픈 소스 모델이 GPT-4o, Gemini 1.5-pro-001과 같은 대형 모델을 성능에서 능가하게 합니다.
- CQoT 프로세스는 특정 모델이나 아키텍처에 의존하지 않으며, 다양한 기술과 전략을 추가로 사용할 수 있도록 합니다.

### 6. 한계
- GPT-4o는 평가에서 드물게 해석 오류를 범했습니다.
- CQoT 접근 방식은 한정된 LLMs에 대해서만 테스트되었고, 모든 모델에서 성능을 보장할 수는 없습니다.
- 모델 추론 중의 처리 시간은 몇 초에서 몇 분이 걸릴 수 있습니다.

### 7. 관련 연구 및 향후 연구 방향
- Toulmin의 모델과 관련된 비판적 질문의 개념은 다른 연구자들에 의해 탐구되었습니다.
- 향후 CQoT 접근 방식이 LLM의 크기에 따라 어떻게 확장되는지를 연구할 계획입니다.

## 기술 용어
- LLM: Large Language Models
- CQoT: Critical Questions of Thought
- CQs: Critical Questions
- CoT: Chain-of-Thought
- MT-Bench: Multitask Benchmark
- reasoning protocol: 추론 프로토콜

## 표와 그림
- Table 1
- Figure 6

이 내용은 CQoT 접근 방식의 이점과 한계, 그리고 관련 연구에 대한 깊이를 제공하면서 연구의 목적과 결과를 요약합니다.

---

## INTRODUCTION

# 요약

본 연구는 AI 연구의 최근 발전에도 불구하고, 최첨단 Large Language models (LLMs)이 여전히 논리적이고 수학적인 추론에 어려움을 겪고 있다는 문제를 다룬다. 특히, generative AI는 데이터 패턴 식별기로 작용하며, 훈련 데이터에 포함되지 않거나 이전에 접한 적이 없는 추론 문제에 대해서는 성과를 잘 내지 못한다. LLMs는 단순히 특정한 휴리스틱을 기억해낼 뿐, 산술 문제를 다룰 때 적절하게 일반화하지 못하는 경우가 많다.

이러한 문제를 해결하기 위해, 본 연구는 test-time compute 방법론을 활용하여 LLM의 추론 능력을 개선하는 CQoT (Critical-Questions-of-Thought) 접근 방식을 소개한다. 본 연구 결과는 다음과 같다:

- **CQoT 접근법의 도입**: LLM의 추론을 지원하기 위한 새로운 접근 방식을 제시한다.
- **MT-Bench Reasoning 및 Math 작업에 대한 평가**: 다양한 LLM에 대해 제안된 접근 방식의 광범위한 평가를 제공한다.

CQoT 기법은 LLM의 기본 성능에 비해 놀라운 개선을 보여주며, generative AI 모델의 능력을 향상할 수 있다는 test-time compute 가설을 추가적으로 입증하였다. 우리 연구는 오픈 사이언스의 원칙에 부합하여, 연구 시점에서 자유롭게 이용 가능한 LLM만을 이용하였다.

# 섹션 요약

## 제2장: 이론적 배경
- 논증 개념(스킴 및 비판 질문 포함)과 LLMs에 대한 이론적 배경을 제공함.

## 제3장: 방법론
- CQoT 파이프라인의 세부 내용을 기술하고 사용된 방법론을 명시함.

## 제4장: 평가 및 결과 분석
- CQoT 접근 방식을 테스트하여 얻은 결과에 대한 평가 및 분석을 수행함.

## 제5장: 논의
- 결과에 대한 추가 논의를 제공함.

## 제6장: 관련 문헌 및 미래 연구 방향
- 관련 문헌을 검토하고 잠재적 미래 연구 방향을 개략적으로 설명함.

## 제7장: 결론
- 연구의 전체적인 요약과 결론을 제시함.

# KEYWORDS
- Large Language models (LLMs)
- generative AI
- test-time compute
- Critical-Questions-of-Thought (CQoT)
- argumentation theory
- MT-Bench Reasoning
- Toulmin’s schema

결과, 평가 점수 및 전체 파이프라인은 [여기](https://github.com/FCast07/CQoT)에서 확인할 수 있다.

---

## REFERENCES

## 개요
- 저자: Ekin Akyürek, Mehul Damani, Linlu Qiu, Han Guo, Yoon Kim, Jacob Andreas
- 제목: The surprising effectiveness of test-time training for abstract reasoning
- 연도: 2024

## 핵심 포인트
- **연구 목적**: Test-time training이 abstract reasoning에서의 성능 향상에 미치는 영향 분석.
- **방법론**: 
  - 대량의 데이터 세트와 hyperparameter 조정 활용.
  - 다양한 LLMs (Large Language Models)에 대한 실험 수행.
- **주요 발견**:
  - Test-time training이 LLM의 추상적 사고 능력을 유의미하게 향상시킨다는 놀라운 결과 도출.
  - 실험 결과, 기존의 학습 방식보다 더 나은 추론 품질을 보여줌. 

## 부록
- **CQoT 파이프라인**:
  - Figure 2: CQoT 접근법의 절차적 구조 설명.
  - Step 1부터 4까지의 명령어 및 지침 포함.

### 부록 내용 요약
- **Step 1**: 사용자 프롬프트를 읽고 단계별 추론 계획을 수립. 
- **Step 2**: 제공된 추론 단계에 대한 비판적 평가를 진행. 
- **Step 3**: 이전 단계의 정확성을 확인하고 재검토. 
- **Step 4**: 최종 응답을 작성하는 단계.

## 키워드
- Test-time training
- Abstract reasoning
- Large Language Models (LLMs)
- CQoT pipeline
- Hyperparameter tuning

도움이 필요하시면 언제든지 질문해 주세요!

---

## ABSTRACT

## 연구 요약

- 최근 AI 연구에서의 눈에 띄는 발전에도 불구하고, 최신의 Large Language Models (LLMs)조차도 논리적 및 수학적 추론을 수행하는 데 어려움을 겪고 있다는 점을 강조하고 있습니다.
- 연구 결과에 따르면, LLMs는 여전히 (아주 진보된) 데이터 패턴 식별기로 작동하며, 이들이 이전에 본 적이 없거나 학습 데이터에 가까운 샘플이 아닌 추론 문제를 일반화하고 해결하는 데 저조한 성과를 보입니다.
- 이러한 중요한 우려를 해결하기 위해 본 논문에서는 논증 이론의 문헌에서 비판적 질문의 개념을 활용하며, Toulmin의 논증 모델에 특히 중점을 두고 있습니다.
- 비판적 질문의 사용이 LLMs의 추론 능력을 향상시킬 수 있다는 것을 보여줍니다. 모델의 추론 과정 뒤에 있는 논리를 탐구함으로써, LLM은 논리적 오류가 발생하고 있는지를 평가하고, 사용자 요청에 대한 최종 응답을 제공하기 전에 이를 수정할 수 있습니다. 
- 이는 유효한 논증 절차의 골드 스탠다드에서 유래된 개념으로, 결론이 수용된 전제로부터 유도될 때 타당하다는 것입니다.
- 아리스토텔레스의 원칙을 현실적 근사로 바꾸어 설명하자면, 결론은 그렇지 않으면 입증되지 않는 한 유효하다고 할 수 있습니다.
- 이 접근법은 모델의 출력을 추론 파이프라인을 통해 조정하여, 기준선 및 Chain-of-Thought (CoT) 구현에 대한 더 나은 성능을 달성합니다.
- 이를 위해 MT-Bench Reasoning 및 Math 작업에서 제안된 접근법의 광범위한 평가가 다양한 LLM에 대해 제공됩니다.

## KEYWORD  
- Large Language Models (LLMs)  
- 논증 이론 (argumentation theory)  
- Toulmin의 모델 (Toulmin’s model)  
- Chain-of-Thought (CoT)  
- MT-Bench Reasoning  
- Math tasks  
- 추론 (reasoning)  
- 전제 (premises)  
- 결론 (conclusion)  
- 논리적 오류 (logical mistake)  
- 데이터 패턴 (data pattern)

---

## BACKGROUND

## 요약

### 2.1 논증 (Argumentation)
- "Argumentation"이라는 용어는 컴퓨터 과학에서 철학과 인간 추론의 연구에 뿌리를 두고 있는 다양한 작업을 지칭한다.
- Toulmin의 "The Uses of Argument"는 추론에서 결론 뿐만 아니라 결론에 이른 근거도 중요하다는 개념을 공식화하였다.
- Toulmin에 따르면 모든 결론은 "주장(claim)"이라고 하며, 이는 세계에 관한 데이터로 구성되고, 그 주장을 뒷받침하는 보증(warrant)을 제공받는다.
- 모든 주장은 반박(rebuttal)의 대상이 될 수 있으며, 최종 진리는 이 모든 반박을 고려하여 결정된다.
- Toulmin의 schema 예시로 "Harry의 국적"에 대한 추론을 다루며, Harry는 버뮤다에서 태어났지만 그의 영국 시민권이 불확실하다는 사실을 기록한다.

### 2.2 논증 구조 및 비판적 질문 (Argument Structure & Critical Questions)
- Toulmin의 schema는 LLM의 추론을 보강하는 데 필요한 요소들을 제공하며, 현대의 논증 방안 및 비판적 질문을 결합한다.
- 논증의 기초는 사용되는 패턴을 캡처하는 여러 가지 스킴을 통해 작동하는 가정적 추론이 포함된다.
- 중요한 특징은 비판적 질문(CQs)의 목록으로, 이는 스킴이 합리적인 결론으로 이어질 가능성을 강조한다.
- 본 논문에서는 LLM의 추론을 Toulmin schema에 맞춘 구조로 설정하고 비판적 질문을 통해 LLM의 결론의 유효성을 검토한다.

### 2.3 대규모 언어 모델 (LLMs)
- 대규모 언어 모델(LLMs)은 Deep Learning 기술의 정점으로서, transformer 구조로부터 기인하였다.
- ChatGPT의 출시에 따라 generative AI 시스템의 생산과 배포가 폭발적으로 증가하였고, 여러 기술 기업들이 주도하고 있다.
- LLM들은 뛰어난 성능을 가지고 있지만 여전히 복잡한 추론을 요구하는 작업에서는 오류가 발생할 가능성이 있다.
- 일부 연구에서는 LLM이 훈련 데이터를 단순히 암기하는데 능숙하다고 주장하며, 일반화를 잘 하지 못한다고 지적한다.

### 2.3.1 사고 과정 (Chain-of-Thought)
- LLM의 능력을 개선하기 위해 여러 기법들이 개발되었으며, 그 중 Chain of Thought(CoT) 방식이 가장 영향력 있는 방법으로 여겨진다.
- Chain of Thought는 일련의 중간 추론 단계를 상세히 설명하여 더 나은 성능을 달성하는 모형이다.
- Zero-shot-CoT는 특정 작업에 구애받지 않는 간소화된 버전이다.

### 2.4 벤치마크 (Benchmarks)
- LLM의 전체 능력을 평가하기 위해 AI 연구자들은 보다 실용적인 솔루션을 설계하였다.
- MT-Bench는 80개의 도전적인 쿼리를 포함한 포괄적인 벤치마크로, LLM의 다양한 기술 세트를 평가한다.
- 특정 공백을 다루기 위해 본 논문에서는 MT-Bench의 추론 및 수학 문제에만 집중한다.

## KEYWORD
- Argumentation
- Toulmin
- Claim
- Warrant
- Rebuttal
- Backing
- LLMs
- Chain-of-Thought
- Zero-shot-CoT
- Benchmarks
- MT-Bench

---

