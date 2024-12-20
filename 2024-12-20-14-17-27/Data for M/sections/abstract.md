The suite of datasets commonly used to train and evaluate the mathematical capabilities of AI-based
mathematical copilots (primarily large language models) e xhibit several shortcomings. These limitations
include a restricted scope of mathematical complexity, typ ically not exceeding lower undergraduate-level
mathematics, binary rating protocols and other issues, whi ch makes comprehensive proof-based evalua-
tion suites diﬃcult. We systematically explore these limit ations and contend that enhancing the capa-
bilities of large language models, or any forthcoming advan cements in AI-based mathematical assistants
(copilots or “thought partners”), necessitates a paradigm shift in the design of mathematical datasets and
the evaluation criteria of mathematical ability: It is nece ssary to move away from result-based datasets
(theorem statement to theorem proof) and convert the rich fa cets of mathematical research practice to
data LLMs can train on. Examples of these are mathematical wo rkﬂows (sequences of atomic, poten-
tially subﬁeld-dependent tasks that are often performed wh en creating new mathematics), which are
an important part of the proof-discovery process. Addition ally, we advocate for mathematical dataset
developers to consider the concept of “motivated proof” , introduced by G. P´ olya in 1949, which can serve
as a blueprint for datasets that oﬀer a better proof learning signal, alleviating some of the mentioned
limitations. Lastly, we introduce math datasheets for datasets , extending the general, dataset-agnostic
variants of datasheets: We provide a questionnaire designe d speciﬁcally for math datasets that we urge
dataset creators to include with their datasets. This will m ake creators aware of potential limitations of
their datasets while at the same time making it easy for reade rs to assess it from the point of view of
training and evaluating mathematical copilots.
∗Corresponding author: simon.frieder@cs.ox.ac.uk . Contributions: S.F. was the project lead, outlined the vis ion, content
and individual sections, and wrote the paper with signiﬁcan t assistance from Jo.B. on all aspects of formal datasets, K. M.C. for
the datasheets section, Ju.B., A.J, F.R. and G.B. for workﬂo ws, J.L. and T.G. for the motivated proof section, and S.W. on the
recommendation subsections, and Ju.B. for the table. R.R.G ., A.G., A.W., and T.L. provided general and strategic feedb ack.
11 AI Systems for Mathematicians – Present and Future
There has been a rapid surge in research around AI for mathematic s. For example, AlphaGeometry was shown
to solve mathematical geometry problems on the level of the Inter national Math Olympiad (IMO) [ Trinh et al. ,
2024], Numina won the ﬁrst AIMO Progress Prize,1by providing a model capable of turning mathematical
questions into executable Python code, and previously GPT-4 [ OpenAI ,2023] was shown to attain, in some
cases, the performance of an undergraduate university studen t [Frieder et al. ,2023a ]. High accuracies on
standard mathematics benchmarks [ Reid et al. ,2024] suggest that many benchmarks may be close to being
solved.
The rapid progress and proliferation of ideas in this space – while excit ing and productive in many ways –
has led to a series of problems due to a lack of alignment across resea rch directions and a lack of coherence
around clear goals. Problems include:
(1) some datasets being overstudied (e.g., the many versions of th e GSM8K dataset [ Cobbe et al. ,2021]),
whereas other data-related aspects (few datasets comprising a dvanced mathematics, or reﬂecting tool
use in mathematics) are neglected;
(2) various workﬂows and reasoning modes of how professional ma thematicians conduct their research are
not represented in datasets;
(3) diﬀerent ways to express the same mathematical content (in f ormal language, vs. in natural language)
have not been uniﬁed;
(4) scalability of evaluation that aligns with the goals of the tools being developed.
Despite these problems, the landscape of machine learning models th at have been devised (and embraced by
parts of the mathematical community) consists primarily of models t hatlie between the two categories
below , based on the amount of interaction with humans they are designed for:
1.Highly specialized, “narrow” models that fulﬁll all of the criteria of 1) being designed for a pre-
cisely deﬁned mathematical domain or mathematical problem, 2) req uiring domain knowledge to be
used (such as formal languages as input), 3) that cannot explain t hemselves, and 4) do not allow free-
form interaction. Examples of such specialized models vary widely in te rms of how their foundations
look like. Specialized models could rely on symbolic reasoners, such as t he recent solver for elementary
geometry (Newclid [ Sicca et al. ,2024] which supersedes AlphaGeometry [ Trinh et al. ,2024]) or for
inequality problems ([ Wei et al. ,2024]). Olympiad-level mathematics problems are within reach of
both. Alternatively, such specialized models could simply be regressio n models, relying on raw math-
ematical data to infer new relationships between mathematical obj ects, such as for knot theory or
representation theory [ Davies et al. ,2021], or group theory [ He et al. ,2023]. Many further approaches
exist [ Romera-Paredes et al. ,2024,Fawzi et al. ,2022]. These systems typically require a signiﬁcant
amount of specialization by a user, such as mastering a formal input language (e.g., AlphaGeometry)
or understanding the machine learning model itself (e.g., [ Davies et al. ,2021]) beyond the necessary
mathematical domain knowledge.
2.General purpose, “broad” models that can interact with humans via natural language, under-
stand input images, and use tools (being able to call, in particular, spe cialized models, which can be
viewed as a particular kind of “tool”, as we argue below), can provide general assistance to a math-
ematician (both with routine tasks, such as literature search, and domain-dependent tasks, such as
counterexample search) and are not tied to a speciﬁc area of math ematics. These are what we refer
to as“Mathematical Copilots” , as their goal is not simply to provide correct proofs but also to
enhance the user’s understanding of the results and guide them to wards their own discoveries [ Collins
et al. ,2024a ]. Currently, the best candidates for these systems are large lang uage models (LLMs),
which we take to include multi-modal models that also admit images as co mponents of the prompt.
1https://aimoprize.com/updates/2024-07-20-progress-p rize-results
2We contend that LLMs represent early predecessors of future g eneral-purpose models (mathematical
copilots), ultimately acting as mathematicians’ “thought partners ” [Collins et al. ,2024b ]. Anecdotal
evidence of such usefulness of current LLMs has been presented in various discussion forums,2while
noting the failures that LLMs often succumb to. However, there a re concrete ways in which LLMs can
be improved to become mathematical copilots: As indicated by the to ol-integrated-reasoning approach,
championed by models such as ToRA [ Gou et al. ,2024] or Numina,3general LLMs can incorporate other
symbolic systems to which they can delegate symbolic tasks to. The m ixture-of-experts paradigm [ Cai
et al. ,2024], on the other hand, highlights diﬀerent ways in which LLMs can incorp orate other LLMs
as specially trained “modules” to which they can delegate mathematic al tasks that are not symbolic
in nature but still require particular mathematical skills. Such a hiera rchical system can help mathe-
maticians both on routine academic tasks (see [ Frieder et al. ,2023b ] for a short, high-level overview)
and specialized ones.
We envision that such models will require signiﬁcantly less eﬀort from u sers to use them, compared
to specialized models, being self-explanatory, where natural langu age is the main mode of interaction.
(While the outlined architectural approaches provide a viable step f orward, in some cases, no data
exists on which to train these models; see below.)
In addition, a third class of models will likely be developed:
3.Fully automated, “universal” models that can generate mathematical theorems and theories
autonomously, merely by being directed to a mathematical result. W e envision that these systems
will be the true successors of automated theorem provers (ATPs ) such as the Vampire [ Riazanov and
Voronkov ,2002,Kov´ acs and Voronkov ,2013] or E [ Schulz ,2002] ATPs. These systems have not been
widely adopted by the mathematical community. While there have bee n attempts to imbue these
systems with (non-LLM) machine learning techniques [ Holden ,2021], these have not yet dramatically
increased their performance. Nonetheless, once general-purpo se models have been established, it is
conceivable one could put these in automation loops to obtain “AI mat hematicians”. For the domain
of AI, this has already been recently investigated in the form of an “ AI Scientist” [ Lu et al. ,2024a ]
that autonomously generated machine learning research articles. These are systems that conceivably
will require minimal human input, merely guiding them towards certain t heorems that one wants to
see analyzed (proved, refuted, with comments on whether slightly diﬀerent variations of a theorem,
with slightly altered hypotheses, admit a proof).
We focus in this article on general purpose models , as outlined above, which are mathematical copilots .
LLMs are currently the systems that hold the most promise to beco me, given a better data foundation, general
purpose models. Fully automated, universal models are currently o ut of reach, as they are contingent on
the former category of models. These are the systems that are u ltimately sought when one speaks of “AI
Mathematicians” [ Bengio and Malkin ,2024]. However, without the proper datasets, it is unlikely that these
will come into existence. Hence, our focus is on the data that is needed to arrive at general-purpose
models, the mathematical copilots . We have deliberately avoided drawing a hard boundary among the
properties a model must fulﬁll to be placed in one of these three bec ause the boundaries will be ﬂuid, as the
levels of automation and required human interaction are continuous scales.
Currently, the existing datasets only support highly specialized mod els and do not put LLMs on a trajectory
to achieve general-purpose models. In this article, we highlight the lim itations of current datasets (Section 3,
which is retrospective) and necessary changes in terms of data th at will be needed to train the next generation
of LLMs that approximate what we outlined general-purpose models to be (Section 4, which is prospective).
Our main reader audience consists of machine learning researchers , as we intend this article to raise awareness
of these issues. Automated theorem provers (ATPs) and interac tive theorem provers (ITPs), which have
a decades-old history [ Harrison et al. ,2014], also had the ambition of realizing the goal of implementing
2https://www.reddit.com/r/math/comments/14p6j5c/tere nce_tao_on_using_gpt4_to_help_with_math/
3https://huggingface.co/AI-MO/NuminaMath-7B-TIR
3mathematical copilots. Unfortunately, history has shown that if t he computer science community and the
mathematical community do not operate in lockstep, there is a risk o f obtaining systems that will not be of
interest to practicing research mathematicians; maybe controve rsially, Blanchette et al. [2012] mentions that
certain eﬀorts to make these systems more user-friendly have pe rhaps reached a “plateau”. (Nonetheless,
ATPs and ITPs have, in other domains, contributed signiﬁcantly to d riving the ﬁeld of software automation
forward.)
One of the goals of this paper is to make sure that the renewed eﬀor t by computer scientists and machine
learning researchers to provide mathematicians with tools that mak e their trade easier this time is on a track
to converge to the needs of mathematicians. We hope that one of t he ﬁrst manifestations of this will be in
the form of datasets that better capture the various rich facet s of mathematical research so LLM creators
can provide scores on such benchmarks that are more informative for mathematicians regarding how useful
the LLM is for actual daily mathematical practice. While the most-us ed datasets, GSM8K and MATH, are
indicative of LLMs’ reasoning abilities, they are largely irrelevant to m athematical practice.
2 An Overview of Data-Related Issues
Without using tools specialized for mathematics, the current gener al models, LLMs, simply by well-designed
training methodologies and trained on mathematical data, have dem onstrated unprecedented capabilities in
generating humanlike mathematical text, solving complex problems, and even engaging in creative problem-
solving. For example, GPT-4 has performed promisingly on undergra duate-level mathematics formulated
in natural language, as pointed out by Frieder et al. [2023a ]. Math-Specialized Gemini 1.5 Pro [ Reid et al. ,
2024], a commercial model by Google not available to the public, has been re ported to have an accuracy of
over 90% on the MATH dataset [ Hendrycks et al. ,2021], one of the most widely-used datasets for testing
mathematical ability. This score has recently been replicated by an o pen-weight model, QwQ.4Attaining
such a high score is equivalent to achieving the ability of an IMO gold med allist (according to [ Hendrycks
et al. ,2021]). However, to date, no reports have been made where the mathe matical benchmarks of QwQ
are tested for contamination; not undertaking tests may lead to t his score not being reproducible on a
diﬀerent dataset from the same diﬃculty and problem type distribut ion [Yang et al. ,2023,Xu et al. ,2024].
Further notable general-purpose LLMs are open-weight models wit h strong reported performance on baseline
datasets, such as MATH and GSM8K [ Cobbe et al. ,2021], the DeepSeek family of models [ Shao et al. ,2024,
Liu et al. ,2024,Zhu et al. ,2024,Xin et al. ,2024], and the Qwen family of models [ Bai et al. ,2023,Yang
et al. ,2024a ,Hui et al. ,2024,Yang et al. ,2024b ]. Other LLMs focus more on speciﬁc abilities such as
MathPrompter [ Imani et al. ,2023], which associates a conﬁdence value to arithmetic problem solutions ,
MathVista [ Lu et al. ,2024b ], which solves geometric reasoning problems, WizardMath [ Luo et al. ,2023], or
Llemma [ Azerbayev et al. ,2024], which was specialized through further pretraining on a math corpu s, and
is both open-weight and open-source. A special use case where LL Ms have found success is in interactive
theorem provers (ITPs) such as Isabelle [ Nipkow et al. ,2002] or Lean [ de Moura and Ullrich ,2021], where
they are used to prove theorems most prominently in the context o f generating proofs of given formal
statements [ First et al. ,2023,Zheng et al. ,2023,Wang et al. ,2024a ], autoformalization [ Szegedy ,2020,
Jiang et al. ,2023], or providing code snippets of formal mathematics [ Song et al. ,2024a ]. For a survey of
deep learning approaches on both formal and informal (natural la nguage) mathematics, we refer to Lu et al.
[2023], and for more recent information on language models, including their performance on mainstream
datasets, we refer to Zhao et al. [2023].
This paper argues that the current dataset landscape does not s upport the advancement of such general-
purpose AI systems, in particular LLMs, towards a level of mathem atical performance that makes them
usable as daily mathematical thought partners [Collins et al. ,2024b ] that help mathematicians push the
boundaries of what is known, and capture the richness of mathema tical reasoning and invention that human
mathematical minds are capable of [ Zhang et al. ,2023a ,Dehaene ,2011,Feigenson et al. ,2004]. Our focus thus
4https://qwenlm.github.io/blog/qwq-32b-preview/
4includes, in particular, research-level mathematics, which involves many steps beyond deriving or formalizing
proofs – the aspects of mathematical practice that are current ly most strongly represented in data.
The spectrum of tasks a copilot can assist with is not solely related to mathematics: programmers presently
carry out programming tasks, such as ﬁxing bugs or other GitHub is sues [ Jimenez et al. ,2024], using
various code-generating copilots, such as the GitHub Copilot [ Chen et al. ,2021]; the emerging Lean Copilot
ecosystem [ Yang et al. ,2024c ,Song et al. ,2024b ] assists users in the task of formalizing a mathematical
theorem; Tutor CoPilot [ Wang et al. ,2024b ] provides real-time guidance to human tutors that teach school
students mathematics at the level of math word problems. Yet, ma thematics, with its rich set of domain-
dependent workﬂows, tools, and modes of thinking, requires copilo ts with exceptionally broad capabilities. A
mathematical copilot that is useful to a mathematician must signiﬁca ntly exceed the capabilities of the three
exemplary copilots mentioned above, which are systems that are de signed to help with a narrow technical
set of tasks.
Our paper is split into three main sections : In the ensuing Section 3, we review past datasets that may have
limitations of various kinds. We split these into two further categorie s, relating to natural language and
formal language datasets.
To give an overview of our contributions in that section, current na tural language datasets typically model a
question-response interaction, such as posing a problem and writin g a solution. We identify four dimensions
where such datasets frequently fall short of being able to assess advanced mathematics:
•Diﬃculty : Most datasets are situated on a level of diﬃculty at or below the lev el of an undergraduate
degree in mathematics, or impossibly hard, with few datasets at an appropriate level of diﬃculty, from
which model creators can better learn about the strengths and w eaknesses of their system.
•Binary evaluation : Benchmarks typically only support assessing ifthe output was correct or incorrect,
but in case of errors, do not provide information about howthe output failed to be correct, which is crucial
to support.
•Lack of trusted automation evaluation : Benchmarks rely on checking a ﬁnal answer (generally, by
keyword matching), imperfect model-based evaluation, or provide no automatic evaluation at all.
•Standardized Interaction Modes : Often, natural language datasets only contain question-answe r
mathematical problems. The daily experience of a mathematician is mu ch richer than that [ Zhang et al. ,
2023a ], since to prove/search for a theorem, all kinds of “lateral” modes of thinking have to be applied.
Examples are intermediate conjecture formulation, (counter)ex ample search, and ﬁnding analogies with
other theorems. These are typically not found in textbooks, so th ere is no representation of these in
terms of data. We point to Collins et al. for an exposition of the problems of static evaluation for
natural-language mathematics problems in practice.
•Contamination : Many datasets released solely for evaluation and benchmarking pu rposes have a short
half-life, as, once released, they are easily leaked into datasets th at will be used as training data for future
models.
For the other category, datasets around formal mathematics f requently suﬀer from other issues than those
listed above; for instance, datasets for formal mathematics oft en come at a range of diﬃculties, from
competition-level problems [ Zheng et al. ,2022] to undergraduate textbooks [ Azerbayev et al. ,2023], to
some results that are at the mathematical state-of-the-art [ Scholze ,2022,Bordg et al. ,2022]. Moreover,
formalized mathematics evaluation can be easily carried out in a safe a nd automated manner since proofs
can be checked by the ITP.
•Tool misalignment : Various automation tools exist that aid in proving small, intermediate lemmas
arising in the formalization of more comprehensive results. This crea tes incentives to change a proof’s
structure to maximize the use of these tools, potentially resulting in less readable and “human looking”
proofs.
5•Non-trivial data duplication : In mathematics, it is common that one theoretical concept has se veral
formal representations. For example, the concept of a graph ca n be described formally in multiple ways.
Formal libraries typically feature a variety of representations for the same mathematical concept, some
being almost exact copies of each other. Such near-duplication can lead to downstream issues when the
library is both used as training and test data in machine learning appro aches.
•Standardized interaction modes. (Analogous to natural-language, but with diﬀerent characteristic s)
Current formal benchmarks focus on proving theorems in isolation or translating individual statements
into formal code. These tasks do not capture all aspects of adva nced mathematical practice.
These limitations have various consequences: For example, evaluat ing progress of the mathematical capabili-
ties of AI systems, particularly for advanced mathematics, is diﬃcu lt. For instance, improved accuracy on a
standard problem-solving dataset may not provide a meaningful sig nal about what has improved, while per-
forming well on an existing formal benchmark may not accurately ind icate where models currently struggle.
In the next section, Section 4, we discuss how certain aspects of the proof creation can be mapp ed to
datasets. We argue that such datasets that describe intermedia te stages that mathematicians go through
in the long process of devising proofs are potentially highly valuable to support mathematical copilots that
assist humans in these tasks. The overt focus of current datase ts onresult (the ﬁnal proof), rather than
the process that led to that proof, severely diminishes their usefu lness for training LLMs to be used as
mathematical copilots. While from a perspective of pure proof sear ch, results-based datasets are justiﬁed, it
is unlikely that mathematics will soon be reduced purely to proof sear ch, as there are several mathematical
activities (such as ﬁnding the “right” set of deﬁnitions, that makes a mathematical theory clear and easy
to follow) that are not solely about proof search. Such datasets t hat describe these intermediate stages
do not exist at all currently! The GHOSTS dataset, to our knowledg e, is the only one that preliminarily
investigates how well LLMs can engage in literature search. Thus, in Section 4.1, we take a more holistic level
to describe how mathematical workﬂow might be described by datas ets. This problem is essential, as a lot
of mathematical activity is based on chaining together complex work ﬂows. There is currently no clear way
of measuring the advances of AI systems in tackling the full spectr um of mathematical workﬂows. Such data
about intermediate stages in the proof discovery process is often not explicitly contained in textbooks and
articles – the data sources on which current LLMs are trained. In S ection 4.2, novel ways of capturing data
that may contain this information are described. Finally, in Section 4.3, we discuss a stricter proof structure
called a “motivated proof”, requiring the author to explain the origin behind each step of a proof. We then
argue for an evaluation benchmark enforcing this proof structur e from the perspectives of end-user utility
and evidence of LLM reasoning rather than LLM memorization (comin g up with a motivated proof, given
an unmotivated one, requires reasoning and deeper proof unders tanding) and speculate on paths toward
designing such a benchmark.
Lastly, in Section 5, we provide an extension of the well-known “datasheets for datas et” questionnaires [ Gebru
et al. ,2021], speciﬁcally aimed at mathematical datasets, as these come with th eir own speciﬁc characteristics,
not covered by the original datasheets. We hope that our questio nnaire facilitates better cross-disciplinary
collaboration and alignment between AI practitioners and mathemat icians.
We note that in this article we do not focus on datasets that are des igned primarily to be consumed by the
current LLM technology stack, for example, various instruction t uning datasets, such as the OpenMathIn-
struct datase [ Toshniwal et al. ,2024]. These are often based on existing datasets (GSM8K and MATH in
the case of OpenMathInstruct) and thus could be described as derived datasets. Rather, our focus is on
assessing how much and how well primary datasets describe various aspects of doing mathematics .
3 The Past – Common Pitfalls in Current Datasets
In this section, we discuss several issues with current datasets. Note that our limitations are with respect
to the landscape of AI for mathematics at the time of writing (Dec 20 24); it is possible that some of these
6Dataset Reference SizeField Description
Elementary to Middle School Level
Commoncore / MultiArith Roy and Roth [2015] 600 Basic arithmetic Word problems with two steps
MAWPS Koncel-Kedziorski et al. [2016] 3320 Basic arithmetic and algebra Word problems requiring systems of up to two linear
equations (includes MultiArith)
Math23K Wang et al. [2017] 23161 Basic arithmetic Word problems in Chinese
ASDiv Miao et al. [2020] 2305 Basic arithmetic Word problems (selected from the internet)
SVAMP Patel et al. [2021] 1000 Basic arithmetic Word problems requiring up to two steps (der ived from
ASDiv)
GSM8K Cobbe et al. [2021] 8500 Basic arithmetic Word problems requiring 2-8 steps to solve
GSM8K-symbolic Mirzadeh et al. [2024] 5000 Basic arithmetic Variants of GSM8K problems using symbolic tem -
plates
High School to Intermediate Level
Dolphin18K Huang et al. [2016] 18460 Basic arithmetic and algebra Problems and answers from the mathematics category
ofYahoo! Answers
AQuA Ling et al. [2017] 100000 Basic arithmetic and algebra Algebraic multiple-choice word p roblems (similar to
GMAT and GRE)
MATH Hendrycks et al. [2021] 12500 Problem-solving Problems from high school math competition s with
step-by-step solutions
NumGLUE Mishra et al. [2022a ] 101835 Arithmetic reasoning 8 diﬀerent mathematical reasoning t asks (including
previous datasets).
GAOKAO (Math) Zhang et al. [2023b ] 844 Various high school math top-
icsQuestions from the Chinese College Entrance Exam
(single-choice, cloze, open-ended)
Hungarian High School Finals Paster [2023] 33 Problem-solving Problems from the 2023 Hungarian National High
School Finals in mathematics
MATH 401 Yuan et al. [2023] 401 Advanced arithmetic and
computationArithmetic expressions and numerical results
TAL-SCQ5K TAL Education Group [2023] 5000 Various Multiple-choice competition questions from elemen-
tary to high school levels in English and Chinese
AGIEval (Math) Zhong et al. [2024] 1943 Various Problems (in English and Chinese) derived from col-
lege admission tests (GRE, Gaokao, SAT) and high
school competitions (from MATH and AQuA)
College Level
TheoremQA Chen et al. [2023] 800 Various (including algebra,
number theory, graph theory,
information theory)Questions (from the internet and textbooks) and ex-
pert answers based on 354 theorems
ARB Sawada et al. [2023] 234 Various Problems from university exams and competitions at
the undergraduate level
Graduate to Research Level
NaturalProofs Welleck et al. [2021] 25271 Various (focus on algebraic
geometry)Theorems with proofs and reference graphs from
ProofWiki , theStacks project , and textbooks.
GHOSTS Frieder et al. [2023a ] 709 Various Problem-solving, theorem-proving, and retrieval ta sks
derived from textbooks, StackExchange , and existing
datasets (MATH and Symbolic integration)
FrontierMath Glazer et al. [2024] >35 (unknown) Various Challenging problems with automated veriﬁcat ion cre-
ated by mathematicians
Olympiad Level
miniF2F Zheng et al. [2022] 488 Problem-solving, algebra,
number theoryFormalized Olympiad-type problems from AIME,
AMC, IMO, as well as high school and undergradu-
ate courses (also derived from MATH)
OlympiadBench He et al. [2024] 8476 Various Problems and solutions from mathematics and physics
competitions and the Chinese College Entrance Exam
(in English or Chinese and partially with images)
IMO Small Challenge Frieder et al. [2024] 100 Combinatorics Selected problems and solutions from IMO and
BWMC
IMO-AG-30 Trinh et al. [2024] 30 Geometry Plane Euclidean geometry problems from IMO in
JGEX formal language
Various / Mixed Diﬃculty
Mathematics Saxton et al. [2019] Generated Arithmetic, algebra, probabil-
ity, calculusSequential questions generated with modular structure
MMLU (Math) Hendrycks et al. [2020] 960 Elementary, high school, and
college mathematics, and ab-
stract algebraMultiple-choice questions collected from online sources
ranging from elementary to college (similar to GRE)
mathematics
INT Wu et al. [2020] Generated Inequalities, General Mathe-
maticsGenerated formalized (in-)equality theorems based on
ordered ﬁeld axioms
AMPS Hendrycks et al. [2021] ≈5100000 (Linear) algebra, calculus,
statistics, geometry, and num-
ber theoryProblems and step-by-step solutions from Khan
Academy ( >100k) and generated using Mathematica
(≈5M)
Lila Mishra et al. [2022b ] 132239 Arithmetic, (linear) algebra,
calculus, statistics, geometry,
and number theoryDerived from 20 existing datasets (including
NumGLUE, SVAMP, MultiArith, Dolphin18K,
Mathematics, AMPS, GSM8K, MATH) with numbers
or expressions as outputs
CMMLU (Math) Li et al. [2023] 499 Various Multiple-choice questions (in Chinese) from elemen-
tary to college level collected from freely available re-
sources
Table 1: Selected datasets for evaluating the mathematical capab ilities of LLMs.
7limitations are addressed. Indeed, we hope that they areaddressed swiftly. We ﬁrst list issues that are
common to both natural-language datasets and datasets compris ing formalized mathematics. Then, we list
issues that are speciﬁc to either natural-language datasets or fo rmal datasets.
3.1 Common Issues
3.1.1 Diﬃculty
The diﬃculty of mathematical problems typically varies along at least t wo salient dimensions: level of
abstraction and proof (or solution) sophistication. Abstraction v aries from simple “one-layer” deﬁnitions,
such as those that involve properties of topological spaces, to th ose in areas such as algebraic geometry,
where deﬁnitions of highly intricate mathematical objects involve se veral layers.
Proof sophistication is related to problem-solving ability and is often t ested (for humans and AI systems
alike) in mathematical competitions, such as the International Mat hematical Olympiad (IMO). Typical for
these is that the statements to be proved are elementary, but hig hly ingenious proof techniques need to be
used to arrive at the solution.
Several datasets have been proposed which explore proof sophis tication, such as the OlympiadBench [ He
et al. ,2024], the IMO Small Challenge, or the IMO-AG-30 dataset [ Trinh et al. ,2024], but very few existing
datasets reach a level of diﬃculty that is more advanced than that of an undergraduate degree in mathematics
in terms of level of abstraction. For a (non-exhaustive) overview of datasets, ordered by their diﬃculty, see
Table 1.
For example, MATH focuses on high-school competition problems, w hile the recent TheoremQA [ Chen et al. ,
2023] and Advanced Reasoning Benchmark (ARB) [ Sawada et al. ,2023] are upper-undergraduate level. Many
commonly used datasets test mathematics below the undergradua te level, such as GSM8k and the 23 tasks
in the Lila benchmark [ Mishra et al. ,2022b ].
Two datasets that go beyond upper-undergraduate level are th e GHOSTS dataset [ Frieder et al. ,2023c ],
as well as the NaturalProofs(-Gen) [ Welleck et al. ,2021,2022] datasets, which contain problems, theorems,
and proofs on a wide range of more advanced mathematical topics. However, these suﬀer from a lack of
automated evaluation and contain many problems that could, in princ iple, be in the training corpora of
modern LLMs, as we discuss later. FrontierMath [ Glazer et al. ,2024] is also a more advanced dataset, but
is currently not publicly accessible.
Most current LLMS (e.g., the Qwen [ Yang et al. ,2024a ] family of models, or commercial models released
by OpenAI and Google) are evaluated on the MATH dataset [ Hendrycks et al. ,2021] and the GSM8K
dataset [ Cobbe et al. ,2021], with a recent trend of some LLMs using held-out datasets such as the Hungarian
National Finals high-school exam as an additional test of generaliza tion [ Paster ,2023]. The MATH dataset
uses ﬁve categories of diﬃculty and is strictly more diﬃcult than GSM8 K. Nonetheless, state-of-the-art
LLMs have been found to reach an acceptable performance on it [ Frieder et al. ,2023a ]. For instance, Gemini
reaches a performance of about 50%.5, while solving almost all problems on GSM8K. Progress in LLMs is
proceeding at a rapid pace, and the “Math-Specialized” version of G emini 1.5 reaches (at best) a score of
91% on MATH, which is representative of the current state of the a rt (although, due to the closed nature of
this line of research, it is diﬃcult to place this achievement into contex t, such as by analyzing how similar
training data has been to the MATH dataset, and how much was need ed).
While this performance may appear impressive, neither of these dat asets covers a high degree of diﬃculty in
terms of abstractness and proof sophistication. Hence, the cur rent performance of LLMs on these datasets
is not yet indicative of advanced mathematical understanding, whic h is relevant for professional mathemati-
cians.
5https://blog.google/technology/ai/google-gemini-ai/ performance
8This is particularly striking in the case of AlphaGeometry, which can so lve 25 geometry problems from the
IMO out of a test set of 30 problems [ Trinh et al. ,2024] (and 213 out of 231 on a larger benchmark). We
argue that the accompanying dataset, while indeed diﬃcult in terms o f proof sophistication, is not suﬃciently
large to be able to accurately compare AlphaGeometry with other mo dels.
Recommendations. We believe that it is crucial to introduce more diﬃcult datasets into th e evaluation
repertoire of math-AI. And importantly, the skill level of these da tasets should be graded , such that we
can form a nuanced characterization of model capabilities – this can be achieved, in part, by interpolating
diﬃculty level between existing datasets and those representativ e of advanced mathematics. This includes
datasets on graduate-level mathematical domains, such as func tional analysis (to measure handling of argu-
ments involving high levels of abstraction), partial diﬀerential equa tions (to measure handling of intricate
computational arguments), as well as other domains that come wit h their own “mathematical ﬂavor”. At
the same time, more comprehensive datasets illustrating and measu ring advanced problem-solving skills are
needed. The miniF2F [ Zheng et al. ,2022] dataset and the GHOSTS dataset are just the ﬁrst steps in this
direction. For natural language datasets, we note that simply scr aping many competition-level problem sets,
coupled with an evaluation principle that only veriﬁes a “ﬁnal answer” , is not suﬃcient to ensure that systems
can progress to becoming useable mathematical copilots. Such pro blem sets, even if some of them ultimately
are only math word problems, require expert, specialized knowledge and training for humans to be proﬁcient.
Without a detailed evaluation protocol (see Section 3.1.2), not much insight will be gained into why poor
performance was obtained - and, conversely, human evaluation will be very costly (see Section 3.2.1).
3.1.2 Binary Benchmarks
Most datasets tailored for machine learning, except GHOSTS and Na turalProofs-Gen, including the dataset
for AlphaGeometry, use a simple correct-incorrect rating scheme . The given feedback indicates ifa system
fails to solve a problem correctly, but without any indication of how it fails. Binary evaluation thus provides
limited information on how to improve or interpret performance.
GHOSTS and NaturalProofs-Gen address this problem by using labels that are attached to language model
outputs, which provide a classiﬁcation of (mathematical) errors. F or instance, GHOSTS distinguishes two
types of labels, called “error codes” and “warning codes”, which ma ke up, in total, 15 error or warning labels,
while NaturalProofs-Gen distinguishes between 11 types of errors .
A small number of datasets use non-binary error rating schemes, to our knowledge these are only TheoremQA
(3-point scheme) and ARB (5-point).
Finally, formalized mathematics oﬀers feedback from the interactiv e theorem prover (ITP) when a system
fails to produce a correct proof (one case being timeouts). Howev er, this feedback is more akin to a compiler
error than high-level feedback on the mathematical reasoning pr ocess. We speculate that this feedback may
be useful but still limited in its ability to diagnose AI systems.
Recommendations. We believe that it is crucial to develop datasets that support multi-a spect feedback.
Relying on a single numerical representation, in the face of the diver sity of mathematical failure modes, risks
providing a signal that is too weak to be suitable for learning or evalua tion – which is especially important
to guard against when we consider deploying systems alongside peop le, who may care not only that a model
is correct but also that the response is appropriately helpful [ Collins et al. ,2024a ].
One of the reasons that AI researchers may have avoided multi-as pect feedback, particularly subjective feed-
back, is for fear of the diﬃculty of obtaining consistent human anno tations. While annotator disagreement is
a challenge, we suggest that the math-AI community look to the way s in which computer vision researchers
have worked on developing new theoretical and empirical tools which lean in to the diversity of human re-
sponses [ Uma et al. ,2021,Collins et al. ,2022,Sucholutsky et al. ,2023,Gordon et al. ,2022]. Appropriately
interleaving formality and subjectivity – especially for advanced mat hematics, where there is a limited pool
9of possible human annotators – is a challenge, but one which demands cross-disciplinary collaboration and
is ripe for future work.
As a middle-ground, we also recommend considering evaluation metho ds that do not assign numerical ratings
at all – but rather annotate the outputs of AI systems with error codes and warning codes, then derive ratings
from the codes directly (where no error codes mean a perfect rat ing).
3.1.3 Standardized Interaction Modes
Almost all datasets to date that are designed to evaluate LLMs cap ture only textbook-like questions. More-
over, owing to issues of automatic evaluation described in Section 3.2.1, the majority of datasets focus on a
smaller subset of questions with a unique, typically numerical, answer . While such questions might span a
range of diﬀerent topics, from numerical (e.g., GSM8K, problems of level 1-2 from MATH, MultArith) and
symbolic evaluations (the dataset associated with the work of [ Lample and Charton ,2020]) to somewhat
complex problem-solving tasks (problems of level 4-5 from MATH), t hey do not come close to covering all
aspects of the mathematical tasks a mathematician might encount er in their daily practice. We believe that
any future mathematical assistant should provide support for these tasks.
In the following list, we describe diﬀerent dimensions of interaction mo des for natural-language mathematics
(both question types as well as session types), across which we be lieve that mathematical assistants should
be evaluated.
Question Types.
1.School/University Curriculum-Like Questions that are encountered in educational settings and
have well-deﬁned answers. This includes questions with arithmetic, s ymbolic content, math word
problems, as well as problem-solving and proofs.
2.Proof-Speciﬁc Questions as the concept of a mathematical proof is varied and gives rise to a h ost
of speciﬁc questions about proofs, which go beyond the type of qu estions related to proofs from the
previous point. These are advanced questions concerning matter s such as: Establishing whether a proof
is eﬀective or not, in the sense of proving a general statement abo ut a mathematical object merely by
proving its existence as opposed to producing a witness or an algorit hm that computes; investigating
what distinct proof strategies might be used to prove a certain sta tement; exploring the distinction
between whether an “elementary” or an “advanced” proof is given .
3.Mathematical explanations and intuition , e.g., by providing (counter-)examples. Such questions
are open-ended and have potentially (inﬁnitely) many correct answ ers. This freeform exploration is
crucial in the process of establishing the truth value of a given (adv anced) mathematical statement,
where one swings between attempting a direct proof of the statem ent and ﬁnding a counterexample to
the statement.
4.Retrieval Tasks for deﬁnitions and mathematical facts, either from name to state ment or reverse
(“mathematical search engine”). This can range from a well-deﬁne d answer (e.g., “ Deﬁne this mathe-
matical object! ”) to open-ended questions (“ what are the most important theorems in a certain ﬁeld?;
which results are relevant to prove a certain statement?; ha s a form of this statement already been
proved? ”). This tests the capabilities of mathematical assistants to provid e high-level explanations
similar to those of a human expert in a certain mathematical ﬁeld.
5.Informal Proof Completion , where a proof (or generally a mathematical statement) needs to be
checked or completed. In the best case, the mathematical assist ant should be able to provide a correc-
tion and ﬁll in gaps. In such functionality, mathematical assistants can be running in the background
to act as “co-pilots” and “mathematical grammar-checkers” — as the current generation of copilots6
does successfully for programmers.
6Such as GitHub’s Copilot: https://github.com/features/copilot
106.Mixed-mode interactions , where translation between formal and informal mathematics nee ds to be
performed. These are particularly important for the combination o f ITPs and general-purpose LLMs,
which has recently picked up interest (e.g., [ Jiang et al. ,2023,First et al. ,2023,Frieder et al. ,2023c ]).
To our knowledge, GHOSTS is the only natural-language dataset tha t focuses on all of the ﬁrst four items
from above. Accompanying this variety of questions ( what is asked) are session types that describe how the
questions are posed.
Session Types.
1.Zero-Shot , where the model is prompted without further information.
2.In-Context Learning , where additional background information is provided, ranging fro m clariﬁca-
tions of the notation to context (e.g., the chapter of the book or p aper), to similar questions with
corresponding proof.
3.Interactive , where the prompter (whose mathematical abilities can span a wide s pectrum) solves
mathematical questions together with the language model in an inte ractive way as in Collins et al.
[2024a ].
In practice, typical mathematical workﬂows require a mixture of d iﬀerent question and session types. Even
if a question is not open-ended, the amount of mathematical detail and rigor the answer should contain will
depend on the user’s background. In part, this should be deduced from the way the question is phrased.
Currently, no datasets oﬀer support for this.
We note that with the exception of Collins et al. [2024a ] and the collection of CheckMate, almost all datasets
are zero-shot. Interactive training modes are extensively employ ed in a formal language setup.
For formal mathematics, diﬀerent considerations apply, as outline d below. While modern LLMs can, to a
degree, perform the tasks below, they are not specialized for the se tasks:
•Refactoring formal mathematics to yield nicer-looking proof is a signiﬁcant under taking. A tool that
takes as input a formal proof and refactors it along desired criter ia would be a welcome addition to the
toolbox of researchers working in formalizing mathematics. To our k nowledge, the only work to date
that attempts this is the ImProver [Ahuja et al. ,2024] for Lean, which allows formal proof creation of
speciﬁc length.
•Interoperability between diﬀerent libraries of formal proofs (such as Lean’s Mathlib library and Is-
abelle’s AFP) is a long-term (but still largely unachieved7) goal. Currently, it takes intimate knowledge
of the various formal libraries in order to assess which library, and e nsuing ITP, would best be used to
formalize a given mathematical theorem. A tool that can assess th e suitability of a certain ITP and
its library before starting the formalization process could make for malization more accessible.
Recommendations. We advise exploring more diverse mathematical interaction modes – a cross a variety
of question and session types – as outlined here, both for formal a s well as informal datasets. Our list is
not exhaustive and can also be broken down to a more detailed level. I n particular, oral, mathematical
communication is not well mapped to data (see Section 4.2). Mathematical collaboration often involves an
exchange of very high-level ideas at a rapid pace. Speciﬁc, wide-ra nging recommendations can be found in
Section 4. We believe capturing this in data will help to lead to more widespread ma thematical assistants.
Finally, we believe that input from research in mathematical educatio n must be taken into account to derive
curated datasets that exhibit richer interaction modes.
7A score of overlap by assessing how many theorems out of 100 th eorems have been formalized in diﬀerent ITPs is provided
here:https://www.cs.ru.nl/ ~freek/100/
113.1.4 Contamination
When releasing a dataset, control is lost over whether the datase t ends up as training data for machine
learning models. For several of the state-of-the-art models, su ch as GPT-4 [ OpenAI ,2023], that perform
well on benchmarks, no information is available in the ensuing on wheth er eﬀorts were made to ensure that
training datasets were decontaminated and no datapoints from th e evaluation benchmark were included in
the training set. For Gemini 1.5 [ Reid et al. ,2024], Qwen2 [ Yang et al. ,2024a ] and DeepSeekMath [ Shao
et al. ,2024], onlyn-gram decontamination approaches have been tested. For comple x datapoints, such
as math, n-grams are unfortunately not always suﬃcient to ensure the train ing dataset is clean. There is
evidence that suggests that several such modern models are alre ady contaminated [ Xu et al. ,2024]. While
mitigating approaches have been proposed, such as generating ne w data, either from scratch [ Mishra et al. ,
2024] or by using existing datasets as seeds [ Zhou et al. ,2024], it is not clear whether these can scale to more
sophisticated mathematics, as the methods were tested using mat hematics on the level of grade-school, and it
is unclear how well they would scale to much higher levels of mathematic al abstractions and problem-solving
diﬃculty (the two main metrics of diﬃculty, as outlined in 3.1.1.
Recommendations. If the dataset is suﬃciently large, it is advisable to keep a part of the dataset hidden
from the public so that the dataset creators can compare how well newly-released, publicly accessible open-
weight models score in the public versus the hidden part of the datas et. Diverging scores on two splits of the
dataset can indicate contamination. Care must be taken that data points from the hidden datasets are from
the same distribution compared. For mathematics, this means at min imum: Same domain, diﬃculty range,
and proof technique. This can be challenging: Given a speciﬁc problem P, it takes eﬀort to source a new
problem P⋆, that on all relevant metrics (including the mentioned ones) is similar t oP, but at the same time
is not completely analogous to P– as it would be by, e.g., merely changing items in the problem statement
that have a negligible on the proof (this is an approach followed by GSM 8K-Symbolic dataset [ Mirzadeh et al. ,
2024], which nonetheless turned out to be challenging for LLMs, highlightin g their current limited reasoning
capabilities). The approach advocated here has limitations for mode ls released as-a-service [ La Malfa et al. ,
2024], via APIs or GUIs, as running the hidden dataset through risks it au tomatically being used at a later
stage as training data for those models.
3.2 Distinct Issues
This section will detail issues that speciﬁcally appear with either natu ral language or formal language datasets,
or mixed datasets. The most prominent diﬃculty with natural langua ge datasets is the lack of trusted
automatic evaluation as will be explained in Section 3.2.1.
A natural way to circumvent the diﬃculty of evaluating natural lang uage proofs is by making use of formal
language datasets. Instead of having an LLM generate natural la nguage mathematical proofs, one can train
it to generate proofs in a veriﬁable formal language such as Lean or Isabelle.
Therefore, existing libraries of formal proofs can play a crucial ro le in the development of machine learning-
based automatic theorem provers. Sections 3.2.2 and3.2.3 will provide details on how some of the largest
existing collections of formal proofs have been and are being creat ed. This is followed by an analysis of how
this process aﬀects the use of formal proof libraries as evaluation datasets; with some remarks relevant to
using formal libraries for training.
More concretely, Isabelle’s Archive of Formal Proofs (AFP) and Le an’s Mathlib will be investigated. This
choice is due to the authors’ familiarity with these libraries but many o f the points mentioned below will
also be valid (at least to some extent) for other systems.
One particular issue relevant to all datasets is their scale. The lack o f a large-scale dataset consisting of pairs
of formal and informal mathematics is a signiﬁcant bottleneck for a utoformalization. Current datasets, such
as miniF2F are on the order of a few hundred datapoints, which are e nough for assessing autoformalization,
but not for training models to support autoformalization. A recent eﬀort [ Ying et al. ,2024] scales this to
1257k datapoints of pairs. Nonetheless, this scale is not yet compara ble to the scale at which LLMs can be
trained on informal mathematics.
3.2.1 Lack of Trusted Automatic Evaluation
The easiest way to automate the evaluation of mathematical promp ts is to formulate them in a way such
that the answer can be represented as a single token (e.g., a numbe r or a mathematical term). Automatic
evaluation can then be performed by keyword-matching the token to the gold-truth answer. A slightly more
advanced variant is pursued by the MATH dataset, which allows a rea soning section, but encloses the ﬁnal
answer in a \boxed environment (and only this is keyword-matched).
No large machine learning dataset on mathematics currently exists t hat allows an arbitrary proof of an AI
system to be checked for correctness against the gold-standar d proof in the evaluation dataset. A proof-of-
concept, highlighted by the IMO Small Challenge8, shows how partial automation might be achieved, where
a necessary test for correctness is carried out using detailed pro of annotation. This builds on the idea that
a system like an LLM, combined with a deterministic form of matching, c an at least exclude incorrect proof
candidates. If the gold truth is suﬃciently rich, the annotations he lp the LLM break down a proof and assist
it in understanding its main features (accepting that subtler points of proofs may still be currently out of
reach for LLM understanding).
Some success has been attained in using an LLM to grade (or teach) another LLM [ Eldan and Li ,2023,
Mukherjee et al. ,2023]. Yet, for mathematics, we believe that this is not necessarily the rig ht approach
forward yet. The current generation of models do not have a suﬃc iently high performance on mathematics
to be used as graders: for tasks that would often be deemed simple r than mathematics, this approach can
fail [Wang et al. ,2023], although for solving programming puzzles this approach was succe ssful [ Haluptzok
et al. ,2023]. Anecdotal evidence suggests that adapting the approach to pr oofs is challenging because of
the multitude of potential proof variations for a single statement, which gives rise to a diverse set of textual
expressions.
At present, grading can, at best, be automated by the use of det ailed human annotation for each problem
in combination with LLM assistance based on such annotation.
Recommendations. In general, we recommend developing evaluation methodologies that allow for natural
language proofs to be checked for correctness. This is diﬃcult in ge neral. A middle ground is to include as
much metadata as possible when annotating datasets with manual e ﬀort, with a view towards supporting
LLMs in using this metadata to assess proof candidates. Second, w e recommend more research that quantiﬁes
the degree to which LLMs can evaluate mathematics. This will help in ma king objective statements about
how good or how poor LLMs are at evaluating diﬀerent kinds of mathe matics, and help in identifying areas
for improvement.
3.2.2 Tool Misalignment
As writing formal proofs imposes slightly diﬀerent challenges to writin g informal proofs, it is important to
distinguish mathematical proﬁciency from proﬁciency in using tools p rovided by the formal environment.
One cause of this discrepancy is that side conditions deemed trivial in conventional mathematical literature
have to be formalized as diligently as the rest of the mathematical te xt. On the other hand, proving many
statements considered routine by mathematicians can be mechaniz ed.
For example, proving that a function is continuous often correspo nds to choosing the correct subset of a few
relevant lemmas and this can be achieved with a simple search algorithm , such as Lean’s continuity tactic.
Next to this domain-speciﬁc formalization aid, there are also genera l-purpose automation tools that can
be used to formalize certain simple statements. For example, Isabe lle’s Sledgehammer tool [ Paulson and
8www.imo-small-challenge.io
13Susanto ,2007,Meng and Paulson ,2008] translates the given statement so that it can be understood by a
number of external automatic theorem provers (ATPs). The ATP s, in turn, attempt to prove the statement
and send the proof back to Isabelle.
Automation and Proofs Naturally, the existence of automation aﬀects how the task of for malization is
approached: Without automation, formalization would consist of tr anslating a mathematical proof step-by-
step into the ITP’s logic. But having access to advanced tactics and general-purpose ATPs, one only needs
to repeatedly break down the proof into smaller pieces until these c an be tackled by automation.
Eventually, this can lead to proofs being formalized in a way that is not very close to the original natural
language proof. For example, elementary homework-style problem s often consist of long calculations that
might correspond to one single tactic invocation in the formal syste m. Also, in more advanced topics, the
automation of a theorem prover can make the proof less readable o r skew its focus. For example, natural
language proofs typically make it very clear which deﬁnitions need to b e unfolded and when. In Lean, such
unfolding does not have to be made explicit, which can widen the gap be tween formal and informal.
The impact of these mechanisms needs to be kept in mind when formal datasets such as Lean’s Mathlib or
Isabelle’s AFP are used for LLM evaluation. In particular, it is likely tha t current datasets overly reward
models for their ability to deploy the language-speciﬁc automation, r ather than complete “understanding” of
the underlying mathematics. As some evidence of this, Hu et al. [2024] show that LLM performance drops
signiﬁcantly when common automation tactics are turned oﬀ, even f or theorems that have human-written
proofs that do not rely on the automated tactics.
Strong automation and the Archive of Formal Proofs (AFP) These matters are especially signiﬁ-
cant with the Isabelle AFP because of the powerful general-purpo se automation that has been widely used in
its development over the last decade. It can therefore be expect ed that a large subset of theorems in today’s
AFP have been formalized by repeatedly breaking them down into sma ller subproblems until Sledgehammer
could ﬁnd their proof.
A natural way to turn the AFP into a proof dataset is by splitting up a ll formal proofs into their individual
steps [ Jiang et al. ,2021]. However, by the above characterization, such a dataset might b e skewed towards
being tractable for automation because of the particular way in whic h AFP theorems have come into existence.
This can make it hard to assess the level of diﬃculty in the problem set .
Especially when equipping LLMs with the ability to access existing autom ation, careful evaluation is essential.
It is important to determine whether the model genuinely “underst ands” complex mathematical concepts and
can scale this understanding up to more diﬃcult problems; the altern ative being that the model merely excels
at ﬁnding “low-hanging fruits”, which, when combined with non-ML au tomation, might appear deceptively
impressive.
We would like to stress that we believe that the use of formal mathem atics datasets such as the AFP is a
valid evaluation tool. The results of recent publications [ First et al. ,2023,Jiang et al. ,2022,Miku/suppress la et al. ,
2024] are especially promising, and we are looking forward to their continu ation. Nevertheless, we believe
that future evaluation should carefully consider the impact of exist ing automation in ITPs on their libraries.
Recommendations. The available formal mathematical libraries that include deep, resea rch-level results
have generally been created using a signiﬁcant amount of automatio n. Researchers could create small, speciﬁc
additional test sets of proofs that are formalized without automa tion and evaluate mathematical assistants
on these.
3.2.3 Non-Trivial Data Duplication
Next to these aspects related to the nature of theorem provers , there are also challenges intrinsic to mathe-
matics itself. In particular, mathematics has a self-similar structur e: there are profound connections between
14areas that are seemingly disconnected, and many mathematical st atements have several related versions, de-
pending on the perspective and level of generality chosen. This sec tion will detail some of the inherent
challenges this creates for the construction of formal mathemat ical libraries and then consider the impact of
using them as datasets.
Ideally, a formal library should have as little duplication as possible to a llow for a smoother user experience
and to reduce the amount of code maintenance required. At the sa me time, this ideal can seldom be upheld
fully since formalizing theorems only in their most general form is intra ctable. Some level of non-trivial
duplication is therefore accepted and common in formalization.
As an example, Lean’s Mathlib often provides several versions of a le mma,9which makes it more convenient
to use the library. Instead of having to “import” a lemma and then tr ansform it into the right format, one
can directly refer to commonly used variants. For example, the sta tement that
a+b+ (c+d) =a+c+ (b+d) (1)
in a commutative semigroup is explicitly formalized even though it could e asily be derived from associativity
and commutativity whenever needed. Furthermore, there is supp ort for automatically generating lemmas,
e.g., to generate the additive version of an abstract algebra state ment given in terms of multiplication.
Next to this, the rules and customs of how a collection of formal pro ofs is built and maintained have a
signiﬁcant impact on its properties as a machine-learning dataset. C ompared with Mathlib, the Isabelle
AFP is more static and aims at being archival, i.e., providing long-lasting s upport for its content and not
removing previously deﬁned concepts. This makes duplication inevita ble as soon as parts of the library go
through a larger restructuring or even redevelopment. For exam ple, there are two separate algebra libraries
for Isabelle, one in the AFP and a second one using a diﬀerent formaliz ation approach in the Isabelle
HOL-Library, which often gets used in conjunction with the AFP.
As a further example, consider the AFP section on category theor y. Currently, there are at least ﬁve
separate formalizations of category theory at various stages of development with all of them taking diﬀerent
approaches10. This is likely to be for historical reasons, but also because exploring diﬀerent representations
of category theory is an interesting topic in mathematical foundat ions.
Naturally, if duplication is present in the formal library, a lot of care b ecomes necessary when designing
machine-learning datasets from it. If data is just randomly split into a training and validation set, then
leakage can occur on one hand. Of course, the duplication will typica lly be on the level of mathematical
concepts and not exist as a verbatim doubling of formal language co de. Nevertheless, disregarding the
issue of duplication makes it hard to gauge to what extent a model ma nages to produce formal proofs from
the ground up. Possibly, parts of the model’s performance simply st em from learning how to translate
between diﬀerent representations of the same mathematical con cept. On the other hand, duplication brings
to the forefront the issue of data representation, as machine lea rning models will only perform well on that
representation on which they have been trained, which is in contras t to human mathematical reasoning,
which, to a degree, is robust against diﬀerent formal representa tions of the same mathematical objects.
Translation of formal representations constitutes a highly intere sting and relevant skill in its own right.
Nevertheless, good test design should enable researchers to jud ge to which degree the respective skills are
achieved.
Recommendations. Following the discussion above, we recommend developing methodolog ies that ensure
that train/test splits adequately measure a model’s ability to genera lize. One direction is to test on new
formalizations that occur after a model has been trained, as was e xplored in Hu et al. [2024]. Nevertheless,
9We note that this facility is not exclusive to Lean; e.g., Isa belle provides several versions of a lemma.
10cf.https://www.isa-afp.org/topics/mathematics/category -theory/ not counting generalizations of category theory
and continuations of previous developments.
15care should be taken to ensure that the mathematics being formaliz ed does not occur in previous projects.
Hence, we particularly recommend evaluating on domains that have n ot previously been formalized.
More broadly, the ideal evaluation of digital mathematical assistan ts should include case studies in which
previously unformalized proofs get formalized using the assistant. There are various ways to realize this.
On a small scale, researchers can qualitatively evaluate the LLM by f ormalizing some reasonably diﬃcult,
previously unformalized proof. On a larger scale, the assistant can be provided as a plugin to theorem
provers, which a large number of people working in formalization can t hen use in real-world scenarios. If
there are enough users, such a setup could even use A/B testing f or multiple architectures of mathematical
assistants.
4 The Future – Novel Datasets to Support Mathematical Copilo ts
In this section, we cover various aspects of mathematical resear ch practice that, to date, are not covered at
all by any of the existing datasets. This contrasts with the previou s section on mathematical datasets that
covered parts of mathematical practice, albeit with the noted limita tions. Current datasets exclusively are
focussed on publishing the results rather than the intermediate steps that mathematician goes thro ugh in
the process of devising a proof. The diﬀerent types of workﬂows, the proof-counterexample dialectic, and
proof transfer,
etc., are all examples of intermediate processes that do not have c lear representations in data that can be
used to ﬁne-tune LLMs. Contrasting with the previous section, wh ere we made speciﬁc recommendations
on how to improve existing datasets, in this section, we do not make speciﬁc recommendations , as our
recommendation is to simply devise such datasets. While a few inroads have been made into non-proof-based
datasets, see Section 3.1.3 these are still very much at their inception, and, to our knowledge, the GHOSTS
dataset is the only attempt to date to try to “data-ify” some aspe cts (solely related to mathematical literature
search) of daily mathematical process.
4.1 Mapping Mathematical Workﬂows to Data
The previous sections have shown that existing datasets and benc hmarks only deal with speciﬁc mathematical
tasks. In particular, they focus mostly on question answering and theorem proving, with solutions being
presented in a streamlined way (as is typical for results in mathemat ical textbooks). In consequence, they
do not suﬃciently cover all steps in typical mathematical workﬂows , such as surveying mathematical topics,
gathering related results, establishing high-level proof strategie s and intuition, refactoring proofs, or carrying
out ﬁeld-speciﬁc routines. Yet, we would like to evaluate and train ma thematical copilots on these tasks,
too, in order to obtain full-spectrum assistance across all facets of mathematical research practice. We
note that datasets used to pre-train LLMs exhibit broader cover age, e.g., of mathematics-related Q&A
communities, blogs, and educational material; however, it is hard to assess and control the quality of the
included mathematical content. This results in a weak learning signal and, for a strong mathematical copilot,
one likely requires ﬁne-tuning on a comprehensive, high-quality data set of mathematical workﬂow steps.
We advocate a more bottom-up approach that consists of creatin g a taxonomy of workﬂows, i.e., isolating
and categorizing workﬂow steps. Speciﬁcally, many mathematical w orkﬂows can be modularized into smaller
sequential steps, which themselves can be ordered along diﬀerent dimensions, e.g., their mathematical depth,
level of abstraction (from general, high-level proof techniques a nd principles to specialized, problem-speciﬁc
approaches), mathematical subject, how well a symbolic approac h might handle them, whether the workﬂow
step is strictly mathematical or meta-mathematical (e.g., literatur e search). With this in view, we distinguish
between general global workﬂows, which are used across mathematical ﬁelds, and ﬁeld-sp eciﬁclocal workﬂows.
For instance, we refer to the Tricki11for a collection of problem-solving techniques that can be viewed as
abstract workﬂows. General proof techniques, such as lineariza tion and ﬁxed point theory, can be viewed as
11https://www.tricki.org
16global workﬂows. However, we note that speciﬁc instantiations of such techniques, e.g., related to dynamical
systems, can also be classiﬁed as local workﬂows. Examples of even more local workﬂows include approaches
tailored to speciﬁc kinds of partial diﬀerential equations, e.g., the m ethod of characteristics, maximum
principle, energy estimates, or Green’s functions, as these metho ds frequently occur as individual steps in
larger chains of arguments in research-level mathematics.
There is no hard boundary for transitioning between local and globa l workﬂows. For example, the “routine”
task in analysis to upper bound an expression eﬃciently, as opposed to evaluating it exactly, is found
both in elementary contexts, such as proving inequalities such as ve rsions of arithmetic mean-geometric
mean inequality, up to more advanced cases, such as for ordinary d iﬀerential equations (ODEs) or partial
diﬀerential equations (PDEs), where a routine task is that of apply ing an “energy method” or “Lyapunov
functional method”. We, therefore, deliberately do not draw a sp eciﬁc boundary of when to categorize a
workﬂow step as local vs. global.
While creating a complete taxonomy of workﬂow steps is beyond the s cope of this article, we want to examine
selected workﬂows and their steps (both local and global) in order t o highlight issues in translating these to
data and speciﬁc challenges. We note that these are merely illustrat ive examples meant to show how ﬁrst
steps could be undertaken to generate datasets that support s uch workﬂows.
While a workﬂow (indicated with arrows below) can, in principle, easily be mapped to data by converting
it tontuples of datapoints (where ndenotes the number of workﬂow steps) and ﬁlling text in between, in
practice, in certain cases, issues may arise. We give examples of bot h global and local workﬂows below and
highlight both examples where these can be transformed to data in a straightforward manner, as well as
cases in which this transformation is more diﬃcult. We urge the commu nity to explore such translation of
workﬂows to data further.
Global workﬂows Literature search is one of the most general workﬂows across th e sciences, having par-
ticularities in how it takes place in mathematics. Prior work can be relat ed to the problem a mathematician
has at hand in many ways. One might, for instance, want to know wha t is known about a particular math-
ematical object at hand. The context of a problem might have many options for what to look for, so the
ﬁrst step in the workﬂow might be to identify an object that has a go od chance of having been seen before.
One example is integer sequences: perhaps the solutions to a combin atorial problem are computable in small
cases, and it is often useful to know if the resulting sequence has b een encountered in the context of other
problems (there might be many ways to get a sequence: for instanc e, we might have to choose variables to
ﬁx and then only vary one parameter of the problem). For this part icular case, the Online Encyclopedia of
Integer Sequences12is a well-known, eﬃcient, specialized tool, with many pointers to the lite rature, and the
ability to recognize partial matches (e.g., perhaps one’s sequence is coarser than the one from relevant prior
work). In case there are no matches, we can try to repeat the pr ocess with other candidate objects; in case
there are, the challenge turns to assess whether any of the resu lts seem meaningfully related to the current
case (and given only a few integers, there are often too many sequ ences containing them). For instance, the
sequence 1 ,4,44 appears in path-counting problems in some lattices, or in a few num ber-theoretic contexts
(like products of odd-indexed Lucas numbers), as well as many oth er contexts, and more context that was not
included during the search might be relevant in identifying which of the se sequences might be meaningfully
related to the current problem. We could broadly summarize this wor kﬂow as:
Identify objects to search for →ﬁnd related work describing the object →assess potential relation to current
context
We might expect LLMs to help generalize this process beyond what sp ecialized tools, such as the OEIS,
are capable of. Most mathematical objects are signiﬁcantly harde r to describe than integer sequences: for
instance, one might have a particular topology on a function space t hat might be unique to the current
context, but something of the same “shape” might have been seen before. The assistant would have to
12https://oeis.org/
17recognize and know how to describe this shape, and identify matche s across potential diﬀerences in what
deﬁnitions are implicitly or explicitly used, as well as potential equivalen t deﬁnitions that might cause a
description in the literature to diﬀer on the surface (e.g., mention “a ccumulation points” vs “limit point”).
Examples of this workﬂow for training and evaluation might be automa tically extractable in a post-hoc
fashion from the mathematical literature itself: one might be able to look at how previous work is referenced
in existing proofs as a source of examples of relevant previous work (other matches for the same object that
are not the paper that was cited are most likely examples of spurious matches).
Local workﬂows We list below examples from two subﬁelds of mathematics (diﬀerential equations and
knot theory/low-dimensional topology).
•Suppose, for instance, one has a ﬁrst-order ODE ∂tu=F(u) with some initial data u(0) =u0and
wants to know how the solution grows in time. A standard technique is to introduce a key functional
E(u) of the solution (often something like an “energy” or “Lyapunov fu nctional”) and then compute
the derivative ∂tE(u) using the ODE and the chain rule (for PDEs, one often has to also pe rform
several times integration by parts). Then, one bounds this deriva tive as best one can.
The goal is to reach some diﬀerential inequality of Gronwall type, e.g .,∂tE(u)≤CE(u), so that a
Gronwall-type lemma may be applied (but it is not always precisely the Gr onwall lemma, but something
similar).
Summarizing, the workﬂow is thus of the form:
ODE/PDE →ﬁnd functional →compute derivative of functional →bound derivative →reach
Gronwall-type inequality
We note that individual steps of this may be solved using symbolic-num eric methods, which opens the
possibility of using a tool-integrated-reasoning (TIR) approach to enable an LLM to discharge these
proof steps to symbolic or numeric tools to, e.g., compute derivative s symbolically. Thus, one option
to encapsulate these workﬂow steps is in datapoints whose core fo rm is
(ODE/PDE, functional, functional derivative, derivative bound, Gronwall-type inequality)
and where there is ﬁller text between the raw mathematical object s (i.e., the ODE, the functional,
etc.). The raw mathematical objects should be symbolically or numer ically generated so that custom
ﬁller text can be added in between them, and an LLM can observe a ra nge of ways in which to speak
and textually connect a ﬁxed tuple of mathematical objects.
What one typically wants, as a mathematician, in the case of this work ﬂow, is to try various guesses for
the functional. If a TIR approach is used, this data representatio n of this workﬂow should speciﬁcally
oﬀer “entry points” to make it easy for an LLM to accept arbitrary input at certain places and use
tools to automatically run the essential parts of the workﬂow. An L LM is then much better equipped
to run the workﬂow steps and produce an estimate, either automa tically or semi-automatically. One
can preliminarily do this already through conversation with current s tate-of-the-art LLMs, but with a
lot of mistakes on the LLM’s part, which a stronger grounding in data would help to correct.
We now consider typical workﬂows in low-dimensional topology, which is an area of mathematics that has a
unique ﬂavor and uses tools from geometry, algebra, PDEs, group theory, combinatorics, and mathematical
physics. Hence, some of these workﬂows are more challenging to co nvert to data. Low-dimensional topology
is the study of n-manifolds (certain topological spaces that are locally homeomorph ic toRn) of dimension
n≤4. A knot is a simple closed curve embedded in R3. Knot theory plays a fundamental role in low-
dimensional topology as every 3- and 4-manifold can be represente d by a framed link; i.e., a collection of
knots labeled by integers, called a Kirby diagram [ Kirby ,1978]. We refer the reader to Juh´ asz [2023] for
more detail on low-dimensional topology and knot theory and explan ations of the mathematical terms used
below.
18•A central type of question in this area is classiﬁcation, which require s being able to show whether two
objects (e.g., knots or manifolds) are equivalent. The ﬁrst step is ﬁ nding a suitable representation.
In case of knots, this could be a projection to the plane, called a kno t diagram, a closure of a braid
(a number of parallel strands running around a central axis), or a grid diagram. Knot diagrams
can be encoded numerically as PD, DT, or Gauss codes, and braids as braid words. Manifolds can
be represented using Kirby diagrams, as triangulations, branched covers along links, or as geometric
objects (e.g., hyperbolic 3-manifolds).
To show that two representations of the same knot or manifold are equivalent, one ﬁnds a sequence
of certain moves connecting them, which can be Reidemeister moves [Reidemeister ,1927] in case of
knot diagrams, Markov moves for braids, or Kirby moves in case of K irby diagrams. These search
problems lend themselves to techniques such as reinforcement lear ning; see [ Gukov et al. ,2021]. The
workﬂow steps can be encoded by a sequence of representations of the object, such that consecutive
representations are related by one of the standard moves. Soft ware packages such as SnapPy [ Culler
et al. ,2024] can be used to check whether these moves are valid and can also list valid moves. We can
hence represent the workﬂow as follows:
choose type of representation and set of moves →ﬁnd representations of two mathematical objects →
repeatedly apply moves to ﬁrst object →representation of second object.
•To show two objects are inequivalent, one deﬁnes invariants, which are typically algebraic objects
(numbers, polynomials, or groups) that are unchanged by the abo ve moves. These moves often also
capture important topological properties of these objects. The most classical invariants are homology
groups and the fundamental group. The Alexander polynomial is a k not invariant derived from the
fundamental group of the knot complement. Representations of the knot group give rise to the more
modern twisted Alexander polynomials. A recent knot invariant root ed in representation theory is
Khovanov homology [ Khovanov ,2000]. Floer homology [ Ozsv´ ath and Szab´ o ,2004] and gauge theory
[Witten ,1994] give rise to highly sophisticated knot and 3- and 4-manifold invariant s. These invariants
often give lower bounds on hard-to-compute topological quantitie s such as the 3- or 4-genus of a knot.
SnapPy is capable of computing many of these knot invariants when r un in SageMath [ The Sage
Developers ,2024]. A typical workﬂow would thus be as follows:
pair of mathematical objects →choose suitable invariant →compute invariant for objects →show
invariants are inequivalent.
•To deﬁne a Floer-theoretic invariant, we construct a chain complex whose boundary map counts some
pseudo-holomorphic curves with certain Lagrangian boundary con ditions in some symplectic manifold.
To show these counts are ﬁnite, one has to prove transversality r esults for the moduli spaces using
diﬃcult methods from PDEs, then obtain a formula for the dimension o f the moduli spaces and
compactify the moduli spaces. The next step is showing the bounda ry map squares to zero, in which
case we have a chan complex, or sometimes we end up with a more comp licated algebraic structure, such
as anA∞-module or a diﬀerential graded algebra. One often has to use spec ial coeﬃcient systems,
such as a Novikov ring, and deal with bubbling phenomena. There are many choices that go into
the construction of our chain complexes, so one has to prove indep endence of these choices up to
chain homotopy equivalence, which often relies on continuation maps and pseudo-holomorphic polygon
counts. One then extracts more tractable invariants from the ch ain homotopy type using algebra, such
as taking homology. Diﬀerent invariants are often related by spect ral sequences, deﬁned using ﬁltrations
of the chain complexes. A similar workﬂow exists for gauge-theoret ic invariants. More sophisticated
invariants can be obtained by exploiting certain symmetries, such as Z2or Pin(2). In another popular
direction, one can sometimes construct a homotopy type from cha in complexes; see [ Lipshitz and
Sarkar ,2018]. Certain constructions from algebraic topology can then be invoke d to provide additional
algebraic structure, such as Steenrod operations. We can hence represent the high-level workﬂow for
deﬁning a Floer-theoretic topological invariant as follows:
19associate a symplectic manifold and Lagrangian submanifol ds to our topological object →decide what
pseudo-holomorphic curves to count →prove transversality of the moduli spaces →ﬁnd dimension
formula for moduli spaces →compactify moduli spaces →choose coeﬃcients and the right algebraic
structure →extract invariant using algebra →prove independence of choices.
It is apparent from the complexity of the workﬂow that this is very d iﬃcult to turn into data. As the
number of workﬂow steps increase, the number of datapoints has to increase exponentially to cover all
possible combinations between steps (although not all combinations may be possible in all cases, which
may mitigate this issue).
•After an invariant is deﬁned, we study what topological information it captures and derive applications.
Here, it is important to know what applications are mathematically rele vant. This workﬂow is very
diﬀerent from many other areas of mathematics, where tools are d eveloped to tackle speciﬁc open prob-
lems, and should be compared with Section 4.3on motivated proofs. This step requires sophisticated
intuition and a global vision. One way to turn this into data is to deﬁne p airs
(invariant, topological application) ,
which could be used by a mathematical copilot to recommend potentia l applications of a given type of
invariant. We want to choose applications that are related to proble ms from a list of important open
questions.
•As many of the invariants are hard to compute, it is crucial to develo p methods to compute them.
For Floer-theoretic 3- and 4-manifold invariants, for example, exp erts use surgery formulas, spectral
sequences, grading arguments, exact triangles, gluing formulas, or computations in explicit diagrams
in simpler cases. The diﬃculty lies in the fact that one has to solve non- linear PDEs to obtain the
pseudo-holomorphic curve counts contributing to the boundary m aps in the chain complex, which is not
algorithmic. Knot Floer homology now has a combinatorial deﬁnition an d can be computed by SnapPy.
It is often helpful to restrict attention to special classes of obje cts, such as to the class of alternating
knots, 3-braid closures, etc., and perform computations or prov e results for these. A schematic of this
workﬂow is the following:
invariant →method of computation →class of objects to restrict to .
Hence, a potential data point could look like
(invariant, method of computation, class of objects) .
Certain knot invariants are easy to deﬁne, but no algorithm is known to compute them, such as the
unknotting number or the 4-ball genus, and topologists use compu table invariants, many of them arising
from knot Floer homology, to give lower bounds on these. The paper [Davies et al. ,2021] describes a
workﬂow for using supervised learning to ﬁnd correlations between various invariants, which has led
to an inequality relating the knot signature and hyperbolic invariants . Upper bounds can be obtained
by performing certain moves on knot diagrams, possibly with the help of reinforcement learning or
Bayesian optimization; see [ Gukov et al. ,2023] and [ Applebaum et al. ,2024]. For example, one could
take(4-ball genus, lower bound from Rasmussen s-invariant, torus knots) , which leads to a solution of
Milnor’s conjecture on the 4-ball genus of torus knots [ Rasmussen ,2010].
•The classiﬁcation of smooth 4-manifolds is still wide open. There exist 4-manifolds that are homeo-
morphic but not diﬀeomorphic, which are called exotic pairs. To const ruct these, experts use methods
from algebraic and symplectic geometry, such as blow-ups, ﬁber su ms when given Lefschetz ﬁbrations,
and other gluings, typically along 3-tori, such as knot surgery. To s how two 4-manifolds are homeomor-
phic, one shows they have isomorphic intersection forms and invoke s Freedman’s theorem [ Freedman ,
1982], for which the fundamental group has to satisfy certain restrict ions (e.g., being trivial). The
intersection form and a presentation of the fundamental group c an be read oﬀ a Kirby diagram. This
fundamental group computation is often the most diﬃcult step, an d note that any ﬁnitely presented
20group can arise as the fundamental group of a closed 4-manifold. F urthermore, there is no algorithm
to decide whether a ﬁnitely presented group is trivial. So, some ques tions in low-dimensional topology
are beyond the reach of computers. As mentioned above, one can use Kirby calculus to show if two
4-manifolds are diﬀeomorphic. Swenton’s Knot-Like Objects softw are13is capable of performing Kirby
moves. To show they are not diﬀeomorphic, one usually distinguishes them using the gauge-theoretic
Seiberg–Witten invariants. No algorithm is known to compute these, but they can be computed in
some instances using Taubes’ non-vanishing result for symplectic 4 -manifolds [ Taubes ,1994], together
with various glueing results, such as Fintushel and Stern’s knot sur gery formula [ Fintushel and Stern ,
1998]. A schematic of a typical workﬂow in smooth 4-manifold topology is as follows:
choose method of construction →construct pair of smooth 4-manifolds →ﬁnd their Kirby diagrams
→show they are simply-connected →show they have isomorphic intersection forms (hence
homeomorphic by Freedman) →try to show they are diﬀeomorphic using Kirby calculus; if th is fails
→compute Seiberg–Witten invariants to show not diﬀeomorphi c.
The last step, the computation of Seiberg–Witten invariants, is disc ussed in more detail in the previous
bullet point. Computer algebra systems can be useful for the comp utation of the fundamental group
and the intersection form.
3-manifold topology has a completely diﬀerent ﬂavour. Here, metho ds from geometric group theory, hyper-
bolic geometry, and combinatorial topology dominate. These combin atorial methods include triangulations
and normal surface theory. Geometric group theory studies gro ups using their actions on metric spaces (e.g.,
on the Cayley graph). Also note Perelman’s proof of the 3-dimension al Poincar´ e conjecture using the Ricci
ﬂow, rooted purely in geometric analysis; see [ Morgan and Tian ,2007]. Well-developed computer packages
exist to aid 3-manifold topologists, including the already mentioned Sn apPy for hyperbolic 3-manifolds and
Regina [ Burton ,2004] for triangulations. We do not provide speciﬁc workﬂows in 3-manifo ld topology due
to the diversity of techniques used.
Further considerations. An important aspect that needs to be considered when mapping mat hematical
workﬂows to data is that diﬀerent representations of the same da ta can lead to diﬀerent mathematical
properties that can change the method of proof, as well as the fo undational model most suited for the chosen
representation.
For example, it is an open problem in knot theory whether there exist s a polynomial-time algorithm that
can detect whether a given knot, which is an embedded circle in R3, can be simpliﬁed (without breaking it)
to a standard round circle. Instead of describing the knot as a cur ve inR3, knots are often speciﬁed in terms
of their projection to two dimensions, and data representations o f the knots keep track of which strands are
above and which are below along the projection ray.
The above-mentioned question then becomes to ﬁnd a sequence of deformations of the embedded circle such
that its projection has no crossings. It is known [ Kauﬀman and Lambropoulou ,2012] that for some data
representations of the projected knot (such as Dowker–Thistle thwaite codes [ Dowker and Thistlethwaite ,
1983] with Reidemeister moves as allowed deformations [ Reidemeister ,1927]), there exist examples where
the number of crossings needs to be increased before all crossing s can be removed. In another representation
(grid representation with Dynnikov moves as allowed deformations) , the number of crossings is monotonically
decreasing [ Dynnikov ,2006], but both the representation of the knot as a grid diagram and the carrying out of
the simpliﬁcation steps are more complicated. These distinct repres entations of the same mathematical object
lend themselves to diﬀerent foundational models [ Gukov et al. ,2021,Kauﬀman et al. ,2022]; for example,
braid word representations of knot projections are closer to nat ural language, whereas other representations
are closer to vision tasks or graphs. The diﬀerent representation s also inform the type of algorithm that
needs to be used. If the simpliﬁcation is non-monotonic, a local sear ch can get stuck in local minima.
13https://community.middlebury.edu/ ~mathanimations/klo/
21One common activity in mathematics, when confronted with a new sta tement of unknown truth, a conjecture,
is to engage in the search for proof – or a counterexample. This com es with its own workﬂows. The search
for counterexamples to conjectures is particularly useful for ha rd problems with a truth certiﬁcate that can
be veriﬁed in polynomial time, such as NP-hard or NP-complete proble ms. The idea is to cast the search
problem into a Markov Decision Problem (MDP) whose terminal states are counterexamples, and attempt
to solve the MDP using data science techniques. In the past, deep r einforcement learning has proven to be a
powerful tool. If the RL agent ﬁnds a solution to the MDP, its episod ic rollouts provide truth certiﬁcates for
the counterexample, thus establishing a veriﬁably correct proof b y counter-example, see e.g. [ Gukov et al. ,
2024] for a recent summary of these ideas and [ Gukov et al. ,2021,Wagner ,2021,Gukov et al. ,2023,Charton
et al. ,2024] for some recent concrete applications.
4.2 Data Collection in Real Environments
To gather representative data on mathematical workﬂow steps, as well as other metamathematical items,
such as proof heuristics, limitations of certain proof techniques, e tc., it may be desirable to observe and
absorb the full process of producing mathematics, including all dat a that is not. For an example of real-time
narration of thought processes that arise when doing competitive problem-solving, see co-author Tim Gowers’
series of YouTube videos.14
Unfortunately, many of these intermediate process steps becom e evident only implicitly from data sources.
For example, at the elementary level, various workﬂows to solve var ious limits,
which require repeated applications of known theorems, such as de l’Hˆ opital’s theorem, or related ones to
resolve indeterminate cases, are distilled only by solving a large numbe r of exercises; no explicit annotations
for these workﬂows exist. On a more advanced level, these are oft en conveyed in blogs, talks, and oral
discussions between mathematicians at conferences – and not in th e typical data sources used to train
LLMs.
In principle, one could implement longitudinal studies that track rese arch projects from inception to com-
pletion. However, such data collection would require classifying, str ucturing, and recording diﬀerent tasks
throughout the mathematician’s daily work. The apparent challenge is to scale such approaches while keeping
the overhead as small as possible for the researcher whose work is tracked.
While such approaches are welcome to be tested, as a ﬁrst alternat ive step, we recommend transcribing
from online sources such as lectures, panel discussions, seminars , vlogs, etc. While such data only requires
minimal need for postprocessing and is often already collected in the form of videos, it typically covers
broader mathematical aspects than textbooks. However, while h umans can frequently generalize from a
single instance of a certain workﬂow, LLMs often require a dataset that contains suﬃciently many examples.
While data collection eﬀort will elicit higher-quality mathematical data, the time lag between the time when
new research discoveries are made and when these are represent ed in lectures can be signiﬁcant. On the other
hand, at venues such as conferences, a lot of information about m athematics is exchanged, but not recorded.
While it would technically be possible to record a portion of the convers ations that happen at a conference
in a privacy-preserving manner, and this would be a great source of data, as it one would consistently have
data that is at the forefront of research (unlike the mentioned pa nel discussions, where there is often a time
lag), it would require a paradigm shift from conference participants to accept such data collecting measures.
We urge further conversations about privacy-preserving ways o f curating richer datasets on mathematical
workﬂows, that minimally impinge on mathematicians’ naturalistic prac tices.
4.3 Motivated Proofs
We do not doubt that there is substantial value in bespoke AI tools t hat can automate speciﬁc elements of
a mathematician’s workﬂow. However, if the goal is not only to provid e correct proofs but also to enhance a
14https://www.youtube.com/@TimothyGowers0/videos
22user’s mathematical understanding of the results [ Zhang et al. ,2023a ] and guide new discoveries, we need new
tooling – and we argue, new kinds of data. In particular, we argue fo r data which faithfully represents the
process of proof discovery instead of proof exposition . Towards this goal, we introduce motivated proofs [P´ olya ,
1949,Morris ,2019], which contain and make transparent more of the proof discovery process. We argue for
their value as a standard for LLM evaluation. We then provide some e xamples and discuss some preliminary
observations about current LLM’s ability to construct and identify motivated proofs. Finally, we speculate
on a path towards large-scale evaluation of a model’s ability to produc e motivated proofs.
Broadly speaking, a motivated proof is one that makes clear to the r eader where each step comes from.
For example, many interesting proofs require one to ﬁnd a mathema tical object with certain properties.
An unmotivated proof will simply specify the object and check that it has the desired properties, while a
motivated proof will explain how to arrive at the object.
4.3.1 Examples of motivated proofs
We present two theorems here with examples of motivated proofs. Further examples can be found in Appendix
A.
Cantor’s theorem Cantor’s theorem states that there is no surjection from a set Xto its power set P(X).
The proof proceeds by letting f:X→P(X) be a function and trying to ﬁnd a subset of Xthat is not in
the image of f. From here, an unmotivated proof will simply exhibit a set, namely, {x∈X:x /∈f(x)}, and
verify that it is not in the image of f, which turns out to be straightforward.
By contrast, a motivated proof will systematically search for the r equired subset of X. Not knowing which
subset to take, we can treat the subset as an unknown, just as w e do when solving an equation, and try
to narrow down the possibilities. The most general subset of Xcan be expressed as {x∈X:P(x)}
for some as yet unspeciﬁed property P. We now want to prove, for an arbitrary element yofX, that
f(y)/\e}atio\slash={x∈X:P(x)}. So we need either an element xoff(y) such that ¬P(x) or an element xof the
complement of f(y) such that P(x). There are not many elements around, so trying yis one of the ﬁrst
things to do, and then we ﬁnd that we need either y∈f(y) and¬P(y) ory /∈f(y) andP(y). And now the
property y /∈f(y) is forced on us as our choice of P, and we end up with the same set as before, but this
time with its origin explained.
Nilpotent units Now we consider an early result from commutative algebra. Let Rbe a commutative
ring, and let x∈Rbe nilpotent, then (1 + x) is a unit, meaning it has a multiplicative inverse. This is
typically proved by naming an element y=/summationtextr−1
k=0(−1)k·xkand verifying that this is a multiplicative inverse
element by calculation. We regard this as unmotivated, since the disc overy process of ﬁnding ywas left out.
For a motivated proof, we need to search for an inverse element. N ot knowing which element to take, we
parametrize the most generic element we can. Since the only known e lements of Rare 1 and x, the most
generic element is an integer polynomial in x,/summationtextm
k=0akxk. For this to be a right inverse of 1 + x, we must
have that 1 = (1+ x)(/summationtextm
k=0akxk) =a0+/summationtextm
k=1(ak+ak−1)xk+amxm+1. For this to hold, we must eliminate
all coeﬃcients of the polynomial besides the constant term, which s hould be 1. This gives us that a0= 1,
ak=ak−1for 1≤k≤mandam= 0. The ﬁrst two equations give us that ak= (−1)kfor allk, but this
contradicts the last equation.
But we also know that xis nilpotent, so if we have rsuch that xr= 0, then all coeﬃcients from xronwards
can be ignored. This solves our issue, as we can let m=r−1 to remove the am= 0 condition, and we are
left with ak= (−1)k, so (1 + x) is a unit with inverse/summationtextr−1
k=0(−1)k·xk.
4.3.2 Motivated proofs as an evaluation metric
The standard for a proof’s acceptance into the mathematical liter ature has historically been correctness
rather than a completely motivated account. Moreover, mathema ticians have been incentivized to condense
23and reﬁne their proofs for reasons such as page limits in journals, w hich has further widened the gap between
proof discovery andproof exposition . To assess a model’s capabilities in aiding proof discovery, we suggest
that holding the proof to the standard of being motivated provides advantages over requiring only correctness.
As argued in [ P´ olya ,1949,Morris ,2019], a motivated proof is more informative to the reader, as it provides
more insight into how the proof was discovered and how the reader m ight discover similar results themselves.
More speculatively, a model capable of producing motivated proofs will likely generalize better to novel
problems. The ﬁrst reason for this conjecture is that most result s in the literature are not fully motivated,
and a model that is capable of recognising this is less likely to blindly reca ll its training data. Requiring
proofs to be motivated also restricts the amount of brute-force search a model can perform, so performance
depends more on reasoning ability and less on test-time computation al power.
We will now brieﬂy evaluate current LLMs’ ability to generate motivat ed proofs, as well as to evaluate
whether a given proof is motivated.
Generation of motivated proofs As a preliminary investigation, we prompted o1-preview and Llama
3.2-90B to produce motivated proofs of ﬁve mathematical results . Our goal was not to use best-in-class
LLMs since they typically diﬀer only by a few percentages on common b enchmarks; in contrast, we wanted
to obtain a preliminary assessment of whether LLMs have the ability t o work with the concept of a motivated
proof at all. The results on which we tested the abilities to generate m otivated proofs were selected to be
elementary but to require a slightly non-trivial construction. Afte r deﬁning motivated proofs, we provided
an in-context example of a motivated proof of the other four resu lts and asked the model to generate a new
motivated proof. If the model failed to provide a motivated proof, we would prompt it once to ﬁx it, pointing
out the unmotivated step. Each model was asked twice per problem , ﬁrst with only examples of motivated
proofs in the context, following a traditional chain-of-thought ap proach, then again with both examples and
non-examples, mimicking contrasting chain-of-thought prompting . The problems and associated proofs we
used in the prompts can be found in Appendix A.
In most responses, the model showed some evidence of “underst anding” the concept of motivated proofs by
avoiding unmotivated constructions. However, this often led to ps eudo-motivations, where some justiﬁcation
was given before a construction, but it didn’t provide any useful su bstance besides obscuring the unmotivated
step (and often appealed to some irrelevant fallacies). In the exam ple below, the unmotivated step of Cantor’s
theorem is relegated to the statement “An important question aris es: Does xbelong to its own image f(x)?”.
o1-preview (excerpt)
Our goal is to ﬁnd a subset of Xthat cannot possibly be the image of any element under f. To do this,
we’ll consider how elements of Xrelate to their images under f.
Exploring the Relationship Between Elements and Their Imag es:
For each element x∈X,f(x) is a subset of X. An important question arises: Doesxbelong
to its own image f(x)?
This leads us to categorize the elements of Xinto two groups:
1. Elements that are members of their image: x∈f(x).
2. Elements that are not members of their image: x /∈f(x).
The other common issue was the model making completely unsound de ductions when trying to motivate
their construction, only to arrive at the correct result by chance . This behavior is consistent with the
model not fully understanding the result but having seen it in their tr aining data and attempting post-hoc
rationalization. Below is an example:
24Llama-3.2 (excerpt)
We want to ﬁnd a subset Y⊆Xsuch that φ(x) =Yfor some x∈X. However, we don’t know which
subset to choose.
Let’s try to ﬁnd a property that Yshould satisfy. Since φ(x) =Y, we know that x∈φ(x) =Y. But we
also know that x /∈φ(x), because if x∈φ(x), thenφ(x) would contain at least two elements: xandφ(x).
This suggests that Yshould be a subset of Xthat contains some elements of X, but not all of them. In
particular, Yshould not contain xitself.
With this in mind, let’s deﬁne Y={x∈X|x /∈φ(x)}.
Here, the contradictory claims that x∈φ(x) andx /∈φ(x) have no basis, and if true would imply an
immediate contradiction, making the remainder of the proof redund ant. Also, the condition for Yis in fact
the opposite of what is needed, but this error doesn’t seem to aﬀec t the remainder of the model’s reasoning.
Other problems provided more hopeful examples: a motivated proo f for the large totients problem was
successfully generated both times by o1-preview and once by Llama .
Overall, o1-preview seemed to outperform Llama on most problems. We also observed a slight improvement
by using negative as well as positive examples to “explain” the concep t. As an unfortunate side eﬀect, the
extra information also increased the tendency to “obscure” unmo tivated arguments as discussed above.
Recognition of motivated proofs To conduct a larger scale investigation of a model’s ability to generate
motivated proofs, it would help if there was an existing “judge” mode l which could determine whether or
not a given proof was motivated. In any case, recognition of motiva ted proofs represents an easier sub-goal
towards generating motivated proofs.
We performed a small, preliminary investigation of whether current s tate-of-the-art models can reliably dis-
tinguish a motivated proof from an unmotivated proof. We stress t hat this is only a preliminary investigation
and do not claim to draw any strong conclusion, but hope that this will inspire the community to carry out
larger evaluations in this regard and work towards a standard of ev aluating motivated proofs.
We ﬁrst tested the model’s ability to identify whether a given proof wa s motivated. We tested the ﬁve
problems from the previous section, where each problem had three proofs to be evaluated individually.
This included two human-written proofs, which we judged to be para digmatic examples of motivated and
unmotivated proofs, one unmotivated machine-generated proof and, where available, one motivated machine-
generated proof. The unmotivated machine-generated proof wa s the ﬁrst correct but unmotivated proof
generated by Llama-3.2 in the previous section. For the machine-ge nerated motivated proof, we took the
response in the previous section that we judged to be most motivat ed, which was generated by Llama in the
integer sum problem and o1-preview for nilpotent units and large tot ients, while for the other problems no
responses were deemed suﬃciently motivated.
For some proofs where there were incorrect but largely inconsequ ential components, we manually altered
some equations to enforce correctness and removed any opening or closing sentences that included the phrase
“motivated proof” to avoid misleading the model. As with generation, we prompted the model by explaining
the deﬁnition of a motivated proof and giving an example and non-exa mple for each of the other problems,
where the order of examples and non-examples was alternated to e nsure that the model wasn’t learning
the ordering. Each model was given three attempts per proof per problem, and the results are recorded
below. We use HM, HU, MM and MU as abbreviations for “human motivat ed”, “human unmotivated” and
“machine unmotivated” respectively.
25o1-preview Llama-3.2 Total
HM HU MM MU HM HU MM MU TP TN
Cantor’s theorem 3/3 3/3 - 3/3 3/3 0/3 - 0/3 6/6 6/12
Small doubling 3/3 3/3 - 2/3 3/3 3/3 - 2/3 6/6 10/12
Integer sum 3/3 3/3 3/3 2/3 2/3 3/3 3/3 0/3 11/12 8/12
Nilpotent units 3/3 3/3 3/3 3/3 2/3 3/3 3/3 0/3 11/12 6/12
Large totients 3/3 3/3 3/3 3/3 3/3 2/3 3/3 1/3 12/12 9/12
Total 15/15 15/15 9/9 13/15 13/15 8/15 9/9 3/15 46/48 39/60
Under this setup, o1-preview performed strongly, while Llama was h eavily biased towards accepting a proof
as motivated. A possible explanation for Llama’s poor performance in the MU set is that the machine-
generated unmotivated proofs, unlike the human-generated one s, were attempts at generating motivated
proofs, so these proofs contained some superﬁcial features su ch as proof length and “chatty” language that
the model had associated with motivated proofs.
In an eﬀort to address this issue, we re-framed the experiment as a binary choice task. This was largely the
same as above, but instead of being given a single proof to judge, th e models were given two proofs and
were told that one was motivated and one was unmotivated, and to j udge which was motivated. Again we
recorded the success rate over three valid attempts per (unmot ivated,motivated) pair, per problem. The
results are shown below.
o1-preview Llama-3.2 Total
Unmotivated proof source Human Model Human Model
Cantor’s theorem 3/3 3/3 3/3 3/3 12/12
Small doubling 3/3 3/3 3/3 3/3 12/12
Integer sum 6/6 6/6 6/6 6/6 24/24
Nilpotent inverses 6/6 3/6 0/6 2/6 11/24
Large totients 6/6 4/6 6/6 5/6 21/24
Total 24/24 19/24 18/24 19/24 80/96
This improved evaluation method narrowed the gap between the two models, especially when using the
MU proof which Llama previously struggled with, providing some eviden ce that the binary choice strategy
reduces the model’s tendency to be misled by superﬁcial features c ommon to motivated proofs.
We stress that this is only a preliminary investigation, and that a large r investigation would be required
to make strong claims about an LLM’s ability to judge motivated proof s. We welcome the community to
conduct a larger investigation, advising the following notes of cautio n based oﬀ our experience and some
speculation:
•It is easier for models to decide between two proofs, which is motivat ed, than to make an absolute
judgement of a single proof.
•Models can be sensitive to the order in which the proofs are present ed, so it is important to permute
these (including the in-context examples).
•Models can be misled by superﬁcial features common to motivated pr oofs, so it is important that false
examples also have these features. We achieved this to some exten t by using an LLM’s failed attempt at
writing a motivated proof, but this could potentially also be achieved w ith care in a human-generated
dataset.
Recommendations The existing mathematical literature, machine learning datasets an d output evalua-
tion standards are concentrated mostly on proof correctness, and our principal recommendation is to increase
emphasis on proof motivation to better reﬂect the proof discover y process. One natural path forward would
be to create a corpus of mathematical results with corresponding motivated and unmotivated proofs, and
26then to conduct a detailed evaluation of current models’ ability to dis tinguish these. Once it is ascertained
that models can judge motivation with high accuracy, one can design metrics for motivated proof generation.
5 Mathematical Datasheet for Datasets
We next propose an amendment to the datasheets for datasets ( DfD) framework [ Gebru et al. ,2021], speciﬁc
for datasets in mathematics. The DfD framework provides a compr ehensive questionnaire that any dataset
developer would beneﬁt from answering; we encourage developers of new mathematical datasets to include all
original DfD questions as well as our new set of questions outlined be low, yielding mathematical datasheets
for datasets ( mDfDs). (We note that there have been other important calls for da ta labelling, e.g., data
cards [ Pushkarna et al. ,2022] and data statements [ Bender and Friedman ,2018]; we choose DfD as a starting
point given its comprehensiveness and generality.)
Based on the survey of the landscape of mathematical datasets p rovided in this article, we propose the
inclusion of the additional questions for any dataset involving mathe matics, as outlined in Figure 1. We
include two additional sets of questions to consider on a case-by-c ase basis, depending on whether the
dataset includes formal or informal mathematics. If both, we enc ourage providing information for each set
of questions. We strive for only light—but we argue critical—additions to the DfD framework to avoid excess
burden on research teams.