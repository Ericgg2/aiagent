We have outlined diﬃculties that pertain to natural language as well f ormal language mathematics datasets
that we believe are present hindrances to the progress of AI syst ems towards becoming real mathematical
thought partners that are as, if not more, useful to mathematicians as GitHub’s Copilo t15is to programmers.
The advantages and disadvantages of natural language and form al language datasets are frequently com-
plementary. What is easy in one representation of mathematics is of ten hard in the other. For example,
automatic evaluation is easy in formal language but hard in natural la nguage; representing rich interaction
modes is often comparatively easy in natural language but harder t o express in formal language.
We have identiﬁed several facets of mathematical practice that a re currently not represented in the data
used to design and evaluate the deployment of AI systems for math ematics, such as various workﬂows. We
acknowledge that the aspects of workﬂows we highlight here likely do not capture allpossible facets of
mathematical practice - but we believe they represent an importan t start, oﬀering an outline for what we
may be able to curate to more human-compatible and explainable math ematical AI systems.
While our aim has been exclusively in mathematics, these approaches o f mapping processes of scientiﬁc
discovery to data are not restricted to mathematics and may be ad apted to other scientiﬁc domains as well.
Some of the workﬂow items, like those related to literature search a re directly relevant to other domains.
We urge the community to explore how intermediate steps in the proc ess of scientiﬁc discovery look like in
other areas of science as well.
Regarding purely proof creation, time will tell whether human-anno tated proofs are necessary–or whether
a purely formal approach together with ingenious proof search te chniques will succeed. The comparatively
short history of machine learning has taught us to expect the unex pected. In the short term, however, it is
imperative to establish better datasets and novel benchmarks fo r mathematics (either in natural language
or formal language), to go beyond the current ones that only tes t proof or result creation - and also test
the ability to assess diﬀerent mathematical workﬂows, to summariz e mathematics, to explain limitations of
proof techniques etc. This will support the next generation of mac hine learning models and AI tools that can
help us discover more mathematics fast and, subsequently assist w ith any other scientiﬁc discipline that uses
15https://github.com/features/copilot
27Questions for all mathematics datasets:
•Does your dataset cover only end results (statements and proof s), or (also) intermediate proof rep-
resentations (which ones)?
•What is the precise focus of the dataset (proofs, workﬂows of va rious kinds, reasoning arguments,
heuristics, etc.)?
•If proofs are included, are they motivated? Who conﬁrmed that th ey are motivated?
•What is the type (degree of abstraction vs. proof complexity) and level of diﬃculty (e.g., grade
school, high school, undergraduate, IMO, a mix) of the mathematic al items?
•Who determined the diﬃculty rating?
•What scale did you use to determine diﬃculty rating (e.g., 5-point Liker t scale)?
•Wich MSC codes represent your dataset best? (List all applicable on es)
(Case-based) For datasets that include formal mathematics :
•Which formal mathematics language and corresponding ATP/ITP wa s used (e.g., Lean, Isabelle,
Coq, Prover9, Vampire)?
•What version of it was used? (Ideally reference the speciﬁc commit – if available, such as in the case
of Lean)
•Which dependencies are used? (That is, does the data set stand on its own, or does it depend on
existing libraries of formal mathematics (e.g., Isabelle AFP or Mathlib) ? If so, what version of the
library are you using, and when was it last updated?)
(Case-based) For datasets that include informal mathemati cs:
•Which items (statements, proofs, workﬂow steps, etc.) are chec ked for correctness?
•For proofs: On what level of detail are your datapoints? (The leve l of detail can vary dramatically,
from a high-level sketch of a proof, down to a “formalizable” proof that has all details so that its
formalization does not need any ﬁlling of mathematical gaps.)
•What procedure is used to check for correctness?
•Who (and how many people) checked correctness?
•If any other annotations are made about the informal mathematic s that are not covered by the
previous questions (e.g., whether a proof is aesthetically-pleasing, whether a speciﬁc workﬂow repre-
sentation was used), please provide information on how (and by who m) they were procured.
•What language is the informal mathematics written in (e.g., English, Ge rman, French, Japanese,
Chinese)?
Figure 1: The questionnaire for mDfDs. We note that some of the questions are dependent on each o ther, so
all need to be answered. E.g., for the ﬁrst question, what counts a s an “undergraduate” diﬀers from country
to country (and even from university to university). The second q uestion is thus necessary to put the ﬁrst
in context.
mathematics as a foundation (e.g. systems biology that relies on ord inary diﬀerential equations, or physics
that relies on several subﬁelds of mathematics – and inspires new su bﬁelds at the same time). At the same
time, better mathematical copilots may have strong educational b eneﬁts.
Having a deeper understanding of the processes by which one arriv es at a proof (heuristics, workﬂows, etc.),
which are all concentrated in the concept of a motivated proof, ma thematical copilots can also teach the
next generation of mathematical minds.
Even though the history of the concept of “proof” spans millennia, the story is ongoing, as currently, the
search for a machine-learnable “proof data structure” is an impor tant focus point and represents a new
chapter in the ongoing story of what a proof really is.
28Acknowledgements
Thomas Lukasiewicz was supported by the AXA Research Fund. Kat herine M. Collins acknowledges support
from the Cambridge Trust. The work of Fabian Ruehle is supported b y NSF grants PHY-2210333, PHY-
2019786 (The NSF AI Institute for Artiﬁcial Intelligence and Funda mental Interactions), and startup funding
from Northeastern University. Timothy Gowers would like to acknow ledge generous support from the Astera
Institute. We thank Terence Tao for useful remarks.
29References
Trieu H Trinh, Yuhuai Wu, Quoc V Le, He He, and Thang Luong. Solving olympiad geometry without
human demonstrations. Nature , 625(7995):476–482, 2024.
OpenAI. GPT-4 technical report. arXiv preprint 2303.0877 , 2023.
Simon Frieder, Luca Pinchetti, Ryan-Rhys Griﬃths, Tommaso Salvat ori, Thomas Lukasiewicz, Philipp Chris-
tian Petersen, Alexis Chevalier, and Julius Berner. Mathematical ca pabilities of ChatGPT. In Advances
in Neural Information Processing Systems , volume 36, 2023a.
Machel Reid, Nikolay Savinov, Denis Teplyashin, Dmitry Lepikhin, Timot hy Lillicrap, Jean-baptiste Alayrac,
Radu Soricut, Angeliki Lazaridou, Orhan Firat, Julian Schrittwieser , et al. Gemini 1.5: Unlocking multi-
modal understanding across millions of tokens of context. arXiv preprint arXiv:2403.05530 , 2024.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, an d Heewoo Jun et al. Training veriﬁers
to solve math word problems. arXiv preprint arXiv:2110.14168 , 2021.
Vladmir Sicca, Tianxiang Xia, Math¨ ıs F´ ed´ erico, Philip John Gorinski, S imon Frieder, and Shangling Jui.
Newclid: A user-friendly replacement for AlphaGeometry. arXiv preprint arXiv:2411.11938 , 2024.
Chenrui Wei, Mengzhou Sun, and Wei Wang. Proving olympiad algebra ic inequalities without human
demonstrations. arXiv preprint arXiv:2406.14219 , 2024.
Alex Davies, Petar Veliˇ ckovi´ c, Lars Buesing, Sam Blackwell, and D aniel Zheng et al. Advancing mathematics
by guiding human intuition with AI. Nature , 600(7887):70–74, 2021.
Yang-Hui He, Vishnu Jejjala, Challenger Mishra, and Max Sharnoﬀ. Learning to be simple. arXiv preprint
arXiv:2312.05299 , 2023.
Bernardino Romera-Paredes, Mohammadamin Barekatain, Alexand er Novikov, Matej Balog, M Pawan Ku-
mar, Emilien Dupont, Francisco JR Ruiz, Jordan S Ellenberg, Pengming Wang, Omar Fawzi, et al. Math-
ematical discoveries from program search with large language mode ls.Nature , 625(7995):468–475, 2024.
Alhussein Fawzi, Matej Balog, Aja Huang, Thomas Hubert, Bernard ino Romera-Paredes, Mohammadamin
Barekatain, Alexander Novikov, Francisco J R Ruiz, Julian Schrittwie ser, Grzegorz Swirszcz, et al. Dis-
covering faster matrix multiplication algorithms with reinforcement le arning. Nature , 610(7930):47–53,
2022.
Katherine M Collins, Albert Q Jiang, Simon Frieder, Lionel Wong, Miri Zilk a, Umang Bhatt, Thomas
Lukasiewicz, Yuhuai Wu, Joshua B Tenenbaum, William Hart, et al. Eva luating language models for
mathematics through interactions. Proceedings of the National Academy of Sciences , 121(24):e2318124121,
2024a.
Katherine M Collins, Ilia Sucholutsky, Umang Bhatt, Kartik Chandra, Lionel Wong, Mina Lee, Cedegao E
Zhang, Tan Zhi-Xuan, Mark Ho, Vikash Mansinghka, et al. Building mac hines that learn and think with
people.Nature Human Behaviour , 8(10):1851–1863, 2024b.
Zhibin Gou, Zhihong Shao, Yeyun Gong, yelong shen, Yujiu Yang, Minlie Huang, Nan Duan,
and Weizhu Chen. ToRA: A tool-integrated reasoning agent for mat hematical problem solv-
ing. In The Twelfth International Conference on Learning Represen tations , 2024. URL
https://openreview.net/forum?id=Ep0TtjVoap .
Weilin Cai, Juyong Jiang, Fan Wang, Jing Tang, Sunghun Kim, and Jiayi H uang. A survey on mixture of
experts. Authorea Preprints , 2024.
Simon Frieder, Julius Berner, Philipp Petersen, and Thomas Lukasiew icz. Large language models for math-
ematicians. arXiv preprint arXiv:2312.04556 , 2023b.
30Alexandre Riazanov and Andrei Voronkov. The design and implement ation of VAMPIRE. AI Communica-
tions , 15(2-3):91–110, 2002.
Laura Kov´ acs and Andrei Voronkov. First-order theorem prov ing and VAMPIRE. In International Confer-
ence on Computer Aided Veriﬁcation , pages 1–35. Springer, 2013.
Stephan Schulz. E–a brainiac theorem prover. AI Communications , 15(2-3):111–126, 2002.
Sean B. Holden. Machine learning for automated theorem proving: L earning to solve SAT and QSAT.
Foundations and Trends ®in Machine Learning , 14(6):807–989, 2021. ISSN 1935-8237.
Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeﬀ Clu ne, and David Ha. The AI scientist:
Towards fully automated open-ended scientiﬁc discovery. arXiv preprint arXiv:2408.06292 , 2024a.
Yoshua Bengio and Nikolay Malkin. Machine learning and information the ory concepts towards an AI
mathematician. Bulletin of the American Mathematical Society , 61(3):457–469, 2024.
John Harrison, Josef Urban, and Freek Wiedijk. History of interac tive theorem proving. In Computational
Logic , volume 9, pages 135–214, 2014.
Jasmin Christian Blanchette, Andrei Popescu, Daniel Wand, and Ch ristoph Weidenbach. More SPASS with
Isabelle: Superposition with hard sorts and conﬁgurable simpliﬁcatio n. InInteractive Theorem Proving:
Third International Conference, ITP 2012, Princeton, NJ, U SA, August 13-15, 2012. Proceedings 3 , pages
345–360. Springer, 2012.
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Stev en Basart, Eric Tang, Dawn Song, and
Jacob Steinhardt. Measuring mathematical problem solving with the MATH dataset. In J. Vanschoren
and S. Yeung, editors, Proceedings of the Neural Information Processing Systems T rack on Datasets and
Benchmarks , volume 1. Curran, 2021.
Shuo Yang, Wei-Lin Chiang, Lianmin Zheng, Joseph E Gonzalez, and Io n Stoica. Rethinking benchmark
and contamination for language models with rephrased samples. arXiv preprint arXiv:2311.04850 , 2023.
Ruijie Xu, Zengzhi Wang, Run-Ze Fan, and Pengfei Liu. Benchmark ing benchmark leakage in large language
models. arXiv preprint arXiv:2404.18824 , 2024.
Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Mingc huan Zhang, YK Li, Yu Wu, and
Daya Guo. DeepSeekMath: Pushing the limits of mathematical reaso ning in open language models. arXiv
preprint arXiv:2402.03300 , 2024.
Aixin Liu, Bei Feng, Bin Wang, Bingxuan Wang, Bo Liu, Chenggang Zhao , Chengqi Dengr, Chong Ruan,
Damai Dai, Daya Guo, et al. DeepSeek-V2: a strong, economical, an d eﬃcient mixture-of-experts language
model.arXiv preprint arXiv:2405.04434 , 2024.
Qihao Zhu, Daya Guo, Zhihong Shao, Dejian Yang, Peiyi Wang, Runxin Xu, Y Wu, Yukun Li, Huazuo Gao,
Shirong Ma, et al. DeepSeek-Coder-V2: Breaking the barrier of clo sed-source models in code intelligence.
arXiv preprint arXiv:2406.11931 , 2024.
Huajian Xin, ZZ Ren, Junxiao Song, Zhihong Shao, Wanjia Zhao, Haoc heng Wang, Bo Liu, Liyue Zhang,
Xuan Lu, Qiushi Du, et al. DeepSeek-prover-V1. 5: Harnessing pr oof assistant feedback for reinforcement
learning and Monte-Carlo tree search. arXiv preprint arXiv:2408.08152 , 2024.
Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng , Yang Fan, Wenbin Ge, Yu Han, Fei
Huang, et al. Qwen technical report. arXiv preprint arXiv:2309.16609 , 2023.
An Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zh ou, Chengpeng Li, Chengyuan Li,
Dayiheng Liu, Fei Huang, et al. Qwen2 technical report. arXiv preprint arXiv:2407.10671 , 2024a.
31Binyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang , Tianyu Liu, Jiajun Zhang, Bowen
Yu, Keming Lu, et al. Qwen2.5-Coder technical report. arXiv preprint arXiv:2409.12186 , 2024.
An Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengp eng Li, Dayiheng Liu, Jianhong Tu,
Jingren Zhou, Junyang Lin, et al. Qwen2.5-Math technical report: Toward mathematical expert model
via self-improvement. arXiv preprint arXiv:2409.12122 , 2024b.
Shima Imani, Liang Du, and Harsh Shrivastava. MathPrompter: Mat hematical reasoning using large lan-
guage models. In Sunayana Sitaram, Beata Beigman Klebanov, and J ason D Williams, editors, Proceedings
of the 61st Annual Meeting of the Association for Computatio nal Linguistics (Volume 5: Industry Track) ,
pages 37–42. Association for Computational Linguistics, 2023. do i: 10.18653/v1/2023.acl-industry.4. URL
https://aclanthology.org/2023.acl-industry.4 .
Pan Lu, Hritik Bansal, Tony Xia, Jiacheng Liu, Chunyuan Li, Hannaneh Hajishirzi, Hao Cheng, Kai-Wei
Chang, Michel Galley, and Jianfeng Gao. MathVista: evaluating math ematical reasoning of foundation
models in visual contexts. In The Twelfth International Conference on Learning Represen tations , 2024b.
URLhttps://openreview.net/forum?id=KUNzEQMWU7 .
Haipeng Luo, Qingfeng Sun, Can Xu, Pu Zhao, Jianguang Lou, Chong yang Tao, Xiubo Geng, Qingwei Lin,
Shifeng Chen, and Dongmei Zhang. WizardMath: Empowering mathe matical reasoning for large language
models via Reinforced Evol-Instruct. arXiv preprint arXiv:2308.09583 , 2023.
Zhangir Azerbayev, Hailey Schoelkopf, Keiran Paster, Marco Dos S antos, Stephen Marcus McAleer, Al-
bert Q. Jiang, Jia Deng, Stella Biderman, and Sean Welleck. Llemma: An open language model
for mathematics. In The Twelfth International Conference on Learning Represen tations , 2024. URL
https://openreview.net/forum?id=4WnqRR915j .
Tobias Nipkow, Markus Wenzel, and Lawrence C Paulson. Isabelle/HOL: a proof assistant for higher-order
logic. Springer, 2002.
Leonardo de Moura and Sebastian Ullrich. The Lean 4 theorem prove r and programming language. In
Andr´ e Platzer and Geoﬀ Sutcliﬀe, editors, Automated Deduction – CADE 28 , pages 625–635, Cham, 2021.
Springer International Publishing.
Emily First, Markus Rabe, Talia Ringer, and Yuriy Brun. Baldur: Whole- proof generation and repair with
large language models. In Proceedings of the 31st ACM Joint European Software Enginee ring Conference
and Symposium on the Foundations of Software Engineering , pages 1229–1241, 2023.
Chuanyang Zheng, Haiming Wang, Enze Xie, Zhengying Liu, Jiankai Su n, Huajian Xin, Jianhao Shen,
Zhenguo Li, and Yu Li. Lyra: Orchestrating dual correction in auto mated theorem proving. arXiv
preprint arXiv:2309.15806 , 2023.
Haiming Wang, Huajian Xin, Chuanyang Zheng, Zhengying Liu, Qingxing Cao, Yinya Huang, Jing Xiong,
Han Shi, Enze Xie, Jian Yin, Zhenguo Li, and Xiaodan Liang. LEGO-prov er: Neural theorem proving
with growing libraries. In The Twelfth International Conference on Learning Represen tations , 2024a. URL
https://openreview.net/forum?id=3f5PALef5B .
Christian Szegedy. A promising path towards autoformalization and general artiﬁcial intelligence. In Intel-
ligent Computer Mathematics: 13th International Conferen ce, CICM 2020, Bertinoro, Italy, July 26–31,
2020, Proceedings 13 , pages 3–20. Springer, 2020.
Albert Qiaochu Jiang, Sean Welleck, Jin Peng Zhou, Timothee Lacroix, Jiacheng Liu, Wenda Li, Mateja
Jamnik, Guillaume Lample, and Yuhuai Wu. Draft, Sketch, and Prove : Guiding formal theorem provers
with informal proofs. In The Eleventh International Conference on Learning Represe ntations , 2023. URL
https://openreview.net/forum?id=SMa9EAovKMC .
32Peiyang Song, Kaiyu Yang, and Anima Anandkumar. Towards large lan guage models as copilots for theorem
proving in lean. arXiv preprint arXiv:2404.12534 , 2024a.
Pan Lu, Liang Qiu, Wenhao Yu, Sean Welleck, and Kai-Wei Chang. A sur vey of deep learning for mathe-
matical reasoning. In Anna Rogers, Jordan Boyd-Graber, and Na oaki Okazaki, editors, Proceedings of the
61st Annual Meeting of the Association for Computational Li nguistics (Volume 1: Long Papers) , pages
14605–14631. Association for Computational Linguistics, 2023. d oi: 10.18653/v1/2023.acl-long.817. URL
https://aclanthology.org/2023.acl-long.817 .
Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupe ng Hou, Yingqian Min, Be-
ichen Zhang, Junjie Zhang, Zican Dong, et al. A survey of large langu age models. arXiv preprint
arXiv:2303.18223 , 2023.
Cedegao E Zhang, Katherine M Collins, Adrian Weller, and Joshua B Ten enbaum. AI for mathematics: A
cognitive science perspective. arXiv preprint arXiv:2310.13021 , 2023a.
Stanislas Dehaene. The number sense: How the mind creates mathematics . Oxford University Press USA,
2011.
Lisa Feigenson, Stanislas Dehaene, and Elizabeth Spelke. Core syst ems of number. Trends in Cognitive
Sciences , 8(7):307–314, 2004.
Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin P ei, Oﬁr Press, and
Karthik R Narasimhan. SWE-bench: Can language models resolve rea l-world GitHub is-
sues? In The Twelfth International Conference on Learning Represen tations , 2024. URL
https://openreview.net/forum?id=VTF8yNQM66 .
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, and Henrique P onde de Oliveira Pinto et al. Evalu-
ating large language models trained on code. arXiv preprint arXiv:2107.03374 , 2021.
Kaiyu Yang, Aidan Swope, Alex Gu, Rahul Chalamala, Peiyang Song, Sh ixing Yu, Saad Godil, Ryan J
Prenger, and Animashree Anandkumar. LeanDojo: Theorem prov ing with retrieval-augmented language
models. Advances in Neural Information Processing Systems , 36, 2024c.
Peiyang Song, Kaiyu Yang, and Anima Anandkumar. Towards large lan guage models as copilots for theorem
proving in Lean, 2024b. URL https://arxiv.org/abs/2404.12534 .
Rose E Wang, Ana T Ribeiro, Carly D Robinson, Susanna Loeb, and Dor a Demszky. Tutor CoPilot: A
human-AI approach for scaling real-time expertise. arXiv preprint arXiv:2410.03017 , 2024b.
Kunhao Zheng, Jesse Michael Han, and Stanislas Polu. MiniF2F: a cro ss-system benchmark for formal
Olympiad-level mathematics. In International Conference on Learning Representations , 2022. URL
https://openreview.net/forum?id=9ZPegFuFTFv .
Zhangir Azerbayev, Bartosz Piotrowski, Hailey Schoelkopf, Edwar d W Ayers, Dragomir Radev, and Jeremy
Avigad. ProofNet: Autoformalizing and formally proving undergrad uate-level mathematics. arXiv preprint
arXiv:2302.12433 , 2023.
Peter Scholze. Liquid tensor experiment. Experimental Mathematics , 31(2):349–354, 2022.
Anthony Bordg, Lawrence Paulson, and Wenda Li. Simple type theor y is not too simple: Grothendieck’s
schemes without dependent types. Experimental Mathematics , 31(2):364–382, 2022. doi: 10.1080/105864
58.2022.2062073. URL https://doi.org/10.1080/10586458.2022.2062073 .
Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wort man Vaughan, Hanna Wallach,
Hal Daum´ e Iii, and Kate Crawford. Datasheets for datasets. Communications of the ACM , 64(12):
86–92, 2021.
33Shubham Toshniwal, Ivan Moshkov, Sean Narenthiran, Daria Gitman , Fei Jia, and Igor Gitman.
OpenMathInstruct-1: A 1.8 million math instruction tuning dataset. arXiv preprint arXiv:2402.10176 ,
2024.
Subhro Roy and Dan Roth. Solving general arithmetic word problems . In Llu´ ıs M` arquez, Chris Callison-
Burch, and Jian Su, editors, Proceedings of the 2015 Conference on Empirical Methods in N atural Language
Processing , pages 1743–1752, Lisbon, Portugal, September 2015. Associat ion for Computational Linguistics.
doi: 10.18653/v1/D15-1202. URL https://aclanthology.org/D15-1202 .
Rik Koncel-Kedziorski, Subhro Roy, Aida Amini, Nate Kushman, and Ha nnaneh Hajishirzi. MAWPS: A
math word problem repository. In Proceedings of the 2016 conference of the north american cha pter of
the association for computational linguistics: human lang uage technologies , pages 1152–1157, 2016.
Yan Wang, Xiaojiang Liu, and Shuming Shi. Deep neural solver for mat h word problems. In Proceedings of
the 2017 conference on empirical methods in natural languag e processing , pages 845–854, 2017.
Shen-Yun Miao, Chao-Chun Liang, and Keh-Yih Su. A diverse corpus for evaluating and developing english
math word problem solvers. In Proceedings of the 58th Annual Meeting of the Association fo r Computa-
tional Linguistics , pages 975–984, 2020.
Arkil Patel, Satwik Bhattamishra, and Navin Goyal. Are NLP models re ally able to solve simple math
word problems? In Proceedings of the 2021 Conference of the North American Cha pter of the Associ-
ation for Computational Linguistics: Human Language Techn ologies , pages 2080–2094. Association for
Computational Linguistics, 2021. doi: 10.18653/v1/2021.naacl-ma in.168.
Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Sa my Bengio, and Mehrdad Farajtabar.
GSM-symbolic: Understanding the limitations of mathematical reaso ning in large language models. arXiv
preprint arXiv:2410.05229 , 2024.
Danqing Huang, Shuming Shi, Chin-Yew Lin, Jian Yin, and Wei-Ying Ma. Ho w well do computers solve
math word problems? Large-scale dataset construction and evalu ation. In Proceedings of the 54th Annual
Meeting of the Association for Computational Linguistics ( Volume 1: Long Papers) , pages 887–896, 2016.
Wang Ling, Dani Yogatama, Chris Dyer, and Phil Blunsom. Program in duction by rationale generation:
Learning to solve and explain algebraic word problems. In Proceedings of the 55th Annual Meeting of
the Association for Computational Linguistics , pages 158–167. Association for Computational Linguistics,
2017. doi: 10.18653/v1/P17-1015.
Swaroop Mishra, Arindam Mitra, Neeraj Varshney, Bhavdeep Sach deva, Peter Clark, Chitta Baral, and
Ashwin Kalyan. NumGLUE: A suite of fundamental yet challenging mat hematical reasoning tasks. In
Proceedings of the 60th Annual Meeting of the Association fo r Computational Linguistics (Volume 1: Long
Papers) , pages 3505–3523, 2022a.
Xiaotian Zhang, Chunyang Li, Yi Zong, Zhengyu Ying, Liang He, and X ipeng Qiu. Evaluating the perfor-
mance of large language models on GAOKAO benchmark. arXiv preprint arXiv:2305.12474 , 2023b.
Keiran Paster. Testing language models on a held-out high school na tional ﬁnals exam.
https://huggingface.co/datasets/keirp/hungarian_nat ional_hs_finals_exam , 2023.
Zheng Yuan, Hongyi Yuan, Chuanqi Tan, Wei Wang, and Songfang Huang. How well do large language
models perform in arithmetic tasks? arXiv preprint arXiv:2304.02015 , 2023.
TAL Education Group. TAL-SCQ5K-EN/TAL-SCQ5K-CN. https://github.com/math-eval/TAL-SCQ5K ,
2023.
34Wanjun Zhong, Ruixiang Cui, Yiduo Guo, Yaobo Liang, Shuai Lu, Yanlin Wang, Amin Saied, Weizhu Chen,
and Nan Duan. AGIEval: A human-centric benchmark for evaluating foundation models. In Findings of
the Association for Computational Linguistics: NAACL 2024 , pages 2299–2314, 2024.
Wenhu Chen, Ming Yin, Max Ku, Pan Lu, Yixin Wan, Xueguang Ma, Jianyu Xu, Xinyi Wang, and Tony
Xia. TheoremQA: A theorem-driven question answering dataset. I nProceedings of the 2023 Conference
on Empirical Methods in Natural Language Processing , pages 7889–7901, 2023.
Tomohiro Sawada, Daniel Paleka, Alexander Havrilla, Pranav Tadepa lli, Paula Vidas, Alexander Kranias,
John J Nay, Kshitij Gupta, and Aran Komatsuzaki. ARB: Advanced r easoning benchmark for large
language models. arXiv preprint arXiv:2307.13692 , 2023.
Sean Welleck, Jiacheng Liu, Ronan Le Bras, Hannaneh Hajishirzi, Yej in Choi, and Kyunghyun Cho.
NaturalProofs: Mathematical theorem proving in natural languag e. InThirty-ﬁfth Conference on
Neural Information Processing Systems Datasets and Benchm arks Track (Round 1) , 2021. URL
https://openreview.net/forum?id=Jvxa8adr3iY .
Elliot Glazer, Ege Erdil, Tamay Besiroglu, Diego Chicharro, Evan Chen, Alex Gunning, Caroline Falkman
Olsson, Jean-Stanislas Denain, Anson Ho, Emily de Oliveira Santos, et al. FrontierMath: a benchmark
for evaluating advanced mathematical reasoning in AI. arXiv preprint arXiv:2411.04872 , 2024.
Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han,
Yujie Huang, Yuxiang Zhang, et al. OlympiadBench: A challenging benc hmark for promoting AGI with
Olympiad-level bilingual multimodal scientiﬁc problems. arXiv preprint arXiv:2402.14008 , 2024.
Simon Frieder, Mirek Olˇ s´ ak, Julius Berner, and Thomas Lukasiewic z. The IMO small challenge: Not-too-
hard Olympiad math datasets for LLMs. In The Second Tiny Papers Track at ICLR 2024 , 2024.
David Saxton, Edward Grefenstette, Felix Hill, and Pushmeet Kohli. A nalysing mathematical reasoning
abilities of neural models. In International Conference on Learning Representations , 2019.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Ma zeika, Dawn Song, and Jacob Steinhardt.
Measuring massive multitask language understanding. arXiv preprint arXiv:2009.03300 , 2020.
Yuhuai Wu, Albert Qiaochu Jiang, Jimmy Ba, and Roger Grosse. INT: An inequality benchmark for
evaluating generalization in theorem proving. arXiv preprint arXiv:2007.02924 , 2020.
Swaroop Mishra, Matthew Finlayson, Pan Lu, Leonard Tang, Sean W elleck, Chitta Baral, Tanmay Rajpuro-
hit, Oyvind Tafjord, Ashish Sabharwal, Peter Clark, and Ashwin Kaly an. LILA: A uniﬁed benchmark
for mathematical reasoning. In Yoav Goldberg, Zornitsa Kozarev a, and Yue Zhang, editors, Proceed-
ings of the 2022 Conference on Empirical Methods in Natural L anguage Processing , pages 5807–5832,
Abu Dhabi, United Arab Emirates, December 2022b. Association for Computational Linguistics. doi:
10.18653/v1/2022.emnlp-main.392. URL https://aclanthology.org/2022.emnlp-main.392 .
Haonan Li, Yixuan Zhang, Fajri Koto, Yifei Yang, Hai Zhao, Yeyun Gong, Nan Duan, and Timothy
Baldwin. CMMLU: Measuring massive multitask language understandin g in chinese. arXiv preprint
arXiv:2306.09212 , 2023.
Simon Frieder, Martin Alawadhi, Trimmel, Rashid, and Klaus Gy. LLM vs I TP. InThe 3rd Workshop on
Mathematical Reasoning and AI at NeurIPS’23 , 2023c.
Sean Welleck, Jiacheng Liu, Ximing Lu, Hannaneh Hajishirzi, and Yejin C hoi. NaturalProver: grounded
mathematical proof generation with language models. Advances in Neural Information Processing Systems ,
35:4913–4927, 2022.
Alexandra N Uma, Tommaso Fornaciari, Dirk Hovy, Silviu Paun, Barbar a Plank, and Massimo Poesio.
Learning from disagreement: A survey. Journal of Artiﬁcial Intelligence Research , 72:1385–1470, 2021.
35Katherine M Collins, Umang Bhatt, and Adrian Weller. Eliciting and learnin g with soft labels from every
annotator. In Proceedings of the AAAI Conference on Human Computation and Crowdsourcing , volume 10,
pages 40–52, 2022.
Ilia Sucholutsky, Ruairidh M Battleday, Katherine M Collins, Raja Marj ieh, Joshua Peterson, Pulkit Singh,
Umang Bhatt, Nori Jacoby, Adrian Weller, and Thomas L Griﬃths. On the informativeness of supervision
signals. In Uncertainty in Artiﬁcial Intelligence , pages 2036–2046. PMLR, 2023.
Mitchell L Gordon, Michelle S Lam, Joon Sung Park, Kayur Patel, Jeﬀ H ancock, Tatsunori Hashimoto,
and Michael S Bernstein. Jury learning: Integrating dissenting voic es into machine learning models. In
Proceedings of the 2022 CHI Conference on Human Factors in Co mputing Systems , pages 1–19, 2022.
Guillaume Lample and Fran¸ cois Charton. Deep learning for symbolic ma thematics. In International Con-
ference on Learning Representations , 2020. URL https://openreview.net/forum?id=S1eZYeHFDS .
Riyaz Ahuja, Jeremy Avigad, Prasad Tetali, and Sean Welleck. Impro ver: Agent-based automated proof
optimization. arXiv preprint arXiv:2410.04753 , 2024.
Shubhra Mishra, Gabriel Poesia, Belinda Mo, and Noah D Goodman. Ma thCAMPS: Fine-grained synthesis
of mathematical problems from human curricula. arXiv preprint arXiv:2407.00900 , 2024.
Zihao Zhou, Shudong Liu, Maizhen Ning, Wei Liu, Jindong Wang, Derek F Wong, Xiaowei Huang, Qiufeng
Wang, and Kaizhu Huang. Is your model really a good math reasoner ? evaluating mathematical reasoning
with checklist. arXiv preprint arXiv:2407.08733 , 2024.
Emanuele La Malfa, Aleksandar Petrov, Simon Frieder, Christoph We inhuber, Ryan Burnell, Raza Nazar,
Anthony Cohn, Nigel Shadbolt, and Michael Wooldridge. Language- Models-as-a-Service: Overview of a
new paradigm and its challenges. Journal of Artiﬁcial Intelligence Research , 80:1497–1523, 2024.
Huaiyuan Ying, Zijian Wu, Yihan Geng, Jiayu Wang, Dahua Lin, and Kai C hen. Lean workbook: A large-
scale lean problem set formalized from natural language math proble ms.arXiv preprint arXiv:2406.03847 ,
2024.
Ronen Eldan and Yuanzhi Li. TinyStories: How small can language mod els be and still speak coherent
English? arXiv preprint arXiv:2305.07759 , 2023.
Subhabrata Mukherjee, Arindam Mitra, Ganesh Jawahar, Sahaj A garwal, Hamid Palangi, and Ahmed
Awadallah. Orca: Progressive learning from complex explanation tra ces of GPT-4. arXiv preprint
arXiv:2306.02707 , 2023.
Peiyi Wang, Lei Li, Liang Chen, Dawei Zhu, Binghuai Lin, Yunbo Cao, Qi Liu, Tianyu Liu, and Zhifang Sui.
Large language models are not fair evaluators. arXiv preprint arXiv:2305.17926 , 2023.
Patrick Haluptzok, Matthew Bowers, and Adam Tauman Kalai. Langu age models can teach themselves
to program better. In The Eleventh International Conference on Learning Represe ntations , 2023. URL
https://openreview.net/forum?id=SaRj2ka1XZ3 .
Lawrence C Paulson and Kong Woei Susanto. Source-level proof r econstruction for interactive theorem
proving. In International Conference on Theorem Proving in Higher Orde r Logics , pages 232–245. Springer,
2007.
Jia Meng and Lawrence C Paulson. Translating higher-order clauses to ﬁrst-order clauses. Journal of
Automated Reasoning , 40:35–60, 2008.
Jiewen Hu, Thomas Zhu, and Sean Welleck. miniCTX: Neural theorem p roving with (long-)contexts, 2024.
URLhttps://arxiv.org/abs/2408.03350 .
36Albert Qiaochu Jiang, Wenda Li, Jesse Michael Han, and Yuhuai Wu. L ISA: Language models of ISAbelle
proofs. In 6th Conference on Artiﬁcial Intelligence and Theorem Provi ng, pages 378–392, 2021.
Albert Qiaochu Jiang, Wenda Li, Szymon Tworkowski, Konrad Czecho wski, Tomasz Odrzyg´ o´ zd´ z, Piotr
Mi/suppress lo´ s, Yuhuai Wu, and Mateja Jamnik. Thor: Wielding hammers to int egrate language models and
automated theorem provers. Advances in Neural Information Processing Systems , 35:8360–8373, 2022.
Maciej Miku/suppress la, Szymon Tworkowski, Szymon Antoniak, Bartosz Piot rowski, Albert Q. Jiang, Jin Peng Zhou,
Christian Szegedy, /suppress Lukasz Kuci´ nski, Piotr Mi/suppress lo´ s, and Yuhuai W u. Magnushammer: A transformer-based
approach to premise selection. In The Twelfth International Conference on Learning Represen tations , 2024.
URLhttps://openreview.net/forum?id=oYjPk8mqAV .
Robion Kirby. A calculus for framed links in S3.Invent. Math. , 45(1):35–56, 1978. ISSN 0020-9910,1432-1297.
doi: 10.1007/BF01406222. URL https://doi.org/10.1007/BF01406222 .
Andr´ as Juh´ asz. Diﬀerential and low-dimensional topology , volume 104 of London Mathematical Society
Student Texts . Cambridge University Press, Cambridge, 2023. ISBN 978-1-009- 22060-6; 978-1-009-22057-
6.
Kurt Reidemeister. Elementare begr¨ undung der knotentheorie. Abhandlungen aus dem Mathematis-
chen Seminar der Universit¨ at Hamburg , 5(1):24–32, 1927. doi: 10.1007/BF02952507. URL
https://doi.org/10.1007/BF02952507 .
Sergei Gukov, James Halverson, Fabian Ruehle, and Piotr Su/suppress lkows ki. Learning to unknot. Machine
Learning: Science and Technology , 2(2):025035, apr 2021. doi: 10.1088/2632-2153/abe91f. URL
https://dx.doi.org/10.1088/2632-2153/abe91f .
Marc Culler, Nathan M. Dunﬁeld, Matthias Goerner, and Jeﬀrey R. W eeks. SnapPy, a computer program
for studying the geometry and topology of 3-manifolds. Available at http://snappy.computop.org
(18/12/2024), 2024.
Mikhail Khovanov. A categoriﬁcation of the Jones polynomial. Duke Math. J. , 101(3):359–
426, 2000. ISSN 0012-7094,1547-7398. doi: 1 0 . 1 2 1 5 / S 0 0 1 2- 7 0 9 4- 0 0- 1 0 1 3 1 -7. URL
https://doi.org/10.1215/S0012-7094-00-10131-7 .
Peter Ozsv´ ath and Zolt´ an Szab´ o. Holomorphic disks and topolog ical invariants for closed three-manifolds.
Ann. of Math. (2) , 159(3):1027–1158, 2004. ISSN 0003-486X,1939-8980. doi: 10.4 007/annals.2004.159.1027.
URLhttps://doi.org/10.4007/annals.2004.159.1027 .
Edward Witten. Monopoles and four-manifolds. Math. Res. Lett. , 1(6):769–796, 1994. ISSN 1073-2780. doi:
10.4310/MRL.1994.v1.n6.a13. URL https://doi.org/10.4310/MRL.1994.v1.n6.a13 .
The Sage Developers. SageMath, the Sage Mathematics Software System (Version 10 .5), 2024.
https://www.sagemath.org .
Robert Lipshitz and Sucharit Sarkar. Spatial reﬁnements and Kho vanov homology. In Proceedings of the
International Congress of Mathematicians—Rio de Janeiro 2 018. Vol. II. Invited lectures , pages 1153–1173.
World Sci. Publ., Hackensack, NJ, 2018. ISBN 978-981-3272-91-0 ; 978-981-3272-87-3.
Sergei Gukov, James Halverson, Ciprian Manolescu, and Fabian Rue hle. Searching for ribbons with machine
learning, 2023. URL https://arxiv.org/abs/2304.09304 .
Taylor Applebaum, Sam Blackwell, Alex Davies, Thomas Edlich, Andr´ as Juh´ asz, Marc Lackenby, Nenad
Tomaˇ sev, and Daniel Zheng. The unknotting number, hard unkno t diagrams, and reinforcement learning,
2024. URL https://arxiv.org/abs/2409.09032 .
37Jacob Rasmussen. Khovanov homology and the slice genus. Invent. Math. , 182(2):419–447, 2010. ISSN 0020-
9910,1432-1297. doi: 10.1007/s00222-010-0275-6. URL https://doi.org/10.1007/s00222-010-0275-6 .
Michael Hartley Freedman. The topology of four-dimensional manif olds.J. Diﬀerential Geometry , 17(3):
357–453, 1982. ISSN 0022-040X,1945-743X. URL http://projecteuclid.org/euclid.jdg/1214437136 .
Cliﬀord Henry Taubes. The Seiberg-Witten invariants and symplectic forms. Math. Res. Lett. ,
1(6):809–822, 1994. ISSN 1073-2780. doi: 1 0 . 4 3 1 0 / M R L . 1 9 9 4 . v 1 . n 6 . a 15. URL
https://doi.org/10.4310/MRL.1994.v1.n6.a15 .
Ronald Fintushel and Ronald J. Stern. Knots, links, and 4-manifolds .Invent. Math. , 134
(2):363–400, 1998. ISSN 0020-9910,1432-1297. doi: 1 0 . 1 0 0 7 / s 0 0 2 2 2 0 0 5 0 2 6 8. URL
https://doi.org/10.1007/s002220050268 .
John Morgan and Gang Tian. Ricci ﬂow and the Poincar´ e conjecture , volume 3 of Clay Mathematics
Monographs . American Mathematical Society, Providence, RI; Clay Mathematic s Institute, Cambridge,
MA, 2007. ISBN 978-0-8218-4328-4.
Benjamin A. Burton. Introducing Regina, the 3-manifold topology s oftware. Experiment. Math. , 13(3):
267–272, 2004. ISSN 1058-6458,1944-950X. URL http://projecteuclid.org/euclid.em/1103749834 .
Louis H Kauﬀman and Soﬁa Lambropoulou. Hard unknots and collapsin g tangles. Introductory lectures on
knot theory, Ser. Knots Everything , 46:187–247, 2012.
C.H. Dowker and Morwen B. Thistlethwaite. Classiﬁcation of knot pro jections. Topology and its Applica-
tions , 16(1):19–31, 1983. ISSN 0166-8641. doi: https://doi.org/1 0.1016/0166-8641(83)90004-4. URL
https://www.sciencedirect.com/science/article/pii/0 166864183900044 .
I. A. Dynnikov. Arc-presentations of links: Monotonic simpliﬁcation .Fundamenta Mathematicae , 190(1):
29–76, 2006. URL http://eudml.org/doc/283163 .
L. H. Kauﬀman, N. E. Russkikh, and I. A. Taimanov. Rectangular kn ot diagrams classiﬁcation with deep
learning. Journal of Knot Theory and Its Ramiﬁcations , 31(11):2250067, 2022. doi: 10.1142/S021821652
2500675. URL https://doi.org/10.1142/S0218216522500675 .
Sergei Gukov, James Halverson, and Fabian Ruehle. Rigor with mach ine learning from ﬁeld theory to the
poincar´ econjecture. Nature Reviews Physics , 6(5):310–319, 2024. doi: 10.1038/s42254-024-00709-0. URL
https://doi.org/10.1038/s42254-024-00709-0 .
Adam Zsolt Wagner. Constructions in combinatorics via neural netw orks, 2021. URL
https://arxiv.org/abs/2104.14516 .
Fran¸ cois Charton, Jordan S. Ellenberg, Adam Zsolt Wagner, and G eordie Williamson. PatternBoost: Con-
structions in mathematics with a little help from AI, 2024. URL https://arxiv.org/abs/2411.00566 .
George P´ olya. With, or without, motivation? The American Mathematical Monthly , 56(10):684–691, 1949.
Rebecca Lea Morris. Motivated proofs: What are they, why they m atter and how to write them. The Review
of Symbolic Logic , 13(1):23–46, 2019. doi: 10.1017/S1755020319000583.
Mahima Pushkarna, Andrew Zaldivar, and Oddur Kjartansson. Dat a cards: Purposeful and transparent
dataset documentation for responsible ai. In Proceedings of the 2022 ACM Conference on Fairness, Ac-
countability, and Transparency , pages 1776–1826, 2022.
Emily M. Bender and Batya Friedman. Data statements for natural language processing: Toward mitigating
system bias and enabling better science. Transactions of the Association for Computational Linguis tics,
6:587–604, 2018. doi: 10.1162/tacl a00041. URL https://aclanthology.org/Q18-1041 .
38A Appendix: Problems for Motivated Proof Experiments
For the motivated proof experiments in 4.3, we used ﬁve problems including the two examples. These are
presented how they were presented to the models, including the hu man-written motivated and unmotivated
proof used for in-context examples.
Cantor’s theorem There is no surjection from a set Xto its power set P(X).
MOTIVATED PROOF: Let f:X→P(X) be our function, we need to ﬁnd some S⊆Xnot in the image
off. Not knowing which subset of Xto take, we can treat the subset as an unknown, just as we do whe n
solving an equation, and try to narrow down the possibilities. The mos t general subset of Xcan be expressed
as{x∈X:P(x)}for some as yet unspeciﬁed property P. We now want to prove, for an arbitrary element
yofX, thatf(y)/\e}atio\slash={x∈X:P(x)}. To obtain our contradiction, we need either an element xoff(y)
such that ¬P(x) or an element xof the complement of f(y) such that P(x). There are not many elements
around, so trying yis one of the ﬁrst things to do, and then we ﬁnd that we need either y∈f(y) and¬P(y)
ory /∈f(y) andP(y). The choice P(x) =x /∈f(x) satisﬁes this, so the set S={x∈X:x /∈X}has the
desired property.
UNMOTIVATED PROOF: Let f:X→P(X) be our function, we claim that the set S={x∈X:x /∈f(x)}
is not in the image of f, hencefis not surjective. Suppose there exists y∈Xsuch that f(y) =S. But then
y∈f(y) iﬀy∈Siﬀy /∈f(y) by the deﬁnition of S, giving a contradiction.
Small doubling There exists a subset A of the natural numbers with cardinality n, s uch that the set
A+A=a1+a2:ai,aj∈Ahas cardinality 2 n−1.
MOTIVATED PROOF: We don’t know which set to take for Aso we treat it as an unknown, just as we do
when solving an equation, and try to narrow down the possibilities. Sin ce we know that |A|=n, we can write
A={a1,...,an}fora1,...,andistinct, so we have A+A=ai+aj:i,j= 1,...,n . This isn’t immediately
helpful since we don’t know how many collisions there will be in A+A, but we try to narrow down the
possibilities. The simplest way to distinguish natural numbers is by ord ering them, so we assume without
loss of generality that a1< ... < a n. Applying this monotonicity to our sums, we deduce that ai+aj< ai+ak
whenever j < k .
Trying to distinguish as many elements as possible, we ﬁx some iand take this inequality to its logical
conclusion, ﬁnding that a1+ai< .... < a n+ai, or that we have n distinct elements. However, we can further
extend this chain to the left if 1 < ior the right if i < n , giving us the longer chain a1+a1< ... < a 1+ai<
... < a n+a1< ... < a n+an, which has 2 n−1 distinct elements. If we want to have |A+A|= 2n−1,
then these are all the elements of A+A, but we still have this free parameter i. Repeating the construction
with some j > i and observing the ﬁrst syntactic diﬀerent element, we notice that a1+ai+1=a2+ai, and
isolating the variable i we notice that a2−a1=ai+1−ai. This deﬁnes an arithmetic progression with ﬁrst
elementa1and common diﬀerence a2−a1, so let’s see if that enough.
Suppose A is an arithmetic progression of length n, thenA=a,a+d,...,a + (n−1)d, thenA+A=
2a,2a+d,..., 2a+ (2n−2)dhas size 2 n−1, completing the proof.
UNMOTIVATED PROOF: Let A={1,...,n}, which has cardinality n, then A+A={2,...,2n}has cardi-
nality 2n−1, completing the proof.
Integer sums There is a polynomial P(x) with rational coeﬃcients such that P(n) =/summationtextn
k=0kfor all
non-negative integers n.
MOTIVATED PROOF: We can write a generic polynomial as P(n) =/summationtextm
j=0ajnj. However, since mis
unknown the equation is reasonably unwieldy. Consequently, we wish to ﬁnd an upper bound on the degree
ofP(n). We do this by applying the trivial bound, P(n) =/summationtextn
k=0k≤/summationtextn
k=0n=n2+n, and since this
equation holds for arbitrarily large n, we have that m=degP≤2, so we can write P(n) =a0+a1n+a2n2. To
39ﬁnda0,a1anda2, we can substitute some small values of n, so we have a0=P(0) = 0,a0+a1+a2=P(1) = 1
anda0+ 2a1+ 4a2=P(2) = 3. Solving the resulting linear equation, we have that a0= 0,a1=a2= 1/2
soP(n) =1
2(n2+n).
To conﬁrm that this works for all n, we can use induction. We have checked the base case already so
we only need to do the induction step, so suppose that/summationtextn
k=0k=1
2(n2+n), then we need to show that/summationtextn+1
k=0k=1
2((n+ 1)2+ (n+ 1)). In order to use the induction assumption, we split the LHS to g ive us/summationtextn
k=0k+ (n+ 1) and substitute in the induction assumption. By expanding and sim plifying, we ﬁnd that
both sides of the equation are equal, completing our proof.
UNMOTIVATED PROOF: We show that P(n) =1
2n(n+ 1) works using induction. First we observe that
P(0) = 0 =/summationtext0
k=0k. Then suppose that/summationtextn
k=0k=1
2n(n+1), then we have that/summationtextn+1
k=0k=/summationtextn
k=0k+(n+1) =
1
2n(n+ 1) + (n+ 1) = (n+ 1)(n
2+ 1) =1
2(n+ 1)(n+ 2), completing the proof.
Nilpotent units LetRbe a commutative ring, and let x∈Rbe nilpotent. Then (1 + x) is a unit.
MOTIVATED PROOF: To show that 1+ xis a unit, we need to ﬁnd an inverse element. Not knowing which
element to take, we parametrize the most generic element we can. S ince the only known elements of Rare 1
andx, the most generic element is an integer polynomial in x,/summationtextm
k=0akxk. For this to be a right inverse of
1 +x, we must have that 1 = (1 + x)(/summationtextm
k=0akxk) =a0+/summationtextm
k=1(ak+ak−1)xk+amxm+1. For this to hold,
we must eliminate all coeﬃcients of the polynomial besides the consta nt term, which should be 1. This gives
us thata0= 1,ak=ak−1for 1≤k≤mandam= 0. The ﬁrst two equations give us that ak= (−1)kfor
allk, but this contradicts the last equation.
But we also know that xis nilpotent, so if we have rsuch that xr= 0, then all coeﬃcients from xronwards
can be ignored. This solves our issue, as we can let m=r−1 to remove the am= 0 condition, and we are
left with ak= (−1)k, so (1 + x) is a unit with inverse/summationtextr−1
k=0(−1)k·xk.
UNMOTIVATED PROOF: Let rbe such that xr= 0 from nilpotency, and observe that (1+ x)(/summationtextr−1
k=0(−1)k·
xk) = 1 +−xr= 1 by the formula for summing geometric progressions, hence/summationtextr−1
k=0(−1)k·xkis an inverse
of 1 +xand 1 +xis a unit.
Large totients We deﬁne Euler’s totient function φas follows. If n=/producttextm
i=1pki
iis its prime factorisation,
thenφ(n) =/producttextm
i=1pki−1
i(pi−1). Show that for all ǫ >0,φ(n)/ncan take values in (1 −ǫ,1).
MOTIVATED PROOF: We ﬁrst try to simplify φ(n)/n. Expressing nin its prime factorisation to match
the deﬁnition of φ(n), we have φ(n)/n=/producttextm
i=1(pki−1
i(pi−1)/pki
i) =/producttextm
i=1(1−1/pi). We notice that each
factor is between 0 and 1, so the product is large where there are f ew factors so we let m= 1 (or equivalently,
lettingn=pk), giving us φ(n)/n= (1−1/p). Since this is clearly less than 1, we only need to choose psuch
that 1−ǫ <1−1/p, which simpliﬁes easily to p >1/ǫ. Since there are inﬁnitely many prime numbers, we
can always choose such a p.
UNMOTIVATED PROOF: Let pbe the smallest prime number such that p >1/ǫ, which exists as there are
inﬁnitely many primes. Then we have φ(p)/p= 1−1/p, and asp >1/ǫ, we see that 1 −ǫ <1−1/p < 1−ǫ
as required.
40