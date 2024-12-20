This paper combines several components, each representing an essential building
block of the CQoT pipeline introduced herein. In this section, we will unpack
the notions and tools underpinning such a pipeline.
2.1 Argumentation
The term “argumentation”, as used in computer science, refers to a wide range of
work rooted in philosophy and the study of human reasoning. In this tradition, a
seminal work is Toulmin’s “The Uses of Argument” [52] which began to formalize
the idea that in reasoning it is not just the conclusion that is important, but also
the rationale behind the reached conclusion. In Toulmin’s view, all conclusions
are defeasible in the sense that they can be overturned by subsequent inferences.
Conclusions, which Toulmin calls “claims”, are constructed from data about the
world, are supported by a warrant , a motive for thinking that the conclusion
holds, and this itself is derived from some backing (experience or experimental
data). This whole structure is an argument . All claims may be subject to a
rebuttal , and the final truth will only be determined by taking into account all
such rebuttals (each of which is itself an argument), examining the warrants,
and reaching a verdict on which argument is most plausible.
An example of the use of this kind of reasoning, drawn as a formal schema,
and taken from [52], is shown in Figure 1. Here, we are reasoning about the
nationality of an individual “Harry”, under the rules for British nationality that
held at the time that Toulmin was writing. Here, the data is that Harry was
born in Bermuda. From this it was then possible to make the claim that Harry
was British, this conclusion warranted by the fact that, at the time, an indi-
vidual born in Bermuda was a British citizen. (This warrant was itself backed
by the law of the time concerning British nationality.) The schema explicitly
records that the claim is not certain — a fact denoted by the attachment of
aqualifier , such as “presumably” — and the fact that the claim may be sub-
ject to a rebuttal, such as the fact that Harry might have given up his British
nationality.
We will come back to Toulmin’s schema below as a convenient framework
to consider how we might bolster the performance of reasoning in LLMs, but
3Data
WarrantRebuttale.g. A man born in
Bermuda will be a
British subjectQualifier Claim
e.g. Both of his parents were aliens/he became
a naturalized American/... sinceunless
because
Backinge.g. The following statutes and
other legal provisionse.g. Harry was
born in Bermudatherefore
e.g. Harry is a British subjecte.g. PresumablyFigure 1: Toulmin’s schema: the case of Harry’s nationality.
before doing that, we should acknowledge other work in what has a significant
sub-field within research on artificial intelligence.
One way to consider the kind of reasoning captured by argumentation is as a
formal representation that extends classical logic to permit defeasible reasoning.
This is important because it seems that one way of tractably handling the com-
plexity of lots of knowledge about the world is to permit presumptive reasoning,
that is reasoning that allows for “jumping to conclusions”. (This makes it possi-
ble to represent general patterns of reasoning that summarize plenty of specific
information.) However, jumping to conclusions may sometimes lead to incorrect
claims, and these then need to be withdrawn, so any systems of presumptive
reasoning need to be able to reason defeasibly.
As a result, much of the work on argumentation has been concerned with
defeasibility. The earliest work on argumentation within computer science is
due to Loui [29] and Lin [28, 27], the former laying out in broad terms the
capabilities of argumentation, while the latter focussed on capturing existing
systems of nonmonotonic reasoning (such as default logic [42] and autoepistemic
logic [33]). At the same time, Pollock [39, 40] was exploring the possibilities
of argumentation in great detail, examining the structure of arguments and
considering different ways in which one argument might defeat another.
The seminal work in this area, however, is due to Dung [15], who introduced
the idea that one could consider the properties of a set of arguments at a purely
abstract level. Given a set of arguments and a relation that identifies pairs of
arguments where one attacks the other, it is possible to establish several well-
founded principles under which sets of acceptable arguments may be determined.
For example, any argument that is not attacked is acceptable, and any argument
that is attacked by an acceptable argument is not acceptable (this leads to a
simple fixpoint definition of acceptability). This basic idea has been widely
adapted and extended, see for example [3].
2.2 Argument Structure & Critical Questions
Toulmin’s schema provides us with part of what we need to augment LLM rea-
soning, and we combine that idea with the more recent notions of argument
schemes and critical questions [56, 55]. Broadly speaking, the idea behind argu-
4ment schemes is that presumptive reasoning operates through the application
of a number of schemes that capture common patterns of reasoning. Since they
support presumptive reasoning, they are not expected to be deductive in the
truth-preserving sense that classical logic is. Rather, they capture rules for
drawing inferences that will often provide useful conclusions but will sometimes
lead to invalid claims. In that sense, such schemes are more like the default
rules of default logic [42].
One of the key features of argumentation schemes is the list of associated
critical questions (CQs). The role of these questions is to highlight when the
scheme may or may not lead to reasonable conclusions. The premises, claim
(or conclusion) supported by the argumentation scheme are presumptive, and
a premise or claim is withdrawn unless the CQs posed have been answered suc-
cessfully. In general, CQs can also be used as pointers to counter-arguments
that themselves instantiate argument schemes. CQs can then be used in two
different ways: (i) posing CQs to construct counter-arguments that can them-
selves instantiate schemes with their own CQs; (ii) posing CQs to challenge an
existing argument (e.g. questioning a premise) and which can be responded by
constructing a supporting argument.
What we do in this paper is think of the LLM as providing reasoning that
can be structured as per a Toulmin schema, and then use pertinent critical
questions to check the validity of the presumptive conclusions that the LLM
has reached. As described above, Toulmin’s model of argument includes the
following six components:
•Claim - The conclusion or main argument being made;
•Qualifier - Limits or conditions on the claim;
•Data - The facts, evidence, or premises that support the claim;
•Warrant - The logical connection or justification that bridges the data and
claim;
•Rebuttal - Acknowledgment of counterarguments or exceptions to the
claim;
•Backing - Additional support or justification for the warrant.
We thus introduce critical questions that probe whether these elements hold.
(As we shall see in Section 3, we introduce eight critical questions, particularly
targeting the Data and the Warrant components).
52.3 LLMs
Large Language Models (LLMs)1represent one of the current pinnacles of Deep
Learning technology stemming from the transformer architecture [53]. Since
the release of ChatGPT in November 2022 [35], the production and deployment
of generative AI systems have soared, resulting in new model announcements
almost every week. The competition among proprietary companies, the contri-
bution of the open source community and the huge investments made in the
sector over the past two years have certainly yielded impressive advancements
in the AI landscape. The main actors of this progress include tech firms such
as Anthropic, OpenAI, Google, Meta, NVIDIA and many others. In particular,
Anthropic’s Claude 3.5 Sonnet [2], OpenAI’s GPT-4o [36] and Google’s Gemini
1.5 pro [50] have alternated as the top three models (according to a plethora
of different evaluation benchmarks) during 2024. However, despite their out-
standing performances, these models are still prone to errors, especially when
handling tasks that require complex reasoning capabilities. Some studies claim
that LLMs are just proficient at memorizing training data, but still struggle to
generalize and undertake tasks which are unknown or unlike anything they have
previously seen [46, 32].
2.3.1 Chain-of-Thought
To improve LLM capabilities and curtail their shortcomings, several different
techniques have been developed. Some of such approaches involve training,
fine-tuning or other resource-intensive post-processing stages. Researchers also
engaged with lightweight methods which, in some cases, proved even more suc-
cessful than the aforementioned ones. Among these examples, prompting en-
gineering techniques, i.e., practices to effectively craft prompts that optimize
models’ output, have been largely employed to enhance LLM logical thinking
[43]. Chain of Thought (CoT), probably the most influential of such techniques,
consists of a prompting strategy that details a series of intermediate reasoning
steps to achieve better performance in arithmetic, symbolic and commonsense
inferences [58]. Zero-shot-CoT is a streamlined version of CoT that is task-
agnostic and does not require few-shot examples [25]. In the following, we will
leverage the first prompt of this (originally twofold) approach, rendered by the
well-known phrasing “Let’s think step by step” . For simplicity, we will refer to
it just as CoT.
2.4 Benchmarks
In order to assess the overall capabilities of an LLM, thus ranking the best-
performing ones, AI researchers needed to design solutions that were more prac-
1One could argue that the present state-of-the-art consists of Multimodal Models (MMs),
i.e., AI models that accept as input (and provide as output) other media besides language.
Given the nature of the task we want to achieve, in the present work, we resort to experiment-
ing with language and textual input/output only. We will thus use the term “LLMs” even in
those cases where referring to them as MMs might be more accurate.
6Prompt LLM to 
reason logically.
Each reasoning 
step is split into 
premise & 
conclusionPrompt LLM to 
apply 8 CQs to the 
reasoning steps 
provided by STEP 1 
as premises & 
conclusions.
Mark each one as 
Pass/FailGiven the list of 
PASS/FAIL from 
STEP 2 for each of 
the 8 CQs
Go back to STEP 1Prompt LLM to 
provide the answer 
following protocol 
devised in STEP 1If 7/8 or 8/8 are PASS STEP 1 STEP 2 STEP 3 STEP 4
If iteration 
number <6
If less than 7/8 are PASS
If 6< iteration 
number <11If 5/8, 6/8, 7/8 or 8/8 are PASS
If less than 5/8 are PASS
If iteration 
number = 11Figure 2: The four-step process of the CQoT pipeline.
tical than relying on expensive and time-consuming human testing. With this
in mind, multiple benchmarks were created, each focusing on evaluating specific
models’ skill sets [9]. For example, MT-Bench is a comprehensive multi-turn
benchmark that presents 80 challenging queries, divided into two sub-questions
each, covering 8 different domains (writing, roleplay, reasoning, math, coding,
extraction, stem, humanities) and LLMs’ skills (e.g., causal relations detection,
thinking process, creativity, factual knowledge, instructions compliance) [63].
Unlike other popular benchmarks such as Big-Bench Hard [47], MMLU [20], or
GPQA [41], it does not present multiple options to choose from nor it (always)
includes a fully-fledged reference answer. This allows for a more thorough test
of the models’ capabilities in an open-ended setting. Given the specific gap we
would like to address, we will focus only on the reasoning and math questions
included in the MT-Bench.