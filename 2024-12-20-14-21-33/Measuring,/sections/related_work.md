We consider three categories of related work: the current burden of balancing the benefits of
self-disclosure with the risks, common approaches from prior work to reduce the risk of online self-
disclosure (both non-AI-based and AI-based), and the need for user engagement in the development
of AI technology.
2.1 The Tension Between the Need for Self-Disclosure and the Risks
Online pseudonymous communities, like Reddit, offer internet users a safe, seemingly anonymous
space to seek opportunities to engage with others free from the baggage of their identity. These
interactions often stem from a desire for informational or emotional support, and in seeking
support people disclose many personal details publicly [ 98]. Self-disclosure is an important key to
establishing a sense of solidarity and community – even disclosing negative experiences has been
shown to lead users to feel a sense of support and increased confidence in themselves [ 75]. Online
self-disclosure specifically can establish a sense of belonging, and support the development of new
relationships [ 16,47] – and is especially valuable for users seeking support on sensitive topics
that they might not otherwise be able to receive in their physical communities due to concerns
over factors like social stigma, or embarrassment [ 101]. Anonymity when engaging in public
self-disclosures can provide users a cover for more intimate and open conversations [9, 80].
While self-disclosure fulfills many core social needs and despite users’ need to continuously
make online self-disclosure decisions based on their intended audiences [ 98], prior work has
shown that people do not always accurately anticipate who might see their content [ 93]. Balancing
informational and emotional support needs with the abstract risks associated with their disclosures
(e.g., re-identification, stalking, identity theft, blackmail) is challenging [ 36,93]. Unlike face-to-
face disclosures, online disclosures leave a digital trace that can be screen-captured and linked
to other posts to re-identify and ultimately harm the original posters. To mitigate their risk of
re-identification, users employ tactics such as the use of “throwaway” or “burner” accounts [ 5,50],
but can still end up disclosing enough information about themselves to be re-identified [3, 67].
Work on re-identifying users from anonymous datasets shows that few attributes are needed to
sufficiently re-identify individuals using incomplete datasets: for example, using 15 demographic
attributes, around 99.98% of Americans can be identified; using just 3, around 83% can still be
identified [ 74]. Information as simple as age, gender, and ethnicity can be enough to re-identify an
individual when combined with a medical diagnosis [ 55]. Re-identification risks are highly relevant
to users of online pseudonymous platforms, like Reddit, with communities dedicated to specific
medical diagnoses such as r/Cushings, or r/Marfans wherein users experience many benefits from
personal disclosure in seeking support (e.g., earlier detection and treatment of medical issues that
would have otherwise gone unaddressed) [44, 64].
Relatedly, users’ disclosure is guided by their perception of risk and the sensitivity of the
information that they are disclosing. It follows that prior research on anonymous public self-
disclosure suggests users feel better able to express themselves when posting anonymously, [ 9,80],
as anonymity allows users to avoid the face-to-face stigma of embarrassing or uncomfortable
topics [ 24,26]. Anonymity affords users the opportunity to be honest, unfiltered, and vulnerable;
characteristics they might not be able to exhibit through in-person interactions. Conversely, users’
heightened feelings of anonymity can also result in benign disinhibition, wherein users disclose
more personal information as they feel more secure and less identifiable [49].
Thus providing users with more awareness of risks to their privacy while maintaining the
benefits of disclosures remains a longstanding challenge for security and privacy practitioners.
We extend this body of work by exploring the design considerations, utility, and intrusiveness of
4... Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway
an end-user-facing NLP-based disclosure detection tool in interactions with users of the online
community of Reddit given the impact of pseudonymity on benign disinhibition effects, like
increased self-disclosure.
2.2 Past Approaches to Alleviating the Risks of Self-Disclosure
Non AI-based Tools. Researchers and practitioners in security & privacy have explored approaches
to helping users navigate the risks of self-disclosures with varying success. One ubiquitous, built-in
approach to mitigating users’ risks of online self-disclosure is the employment of customize-able
privacy preferences [ 2,69]. While important, and helpful for users of social networking sites like
Facebook, the use of granular privacy settings is not entirely relevant to mitigating the harmful
self-disclosure risks pseudonymous online community members face since users are intentionally
posting information publicly. Furthermore, despite the protective intention of this, more granularity
in privacy settings can actually encourage self-disclosure. In their study, Brandimarte et al. showed
that in the context of an online social network, participants who were offered finer-grain privacy
controls disclosed more personal information compared to those who were offered weaker controls
[11]. Finer-grain control has also been found to reduce users’ privacy concerns in other areas as well
such as personalization [ 82]. Research has also explored intervention-based strategies for mitigating
a user’s level of disclosure at the time of posting through the use of framing and presentation. For
example, Wang et al. explored the effect of a modified Facebook interface that provided feedback
about a post’s audience and also allowed users to cancel their post within 10 seconds of making it
[92]. Prior work from Braunstein et al. also showed that changing the wording in a survey question
to remind users that they are revealing sensitive information impacts how much they’re willing to
reveal [ 12]. While these specific techniques are slightly difficult to apply to an online community
like Reddit where most posts will be made in public subreddits, they may still be useful for privacy
intervention tools. Tools that detect potentially risky self-disclosures for example, may benefit in
utility by incorporating additional context for these detections. As such, in this study, we explore
the utility of different framing for suggestions by presenting participants with two versions of a
disclosure detection model that vary in granularity.
AI-based Tools/existing NLP Approaches to detecting self-disclosure. With the advancement of
AI technology, over the course of the past few years, we’ve also started to see numerous natural
language processing (NLP) based intervention tools emerge as aids for the prevention of privacy
leaks from self-disclosure [ 14,37,57]. A core benefit offered by NLP-based self-disclosure interven-
tions compared to the aforementioned ones is that they take a more targeted approach to potential
privacy leaks by explicitly pinpointing disclosures made by users in their posts. This offers users
actionable areas for improvement and the agency to control the dissemination of their sensitive
information. Multiple recent works have introduced NLP-based self-disclosure detection models
that are targeted towards specific disclosure categories such as medical conditions [ 87,89,102],
personal opinions [ 18], employment history [ 84], or stories of sexual harassment [ 19]. Other works
developed detection models that consider any type of personal information revealed by users as
a single category [ 10,73,97]. A few studies also developed models capable of more fine-grained
detection of multiple self-disclosure categories at once [ 4,52]. A major limitation in past work is
that it mainly centers around operational changes for enhancing model performance in detecting
self-disclosures, such as improving their accuracy or expanding their granularity of categories.
However, studying the interaction of users with NLP-based self-disclosure detection models and
analyzing user experiences is key in identifying the next steps for the real-world adoption of NLP
models in privacy-preserving tools. To our knowledge there has been no prior work on user’s
reactions to these models, or whether the classifiers used are perceived as being helpful by users.
5Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway Krsek, et al.
Without the incorporation of user feedback, these NLP detection tools run the risk of ignoring the
key benefits of disclosure discussed above. Through seeking out user feedback in the evaluation
of AI-assisted self-disclosure detection technology, we hope to surface where these tools may fall
short in order to ultimately better align them with the preferences and goals of their intended users.
2.3 The Need for User Engagement in the Design of AI Technology
AI technologies have profound social and economic implications across various domains. When
predictive modeling is employed in critical decision-making processes such as credit offers, in-
surance assessments, hiring, and parole decisions [ 20,35], the application of AI can exacerbate
social inequality as these technologies have the potential to shape opportunities, leaving certain
individuals marginalized due to data or model bias [ 8,20,28,65]. Additionally, most AI-based
technologies are developed from data collected from (biased) human decision-makers, or through
training processes which can also introduce bias [20, 81].
It is imperative that the people impacted by AI systems’ deployment be substantively engaged in
providing feedback and design direction, and that these suggestions form a feedback loop that can
directly influence AI systems’ development and broader policy frameworks which are imperative
for ensuring fair and unbiased outcomes [ 46,81]. Engaging users in the design of AI technology
can help mitigate the negative impacts of AI on society and promote ethical and responsible AI
development [ 20,81]. Park et al . [62] shows the importance of integrating user feedback into the
development process of consumer-oriented systems as there is a potential disparity between user
expectations and technological functionalities. Recognizing that user preferences and demands
can evolve rapidly, the paper advocates for an adaptive approach that places user feedback at the
forefront of system design. On a similar note, [ 21] talks about the necessity of ongoing updates
based on user feedback to prevent errors, particularly in dynamic and evolving scenarios. In
contrast to static systems, those that are continually updated and refined based on user interactions
demonstrate a heightened ability to adapt to new information, circumstances, and user expectations.
Several works have delved into growing privacy concerns associated with AI-based technologies.
The impact of AI on privacy interests is discussed by Kerry [45], emphasizing how advances in AI
amplify concerns regarding the use of personal information [7, 58, 59, 91].
The work of Dou et al . [27] is a first step in assessing user preferences for AI-assisted self-
disclosure detection, though it only reports high-level takeaways as to what participants liked and
didn’t like, and the percentage of users who reported that they would continue to use the model. The
goal of Dou et. al.’s paper was to introduce a state-of-the-art disclosure detection model — the user
feedback reporting was primarily to affirm the desirability of their technical contribution to users.
In contrast, our goal centers user needs and preferences by aiming to examine: (i) how users make
sense of and decide to accept or reject AI-detected self-disclosure risks in their content, (ii) whether
and how these AI-detected self-disclosure risks help users make more informed self-disclosure
decisions, and (iii) where the model falls short or could be improved in being of greater use to users
when they must make these self-disclosure decisions. Our study contributes an exploration of the
usefulness, usability, and utility of AI-supported privacy decision-making despite its imperfections.
Our work ultimately aims to fill this void by examining user perspectives on disclosure and privacy
in the area of online communication, contributing knowledge to enhance technical safeguards, and
aligning AI systems with user expectations in the rapidly evolving landscape of digital interactions.
3 SELF-DISCLOSURE DETECTION MODEL
Prior works on self-disclosure detection mostly focused on sentence or post-level classification
[17,88] that simply determines if the given text contains any disclosure. However, it doesn’t
pinpoint the specific spans (i.e., segments of consecutive words) of self-disclosures, providing
6... Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway
Category Example
Demographic Attributes
Age Irecently celebrated my30th birth day, and I’m in my final year of grad school.
Gender Iamaguy and was shamed for doing ballet.
Age/Gender I(20F) had a fight with my boyfriend last night.
Sexual Orientation Iidentifyasalesbian, and I’d like to share my thoughts on this matter.
Husband/BF Myhusband and I plan to travel to Vegas in May. Any recommended hotel?
Wife/GF What’s a good birthday gift idea for mygf?
Relationship Status I’vebeen single for a while now.
Race/Nationality IwasaSwedish tourist in France, once.
Location Ihave justmoved toUnited States, and I’m finding the medical costs quite high.
Pet Irecently gotaLabrador Retriever puppy, and it’s been very fun
Appearance Ihave bright redhair, which always draws a lot of attention.
Name Hello guys, myname isxxx. I’m looking for a Chinese name for myself.
Contact Myinsisxxx.
Personal Experiences
Family Mybrother (23M) fought my husband (30M) at a family dinner.
Health I’vediagnosed with aprostate cancer, but good news is it’s early stage.
Mental Health Ihave bipolar,anxiety,PTSD andADHD, which are parts of me.
Occupation For context, I’maL5software engineer atGoogle.
Education Ijustcompleted myPhD today, and I’m feeling incredibly happy about it!
Finance This year, Imade 100K from Bitcoin, which I used to purchase a new car.
Table 1. Examples for each of the 19 self-disclosure categories, grouped into Demographic Attributes and
Personal Experiences . The categories presented in the above table are those that are detectable by Dou et. al’s
model [27], while the examples used have been drafted by the authors of this paper.
minimal insights and information for users to review. While there are some models that detect
disclosures at the span level, they often have a narrow scope, focusing on a small set of self-
disclosure categories [ 52] or specialized for news comments [ 86]. To bridge these gaps, Dou et al .
[27] recently developed a SOTA self-disclosure detection model that is capable of detecting 17
distinct categories at the word level, which we used as a technology probe in the later user study.
The model demonstrates high performance with 75% F 1in the categorical disclosure setting
(classify each word into one of 17 categories or as non-disclosure) and 82% F 1in the binary disclosure
setting (classify into disclosure or non-disclosure). We experimented with both versions to explore
how different levels of label detail affect user experience — per RQ2. Based on RoBERTa-Large [ 54]
transformer encoder, the model is fine-tuned on a Reddit corpus containing 4.8K human-annotated
disclosure spans. We chose this model over prompting-based LLMs such as GPT-4 [ 61] due to its
superior efficiency and cost-effectiveness, as well as its similar performance: as Ashok and Lipton
[6]shows fine-tuned small models generally outperform zero-shot prompting of larger models on
span annotation tasks.
During inference, instead of feeding the entire post, including both title and body, into the model,
we first used Ersatz [ 94], a neural network-based sentence splitter, to divide posts into individual
sentences. Each sentence is then fed into the model, resulting in better performance over processing
the whole post at once. To be more specific, for a sentence of 𝑛words 𝑥1, ..., 𝑥 𝑛, the model assigns a
corresponding label 𝑦𝑖to each word 𝑥𝑖. In the categorical disclosure setting, we used the IOB2 label
format [ 83], which tags the starting word of a disclosure span as B-[Class] and subsequent words
asI-[Class] (e.g., B-Age, I-Age), while non-disclosure words as O. For the binary disclosure setting,
7Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway Krsek, et al.
Fig. 2. The model classifies each word to a label.
the labels are simply yesorno. As words are tokenized, we use the label of the first token of each
word as a word label. Figure 2 illustrates the model diagram.
In addition to the 17 main categories detected by the model — ranging from age to mental health,
frequently appearing on Reddit — we also addressed the identification of less common but sensitive
details like names and contact information. To identify names, we used LUKE [ 96], the state-of-
the-art named-entity recognition model. For the detection of personally identifiable information,
such as phone numbers and emails, we integrated Microsoft Presidio1. Recognizing that social
media handles are a commonly shared type of contact information on Reddit, we extended Presidio
with custom regular expressions to detect usernames from platforms such as TikTok, Instagram,
and Twitter. Given our emphasis on self-disclosures, we applied the sentence classifier from Dou
et al. [27] as a preliminary self-disclosure filter before using these external tools: The classifier
first identified whether a sentence contained self-disclosure elements; sentences flagged by this
classifier were then subsequently processed through these external models and tools.
Table 1 presents examples for all 19 categories, which are broadly grouped into: demographic
attributes andpersonal experiences . Demographic attributes include static personal characteristics,
typically expressed in a brief manner, such as age, gender, and race. In contrast, personal experiences
relate to activities and events that might identify an individual — e.g., health-related and education-
related activities or questions.
Of note, our goal in this work is notto introduce new state-of-the-art self-disclosure detection
models. Rather, we use these models as a technology probe [ 42] in a study to understand the
opportunities and challenges of using AI to help users make informed decisions when sharing
personally identifiable information online.