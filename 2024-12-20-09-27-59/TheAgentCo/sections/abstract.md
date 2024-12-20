We interact with computers on an everyday basis, be it in everyday life or work,
and many aspects of work can be done entirely with access to a computer and
the Internet. At the same time, thanks to improvements in large language models
(LLMs), there has also been a rapid development in AI agents that interact with
and affect change in their surrounding environments. But how performant are AI
agents at helping to accelerate or even autonomously perform work-related tasks?
The answer to this question has important implications for both industry looking to
adopt AI into their workflows, and for economic policy to understand the effects
that adoption of AI may have on the labor market. To measure the progress of these
LLM agents’ performance on performing real-world professional tasks, in this
paper, we introduce TheAgentCompany, an extensible benchmark for evaluating
AI agents that interact with the world in similar ways to those of a digital worker:
by browsing the Web, writing code, running programs, and communicating with
other coworkers. We build a self-contained environment with internal web sites and
data that mimics a small software company environment, and create a variety of
tasks that may be performed by workers in such a company. We test baseline agents
powered by both closed API-based and open-weights language models (LMs),
and find that with the most competitive agent, 24% of the tasks can be completed
autonomously. This paints a nuanced picture on task automation with LM agents
– in a setting simulating a real workplace, a good portion of simpler tasks could
be solved autonomously, but more difficult long-horizon tasks are still beyond the
reach of current systems.
Website https://the-agent-company.com
Code https://github.com/TheAgentCompany/TheAgentCompany
Evaluations https://github.com/TheAgentCompany/experiments
1 I NTRODUCTION
We are in the midst of a technological transformation. With the rapid year-by-year and month-by-
month progress brought about by large language models (LLMs), we are seeing AI-based assistance
or automation become commonplace in tasks that were unthinkable only a few years ago. In fact, the
pace of progress is so fast that some have gone so far as to claim that the majority of human labor
may be automatable within the next couple of years (Eloundou et al., 2023; Amodei & Fridman,
2024). On the other hand, others are skeptical, claiming that language models cannot truly reason
(Kambhampati et al., 2024), do not generalize well to novel tasks (Chollet et al., 2024), and may only
have an impact on a small minority of the labor market (Wittenstein, 2024).
What is the reason for this disconnect? We argue that it is, in part, due to a lack of objective
benchmarks that not only demonstrate the power of existing LLM-based agents to accelerate a
∗Equal contribution.
1arXiv:2412.14161v1  [cs.CL]  18 Dec 2024Preprint.
Tasks 
Environment Simulated 
Colleague 
Pl ane 
 GitL ab Browser 
> _ 
Terminal 
Python 
Code 
Engineer 
C T O 
HR Agent 
action 
observe 
Evaluation A dmin arrange meeting room 
DS analyze spreadsheet 
SDE prepare code release 
HR resume screening 
PM team sprint planning 
Finance reimburse travel bills 
access bills 
check reimburse 
-ment criteria consult Mike 
conﬁrm reimburse 
amount +1 +1 +0 +0 Score 
2/4Checkpoint-based 
Reproducible 
Self-hosted Diverse 
Realistic 
Professional 
Figure 1: An overview of TheAgentCompany benchmark. It features a reproducible and self-
hosted environment, simulated colleagues to test agent communication capabilities, checkpoint and
execution-based evaluation, and a set of 175 diverse, realistic and professional tasks in a software
engineering company setting.
wide variety of repetitive tasks encountered in every-day workplaces, but also provide appropriate
caveats about the tasks that agents cannot do. This is a pressing issue, because the commercial and
policy implications of diverse and effective acceleration or automation of work-related tasks will be
broad, both positive (e.g. increase of quality of life and accelerated scientific discovery) and negative
(e.g. potential displacement or loss of jobs and increase in wealth disparities). In this paper, we take
some first steps towards resolving this gap and providing a clearer view of where we are now with
respect to acceleration or automation of consequential work-related tasks, and a litmus test for future
development in this direction.
Concretely, we propose a benchmark, TheAgentCompany (Figure 1) that estimates the ability of
AI agents to perform tasks encountered in everyday workplaces. We create a simulated software
development company where agents must perform tasks related to software engineering, project
management, financial analysis, and other typical tasks encountered in such business settings. The
agents must browse the web, code, and interact with other simulated co-workers to achieve success
on the provided tasks. TheAgentCompany’s environment is based entirely on open-source software
and self-hostable for reproducibility purposes, and we create rigorous evaluators that also assign
partial credit when the agent gets the answer partially correct.
We perform experiments using seven large language model backbones, including API-based models
such as Anthropic Claude (Anthropic, 2023), OpenAI GPT-4o (OpenAI, 2024), Google Gemini
(Team et al., 2023), Amazon Nova (Intelligence, 2024), as well as open models including Meta Llama
(Dubey et al., 2024) and Alibaba Qwen (Yang et al., 2024). All models are run using the OpenHands
agent framework (Wang et al., 2024b),1which provides a stable and strong agent harness for both
web browsing and coding. As a result of experiments, we find that the best performing model, Claude
3.5 Sonnet was able to autonomously perform 24.0% of the provided tests to completion, and achieve
a score of 34.4% on our metric that provides extra credit for partially completed tasks.
These results present a nuanced picture of the current ability of AI agents to perform tasks. Agents
powered by the current gold-standard AI techniques are able to autonomously perform a wide
variety of tasks encountered in everyday work. However, they are not close to automating every task
encountered in a workspace, even on the subset of tasks presented in TheAgentCompany, which are
well-scoped administrative and coding tasks encountered in a software company’s day-to-day work.
In the rest of this paper, we explain detail comparisons to other existing benchmarks (§ 2), how we
set up realistic and reproducible environments (§ 3), how we define tasks (§ 4) and how we create
them (§ 5), our baseline agent (§ 6), experimental results (§ 7), and finally implications and future
directions (§ 8).
1https://github.com/All-Hands-AI/OpenHands
2Preprint.
Table 1: Comparison of different AI agent benchmarks. Interface : the interface agent has access to;
 is
web browser,
 is desktop,
 is API usage,
 is Python script,
 is chat platform,
 is bash terminal.
Supported Tasks : tasks in the benchmark, ∗indicate tasks with no association with real-world occupations; SE
refers to software engineering, HRis human resources, PMis project manager. Checkpoint-based evaluation :
if tasks are evaluated at intermediate checkpoints and assigned partial scores. Interact with NPC Agents : If the
agent can interact with other NPC agents during task-solving.
FrameworkDiverse
Real-world WorkTask CategoriesRequires
InteractionLong-Horizon
w/ CheckpointsInterfaceSelf-Hosted
Environment
MiniWob++ (Liu et al., 2018) % Browsing∗% %
 "
Mind2Web (Deng et al., 2023) % Browsing∗% %
 %
WebLINX (Lù et al., 2024) % Browsing∗% %
 %
AssistantBench (Yoran et al., 2024) % Browsing∗% %
 %
WebArena (Zhou et al., 2023) % Browsing∗% %
 "
VisualWebArena (Koh et al., 2024) % Browsing∗% %
 "
VideoWebArena (Jang et al., 2024) % Browsing∗% %
 "
WorkArena (Drouin et al., 2024) " Enterprise Software % %
 %
OSWorld (Xie et al., 2024) " Office, Coding % %
 "
Windows Agent Arena (Bonatti et al., 2024) " Browsing∗, Office, Coding % %
 "
AppWorld (Trivedi et al., 2024) % Daily % %
 "
Gorilla APIBench (Patil et al., 2023) % Coding % %
 "
τ-bench (Yao et al., 2024) " Retail, Airline " %
 %
SWE-bench (Jimenez et al., 2024) % SWE % %
 "
DevBench (Li et al., 2024) % SWE % %
 %
Smallville (Park et al., 2023) % Social∗" %
 "
Sotopia (Zhou et al., 2024) % Social∗" %
 "
TheAgentCompany "SWE, HR, Admin,
PM, Research, Finance" "
 "
2 B ENCHMARK DESIDERATA AND COMPARISON TO OTHER BENCHMARKS
In order to evaluate the ability of agents to perform tasks in complex real-world settings, we built
TheAgentCompany with a number of desiderata in mind. The comparison with several existing
prominent agent benchmarks with respect to these desiderata is in Table 1.
Coverage of Multiple Work-related Tasks: In order to make any valid statements about the
potential of AI to accelerate or automate various types of real-world work, we should have tasks that
are motivated by real-world work across multiple job categories. Many benchmarks are not relevant to
real-world work (e.g. MiniWob++ (Liu et al., 2018)) or very relevant to real-world work, but only over
a limited scope of tasks (e.g. SWE-Bench (Jimenez et al., 2024)). In contrast, TheAgentCompany
contains a set of more diverse, realistic, and professional tasks that would typically be completed by
multiple job roles in a software engineering company.
Requirement for Interaction: If agents are to integrate into real-world workplaces, they will need
to communicate with the other human members of the workspace. Most other benchmarks do not
measure communication or interactivity, with the exception of τ-bench (Yao et al., 2024), which only
measures interaction in customer service scenarios. TheAgentCompany provides a better testbed for
communication as many tasks involve asking and providing information to colleagues as part of a
more complex task.
Long-horizon Tasks with Checkpoints: In real-world settings, many tasks require taking many
different steps to achieve a higher-level goal. One major novel contribution of TheAgentCompany
is that we both (1) contain tasks that require an agent to perform significantly more consecutive
work ( i.e. involving more steps and realistically taking human professionals longer to accomplish)
than previous benchmarks, and (2) provide granular evaluators that measure the ability of models to
perform subtasks of these larger tasks.
Versatile Environment Interface: In order to handle a diversity of tasks in real-world settings,
we minimally should be able to interact with the tools that real-world workers use – including web
interfaces, programs, command-line terminals, and communication tools. TheAgentCompany covers
all of these interfaces, while most previous benchmarks focus only on one or two.
3Preprint.
Self-hosted and Reproducible: In order to allow for careful comparisons between different meth-
ods that remain constant over time, the benchmark should be fully self-hosted and reproducible. This
contrasts with existing benchmarks that do not have execution environments (e.g. Mind2Web (Deng
et al., 2023)) or require the usage of third-party software (e.g. WorkArena (Drouin et al., 2024)).
3 T HEAGENT COMPANY ENVIRONMENT SETUP
Our benchmark is set in an imaginary software engineering startup called TheAgentCompany, hence
the benchmark’s name. Within TheAgentCompany, we create tasks inspired by tasks handled
by workers inside such companies. More details about the company’s imaginary background,
overview and employees can be found in Appendix A. The benchmark environment contains multiple
components.
Local Workspace The local workspace runs locally on the agent’s host, which is analogous to a
human professional’s local workspace, e.g. their work laptop computer. This environment is created
as a sandboxed Docker environment to provide a safe execution environment that will not affect other
parts of the evaluation machine (Wang et al., 2024b).2This environment is where agents work on the
task, and within this environment the TheAgentCompany baseline agent (§ 6) uses a browser, code
editor and a Linux terminal with typical software preinstalled.3
Intranet This part of the environment mimics the company’s internal websites that host code,
documents, project management software, and communications software. To achieve our goal of
a reproducible, self-contained environment, we follow WebArena (Zhou et al., 2023), in using
open-source, self-hostable software to host our environment. The environment mainly contains the
following websites:
1.GitLab,4an open-source alternative to source-code repositories such as GitHub. This is used
for hosting TheAgentCompany’s code repositories and tech-oriented wiki pages.
2.OwnCloud,5an open-source alternative to office software such as Google Drive or Microsoft
Office. This to save and share files, especially for document storage and collaborative
editing.
3.Plane,6an open-source alternative to task management software such as Jira or Linear. This
is used to track issues, run sprints cycles, and manage product roadmaps.
4.RocketChat,7an open-source alternative to communication software such as Slack. This is a
company-internal real-time messaging tool that facilitates collaboration between employees.
All the websites hosted are reproducible and reset-able with mock data inspired by that from a
software engineering company. The data inside these company internal websites are populated with
real-world software project data, as well as data manually curated by co-authors who have some
experience in the relevant corporate roles.
Simulated Colleague Communication One major aspect of working in a company is communicat-
ing with other company members, and in TheAgentCompany we also test the ability of models to
perform this type of communication. Specifically, we allow agents to use RocketChat to message
other company members and obtain information that may not be available in the original task de-
scription. To create these simulated colleagues, we rely on the Sotopia platform (Zhou et al., 2024),
which supports the creation of simulated human characters with LLMs. Each simulated colleague is
equipped with a detailed profile that includes their name, role, responsibilities, and project affiliations.
2https://docs.all-hands.dev/modules/usage/how-to/custom-sandbox-guide
3Other options would include using something like a GUI-based desktop environment with office software
(Xie et al., 2024), but we opt to build a baseline solution that is entirely web-based, reflecting the recent trend of
more enterprise software moving to the cloud.
4https://about.gitlab.com/install/
5https://doc.owncloud.com/
6https://github.com/makeplane/plane
7https://www.rocket.chat/install
4Preprint.
Table 2: Example task intents and checkpoints for three domains.
Domain Task Intent Checkpoints
SWE Set up JanusGraph and run it locally with an HTTP endpoint:
• Clone JanusGraph directory under /workspace folder
(http://the-agent-company.com:8929/root/janusgraph).
• Build the binary file.
• Launch JanusGraph server locally on port 8182 with an HTTP
endpoint.Checkpoint 1 (1pt): Check if Janus-
Graph repo is cloned.
Checkpoint 2 (3pts): Check if the
binary file is built (requires skipping
Docker in pom.xml , hence higher
points).
Checkpoint 3 (2pts): Check the Janus-
Graph Server as an HTTP endpoint.
Finance Navigate to ownCloud at http://the-agent-company.com:8092 and
complete Section B—Alternative Simplified Credit of IRS Form
6765:
• Gather necessary information from
/Documents/Financials/TAC_financials.csv and
/workspace/research_wages.csv .
• Consult
/Documents/Financials/f6765_instructions.pdf
for instructions.
• Contact the finance director (David Wong) on Rocket.Chat
(http://the-agent-company.com:3000/home) for ambiguous
questions.
• Save the filled form as /workspace/filled_f6765.pdf .Checkpoint 1 (5pts): Check if all 16
questions in Section B of the form have
been answered correctly.
Checkpoint 2 (3pts): Check if the
correct finance director (David Wong)
was contacted to answer two ambiguous
questions.
PM Analyze The Agent Company’s performance and create a summary
in Plane:
• Access Plane (http://the-agent-company.com:8091/tac/) and
navigate to "Analytics."
• Collect metrics: Open Tasks, Backlog Tasks, Unstarted Tasks,
Started Tasks, Unassigned Issues, Pending Issues.
• Create a summary and share it on Rocket.Chat
(http://the-agent-company.com:3000/home) in the #kudos
channel.Checkpoint 1 (1pt): Check if Plane was
accessed and the agent navigated to "An-
alytics" section.
Checkpoint 2 (3pts): Check if all re-
quired project metrics were collected.
Checkpoint 3 (1pt): Check if the sum-
mary was shared in the #kudos chan-
nel on Rocket.Chat.
(e.g., Sarah Johnson, who serves as the CTO, oversees technical strategy planning and R&D team
leadership, with access to all technical channels). Agents can interact with these simulated colleagues
through direct messages or in specific channels, as is standard in RocketChat and other platforms.
By default, all simulated human characters are backed by the Claude-3-5-Sonnet-20241022
LLM across experiments, as we found that it provided the best results during preliminary experiments.
For example conversations between the agent and the simulated colleagues drawn from empirical
experiments, please refer to Appendix B.
4 T ASK STRUCTURE
The tasks in TheAgentCompany include a task intent, a list of checkpoints that the agent must achieve,
a programmatic evaluator to check success on these checkpoints, and code to initialize and finalize
the environment. We show some examples in Table 2, and describe each of aspect in detail below.
Task Intent Each task begins with an English description, simulating how a user would instruct an
LLM-based agent to perform a real-world task. In general, we aim for these tasks to be clear enough
so that a human worker would be able to complete the task without asking for further instructions
directly from the user (although they may need to ask questions of their other co-workers).
Checkpoints Tasks are divided into checkpoints representing intermediate milestones, each as-
signed a point value to measure progress. Each checkpoint is awarded a certain number of points
based on its significance to the overall completion of the task. Checkpoints are written in English,
and typically specify one or more of the following:
5Preprint.
•Action Completion: Verifying whether required actions, such as using tools, navigating to URLs,
or collecting data, were carried out successfully.
•Data Accuracy: Evaluating the correctness and completeness of the output, such as extracted data
or formatted documents.
•Collaboration: Assessing interactions with simulated colleagues or sharing of output, such as
posting messages or asking for additional information to complete the task.
Evaluators Checkpoints are created in the task design phase, but for actual evaluation, each of
the checkpoints must be concretely implemented through an evaluator – a program that checks the
completion of the checkpoint. These evaluators are implemented by examining environment states,
such as the local workspace, intranet status, simulated colleague interactions, or by analyzing agent
trajectories, like verifying browsing history or action sequences.
In most cases, these evaluators are deterministic and written as simple Python functions. For instance,
in the SWE task in Table 2, the checkpoints are deterministic: verifying if the JanusGraph repository is
cloned, the binary file is built, and the server is launched with an HTTP endpoint. However, for tasks
with more complex and unstructured deliverables, such as in Table 2, the last checkpoint in the Finance
task requires contacting the correct finance director (David Wong) to resolve ambiguous questions,
which involves a judgment from a (simulated) human colleague, deterministic evaluation can be
challenging due to subjectivity and variability. In such cases, we employ LLM-based evaluation.
This involves prompting LLMs with predefined rubrics or reference outputs to assess the agent’s
deliverables, enabling a more nuanced and flexible evaluation of these tasks. Same as the NPC
backbone, all LLM-based evaluators are backed by the Claude-3-5-Sonnet-20241022 .
4.1 E VALUATION METRICS
Due to our checkpoint-based evaluation scheme and the need for showcasing both the progress of
the agent’s capability improvement as well as the eventual goal completion ability, we calculate two
scalar agent capability metrics and two efficiency metrics.
Full completion score We define the full completion score Sfullas:
Sfull=1if all checkpoints are successfully passed ,
0otherwise .
This binary metric evaluates whether the agent successfully completed the task by passing all
checkpoints.
Partial completion score To provide a more nuanced measure that rewards partial task completion
while strongly incentivizing full task completion, we define partial completion score Spartial as:
Spartial = 0.5·Result
Total+ 0.5·Sfull,
where:
• Result: Sum of awarded points across all checkpoints (including partial credit),
• Total: Sum of the total points for all checkpoints,
•Result
Total: Fractional progress toward full completion,
•Sfull: Binary indicator equal to 1when the task is fully completed.
This formulation ensures that agents are awarded partial credit in proportion to the points achieved,
reflecting their progress toward task completion. At the same time, full task completion is strongly
incentivized by incorporating an additional 50% credit, which is awarded only when all checkpoints
are successfully completed. This design ensures that agents achieving partial progress receive scores
scaled linearly with their performance, while those reaching 100% completion are distinctly rewarded
to emphasize the importance of achieving the end goal.
6Preprint.
Clone 
Repo 
Checkpoints 
Score : 4/8 Access and 
Update 
Sprint Issues Notify issue 
assignees via Incorporate 
feedback from 
manager 
Share with 
manager 
2/21/1
1/20/2
0/1
Run 
Code 
Coverage 
Upload 
report 
Checkpoint Checkpoint 
Checkpoint Checkpoint 
Checkpoint 
Input Task Intent 
Figure 2: Example TheAgentCompany workflow illustrating an agent managing a sprint for the
RisingWave project. The task involves identifying and moving unfinished issues to next sprint cycle,
notifying assignees of those issues, running a code coverage script, uploading summarized report to
OwnCloud, and incorporating feedback on report from a simulated project manager.
Number of steps The number of steps is defined as the total number of LLM calls made during the
task execution. This metric quantifies the operational effort required to perform the task.
Cost per instance Thecost per instance measures the monetary cost of querying the underlying
LLM through its API to complete a task. Assuming no prompt caching, the cost is calculated as:
Cost = (Prompt token count ×Prompt token cost )+(Completion token count ×Completion token cost ).
This efficiency metric reflects the computational expense of task completion based on token usage.
4.2 W ORKFLOW
Each task typically follows a workflow involving the following stages:
1.Initialization: The agent sets up its workspace and prepares to execute the task.
2.Execution: The agent completes subtasks, such as navigating tools, collecting data, or processing
information or if required by the task, the agent interacts with simulated colleagues or shares
results via communication platforms.
3.Finalization: The agent produces and submits the final output for evaluation.
Example Task We consider a task designed to evaluate an agent’s ability to perform realistic project
management workflows using multiple tools and services hosted in the benchmark. The task involves
managing a sprint for the RisingWave project, requiring the agent to execute interdependent steps
such as sprint issue management, team communication, repository operations, and report generation
while incorporating feedback from a simulated project manager.
The workflow as illustrated in Figure 2 begins with the agent identifying unfinished issues in the
current sprint on Plane and updating their sprint assignments. This step is worth 2 points and is fully
completed, earning the agent the maximum score of 2/2. Next, the agent successfully notifies the
relevant assignees using Rocket.Chat regarding their pending tasks and earns 1/1 point.
The agent then proceeds to clone the RisingWave repository from GitLab and execute a Python
script in the terminal to calculate updated code coverage. This step, worth 2 points, is only partially
completed, as the agent successfully clones the repository but fails to run code coverage. As a result,
the agent earns 1/2 points for this checkpoint. The subsequent steps—generating and sharing the sprint
summary report on OwnCloud and incorporating feedback from a simulated project manager—are
not completed, resulting in 0/2 and 0/1 scores, respectively. Notably, the checkpoints can also fail if
the report does not meet quality standards as assessed by the LLM-based evaluator, which evaluates
the report for clarity, completeness, and successful incorporation of feedback. This ensures that the
assessment reflects both the generation of outputs and their qualitative relevance to the task.
7Preprint.
Finally, the overall score is calculated using the partial completion formula defined in § 4.1, where
the total possible points are 8, and the awarded points sum to 4. Substituting these values, the agent
achieves a final score of 0.25(25%). Our scoring mechanism thus rewards incremental progress
while strongly incentivizing full completion.
This example represents a typical task in the TheAgentCompany benchmark, where agents are re-
quired to handle complex workflows involving multiple tools and interdependent steps. By evaluating
both partial progress and overall outcomes, our benchmark provides a rigorous and realistic measure
of agent performance, allowing us to identify their strengths and pinpoint areas for improvement in
task execution.
5 T ASK CREATION
5.1 C HOOSING TASK CATEGORIES
Many previous agent benchmarks discussed in § 2 were created to evaluate agents on tasks people
perform in daily life (Zhou et al., 2023; Lù et al., 2024; Deng et al., 2023), or tasks that accomplish
digital chores (Yoran et al., 2024; Trivedi et al., 2024). Obtaining realistic tasks for the benchmark
poses challenges. Some benchmark (Xie et al., 2024; Drouin et al., 2024; Yoran et al., 2024)
crowdsourced tasks based on predetermined interfaces, platforms, and services available to the agent.
They also adopt a strategy to first gather task templates and then instantiate more task instances
by filling in the variables. Some benchmark (Zhou et al., 2023; Koh et al., 2024; Bonatti et al.,
2024) took a semi-systematic approach of reviewing the action history of the research team and
choosing tasks that reflected the types of task that the researchers carried out in their daily life. There
are several obvious issues with this if we want to evaluate agents with broader implications in the
TheAgentCompany benchmark. Despite some grounding in realistic data, the process of creating
tasks from these data was susceptible to heuristic, and no consideration was made for how important
or time-consuming the tasks are. The tasks are biased towards those important for academics in
computer science and do not reflect the tasks performed by the entire population.
In TheAgentCompany, we attempt to cover a wide variety of tasks motivated by real-world work .
While it is highly challenging to create a representative sample of tasks, fortunately we can rely on
existing resources created for other purposes as a reference. Specifically, we start by referencing the
29.1 release of O*NET database (O*NET, 2024; Rounds et al., 1999), which is a database of jobs
performed by workers in the US created by the US Department of Labor. It also contains information
about tasks performed within the context of each job, abilities required to perform each task, whether
the task is a major or minor task for that job category, and other pieces of relevant information.
Based on this data, we first identified a few categories of occupation categories to focus on. First,
based on statistics from O*NET, we identified job categories that have a large number of people
performing this job. Then, we used median salary information for each of these job categories from
the US department of labor statistics, and multiplied the number of employees in that category to
estimate the aggregate value of performing this job.
Based on this, we identified several categories of jobs such as “General and Operations Managers”,
“Registered Nurses”, “Software Developers”, and “Financial Managers” that have both a high pop-
ulation and high average salary. Because TheAgentCompany is designed to be a non-embodied
benchmark in the digital domain, we excluded the categories that require extensive physical labor
such as “Registered Nurses”, and eventually settled on the setting of a software company, which
would allow us to cover tasks from the other categories.
5.2 C HOOSING TASKS
Next, within this setting we chose tasks to implement. In this setting, we attempted to create a diversity
of tasks, but mostly focused on concrete tasks that have well-defined goals and success criteria. These
tasks were created through a combination of referencing the O*NET task list, introspection based on
paper co-authors who had experience in each task category, and brainstorming lists with language
models. It is important to note that in no cases have we covered an extensive list of all the tasks
that are performed in a particular occupational category , and therefore we caution against making
any assumptions about whether a particular jobmay be in danger of full automation based solely on
8Preprint.
A g e n t[ 1 ]  M e s s a g e
F i n d  A P I  s e r v e r  c o d e b a s e  i n  i n t e r n a l  w i k i ,  c l o n e  t h e   
r e p o s i t o r y  t o  / w o r k s p a c e  f o l d e r ,  a n d  s t a r t  u p  t h e  
A P I  s e r v e r  l o c a l l y ,  t h e n  . . . .
E v e n t  H i s t o r y
[ P a s t  A c t i o n ( s )  &  O b s e r v a t i o n ( s ) ][ 6 ]  I P y t h o n R u n C e l l A c t i o n  
< e x e c u t e _ i p y t h o n >
f r o m  a p i s e r v e r  i m p o r t  *
a p i _ s e r v e r . r u n ( p o r t = 8 0 8 0 )
. . [ 7 ]  I P y t h o n R u n C e l l O b s e r v a t i o n
. . .
L i s t e n i n g  t o  0 . 0 . 0 . 0 : 8 0 8 0
T h e A g e n t C o m p a n y  A P I  s e r v e r  s t a r t e d .[ 4 ]  C m d R u n A c t i o n
< e x e c u t e _ b a s h >
g i t  c l o n e  g i t : / / r e p o s / a p i s e r v e r
< / e x e c u t e _ b a s h >
A c t i o n[ 5 ]  C m d R u n O b s e r v a t i o n
 C l o n i n g  i n t o  ` a p i s e r v e r ` . . . 
 r e m o t e :  C o u n t i n g  o b j e c t s :  1 0 ,  d o n e . 
 r e m o t e :  C o m p r e s s i n g  o b j e c t s :  1 0 0 %  ( 8 / 8 ) ,  d o n e . 
 r e m o v e :  T o t a l  1 0  ( d e l t a  1 ) ,  r e u s e d  1 0  ( d e l t a  1 ) 
 U n p a c k i n g  o b j e c t s :  1 0 0 %  ( 1 0 / 1 0 ) ,  d o n e .[ 2 ]  B r o w s e I n t e r a c t i v e A c t i o n
< e x e c u t e _ b r o w s e >
i n p u t ( “ a p i  s e r v e r ” ,  “ s e a r c h b o x ” )
c l i c k ( “ s e a r c h ” )
< / e x e c u t e _ b r o w s e > [ 3 ]  B r o w s e r O u t p u t O b s e r v a t i o n
 A P I  S e r v e r  R e p o :  g i t : / / r e p o s / a p i s e r v e rI n t e r a c t i v e  P y t h o n  
( I P y t h o n )  S e r v e rB a s h  S h e l lB r o w s e r
P l a y w r i g h t  C h r o m i u m
O b s e r v a t i o n
A c t i o n
Figure 3: Overview of OpenHands’ default CodeAct + Browsing agent architecture, the baseline
agent used throughout the experiments.
TheAgentCompany. Rather, it may provide insight into whether certain tasks within jobs may be
accelerated or automated, and inform further analysis by labor professionals into this question.
5.3 M ANUAL TASK CURATION
Once we set up the environment required for our desired jobs and task categories (§ 3), we return to
the curated list, and perform a manual curation process for tasks. For each task, this consists of the
following steps: We first create a description of task intent, checkpoints, and how to evaluate each
checkpoint. We then identify and import the required data for the task that are currently missing in
the company Intranet services and create any necessary data. We then write scripts to configure the
required initialization state in the local workspace. Finally, we implement the checkpoint evaluators
that calculate the scalar scores for each checkpoint.
All tasks were created by coauthors of the paper. Overall, it took 20 computer science students,
software engineers, and project managers over 2 months, consuming approximately 3,000 person-
hours in total. Some of the more complex tasks take more than 10 hours each to design, implement,
test, and verify. To ensure quality control of the task creation process, we implement several check and
verification processes. For each task implementation, we require screenshot proof that the evaluator
is valid and that the task is able to get a full score when successfully completed. We also encourage
including tests for the implemented evaluator programs. Each task contribution is also code reviewed
by a panel of lead authors before merging into the benchmark. After creating all tasks, a final round
of manual human double-check of required environment data, evaluator behavior, and checkpoint
scoring for every task is performed to ensure quality. Notably, during the process a person who has
not curated the tasks checks all the checkpoint score assignments to make sure that the importance
scoring is consistent over all the tasks and that it correlates reasonably with the relative importance of
the checkpoint within the task.
6 B ASELINE AGENT
To test the current state-of-the-art performance on the TheAgentCompany benchmark, we need agents
that can at least perform tasks using a browser, operate a local workspace using a terminal, and write
and execute programs to perform most of the tasks. Throughout this paper, we experiment with
OpenHands’ main agent (Wang et al., 2024b;a; Song et al., 2024), CodeAct Agent with Browsing.8
An overview of the agent architecture is illustrated in Figure 3.
Interfaces The agent can interact with the environment through 3 interfaces. (1) A bash shell
that connects with the local workspace operating system environment for command execution.
(2) A Jupyter IPython server to handle interactive python (IPython) code execution requests and
return the execution results back. (3) A Chromium browser based on Playwright. The provider
8More specifically, version 0.14.2. Full details can be found in https://github.com/All-Hands-AI/OpenHands/
tree/main/openhands/agenthub/codeact_agent
9Preprint.
provides a set of action primitives defined by BrowserGym (ServiceNow; Drouin et al., 2024), such
as navigation, clicking, typing, and scrolling. After executing these actions, the browser runtime
provides a rich set of observations about the current state of the browser, including HTML, DOM,
accessibility tree (Mozilla), screenshot, opened tabs, etc. These observations can be also augmented
with configurable attributes that could allow agents to better understand web page observations, such
as using a set-of-marks on screenshot (Yang et al., 2023; He et al., 2024), visible element marking,
focused element, interactable element marking, in-viewport element filtering (Zhou et al., 2023), etc.
Actions The agent connects with the environment through a core set of general actions. Actions
IPythonRunCellAction andCmdRunAction enable the agent to execute arbitrary Python
code and bash commands inside the sandbox environment ( e.g., a secure isolated Linux operating
system used as our local workspace). BrowserInteractiveAction enables interaction with a
web browser with a domain-specific language for browsing introduced by BrowserGym (Chezelles
et al., 2024; Drouin et al., 2024). These actions provide a comprehensive, yet flexible set of primitives
that cover most of the tasks performed by human employees of TheAgentCompany, including
navigation, click, hovering, and typing, etc.
Observations Observations describe the environmental changes that the agent observes. The
main types of observations used in the CodeAct agent include the execution result of bash terminal
commands, Python programs, and browser actions. Specifically, the execution result of browser
actions is usually browser snapshots and textual representation in the form of accessibility tree of the
current browser viewport.
Workflow At each step, the underlying backbone LLM will take in prompts consisting of previous
agent history and the current observation of the environment, and generate a response consisting of the
action to execute next. On a higher level, the agent can perform the task by executing code, including
executing bash commands, Python code, or browser-specific programming language (defined in
BrowserGym).9This general action space allows the agent to perform various tasks, including editing
files, browsing the Web, running programs, etc.
7 E XPERIMENTAL RESULTS
In this section, we evaluate popular foundation models, both closed and open, on TheAgentCompany
benchmark. We use OpenHands CodeAct agent (§ 6) for all experiments This serves as a baseline for
future development of both the foundation LLMs and the agent infrastructure. Note that since LLM
evaluators and NPCs are part of the environment rather than the agent being evaulated, we fix their
backbone LLM to Claude-3-5-Sonnet-20241022 , which demonstrated the best qualitative
accuracy in simulating human colleagues and judging deliverables in preliminary experiments.
7.1 R ESULT OVERVIEW
Table 3 shows the evaluation results of both closed and open foundation models on the full evaluation
set of TheAgentCompany (175 tasks). We can see that the Claude-3.5-Sonnet is the clear winner
across all models. However, even with the strongest frontier model, it only manages to complete 24%
of the total tasks and achieves a score of 34.4% taking into account partial completion credits. Note
that this result comes at a cost: It requires an average of almost 30 steps and more than $6 to complete
each task, making it the most expensive model to run both in time and in cost. This is expected as
most of the tasks in our benchmark are of long-horizon nature. The Gemini 2.0 Flash model that
comes second in terms of capability requires 40 steps on average to complete the tasks, which is time
consuming, yet only to achieve less than half the success rate compared to the top-performing model.
Surprisingly, its cost is less than $1, making it a very cost-efficient yet relatively strong model. A
qualitative examination demonstrated that this was due to instances where the agent got stuck in a
loop or aimlessly explored the environment.
Among the open-weight models, Llama 3.1 (405B) achieves the highest performance, nearly on par
with OpenAI’s GPT-4o model, though still having a big gap behind the leading Claude 3.5 Sonnet.
9https://github.com/ServiceNow/BrowserGym/blob/main/browsergym/core/src/browsergym/core/action/
functions.py
10Preprint.
Table 3: Performance comparison of various foundation models on TheAgentCompany.
Model Success Score Steps Costs
API-based Models
Claude-3.5-Sonnet 24.0% 34.4% 29.17 $6.34
Gemini-2.0-Flash 11.4% 19.0% 39.85 $0.79
GPT-4o 8.6% 16.7% 14.55 $1.29
Gemini-1.5-Pro 3.4% 8.0% 22.10 $6.78
Amazon-Nova-Pro-v1 1.7% 5.7% 19.59 $1.55
Open-weights Models
Llama-3.1-405b 7.4% 14.1% 22.95 $3.21
Llama-3.3-70b 6.9% 12.8% 20.93 $0.93
Qwen-2.5-72b 5.7% 11.8% 23.99 $1.53
Llama-3.1-70b 1.7% 6.5% 19.18 $0.83
Qwen-2-72b 1.1% 4.2% 23.70 $0.28
Table 4: Performance of the models in tasks that require different platforms in TheAgentCompany.
All numbers are percentages (%).
GitLab (71 tasks) Plane (17 tasks) RocketChat (79 tasks) ownCloud (70 tasks)
Model Success (%) Score (%) Success (%) Score (%) Success (%) Score (%) Success (%) Score (%)
API-based Models
Claude-3.5-Sonnet 30.99 40.25 41.18 50.37 21.52 34.68 10.00 21.81
Gemini-2.0-Flash 11.27 18.21 17.65 29.84 13.92 23.34 2.86 8.52
GPT-4o 11.27 19.46 23.53 33.68 5.06 16.08 1.43 7.76
Gemini-1.5-Pro 2.82 3.88 5.88 14.05 3.80 10.97 0.00 4.22
Amazon-Nova-Pro-v1 2.82 7.22 5.88 16.67 1.27 5.36 0.00 2.43
Open-weights Models
Llama-3.1-405b 5.63 11.84 29.41 39.12 8.86 16.46 0.00 4.45
Llama-3.3-70b 8.45 14.26 11.76 21.65 5.06 12.06 0.00 3.76
Qwen-2.5-72b 5.63 11.33 11.76 23.56 5.06 12.60 0.00 4.14
Llama-3.1-70b 1.41 6.09 5.88 15.35 2.53 8.23 0.00 3.32
Qwen-2-72b 1.41 1.94 5.88 12.45 0.00 4.88 0.00 2.60
Interestingly, comparing the number of steps and costs between the open Llama 3.1 (405B) model
and the closed OpenAI GPT-4o model, Llama 3.1 takes more steps and costs nearly 2x more to run,
while having a lower success than GPT-4o. Anecdotally, our inspection showed that GPT-4o seems
to be better at giving up early, saving steps and costs if the task is clearly out of the capacity range of
the agent. This suggests that open-weight models are not always the most cost-effective choice in
agents given serving cost, especially with highly complex tasks.
On the other hand, the newer generation of Llama model, Llama 3.3 (70B) achieves a considerably
high performance of 6.9% success rate, on par with the much larger (405B), older generation (Llama
3.1) model. This model also costs significantly less because of its smaller size. This suggests a
promising future for LLM development, as smaller and more efficient models begin to catch up in
agent performance.
7.2 A NALYSIS
How well do agents operate on different platforms? Table 4 presents performance breakdown on
tasks that involve different platforms in TheAgentCompany. A task is categorized under a platform
if one of the platforms that the task requires it. From Figure 4a, we can see that most models
struggle with RocketChat and ownCloud. RocketChat platform is where all the social interaction
with peers happens, and the low performance on this platform suggests that current-day LLMs still
need improvements in communicating with others. ownCloud platform provides online Office suite
functionality, and due to the complexity of the UI of web-based Office software, it is expected that
current LLMs fail badly on the platform. This suggests that the browsing capability of the agents,
especially on more complex websites, still needs improvement. These results underscore the inherent
challenges and complexities of performing tasks that occur in real-world work environments, involve
social interaction, or require understanding and navigating complex web interfaces.
11Preprint.
Table 5: Performance of various models in tasks with different nature in TheAgentCompany. All
numbers are percentages (%).
SDE (69 tasks) PM(28 tasks) DS(14 tasks) Admin (15 tasks) HR(29 tasks) Finance (12 tasks) Other (8 tasks)
Model Success Score Success Score Success Score Success Score Success Score Success Score Success Score
API-based Models
Claude-3.5-Sonnet 30.43 38.02 35.71 51.31 14.29 21.70 0.00 11.59 24.14 34.49 8.33 25.17 12.50 22.40
Gemini-2.0-Flash 13.04 18.99 17.86 31.71 0.00 6.49 6.67 15.20 17.24 23.08 0.00 4.31 0.00 10.05
GPT-4o 13.04 19.18 17.86 32.27 0.00 4.70 6.67 13.89 0.00 8.28 0.00 7.36 0.00 10.78
Gemini-1.5-Pro 4.35 5.64 3.57 13.19 0.00 4.82 6.67 9.92 3.45 11.42 0.00 2.78 0.00 8.07
Amazon-Nova-Pro-v1 2.90 6.07 3.57 12.54 0.00 3.27 0.00 0.00 0.00 4.27 0.00 2.78 0.00 2.86
Open-weights Models
Llama-3.1-405b 5.80 11.33 21.43 35.62 0.00 5.42 0.00 3.33 6.90 12.56 0.00 5.00 12.50 17.45
Llama-3.3-70b 11.59 16.49 7.14 19.83 0.00 4.70 0.00 1.67 6.90 11.38 0.00 5.69 0.00 7.03
Qwen-2.5-72b 7.25 11.99 10.71 22.90 0.00 5.42 0.00 2.14 6.90 12.36 0.00 7.15 0.00 5.99
Llama-3.1-70b 1.45 4.77 3.57 15.16 0.00 5.42 0.00 2.42 3.45 7.19 0.00 3.82 0.00 2.86
Qwen-2-72b 2.90 3.68 0.00 7.44 0.00 4.70 0.00 0.56 0.00 4.14 0.00 3.61 0.00 4.95
Platform02040
GitLab Plane RocketChat ownCloudClaude-3.5-sonnet Llama-3.1-405B
(a) Success rate across platforms
Task Category02040
SDE PM DS Admin HR Finance OtherClaude-3.5-sonnet Llama-3.1-405B (b) Success rate across task categories
Figure 4: Comparing agent success rate across platforms (left) and task categories (right).
How well do agents perform on different type of tasks? Table 5 presents performance breakdown
on different types of tasks in TheAgentCompany. According to the nature of the task, i.e. what kind
of professionals are usually assigned with the task, the tasks in TheAgentCompany can be categorized
into several job departments: Software Development Engineering (SDE), Project Management (PM),
Data Science (DS), Administrative (Admin), Human Resources (HR), Financial (Finance) and all the
remaining (Other).
From the success rate demonstrated in Figure 4b, we can see that data science, administrative, and
finance tasks are among the lowest, with many LLMs completing none of the tasks successfully, and
even the strongest Claude model achieving much less than the rest of the tasks. On the other hand,
software engineering tasks, which may seem like much harder tasks for many humans, result in a
higher success rate. This suggests that there exists a gap between the perceived difficulty of the tasks
for humans versus the difficulty for LLM agents.
For example, some tasks in the administrative and finance category involves making spreadsheets,
collecting and filling in a lot of information from various people, or reading and understanding
images scanned by employees. These tasks are arguably easier conceptually for humans in terms of
professional skill sets than software engineering, as SDE jobs usually have a higher barrier of entry
and more prerequisites for certain knowledge. However, most LLMs achieve a much higher score on
the SDE tasks. However, LLMs fail these seemingly easier tasks due to lack of ability to understand
documents, communicate with other people, navigate complex software and tedious processes, and
autonomously automate repetitive tasks. We hypothesize that part of the reason lies in the fact that
current LLM development is heavily based on software engineering abilities, such as coding, due
to several high profile benchmarks that measure this capability ( e.g. HumanEval, SWE-Bench) as
well as the abundance of publicly available training data related to software. On the other hand,
administrative and financial tasks, are usually private data within companies, not readily available for
training LLMs.
12Preprint.
7.3 C OMMON AGENT FAILURES
Overall, the agent performance on TheAgentCompany is still low and a majority of tasks are failed.
Among those, we try to find some common and interesting agent mistakes that are often surprising
because they are usually not made by humans.
Lack of commonsense Some tasks are failed because the agent lacks the common sense and
domain background knowledge required to infer implicit assumptions. For example, one task asked
the agent to “Write the responses to /workspace/answer.docx ” but does not explicitly states
that this is a Microsoft Word file. A human can infer this requirement from the file extension. The
agent instead treats it as a plain text file, writing text directly to the file, resulting in a task failure.
Lack of social skills Sometimes, the agent fails to understand the implications and goals in the
social conversations with colleagues in TheAgentCompany. For example, one task involves asking
Alex for help, and the agent first successfully asks the right question “Could you tell me who I should
introduce myself to next on the team?” Then the simulated colleague Alex replied “You should
introduce yourself to Chen Xinyi next. She’s on our frontend team and would be a great person to
connect with!” At this point, a human would then talk to Chen Xinyi, but instead the agent then
decides to not follow up with her, and prematurely considers the task accomplished.
Incompetence in browsing Often times, the biggest obstacle in tasks is the parts that require
browsing the Web. This is expected as browsing is still hard for agents given the complexity of
modern-day web UIs and the numerous distractions on a webpage. For example, on many tasks that
involve ownCloud, the closable popup that sometimes shows up and asks the user to download the
mobile phone apps for a better experience has become an obstacle. Humans can simply click on the
‘x’ to close the popup, while the agents are stuck. Similarly, when trying to download a file from
ownCloud, there are several popups to click through before the actual download, and each step is
error prone for agents due to the complex UI.
Deceiving oneself Interestingly, we find that for some tasks, when the agent is not clear what the
next steps should be, it sometimes try to be clever and create fake “shortcuts” that omit the hard part
of a task. For example, during the execution of one task, the agent cannot find the right person to
ask questions on RocketChat. As a result, it then decides to create a shortcut solution by renaming
another user to the name of the intended user.
8 I MPLICATIONS AND FUTURE DIRECTIONS
In this paper, we present TheAgentCompany, a new benchmark that stands out because it specifically
focuses on real-world tasks that would be tackled within the context of real-world work. Unsurpris-
ingly, current state-of-the-art agents fail to solve a majority of the tasks, suggesting that there is a big
gap for current AI agents to autonomously perform most of the jobs a human worker would do, even
in a relatively simplified benchmarking setting. Looking at how different models perform on different
types of tasks, we argue that tasks that involve social interaction with other humans, navigating
through complex user interfaces designed for professionals, and tasks that are typically performed
in private, without a significant open and publicly available resources, are the most challenging.
However, we believe that currently new LLMs are making significant progress: not only are they
becoming more and more capable in terms of raw performance, but also more cost-efficient ( e.g.
Gemini 2.0 Flash). Open-weights models are closing the gap between proprietary frontier models
too, and the newer models are getting smaller ( e.g. Llama 3.3 70B) but with equivalent performance
to previous huge models, also showcasing that efficiency will further improve.
That said, this is just a first step towards forming a firmer grasp on how AI may affect the tasks
performed within a workspace, and it has its limitations. First, our tasks are generally on the more
straightforward side due to the need to automatically evaluate with programs and test cases, and we
do not cover more complex creative tasks such as brainstorming new product ideas or designing
system architectures. Second, we are only using one agent scaffold as the baseline performance,
and others may differ in performance. Third, while it would be interesting to know the actual
performance of human professionals on these tasks to understand how LLM agents perform in
13Preprint.
comparison, due to resource limitations we were not able to perform this comparison in the current
iteration of TheAgentCompany. Fourth, the topic and content of the tasks were mostly created
through introspection by people familiar with these workspaces, which may result in some disconnect
with actual tasks performed in enterprise settings.
Based on this, there are many future directions for further improvement of TheAgentCompany or
other related benchmarks in this space. These include further expanding the benchmark tasks to
those encountered in other industries, or tasks that require physical labor. Benchmarking may also be
expanded with tasks that have more vague intents to better simulate real-world scenarios where the
goal is not immediately clear at the very beginning. Further, benchmarks could also be expanded to
include higher-level longer-horizon tasks such as conceptualizing a new product and carrying it to
execution. We hope that TheAgentCompany provides a first step, but not the only step, towards these
goals, and that we or others may build upon the open source release of TheAgentCompany to further
expand in these promising directions.
AUTHOR CONTRIBUTIONS
This work was an open source collaborative effort between multiple institutions and many independent
individuals. We used a point-based system to determine contributions and award authorship. Frank
Xu, Boxuan Li and Yufan Song led the project, coordinating overall development and paper writing
efforts. Detailed contributions were as follows:
•Task Design: Frank Xu, Yufan Song, Boxuan Li, Zora Wang, Shuyan Zhou, Graham Neubig
•Infrastructure Development: Yufan Song, Boxuan Li
•Experiment: Boxuan Li, Frank Xu, Yufan Song
•Sotopia Integration: Yufan Song, Xuhui Zhou
•Task Development: Boxuan Li, Yufan Song, Frank Xu, Graham Neubig, Yuxuan Tang, Mengxue
Bao, Kritanjali Jain, Zhitong Guo, Murong Cao, Mingyang Yang, Hao Yang Lu, Amaad Martin,
Zhe Su, Leander Maben, Raj Mehta, Yiqing Xie, Zora Wang, Xuhui Zhou, Wayne Chi, Lawrence
Jang
•Ideation, Discussion and Formulation: Frank Xu, Shuyan Zhou, Xuhui Zhou, Zora Wang,
Wayne Chi, Yufan Song, Boxuan Li, Lawrence Jang, Graham Neubig
•Advising : Graham Neubig advised the project, providing guidance, resources, and substantial
paper editing.
ACKNOWLEDGMENTS
This work was supported by a grant from Open Philanthropy. We thank Daniel Fried, Ruslan
Salakhutdinov, Chris Donahue, Jing Yu Koh, Brandon Trabucco, Julie Nys, Olga Rogunova, Aditya
Soni, Alex Lawsen, and Stephen McAleer for their insightful discussions in various stages of the
project. We also thank the OpenHands team for their help on some of the task implementations.