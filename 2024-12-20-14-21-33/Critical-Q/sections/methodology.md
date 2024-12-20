Our Critical-Questions-of-Thought (CQoT) approach can be summarised by the
four steps illustrated in Figure 2. The chosen name already hints at the main
component of this technique, i.e., the critical questions, whose contribution
occur in Step 2 of the pipeline. For each CQ we identify which elements of
Toulmin’s model the question targets. Note that we are not trying to claim
that an LLM follows the Toulmin model of argumentation, but rather that
LLMs engage in presumptive reasoning, and so a set of CQs that cover all
the elements of Toulmin’s general schema of presumptive reasoning provide a
suitable battery of queries with which to test any conclusions that an LLM
comes up with. The leveraged critical questions are:
1. Does the reasoning process start with clearly defined premises? (Data)
2. Are the premises supported by evidence or accepted facts? (Data)
73. Does the reasoning process use logical connections between premises and
conclusions? (Warrant)
4. Are the logical connections used in the reasoning process valid? (Warrant)
5. Does the reasoning process avoid fallacies or logical errors? (Warrant,
Backing)
6. Is the conclusion logically derived from the premises? (Claim)
7. Is the reasoning process consistent with established knowledge or princi-
ples? (Backing)
8. Does the reasoning process lead to a conclusion that is plausible and rea-
sonable? (Claim, Qualifier, Rebuttal)
The reasoning is critically evaluated against these questions, with a conclusion
being ruled out unless a majority of the CQs are answered positively.
Aligned with the open science principle, we tested our approach by resorting
only to freely available LLMs, either open source (e.g., hosted on HuggingFace)
or through a free plan. In particular, we chose Gemini 1.5-pro-001 due to its
being among the top-performing ones at the time of the experiments, and we had
access to it thanks to the free credits provided by Google Cloud. Similarly, given
their high performances and the availability of a free plan, we also picked GPT-
4oandClaude Sonnet 3.5 (both October 2024 versions). Finally, we opted for
Llama 3.1-70b-Instruct andNemotron-51b-Instruct because, once again, they
were among the top-tier open-sourced LLMs for their size category at the time
of the experiment. We also tried to diversify the models as much as possible by
selecting the products of different companies to test our approach on a broader
spectrum of samples.
3.1 Critical-Questions-of-Thought pipeline
Critical-Questions-of-Thought is a simple approach that can be implemented
on top of any LLMs. In this section, we introduce and break down each of
the four stages that compose the CQoT pipeline, as depicted in Figure 2. In a
nutshell, Steps 1, 2 and 4 can be interpreted as different prompting strategies
leveraging the outcome of the previous steps. Step 3 operates as a checkpoint.
It verifies the model’s responses to the CQs and decides whether the pipeline
should continue to the final phase or iterate over, effectively starting again from
the initial stage. More precisely:
•Step 1. Prompt the LLM to reason logically about the input query and
sketch a plan to follow. The model must divide each reasoning process
into premises and conclusions so that each conclusion derives from the
respective premises. No final response should be provided.
8•Step 2. The model will now have to assess the validity of the previously
envisaged reasoning steps by checking whether they address the critical
questions devised in Section 3. All such CQs are related to the validity of
logical reasoning and refer to specific elements of the Toulmin representa-
tion of arguments.
•Step 3. The model has to evaluate the replies to the critical questions.
If there are at least 7/8 positive answers, then the pipeline will move to
Step 4 . Otherwise, the pipeline will start again from Step 1 . This will
occur for a maximum of five iterations, after which the requirement will
drop to a minimum of 5/8 positive answers. If this score has not been
reached after a total of ten iterations, the pipeline will, regardless, move
toStep 4 with the latest generated reasoning plan.
•Step 4. Having determined the correctness of the model reasoning pro-
cess, the LLM is now required to strictly follow it in order to provide the
final reply to the original user prompt.
CQoT proceeding has been automated as a Python class, and we publicly share
the code on our GitHub repo. Notice that, in order to use the script, we need
to have access to the underlying LLM weights. Alternatively, our approach can
also be leveraged by proprietary models by manually following the four-step
pipeline and their specific prompts (see Figure 7 in the Appendix for in-depth
instructions), where the user will act as the ‘verifier’ (Step 3). As a comparative
example of the results achieved by the CQoT approach against the baseline
model, we can examine Figure 3. Here, we can see how Llama 3.1 70b-Instruct,
when challenged by a logical puzzle, outputs the wrong response. However,
when leveraging the CQoT pipeline (hidden for simplicity in this instance), the
LLM answers correctly. More precisely, given the riddle:
“Each problem consists of three statements. Based on the first two
statements, the third statement may be true, false, or uncertain. n1.
Oranges cost more than apples. n2. Oranges cost less than bananas.
n3. Bananas cost more than apples and bananas cost more than
orange. If the first two statements are true, then the third statement
is”
the baseline model replied “If the first two statements are true, then the third
statement is FALSE.” , whereas the CQoT augmented counterpart rightly re-
sponded “If the first two statements are true, then the third statement is true.” .
4 Evaluation
4.1 Experimental setup
In this section, we lay out the specifics of how we appraised the CQoT pipeline
(Figure 2) against the chosen LLMs in their standard and CoT-augmented ver-
9 
 
 
“Each problem consists of three statements. Based on the 
first two statements, the third statement may be true, false, 
or uncertain. \n1. Oranges cost more than apples. \n2. 
Oranges cost less than bananas. \n3. Bananas cost more 
than apples and bananas cost more than orange. \nIf the 
first two statements are true, then the third statement is” 
Llama  3.1 70b -Instruct  Llama  3.1 70b -Instruct with CQoT  
If the first two statements are true, then the 
third statement is FALSE. Here's why: 
 
- Statement 1 says oranges cost more than apples.  
- Statement 2 says oranges cost less than bananas.  
- Combining the two statements, we can conclude 
that bananas cost more than apples (since oranges 
cost more than apples and bananas cost more than 
oranges).  
- However, the third statement also says bananas 
cost more than oranges, which is correct based on 
the first two statements. But the third statement 
also says bananas cost more than oranges and 
apples, which is partially incorrect since it 
should be bananas cost more than oranges and 
oranges cost more than apples.  
 
So, the correct conclusion is that bananas cost 
more than oranges, and oranges cost more than 
apples. 
 **Step 1: Understand the Given Statements ** 
 
- Statement 1: Oranges cost more than apples.  
- Statement 2: Oranges cost less than bananas.  
- Statement 3: Bananas cost more than apples and bananas 
cost more than oranges . 
 
**Step 2: Analyze Statement 1 ** 
 
- Oranges > Apples (in terms of cost ). 
 
**Step 3: Analyze Statement 2 ** 
 
- Oranges < Bananas (in terms of cost ). 
 
**Step 4: Combine the Implications of Statements 1 and 2 ** 
 
- From Statement 1 and Statement 2, we can deduce the cost 
hierarchy: Apples < Oranges < Bananas . 
 
**Step 5: Evaluate Statement 3 Against the Combined 
Implications**  
 
- Part A of Statement 3: Bananas cost more than apples. This 
is true based on the hierarchy (Apples < Oranges < Bananas).  
- Part B of Statement 3: Bananas cost more than oranges. 
This is also true based on the hierarchy (Apples < Oranges < 
Bananas).  
 
**Step 6: Assess the Truth Value of Statement 3**  
 
- Since both parts of Statement 3 are true based on the 
hierarchy established from the first two statements, 
Statement 3 is true.  
 
**Conclusion**  
 
 - If the first two statements are true, then the third  
   statement is true.          Question      
? Figure 3: Comparison between the responses given by the baseline Llama 3.1 70b-Instruct
(wrong, red coloured) and its CQoT counterpart (correct, green coloured). Notice that the
multiple ‘Step’ mentioned in the latter reply do not refer to the CQoT pipeline: it is just how
the output has been phrased by the model.
sions. We also tested the same baseline models by means of an ablation study.
Through a slightly modified version of the previously outlined CQoT pipeline
obtained by skipping the second and third stages (Figure 4), we checked whether
the addition provided by the CQs is what increases the LLMs’ reasoning per-
formances. Our findings showed that the presence of CQs indeed enhances the
models’ ability to reply logically. Once again, we share all the evaluation results,
including LLMs’ responses, judge scores and their mean, on our GitHub repo.
4.1.1 Parameters
We previously reported that the experiment has been conducted with both
open source and (free plan version of) proprietary LLMs. Where we had access
to the full models’ inference parameters, i.e., with Llama 3.1-70b-Instruct and
Nemotron-51b-Instruct, we tuned them as follows. return full text: False;
temperature: 0.8 (temperature: 0.2 for Step 2 and Step 4, which need to be
as objective as possible); topp:0.95;dosample: True; maxnewtokens: 2000.
The underlying idea of this setting was to control the creativity of the LLM
while saving the available compute. When leveraging Gemini 1.5-pro-001 on the
Google Vertex AI platform, we were able to adjust fewer parameters: temperature: 1
(temperature: 0 for Step 2 and Step 4, which need to be as objective as possi-
10ble); topp:0.95;maxnewtokens: 8192. The rationale behind the latter value
mostly stems from the presence of fast computing resources on the platform.
4.1.2 MT-Bench
As mentioned earlier, we opted for MT-Bench math and reasoning questions2
to assess the performances of our pipeline. Unfortunately, it is a well-known
issue that popular benchmark data may contaminate the models’ training data,
thus affecting the validity of the LLMs’ output. This problem has led the AI
community to devise alternative evaluation methods such as LiveBench, which
contains frequently updated questions from recent information sources [59], and
Chatbot Arena, an open platform to appraise LLMs via human preferences
[11]. Although MT-Bench has been available for about a year at the time of the
writing [63] and the risk that the models’ training data has been contaminated
with MT-Bench prompt exists, we tested the same LLMs with and without
CoT and CQoT, thus ensuring a fair comparison of the performances (i.e., if
the baseline has been contaminated, so is the CoT and the CQoT version,
therefore effectively putting them on equal ground for evaluation)3. For the
CoT-augmented version of the underlying model, we employed a specific prompt,
as detailed in Figure 9. Overall, each harnessed model has been input with a
total of 40 questions, evenly divided between reasoning and math topics. We
argue that the collected answers suffice to render a meaningful sample of the
differences between the standard LLM, its CoT implementation, and the CQoT
pipeline.
4.1.3 Ablation study
To effectively verify that the CQoT results were indeed dependent on the probing
impact of the critical questions, we devised an additional test. We evaluated
both Llama 3.1 70b-Instruct and Nemotron-51b-Instruct on a slightly different
pipeline composed only of the first and fourth steps of the CQoT method. We
opted for these two models out of the five we previously examined due to their
being open-source and thus being easier to use for reproducing our findings. The
idea was to determine whether the strengths of the CQoT approach lay solely
in the envisaged reasoning plan or whether the presence of CQs was granting
further improvements. The full pipeline leveraged for this ablation study is
described in Figure 4, whereas the respective prompts are presented in Figure
8 in the Appendix.
2We closely followed the MT-Bench prompts as stored on HuggingFace.
3Indeed, using MT-Bench, in this case, provides a stiffer test for the CQoT approach than
using a benchmark that we know has not been contaminated. If there is contamination, it will
tend to raise the performance of the LLMs on MT-Bench, reducing the headroom for CQoT
to improve their performance.
11Prompt LLM to 
reason logically.
Each reasoning 
step is split into 
premise & 
conclusionPrompt LLM to 
provide the answer 
following protocol 
devised in STEP 1STEP 1 STEP 4Figure 4: Two-step pipeline for the ablation study.
4.1.4 LLM as a Judge
Drawing from the research of Zheng et al. [63], where it has been established
how state-of-the-art LLMs can achieve an agreement rate on par with human ex-
perts when assessing model responses, we followed a similar evaluation strategy.
When choosing the judge, we considered both GPT-4o and Claude 3.5 Sonnet
as promising options. The former was better at appraising math questions, and
the latter was stronger at assessing reasoning queries [48]. Given that, at the
time of the experiment, the free tier version of GPT-4o (October 2024 version)
was more generous than Claude in granting a larger number of requests per day,
we selected the first as the judging model. The prompts provided to evaluate
the LLMs’ response quality are also taken from the study conducted by Zheng
et al. [63], although we slightly reshaped such prompts to better reflect the
task of handling only reasoning and math-related queries (see Figure 10 in the
Appendix). Such prompts instruct the judging model to assess responses us-
ing a 1-10 scoring system, where higher grades mean better performances. To
avoid fluctuations in the judge rates and restrict the potential randomness of
the outcome, we manually prompted GPT-4o multiple times for each answer to
be evaluated until the same score occurred three times. Such a score was then
identified as being representative of the response of the appraised model. We
argue that this method ensures a more reliable grading of the evaluated answers
compared to single scoring. Additionally, there were instances where we further
prompted the judge with follow-up inputs. In particular, we employed a specific
instruction (see Figure 11 in the Appendix) that proved useful in balancing the
assessment whenever the score penalized the lack of conciseness (a criterion,
we believe, is not fundamental when testing reasoning capabilities). We also
repeated the reference answer when the judge wasn’t properly acknowledging it
12(although this was an event that seldom occurred).
4.2 Results
Results of the laid-out evaluation, obtained by testing the whole pipeline, can
be seen in Tables 1, Figure 5 and Figure 6, whereas the outcome of the follow-
up ablation experiment, comparing a pipeline composed only by Step 1 and
4 against the baseline and its CQoT version, can be seen in Table 2. Both
tables are arranged in a similar way, emphasizing in bold the LLMs’ highest
performance according to the task (math or logical reasoning) and the technique
harnessed (standard baseline, Step1 4, CoT or CQoT). The numbers displayed
are the mean of the values scored (i.e., assigned by the LLM judge) by a model
under a task with a specific technique. Figure 5 graphically showcases the same
average numbers by means of a barplot, focusing on the baseline and CQoT,
separating the two tasks of comparison. Figure 6 provides a more detailed
visualization of the mean scores (points) per model per task and the respective
standard errors (bars). The collected data is examined in the next section.
ModelsMT-Bench (Reasoning) MT-Bench (Math)
Standard CoT CQoT Standard CoT CQoT
Claude Sonnet 3.5 8.6 8.55 8.95 9.25 9.8 9.8
GPT-4o 8.3 8.2 8.45 9.5 8.95 9.6
Gemini 1.5-pro-001 8.45 8.25 8.9 8.75 8.85 9.65
Llama 3.1-70b-Instruct 8.05 7.5 8.4 8.95 9.35 9.55
Nemotron-51b-Instruct 6.75 7.7 7.3 8.75 8.55 9.15
Table 1: Evaluation scores (mean) in a range of 1-10, with the highest results per row
highlighted in bold.
ModelsMT-Bench (Reasoning) MT-Bench (Math)
Standard Step1 4CQoT Standard Step1 4CQoT
Llama 3.1-70b-Instruct 8.05 8.3 8.4 8.95 9.25 9.55
Nemotron-51b-Instruct 6.75 6.85 7.3 8.75 9 9.15
Table 2: Evaluation scores (mean) in a range of 1-10, with the highest results per row
highlighted in bold. The table compares the outcomes ensuing from the baseline and the full
CQoT pipeline with the results achieved by following Step 1 and Step 4 only.
4.3 Analysis
Employing the CQoT pipeline creates a significant increase in the performance
of models on the MT-Bench Reasoning and Math tasks when compared with
both the baseline performance (the raw LLM output) and the performance of
the LLMs augmented with CoT. These improvements are particularly marked
13Figure 5: Comparison between performance achieved by the baseline model with (CQoT)
and without (Standard) the Critical-Questions-of-Thought approach.
for GPT-4o, Gemini 1.5-pro-001 and Llama 3.1-70b-Instruct. They are some-
what less impressive for Claude Sonnet 3.5, where CoT and CQoT give the
same performance on the Math benchmark, and for Nemotron-51b-Instruct,
where CQoT performs worse than CoT on the Reasoning benchmark. However,
considering these as 20 separate tests (CQoT against the baseline and against
CoT on two domains and across five models), CQoT has the undoubted best
performance on 18 of these separate tests and has the joint best performance on
another (Table 1). The magnitude of the overall improvement can be appreci-
ated in Figure 6, where CQoT exhibits a lower standard error for the majority of
the samples considered, thus showing more stability than the standard and CoT
approach. Furthermore, we can quantify the enhancement achieved by CQoT
by expressing its results as a percentage, as shown in Table 3. The four columns
represent the difference between the mean scores obtained by CQoT with the
baseline and the CoT mean scores, respectively. The average of such values
is +4.61% for reasoning questions and + 5.4% for math questions, meaning
that our technique ensures an overarching improvement of approximately 5%
against the other contending approaches. Finally, notice how, thanks to CQoT,
the open source Llama 3.1-70b-Instruct outperforms the baseline responses of
the proprietary GPT-4o (also rumoured to be a much larger model) on the
MT-Bench Reasoning tasks whilst exceeding all the proprietary LLMs on the
MT-Bench Math queries. Similarly, Nemotron-51b-Instruct, which is an even
smaller model, exceptionally manages to score higher than Gemini 1.5-pro-001
145678910
Standard.scoreCoT.scoreCQoT.scoreMean scorecategorymathreasoningClaude Sonnet 3.5
5678910
Standard.scoreCoT.scoreCQoT.scoreMean scorecategorymathreasoningLlama 3.1−70b−Instruct
5678910
Standard.scoreCoT.scoreCQoT.scoreMean scorecategorymathreasoningGemini 1.5−pro−001
5678910
Standard.scoreCoT.scoreCQoT.scoreMean scorecategorymathreasoningGPT−4o
5678910
Standard.scoreCoT.scoreCQoT.scoreMean scorecategorymathreasoningNemotron−51b−Instruct
5Figure 6: Comparison between performance achieved by the baseline model (Standard), its
CoT augmented version (CoT) and the Critical-Questions-of-Thought approach (CQoT). The
point represents the mean score, and the bars are the standard error.
on mathematical questions. As a last remark, we observed how the role of crit-
ical questions in probing the reasoning plan sketched by the underlying model
is essential in steering the final output towards better (more correct) responses.
Indeed, results from the ablation study (Table 2) show how CQs describe the
rationale behind the performance enhancement. Nonetheless, it is interesting
to see that a pipeline composed only of Steps 1 and 4 would still score higher
than the standard baseline, emphasising how each stage of the CQoT approach
15contributes to the LLM’s improved output.
Models + CQoTMT-Bench (Reasoning) MT-Bench (Math)
Standard CoT Standard CoT
Claude Sonnet 3.5 +4.06% +4.68% +5.95% +0%
GPT-4o +1.81% +3.04% +1.05% +7.26%
Gemini 1.5-pro-001 +5.33% +7.88% +10.29% +9.04%
Llama 3.1-70b-Instruct +4.35% +12% +6.70% +2.14%
Nemotron-51b-Instruct +8.15% -5.19% +4.57% +7.02%
Average +4.74% +4.48% +5.71% +5.09%
Table 3: Percentage of CQoT performances listed in Table 1. The columns ‘Standard’ display
the score obtained by confronting CQoT with the baseline model results. ‘CoT’ columns
showcase the score obtained by comparing CQoT with the baseline model augmented with
CoT.