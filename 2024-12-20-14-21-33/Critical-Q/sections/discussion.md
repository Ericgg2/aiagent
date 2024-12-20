As humans take more time to elaborate and solve hard problems [23], it is
plausible to assume that, by giving more ‘time to think’ to LLMs during in-
ference, the models’ capability to correctly address challenging reasoning issues
should likewise increase. This is exactly what the test-time compute paradigm
has confirmed, especially through LLMs such as OpenAI’s o1 [37], DeepSeek’s
R1-Lite-Preview [49] and Qwen’s QwQ [51]. However, another main feature of
human thinking is its argumentative nature and how it is fundamental to formu-
late arguments that challenge (or support) specific information to consolidate
our knowledge. Indeed, Mercier and Sperber claim that reasoning evolved as
a byproduct of the generation and evaluation of arguments [30]. This notion
underpins the purpose of the critical questions as means to probe the reliability
of the information embedded in the inquired argument. The CQoT approach
combines together CQs, inspired by Toulmin’s model, and the test-time com-
pute paradigm into a pipeline that allows LLMs to enhance their logical and
mathematical skills.
We noticed that the driving engine of the CQoT pipeline is the reasoning
protocol generated in Step 1, which steers the underlying model’s thinking pro-
cess. The LLM’s reply will be reliant on such a protocol, thus possibly leading
to an erroneous response if the provided reasoning plan presents any mistakes.
The employment of CQs (implemented in Step 2 and verified in Step 3) will
mostly filter out each of such wrongly designed protocols, but some may still
be able to elude the test, especially for smaller and less performing models4.
4Notice that we will not be able to address this issue by modifying Step 3 and requesting,
when the replies to the CQs are not all positive, to output the reasoning protocol that occurred
the most during the previous iterations. That is because, even if such a protocol appeared
multiple times, there is no guarantee that it is going to be the most suited for the situation
at hand.
16In general, thanks to CQoT, the underlying LLM is more likely to output the
correct reply if this appears at least once among its potential responses. We
have not observed an ability from the model to output completely ‘new’ replies
(i.e., responses that will never occur in the baseline LLM) due to CQoT. This is
somehow aligned with previous findings [45], suggesting that to optimally lever-
age LLMs’ capabilities, it is often a trade-off between test-time compute and
pre-training. This means that, at times, the model simply needs more ingrained
knowledge to be able to output the correct response.
Surprisingly, while evaluating the models, we realised how most baselines
perform better without CoT, especially on the MT-Bench Reasoning tasks (Ta-
ble 1, Figure 6). This curious behaviour could stem from their training or
post-processing stages, where they may have already been combined with so-
phisticated, holistic thinking strategies, thus scoring poorly when prompted
with Chain-of-Thought, which could break down such entrenched reasoning
processes. Another explanation may relate to how CoT steps could inadver-
tently amplify flawed logic or incorrect premises, which can cascade into the
final answer. However, while reasonable, these are only educated guesses given
that we did not have access to the underlying training data or, particularly for
proprietary models, in-depth strategies working under the hood of such models.
It may be interesting to investigate this odd occurrence in future works.
Overall, we can summarize the pros and cons of our findings as follows.
5.1 Advantages
•The use of the CQoT approach allows open-source (arguably smaller) mod-
els such as Nemotron-51b-Instruct and Llama 3.1-70b-Instruct to outper-
form notably state-of-the-art proprietary (arguably larger) models such
as GPT-4o, Gemini 1.5-pro-001 and Claude Sonnet 3.5 on most of their
baseline outputs.
•The CQoT procedure is highly versatile and works on top of LLMs’ re-
sponses, meaning that it is independent of specific models or their archi-
tecture (e.g., state space model-inspired Mamba [17] or the hybrid Jamba
[26]).
•The outcome of the pipeline presented herein does not prevent the under-
lying models from employing additional techniques (e.g., prompting engi-
neering) or strategies (e.g., multiple sampling) to further enhance LLMs’
capabilities.
5.2 Limitations
•We acknowledge that the judge (GPT-4o) committed mistakes, albeit
rarely, in its evaluation by erroneously interpreting the reference answers
and giving a lower score to the tested models. We correct this by prompt-
ing the reference answer once again, thus solving the unbalanced assess-
ment.
17•Despite the impressive results achieved, we have tested the CQoT ap-
proach only on the reported LLMs. Our idea was to showcase a significant
sample of models to prove the advantage of our pipeline. Nonetheless,
although there does not seem to be any evidence against this, we can-
not guarantee CQoT performances on every other existing model, espe-
cially smaller ones. Indeed, we noticed how Nemotron-51b-Instruct scored
higher with CoT prompting on the MT-Bench Reasoning questions than
with CQoT (Table 1, Figure 6). Given that this trend reverts with Llama
3.1-70b-Instruct, this result may suggest a threshold of 70b parameters
for the Critical-Questions-of-Thought approach to provide superior per-
formances. That could be related to the fact that smaller models are less
prone to utterly follow the provided instructions, an essential condition to
benefit from CQoT. As a disclaimer, we underscore that we are not aware
of the exact model parameters of proprietary models (i.e., GPT-4o, Gem-
ini 1.5-pro-001 and Claude Sonnet 3.5), but we argue that their extensive
fine-tuning and post-training allows them to comply to instructions better
than many other competitors. We plan to investigate how this approach
scales with LLMs’ sizes in a future study.
•Considering that we are leveraging a test-time compute approach that
works during model inference, one of the main limitations will be the
duration of the overall process. Obtaining an output through the CQoT
pipeline may require from seconds to minutes, depending on the available
hardware.
6 Related and Future Work
The notion of critical questions for Toulmin’s model of argument has been ex-
plored by a number of researchers. Among these, we acknowledge the work of Yu
and Zenker [61] where the authors build upon Toulmin’s schema and articulate
a three-part meta-level CQ list to achieve complete and applicable argument
evaluation, that is based on three fundamental attack types: against premise,
inference, and conclusion. However, in contrast to our approach, some of the
CQs are argument scheme-specific and therefore rely on identifying a particu-
lar argument scheme to complete the argument evaluation. Additionally, there
is no mention of a practical combination of such a meta-level approach with
LLMs. The literature also presents studies extending Toulmin’s schema to ad-
dress argument evaluation [54] and to prompt LLMs to output explicitly named
argument components as classified by the schema [18]. Regardless, neither paper
leverages critical questions. Unlike the previous two, the EQRbot [5, 7], devised
to deliver customised healthcare explanations to patients’ requests, makes use
of critical questions to assess the validity of a bespoke argument scheme instan-
tiation. Such a scheme is meant to succinctly convey relevant information to
the user. Nevertheless, although the EQRbot is AI-driven and harnesses CQs,
it does not employ LLMs in particular, nor does it specifically enhance their
18reasoning capabilities.
On the other hand, numerous studies have tried to address some of the
current limitations of LLMs. For example, Freedman et al. [16] propose the use
of LLMs to generate arguments for and against a claim, assigning strengths to
each argument using the LLM itself, and then employing formal argumentation
semantics to determine a final decision. This is designed to allow humans to
gain a better understanding of the reasoning and potential interaction with
the argumentation framework to improve the trustworthiness of the decision
making. Nonetheless, unlike CQoT, the authors did not specifically focus on
appraising the logical and mathematical thinking of the underlying model.
Cumulative reasoning (CR) [62] is another technique aimed at enhancing the
problem-solving capabilities of Large Language Models (LLMs). The authors
demonstrate CR’s superior performance on various complex reasoning tasks
including maths problems. In order to evaluate their proposed approach the
authors use three sources: FOLIO [19], Game of 24 and the MATH [21] data
set. These are different to the types of tasks and benchmarks that we have used,
furthermore, our emphasis has been on scoring the reasoning rather than the
accuracy of the end result. Lastly, this approach does not use computational
argumentation.
Another technique that aims to validate the reasoning of an LLM and specif-
ically to detect factual errors is proposed by [14]. Their approach mimics the
legal process of cross-examination, which bears some similarity to the intent
and use of critical questions. The authors have evaluated their method with
different data sets covering a range of queries and trivia questions. They used
three cross-examination settings that rely on distinct combinations of LLMs and
concluded that their technique shows promising improvements in checking the
factual accuracy and reliability of LLMs. In contrast to ours, the aim of their
evaluation did not include checking the reasoning capability or the quality of
the response but rather focused on factual accuracy.
In the context of LLMs test-time compute scaling, Snell et al. [45] provide
a broader analysis of different approaches and their effectiveness. Chen et al.
[10] outline a two-stage algorithm that generates candidate solutions and then
chooses the best one via a knockout tournament where only the winners, among
each pair of candidates, move on to the next round. Such an algorithm seems to
enhance the underlying models’ capabilities on mathematical and engineering
questions of the MMLU-Pro benchmark [57]. Similarly, Brown et al.’s work
[4] introduces and evaluates a repeated sampling technique to improve models’
output on coding and mathematical tasks. Overall, these papers highlight the
potential of using test-time compute to enhance LLM reasoning abilities but
also describe a much more inconvenient and costly approach compared to the
CQoT approach, which does not require tens (or hundreds) of samples to run.
The pipeline introduced herein can be extended in a number of ways. The
recently discovered test-time training technique, which introduces an on-the-fly
fine-tuning tailored to the problem at hand (the training leverages data obtained
by different variations of the task at hand [1]), has been proven quite successful
against the Abstraction and Reasoning Corpus (ARC) benchmark [13], infor-
19mally denoted as the ‘AGI challenge’ after the publication of the competition on
Kaggle [12]. We argue that the CQoT approach could be combined with test-
time training to augment the LLMs’ performances even further. Analogously, a
cooperative method based on the critique model designed by Xi et al.[60] and
our pipeline would provide larger improvements on difficult mathematical prob-
lems. Lastly, we envisage future research directions on how CQoT scales with
different underlying model sizes and how it interacts with different prompting
techniques.