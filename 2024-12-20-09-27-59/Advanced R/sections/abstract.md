This paper presents the Advanced Reasoning and Trans-
formation Engine for Multi-Step Insight Synthesis in
Data Analytics (ARTEMIS-DA) , a novel framework
designed to augment Large Language Models (LLMs)
for solving complex, multi-step data analytics tasks.
ARTEMIS-DA integrates three core components: the
Planner , which dissects complex user queries into struc-
tured, sequential instructions encompassing data prepro-
cessing, transformation, predictive modeling, and visual-
ization; the Coder , which dynamically generates and ex-
ecutes Python code to implement these instructions; and
theGrapher , which interprets generated visualizations to
derive actionable insights. By orchestrating the collabo-
ration between these components, ARTEMIS-DA effec-
tively manages sophisticated analytical workflows involv-
ing advanced reasoning, multi-step transformations, and
synthesis across diverse data modalities. The framework
achieves state-of-the-art (SOTA) performance on bench-
marks such as WikiTableQuestions and TabFact, demon-
strating its ability to tackle intricate analytical tasks with
precision and adaptability. By combining the reasoning
capabilities of LLMs with automated code generation and
execution and visual analysis, ARTEMIS-DA offers a ro-
bust, scalable solution for multi-step insight synthesis, ad-
dressing a wide range of challenges in data analytics.1 Introduction
The advent of Large Language Models (LLMs), such as
GPT-3 [1], GPT-4 [15], and Llama 3 [5], has revolution-
ized the fields of artificial intelligence (AI) and natural
language processing (NLP). These models have demon-
strated remarkable capabilities in complex interpretation,
reasoning, and generating human-like language, achiev-
ing success in diverse applications such as language trans-
lation, summarization, content generation, and question-
answering. Their ability to process and generate coher-
ent text has also made them powerful tools for tasks re-
quiring nuanced understanding and reasoning. However,
while LLMs have been extensively explored in these do-
mains, their potential in transforming the field of data an-
alytics remains underutilized. The inherent reasoning and
code-generation capabilities of LLMs suggest immense
promise for enabling non-technical users to interact with
complex datasets using natural language, bridging the gap
between advanced analytics and accessibility.
Recent efforts, including TableLLM [12], CABINET
[18], and Chain-of-Table [22], have begun to explore this
intersection. These studies focus on table-based ques-
tion answering and reasoning tasks, leveraging LLMs to
interpret and respond to queries grounded in structured
datasets. While these works demonstrate the potential ofarXiv:2412.14146v1  [cs.AI]  18 Dec 2024ARTEMIS-DA A P REPRINT
LLMs for data analytics, they primarily address single-
step tasks, leaving multi-step analytical processes—such
as complex data transformation, predictive modeling, and
visualization—relatively unexplored. These tasks often
require sequential reasoning, complex task decomposi-
tion, and precise execution across diverse operations, pre-
senting challenges that current frameworks are not yet
equipped to manage effectively.
To address this gap, we propose the Advanced Reason-
ing and Transformation Engine for Multi-Step Insight
Synthesis in Data Analytics (ARTEMIS-DA) , a com-
prehensive framework explicitly designed to unlock the
potential of LLMs for advanced multi-step data analytics
tasks. ARTEMIS-DA introduces a tri-component archi-
tecture consisting of a Planner , aCoder , and a Grapher ,
each playing a crucial, complementary role. The Planner
acts as the framework’s coordinator, interpreting complex
user queries and decomposing them into a sequence of
structured instructions tailored to the dataset and analyti-
cal goals. These instructions encompass tasks such as data
pre-processing, transformation, predictive analysis, and
visualization. By leveraging the natural language under-
standing and reasoning capabilities of LLMs, the Planner
ensures clarity and structure in task execution, addressing
the intricacies of multi-step analytical workflows.
TheCoder , in turn, translates the Planner’s instructions
into executable Python code, dynamically generating and
executing the necessary operations within a Python en-
vironment. Whether performing data transformations,
training predictive models, or creating visualizations, the
Coder bridges the gap between high-level task specifica-
tions and low-level computational execution. This dy-
namic interplay between the Planner and Coder compo-
nents enables ARTEMIS-DA to handle analytical tasks
autonomously, requiring minimal user intervention.
TheGrapher is another key component of ARTEMIS-
DA, analyzing the generated graphs and visualizations to
extract valuable insights. By interpreting visual represen-
tations of data, the Grapher enables a deeper understand-
ing of the underlying patterns and trends. The Grapher
works in close coordination with the Planner and Coder,
facilitating the seamless integration of data analysis, visu-
alization, and insight extraction into a unified framework.
Together, these components empower ARTEMIS-DA to
deliver actionable insights, facilitating natural language
interactions with complex datasets and enhancing acces-
sibility for users without programming expertise.
ARTEMIS-DA’s effectiveness is underscored by its State-
of-the-Art (SOTA) performance on benchmarks such as
WikiTableQuestions [17] and TabFact [3]. These results
highlight its ability to manage nuanced analytical tasks re-
quiring advanced multi-step reasoning. Beyond answer-
ing structured dataset queries, ARTEMIS-DA demon-
strates versatility in transforming datasets, visualizing re-
sults, and conducting predictive modeling, positioning it
as a transformative tool in LLM-powered data analytics.The remainder of this paper is structured as follows: Sec-
tion 2 reviews related work on LLM applications in data
analytics and automated task decomposition. Section 3
presents the architecture of ARTEMIS-DA, focusing on
its components and their respective roles. Section 4 eval-
uates the framework’s performance on established bench-
marks, while Section 5 demonstrates ARTEMIS-DA’s ca-
pabilities in generating visualizations and predictive mod-
eling. Finally, Section 6 concludes with insights into fu-
ture directions for advancing LLM-powered data analytics
and further enhancing LLMs for other complex tasks that
require multi-step reasoning.
Through the development of ARTEMIS-DA, we con-
tribute a significant advancement to the emerging field
of LLM-driven data analytics, offering a fully integrated
end-to-end system capable of managing complex, multi-
step analytical queries with minimal user intervention.
This framework aims to redefine the accessibility, effi-
ciency, and scope of data analytics, establishing a new
paradigm for LLM-assisted insight synthesis.
2 Related Works
In recent years, Large Language Models (LLMs) have
demonstrated promise in addressing complex tasks in nat-
ural language processing and reasoning. However, when
applied to structured data, such as large tables, unique
challenges arise, requiring specialized frameworks and
adaptations. Recent studies have made significant strides
in enhancing LLMs’ reasoning capabilities with tabu-
lar data, providing the foundation for the ARTEMIS-DA
framework proposed in this paper.
Tabular Reasoning with Pre-trained Language Mod-
els. Traditional approaches with pre-trained language
models such as TaBERT[27], TAPAS[7], TAPEX[11],
ReasTAP[30], and PASTA[6] were developed to combine
free-form questions with structured tabular data. These
models achieved moderate success by integrating table-
based and textual training, enhancing tabular reasoning
capabilities. However, their ability to generalize under ta-
ble perturbations remains limited[2, 31]. Solutions such
as LETA[31] and LATTICE[21] addressed these limita-
tions using data augmentation and order-invariant atten-
tion. However, they require white-box access to models,
making them incompatible with SOTA black-box LLMs.
Table-Specific Architectures for LLMs. Table-specific
models further refined the use of structured tabular
data, emphasizing row and column positioning such
as TableFormer[25] which introduced positional embed-
dings to capture table structure, mitigating the impact of
structural perturbations. Despite these advances, frame-
works like StructGPT[9] highlighted that generic LLMs
still struggle with structured data unless enhanced with
explicit symbolic reasoning. Recently proposed frame-
works such as AutoGPT[20] and DataCopilot[29] began
addressing table-specific challenges by incorporating ad-
vanced reasoning techniques. However, their performance
2ARTEMIS-DA A P REPRINT
remains constrained across diverse scenarios due to their
reliance on generic programming for task execution.
Noise Reduction in Table-Based Question Answering.
Handling noise in large, complex tables is another ac-
tive research area. CABINET[18] introduced a Con-
tent Relevance-Based Noise Reduction strategy, signif-
icantly improving LLM performance by employing an
Unsupervised Relevance Scorer (URS). By filtering ir-
relevant information and focusing on content relevant to
user queries, CABINET achieved notable accuracy im-
provements on datasets like WikiTableQuestions[17] and
FeTaQA[13], underscoring the importance of noise reduc-
tion in reliable table-based reasoning.
Few-Shot and Zero-Shot Learning for Tabular Rea-
soning. Few-shot and zero-shot learning methods have
shown considerable promise in tabular understanding
tasks. Chain-of-Thought (CoT) prompting[23] improved
LLMs’ sequential reasoning capabilities. Building on
this, studies such as[4, 26] integrated symbolic reason-
ing into CoT frameworks, enhancing query decomposi-
tion and understanding. However, these techniques are
not tailored to tabular structures, leading to performance
gaps. Chain-of-Table[22] addressed these limitations by
introducing an iterative approach to transforming table
contexts, enabling more effective reasoning over struc-
tured data and achieving state-of-the-art results on bench-
marks such as WikiTableQuestions[17] and TabFact[3].
Programmatic Approaches to Tabular Question An-
swering. Leveraging programmatic techniques has sig-
nificantly advanced the field of table-based question an-
swering by enabling models to interpret and process
structured data more effectively. Text-to-SQL models
such as TAPEX[11] and OmniTab[10] trained large lan-
guage models (LLMs) to translate natural language ques-
tions into SQL operations, demonstrating the potential
for automated interaction with tabular datasets. Despite
their promise, these models struggled with noisy and
large tables due to limited query comprehension. Pro-
grammatically enhanced solutions, such as Binder[4] and
LEVER[14], improved performance by generating and
verifying SQL or Python code. However, their reliance
on single-pass code generation restricted their adaptabil-
ity to queries requiring dynamic reasoning.
Building on these advancements and addressing the limi-
tations of previous models, we introduce the Advanced
Reasoning and Transformation Engine for Multi-
Step Insight Synthesis in Data Analytics (ARTEMIS-
DA). Unlike prior models, ARTEMIS-DA features a tri-
component architecture consisting of a Planner , aCoder ,
and a Grapher , which collaboratively address complex,
multi-step analytical queries. The Planner generates dy-
namic task sequences tailored to specific datasets and
queries, encompassing data transformation, predictive
analysis, and visualization. The Coder translates these se-
quences into Python code and executes them in real time.
Finally, the Grapher extracts actionable insights from the
visualizations produced by the Coder, enhancing result in-terpretability and ensuring the seamless integration of vi-
sual insights into user workflows.
This seamless integration of the Planner, Coder, and
Grapher components enables ARTEMIS-DA to tackle
intricate tasks requiring sequential reasoning, synthe-
sis, and visualization, achieving state-of-the-art perfor-
mance on benchmarks such as WikiTableQuestions[17]
and TabFact[3]. ARTEMIS-DA extends LLM function-
ality in data analytics, providing a robust, automated so-
lution that empowers technical and non-technical users to
interact with complex datasets through natural language.
3 ARTEMIS-DA Framework
TheAdvanced Reasoning and Transformation Engine
for Multi-Step Insight Synthesis in Data Analytics
(ARTEMIS-DA) is designed to address the challenges of
complex data analytics by combining advanced reason-
ing capabilities with dynamic, real-time code generation,
execution and visual analysis. The framework, shown in
Figure 2, consists of three core components: the Plan-
ner, the Coder and the Grapher . Working in unison,
these components decompose complex queries into se-
quential tasks, automatically generate and execute the re-
quired code for each task, and synthesize insights based
on generated graphs with minimal user intervention.
For the experiments in this paper, all three components
utilize the LLaMA 3 70B model[5], which demonstrated
superior performance across benchmarks. The Grapher
component also employs the LLaMA 3.2 Vision 90B
model for understanding generated graphs. However, the
framework is model-agnostic and can be adapted to work
with other state-of-the-art large language models (LLMs),
such as GPT-4[15] or Mixtral-8x7B[8].
The following sections provide an in-depth exploration
of the Planner, Coder and Grapher components, detail-
ing their roles and interactions. Together, they exemplify
ARTEMIS-DA’s ability to streamline end-to-end data an-
alytics workflows effectively and efficiently.
3.1 Planner Component
ThePlanner serves as the central reasoning and task-
decomposition unit within the ARTEMIS-DA framework,
converting user queries into structured sequences of tasks.
Its primary responsibilities include parsing user inputs,
organizing them into a logical workflow, and interpret-
ing the outputs of executed code and generated visual
insights to guide subsequent steps in the analytical pro-
cess. The Planner is adept at managing complex, multi-
faceted queries that require diverse operations, such as
data transformation, predictive modeling, and visualiza-
tion. By leveraging the advanced reasoning capabilities
of large language models (LLMs), it decomposes intri-
cate requirements into optimized task sequences aligned
with the input data, prior outputs, and specific details of
3ARTEMIS-DA A P REPRINT
Figure 2: ARTEMIS-DA Framework
the user’s query, ensuring clarity for seamless execution
by the Coder and Grapher as required.
For instance, when tasked with analyzing sales patterns
and forecasting future trends, the Planner systematically
outlines essential steps, such as data pre-processing, fea-
ture engineering, model training, evaluation and forecast-
ing, organizing them into a coherent workflow. This pro-
cess is dynamically tailored to the dataset’s properties and
the nuances of the query, enabling an adaptive approach
to multi-step analytical tasks. Each task specification is
then relayed to the Coder or Grapher in sequence, ensur-
ing a smooth and collaborative workflow across the com-
ponents of the ARTEMIS-DA framework.
3.2 Coder Component
Following the Planner’s generation of a structured task se-
quence, the Coder translates these tasks into executable
Python code. It processes instructions for each step—such
as loading data, creating visualizations, or training predic-
tive models—producing contextually relevant and func-
tionally precise code tailored to the task’s requirements.
Operating in real time within a Python environment, the
Coder executes each code snippet, generating intermedi-
ate outputs that are fed back to the Planner for further
analysis and informed decision-making.
The Coder’s capabilities encompass a broad range of an-
alytical operations, from basic data cleaning and sum-marization to advanced predictive modeling and visual-
ization. For instance, when the user requests predictive
analysis on time-series data, the Planner decomposes the
query into multiple simple steps such as splitting the data,
training a suitable model, and visualizing the results. The
Coder generates and executes code for each step, with the
Planner overseeing all steps in the process. This iterative
exchange between the Planner and Coder ensures accurate
execution of each analytical step, maintaining a continu-
ous feedback loop until the analysis is fully completed.
3.3 Grapher Component
TheGrapher serves as a critical component for deriv-
ing actionable insights from visual data, responding to in-
structions generated by the Planner . Upon receiving a
directive to analyze a generated graph from the Planner,
the Grapher processes the visual output and provides in-
sights in a structured question-and-answer format. Its an-
alytical capabilities encompass a broad spectrum, ranging
from basic data extraction from plots to advanced inter-
pretation and trend analysis of complex plots.
For instance, if the Planner requests an analysis of time-
series data, and the Coder generates a corresponding line
plot, the Grapher can identify trends, detect anomalies,
and highlight significant observations. This feedback en-
ables the Planner to refine its understanding and produce
more nuanced insights. Additionally, the Grapher sup-
ports a wide variety of graph types, including bar charts,
pie charts, scatter plots, and heatmaps, among others, en-
suring versatility across diverse data visualization needs.
By seamlessly integrating graph interpretation into the
workflow, the Grapher enhances the framework’s capac-
ity to provide meaningful, data-driven conclusions.
3.4 Workflow and Interaction between Components
The ARTEMIS-DA framework employs a systematic
workflow to process user queries with precision and ef-
ficiency. This process, illustrated in Figure 3, highlights
the seamless interaction between the Planner, Coder, and
Grapher components as outlined below:
1.Input: The workflow begins when the user submits a
dataset and a natural language query describing their
analytical objectives. The Coder starts by generating
the Python code to load the dataset and display the col-
umn types and the first five rows of the dataset.
2.Decomposition: The Planner analyzes the query and
decomposes it into a structured sequence of tasks,
leveraging outputs from df.info() anddf.head()
to extract actionable context. For instance, a query to
compare media categories might involve counting the
number of TV shows and movies, creating a pie chart
for visualization, and analyzing the generated chart for
insights. Each task is methodically assigned to the
Coder or Grapher as appropriate.
4ARTEMIS-DA A P REPRINT
Figure 3: Workflow of the ARTEMIS-DA framework showcasing its multi-component collaboration.
3.Execution: The Coder translates the Planner’s instruc-
tions into executable Python code. Tasks are executed
sequentially, producing intermediate outputs. In the
sample query, the Coder generates the code to count
the specified categories, generate the pie chart, and
prepare the visual output for analysis.
4.Analysis: The Grapher processes the Planner’s in-
structions to derive insights from generated visuals. In
the sample query, the Grapher analyzes the pie chart to
calculate and report the proportions of TV shows and
movies, presenting insights in a structured format.
5.Feedback Loop: Intermediate outputs, such as com-
puted values, visualizations, and insights, are returned
to the Planner. The Planner evaluates these results to
determine if additional steps are necessary. If further
actions are required, new instructions are dynamically
generated for the Coder or Grapher, maintaining a re-
sponsive feedback loop to achieve the task.
6.Finalization: Once all tasks are completed, the Plan-
ner aggregates the results, refines the insights, and
compiles the final output. The final result, enhanced
with additional insights if necessary, is presented to the
user along with a </done> tag, indicating the success-
ful conclusion of the workflow.
3.5 Advantages of the ARTEMIS-DA Framework
The ARTEMIS-DA framework represents a significant
advancement in data analytics by integrating sophisti-
cated natural language understanding with precise com-
putational execution and visual insight synthesis. Its tri-
component architecture—comprising the Planner, Coder,and Grapher—enables the framework to efficiently han-
dle complex, multi-step analytical tasks, all while provid-
ing an intuitive interface suitable for users across various
levels of technical expertise.
ARTEMIS-DA achieves state-of-the-art performance on
challenging datasets such as WikiTableQuestions[17],
TabFact[3], and FeTaQA[13], demonstrating its versatil-
ity in extracting comprehensive, data-driven insights. The
framework’s ability to dynamically interpret user queries,
generate and execute Python code in real-time, and an-
alyze generated visuals further enhances its adaptability
and practical value. These features collectively position
ARTEMIS-DA as a cutting-edge solution for addressing
the modern challenges of data analytics with precision,
efficiency, and user-centered design.
4 Experiments and Evaluation
This section provides an overview of the benchmark
datasets utilized for evaluation, the metrics employed
to compare the performance of the models, the results
achieved by the ARTEMIS-DA framework, and a com-
prehensive analysis of these results.
4.1 Datasets
The ARTEMIS-DA framework is evaluated on three
table-based reasoning datasets: WikiTableQuestions [17],
TabFact [3], and FeTaQA [13]. We evaluate ARTEMIS-
DA exclusively on the test sets of these datasets without
any training or fine-tuning on the training sets. The details
of each dataset are as follows:
5ARTEMIS-DA A P REPRINT
ModelWikiTableQuestions TabFact FeTaQA
Accuracy Accuracy S-BLEU BLEU
With Fine-tuned / Trained
ReasTAP-Large[30] 58.7 86.2 - -
OmniTab-Large[10] 63.3 - 34.9 -
LEVER[14] 65.8 - - -
CABINET[18] 69.1 - 40.5 -
Without Fine-tuning/Training
Binder[4] 64.6 86.0 - -
DATER[26] 65.9 87.4 30.9 29.5
Tab-PoT[24] 66.8 85.8 - -
Chain-of-Table[22] 67.3 86.6 - 32.6
SynTQA (RF)[28] 71.6 - - -
Mix-SC[12] 73.6 88.5 - -
SynTQA (GPT)[28] 74.4 - - -
ARTEMIS-DA (Ours) 80.8 (+6.4) 89.9 (+1.4) 62.7 (+22.2) 46.4 (+13.8)
Table 1: Performance comparison for models on WikiTableQuestions, TabFact and FeTaQA datasets.
ModelWikiTableQuestions TabFact FeTaQA
Accuracy Accuracy S-BLEU BLEU
Best SOTA Model 74.4 [28] 88.5 [12] 40.5 [18] 32.6 [22]
LLaMA 3 70B 72.1 85.1 11.0 20.4
Single Step ARTEMIS-DA 76.6 87.6 40.8 32.8
ARTEMIS-DA (Ours) 80.8 (+4.2) 89.9 (+1.4) 62.7 (+21.9) 46.4 (+13.6)
Table 2: Ablation study of ARTEMIS-DA on WikiTableQuestions, TabFact and FeTaQA datasets.
•TabFact [3]: This dataset serves as a benchmark for
table-based fact verification, comprising statements cre-
ated by crowd workers based on Wikipedia tables. For
example, a statement such as “the industrial and com-
mercial panel has four more members than the cultural
and educational panel” must be classified as “True” or
“False” based on the corresponding table. We report the
accuracy on the test-small set, which consists of 2,024
statements and 298 tables.
•WikiTableQuestions [17]: This dataset includes com-
plex questions generated by crowd workers that are
based on Wikipedia tables. The questions require vari-
ous complex operations such as comparison, aggrega-
tion, and arithmetic, necessitating compositional rea-
soning across multiple entries in the given table. We
utilize the standard test set, containing 4,344 samples.
•FeTaQA [13]: This dataset consists of free-form tables
questions that demand advanced reasoning. Most ques-
tions are based on information extracted from discontin-
uous sections of the table. We evaluate ARTEMIS-DA
on the test set, which includes 2,003 samples.4.2 Evaluation Metrics
To assess the performance of ARTEMIS-DA across the
datasets, we employ a range of metrics tailored to the spe-
cific tasks. For the TabFact [3] dataset, which focuses on
table-based fact verification, we utilize binary classifica-
tion accuracy to evaluate the correctness of statements in
relation to the provided tables. In the case of WikiTable-
Questions [17], we measure denotation accuracy to deter-
mine whether the predicted answers align with the ground
truth, leveraging the LLaMA 3 70B[5] model for veri-
fication. Since FeTaQA [13] aims to generate compre-
hensive, long-form answers rather than short phrases, we
adopt both BLEU [16] and SacreBLEU [19] as our eval-
uation metrics. BLEU, a widely used metric in machine
translation, assesses the quality of generated text by com-
paring it to high-quality reference translations, producing
scores that range from 0 to 1, with higher values indicating
greater similarity. SacreBLEU addresses inconsistencies
commonly found in BLEU score reporting by providing
a standardized framework for computation, ensuring that
results are shareable, comparable, and reproducible across
studies. The use of two distinct metrics for the FeTaQA
6ARTEMIS-DA A P REPRINT
[13] dataset is warranted due to the variation in metrics
employed in different studies. By leveraging these met-
rics, we can effectively evaluate ARTEMIS-DA’s capabil-
ities in table-based reasoning tasks and benchmark its per-
formance against existing models.
4.3 Results
Table 1 highlights ARTEMIS-DA’s state-of-the-art per-
formance across the WikiTableQuestions[17], TabFact[3],
and FeTaQA[13] datasets. These results highlight the
framework’s adaptability and effectiveness in understand-
ing, processing, and reasoning over structured tabular data
across diverse domains and use cases.
In the WikiTableQuestions[17] dataset, ARTEMIS-DA
achieves an accuracy of 80.8% , outperforming previous
models such as SynTQA (GPT)[28], CABINET[18], and
LEVER[14]. This significant improvement of +6.4%
over the prior best underscores ARTEMIS-DA’s superior
compositional reasoning abilities, enabling it to effec-
tively address complex table-based questions that require
multi-step logical reasoning.
Similarly, for the TabFact[3] dataset, ARTEMIS-DA
achieves an accuracy of 89.9% , surpassing Mix-SC[12]
by+1.4% . This result demonstrates ARTEMIS-DA’s ef-
ficiency in verifying factual statements against tabular
data with high precision, showcasing its strength in fact-
checking tasks across diverse data representations.
For the FeTaQA[13] dataset, ARTEMIS-DA delivers ex-
ceptional results in generating high-quality long-form an-
swers. It achieves S-BLEU[19] and BLEU[16] scores
of62.7 and 46.4, respectively, representing a sub-
stantial improvement over previous models, including
CABINET[18] and Chain-of-Table[22], with gains of
+22.2 and +13.8 , respectively. These results highlight
ARTEMIS-DA’s ability to extract, synthesize, and inte-
grate discontinuous information from tables, providing
coherent and contextually rich answers.
Overall, ARTEMIS-DA establishes itself as a highly ver-
satile and effective solution for table-based reasoning and
computational tasks. Leveraging the LLaMA 3 70B[5]
and LLaMA 3.2 Vision 90B models, ARTEMIS-DA con-
sistently delivers state-of-the-art results across multiple
datasets, further cementing its role as a transformative tool
for compositional reasoning, fact verification, and long-
form answer generation in diverse domains.
4.4 Ablation Study
To thoroughly assess the necessity of the multi-step de-
sign in the ARTEMIS-DA framework for addressing com-
plex data analytics tasks, we conduct a detailed ablation
study. The Single-Step ARTEMIS-DA variant eliminates
the multi-step reasoning capability and instead processes
each query in a single step. By including this simplified
variant, we aim to isolate and highlight the specific con-
tributions of the multi-step reasoning approach employedby ARTEMIS-DA when applied to a diverse set of bench-
mark datasets.
As shown in Table 2, Single-Step ARTEMIS-DA achieves
76.6% accuracy on WikiTableQuestions, 87.6% on Tab-
Fact, and achieves 40.8 S-BLEU and 32.8 BLEU on Fe-
TaQA, surpassing LLaMA 3 70B (72.1%, 85.1%, 11.0
S-BLEU, and 20.4 BLEU, respectively) but falling short
of ARTEMIS-DA. The complete model outperforms both,
achieving 80.8% accuracy on WikiTableQuestions ( 4.2%
gain) and 89.9% on TabFact ( 1.4% gain), exceeding the
SOTA benchmarks of 74.4% and 88.5% respectively. On
FeTaQA, ARTEMIS-DA achieves 62.7 S-BLEU and 46.4
BLEU, representing significant improvements of +21.9 S-
BLEU and +13.6 BLEU over Single-Step ARTEMIS-DA.
These results confirm the value of ARTEMIS-DA’s multi-
step approach in handling complex queries, essential for
accurate data analysis with LLMs.
5 ARTEMIS Capability Demonstration
This section presents ARTEMIS-DA’s capabilities in plot
visualization and predictive modeling across a range of
datasets, highlighting its versatility and robustness.
5.1 Plot Visualization
Figure 4 presents a diverse collection of visualizations
generated by ARTEMIS-DA, demonstrating its analyt-
ical capabilities using the Spotify Most Streamed Songs
dataset from Kaggle. These visualizations address a range
of analytical questions, showcasing ARTEMIS-DA’s abil-
ity to effectively generate, interpret, and extract insights
from various plot types. For instance, the box plot com-
pares streams for tracks released in the last 10 years, iden-
tifying streaming trends over time. The pie chart analyzes
the proportion of tracks released by year over the past
five years, highlighting production patterns and identify-
ing peak and low-release years. A heatmap reveals cor-
relations among attributes like danceability%, energy%,
and valence%, uncovering relationships between musical
features. Additionally, the bar plot highlights the top 10
tracks by total streams, offering a view of popular listener
preferences, while the scatter plot explores potential cor-
relations between energy% and danceability%. The his-
togram details the distribution of danceability% across all
tracks, providing insights into its variability. A line plot
illustrates the trend of average energy% of tracks over the
years, shedding light on changes in the energy levels over
time. The violin plot compares the distributions of dance-
ability% and energy%, providing a nuanced understand-
ing of their variability. Lastly, the radar chart contrasts at-
tributes such as danceability%, valence%, energy%, and
acousticness% for the top 5 tracks by total streams, of-
fering a comparison of these popular tracks. Together,
these plots underscore ARTEMIS-DA’s versatility and ef-
fectiveness in generating insightful, data-driven visualiza-
tions from complex datasets.
7ARTEMIS-DA A P REPRINT
Figure 4: ARTEMIS-DA’s visualizations using the Spotify Most Streamed Songs dataset.
5.2 Predictive Modeling
Figure 5 illustrates ARTEMIS-DA’s predictive modeling
capabilities, emphasizing its effectiveness across diverse
datasets and analytical tasks. These examples demon-
strate the framework’s ability to adapt seamlessly to vari-
ous problem domains, showcasing ARTEMIS-DA as a ro-
bust solution for a wide range of predictive applications.
•Classification of Gender Data: The top-left sub-
figure highlights ARTEMIS-DA’s ability to handle bi-
nary classification tasks using the Gender Classification
dataset. By building a model to predict gender based on
input features, ARTEMIS-DA achieves an accuracy of
96.7%, demonstrating its proficiency in solving classi-
fication problems and its applicability to tasks such as
customer profiling and demographics analysis.
•Clustering of Superhero Powers: The top-right sub-
figures demonstrate ARTEMIS-DA’s clustering capa-
bilities using the Superhero Power Analytics Dataset .
ARTEMIS-DA groups superheroes based on their
power attributes, leveraging dimensionality reduction
and visualization techniques. This task highlights
ARTEMIS-DA’s versatility in unsupervised learning,
particularly in applications such as customer segmenta-
tion, anomaly detection, and clustering-based insights.•Time Series Forecasting on Stock Exchange Data:
The middle-left sub-figure demonstrates ARTEMIS-
DA’s strength in time-series forecasting. Utiliz-
ing an advanced Long Short-Term Memory (LSTM)
model, ARTEMIS-DA predicts trends and fluctua-
tions in stock prices using historical data from the
Stock Exchange Data dataset. This capability high-
lights ARTEMIS-DA’s applicability to predictive finan-
cial analysis, such as stock market forecasting, eco-
nomic modeling, and investment strategy development.
•Text Classification of BBC Articles: The middle-right
sub-figures showcase ARTEMIS-DA’s application to
natural language processing (NLP), specifically in text
classification. Using the BBC Document Classification
dataset, ARTEMIS-DA successfully categorizes news
articles by topic. This task underscores ARTEMIS-
DA’s ability to process unstructured text data, making
it an effective tool for applications like content catego-
rization, sentiment analysis, and automated tagging.
•Sentiment Analysis on Disneyland Reviews: The
bottom-left sub-figure illustrates ARTEMIS-DA’s abil-
ity to perform sentiment analysis on text reviews using
the Disneyland Reviews dataset. ARTEMIS-DA effec-
tively identifies the Disneyland location with the highest
8ARTEMIS-DA A P REPRINT
Figure 5: ARTEMIS-DA’s predictive modeling capabilities demonstrated through classification for numerical features
and text datasets, time series forecasting on stock exchange data and clustering of superhero stats.
percentage of positive reviews, showcasing its utility in
analyzing customer or consumer sentiment.
•Regression for Housing Prices: The bottom-right
sub-figures demonstrate ARTEMIS-DA’s regression
modeling capabilities using the Housing Price Dataset .
ARTEMIS-DA applies feature selection via heatmaps
and builds a regression model that achieves an R2score
of 0.78, highlighting its ability to uncover relationships
between variables and predict continuous outcomes.
These examples illustrate ARTEMIS-DA’s adaptability in
addressing a broad spectrum of predictive modeling tasks,
from binary classification and NLP to time-series fore-
casting, clustering, sentiment analysis, and regression.
ARTEMIS-DA’s robust performance across different do-
mains makes it an ideal solution for data-driven applica-
tions in diverse industries, offering powerful tools for data
exploration and predictive analytics, machine learning.