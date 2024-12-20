Despite the remarkable leap forward and recent advancements in AI research, it
is a well-known issue that even state-of-the-art Large Language models (LLMs)
1arXiv:2412.15177v1  [cs.AI]  19 Dec 2024experience sustained difficulties with logical and mathematical reasoning [46,
32]. The results seem to suggest that generative AIs still work as (highly
advanced) data pattern identifiers (even in text-to-video models [24]), scor-
ing poorly when the input lies in reasoning problems the models have never
previously seen or that are not close to samples presented in their training
data. Alternatively, it has been postulated that LLMs only memorize a specific
set of heuristics without being able to generalize properly when dealing with
arithmetic [34]. This is somehow surprising given the introduction of the test-
time compute paradigm, where the allocation of more compute time during the
model inference process should ensure better performance [37, 49, 51]. This is
more important than ever now that we are starting to see some diminishing
returns from the previous pre-training scaling law paradigm, i.e., the idea that
increasing training data and model parameters will improve overall performance
[22, 38, 31]. To address this compelling concern, we harness and expand the
promising test-time compute approach (proved to satisfy a scaling law similar
to the previous pre-training hypothesis [10]) by employing the notion of critical
questions from argumentation theory to improve the reasoning capabilities of
LLMs. Harnessing computational argumentation to enhance LLMs’ thinking
processes is briefly explored in the literature and hints at better performance
achievements [8, 6]. However, unlike previous approaches, what critical ques-
tions provide is a mechanism for probing the reasoning process, thus checking
the rationale behind the inferences drawn by the models. Given such examina-
tion, the LLM is able to assess whether some logical mistake is occurring and
can correct it before providing the final reply to the user prompt. The underly-
ing idea is drawn from the gold standard of any valid argumentative procedure:
the conclusion is valid if it is entailed by accepted premises [44]. In other words,
adapting a form of the Aristotelian principle to a real-world context marked
by incomplete information and presumptive reasoning, the conclusion stands
as valid unless disproved. In particular, our work sits within the tradition of
Toulmin’s schema and its defeasible account of argumentative conclusions.
The main contributions arising from this paper can be summarized as:
1. The introduction of the novel Critical-Questions-of-Thought (CQoT) ap-
proach to support reasoning in LLMs;
2. The provision of an extensive evaluation of the proposed approach on the
MT-Bench Reasoning and Math tasks, across a range of LLMs.
Overall, we show that the CQoT technique provides remarkable improvements
over the LLMs’ baseline performance, thus further corroborating the test-time
compute hypothesis: it is possible to enhance the capabilities of generative AI
models by granting more “time to think”. Note that our work is aligned with
the principle of open science, which we advocate for, and hence only makes
use of LLMs that are freely available at the time of the research, either as
open source or through a limited free plan. Results, evaluation scores and
the complete pipeline, rendered as a Python script, can be found at https:
//github.com/FCast07/CQoT .
2The structure of this paper is as follows. We start by providing an overview
of the required theoretical background, focusing on argumentation notions (in-
cluding schemes and critical questions) and LLMs in Section 2. We then proceed
by specifying the methodology employed and by detailing the CQoT pipeline
in Section 3. The evaluation and analysis of the results obtained by testing
the CQoT approach are carried out in Section 4, whereas a further discussion is
given in Section 5. Finally, we review the related literature and outline potential
future work in Section 6, after which we conclude in Section 7.