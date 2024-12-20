Our findings highlight both the promise and peril of using AI-assisted self-disclosure detection tools
to help users make informed decisions about what to disclose when sharing personal information
online. Whereas prior work in this space has focused on the technical challenge of developing
effective self-disclosure classification models, we show the problem is inherently socio-technical and
emblematic of Ackerman’s social-technical gap [ 1]. An effective solution cannot stop at achieving
a high F 1score; it will require significant consideration of, e.g., users’ lived threat models, posting
context, risk mitigation strategies, and understanding of risk. To that end, we culminate with a
discussion on how such tools can be designed in a manner that is not only effective at detecting
risky disclosures but useful in helping users make informed decisions.
To summarize our findings, the majority of participants responded positively to our model —
particularly the categorical disclosure variant — describing its utility in facilitating self-reflection
and in catching user’s mistakes. Users also anticipated it being helpful in making decisions about
content they might be uncertain about sharing. We also found that users appreciated the presence
of coarse explanations provided by the categorical disclosure version of our model: since users’
conceptions of risk may have differed from what the model was trained to identify, they were more
likely to accept model outputs when given the “category” of the detected disclosure versus just the
fact that a given span of text had some kind of disclosure. Finally, our findings also surface many
weaknesses of existing models that highlight directions for future modeling and design work.
For future modeling work, our findings identify new categories of disclosure users desired the
model to detect, the need to distinguish between factual and non-factual disclosures, to account for a
user’s history of disclosures, and the need to help users de-risk disclosures while preserving semantic
meaning. For future design work, our findings suggest a need to design effective explanations,
account for posting context and disclosure norms, and prioritize disclosures that are particularly
important for users to heed so as to avoid habituation effects from over-warning users. Below, we
center and embellish upon a few promising design implications for AI tools that aim to help users
navigate self-disclosure risks online.
6.1 Practical Implications for Deploying Self-Disclosure Detection Tools
Our study raises important considerations for any practitioners or researchers hoping to apply the
use of AI-assisted self-disclosure detection to existing systems, and showcases its potential utility
across a multitude of contexts. Beyond being helpful as a standalone tool users could use across social
media sites, we could also envision this being integrated into the design of platforms themselves,
presented to users at the time of drafting a post. For example, such a tool could be smoothly
integrated into existing features Reddit has released for making sure users adhere to community
19Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway Krsek, et al.
guidelines4, though some work would be needed to ensure that the model suggestions complemented
community guidelines as opposed to conflicting with them (e.g. including or excluding specific
information from their posts). AI-assisted self-disclosure detection can be especially useful to
individuals seeking support in scenarios where discretion is crucial: for example, on platforms
where domestic violence survivors are seeking support, where employees discuss how to navigate
work-related issues (e.g. Blind), or even in contexts where whistle-blowers are reporting violations
by companies or institutions. In the following paragraphs, we explore important considerations for
any future NLP-based self-disclosure detection tools intended for use by end-users.
Surfacing only high-confidence outputs. Our model made mistakes. While some participants found
value in these mistakes in that the detected disclosures still drew their attention to other potentially
risky disclosures in their posts, too many mistakes reduced users’ confidence in the effectiveness
of the model overall. Indeed, 29% of participants either described not wanting to use the model, or
being hesitant to use the model until performance improved. Some participants also found that the
model surfaced too many potentially risky disclosures. Prior work in usable privacy has shown that
warnings can have a “crying wolf” effect — i.e., habituation [ 68] — where users react less strongly
to warnings with each subsequent exposure. Taken altogether, it would seem prudent for future
work to explore better ways of handling model inaccuracies for disclosure detection tools.
We envision two such approaches worthy of future investigation. First, researchers may want to
explore other ways of presenting detected disclosure spans that lean further into the concept of
self-reflection: i.e., users may be more willing to tolerate inaccuracies if detected disclosure spans
are presented as suggestions for reflection rather than as definitive problems. Second, given the
strong negative impact of mistaken outputs future self-disclosure detection tools may only want to
surface high-confidence decisions, so as not to break trust with users. Future work can explore the
appropriate confidence threshold, which may be variable by user, by disclosure category, and by
threat model (e.g., users may be more willing to accept low confidence outputs when they feel in
more immediate danger by a stalker or abusive ex-partner).
Concretizing Risk with Fine-Grained Explanations. Participants expressed a preference for the
categorical disclosure model outputs over the binary disclosure model outputs because the category
labels gave them a sense of why the model flagged a span as a potentially risky disclosure. The
category labels, thus, served as a “coarse” explanation. Future iterations of the model should explore
more fine-grained explanations that help users understand and contextualize risk. These fine-
grained explanations may include, for example, estimates of k-anonymity loss, worst-case scenarios
for how these disclosures could be used against users, or even a threat severity ranking for a given
disclosure (each of which was requested in future iterations of the model by participants). All of
these explanations might help concretize the otherwise abstract risks of online self-disclosure.
Generative Models to Help Users De-Risk Disclosures. Another idea worth exploring in future work
is to provide users with suggestions on how to rephrase detected disclosures in a manner that
preserves semantic meaning but de-risks the disclosure. A naive approach would be to fine-tune or
prompt-engineer a transformer-based model (e.g., an API-based model like ChatGPT [ 34] or an
open-source model like LLaMa-2 [ 85]) to take an input span of text — and the surrounding post
context — and generate suggested rephrasings of the text span that reduce disclosure risk. Future
work should explore the relative costs and benefits of this naive approach versus a more involved
4Reddit announced the development of a post-guidance feature as part of their efforts to support moderators in sharing and
enforcing “community guidelines. ” This was noted in a post in rmodnews, an official community dedicated to announcements
from Reddit, Inc. pertaining to moderation: https://www.reddit.com/r/modnews/comments/1cnacle/new_tools_to_help_
mods_educate_and_inform/
20... Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway
approach in which the fine-tuned model more formally optimizes for an operationalized definition
of privacy (e.g., k-anonymity loss) when generating suggested rephrasings.
Several participants also expressed a desire for suggested rephrasings to be personalized to their
posting history. For example, some participants wanted the model to “learn” what they do and don’t
tend to disclose, providing suggestions based on these tendencies. Others described a desire for
the suggestions and risks to be presented in the context of past disclosures that users made on the
platform (e.g., “Because you disclosed your age in a past post, sharing your location and occupation
in this one will decrease your anonymity by x%”). Further exploration of these features could also
contribute to reduced cognitive load, and minimize aforementioned habituation effects raised by
prior literature which are more common for generic and non-personalized warnings [103].
Accounting for posting context. A core insight from our study is that it is critically important for
disclosure detection models to account for posting context and the disclosure norms therein. The
third most common reason for users’ rejection of a detected disclosure was that the model failed to
account for the context in which a detected disclosure span was being posted.
One way the model failed to account for context was by neglecting the subreddit in which a
disclosure was being made. Disclosing one’s location in a subreddit about that location was one
common example — there is little point in hiding that one is in or from Texas when posting in a
subreddit about Texas. A second way the model failed to account for context was by neglecting
disclosure norms. In some subreddits, norms and guidelines necessitate certain disclosures (e.g., age
and gender). Disclosing this information is still risky, but participants mentioned that the model
should at least account for this requirement and suggest alternative mitigation strategies (e.g.,
perturbing one’s age within plausible bounds).
Responding to natural language instructions and feedback. Participants brought up a number
of idiosyncratic weaknesses in the model outputs. For example, participants mentioned that the
model failed to account for user’s own privacy mitigation strategies (e.g., perturbing personal
information in their posts), had difficulty distinguishing between hypothetical and real situations,
missed some categories of disclosure that participants felt were important, and over-highlighted
some disclosures that participants felt were not risky for their particular situation. Addressing each
of these weaknesses systematically at the model level would be difficult, but future work might
explore the creation of instructable, transformer-based language models that can alter their behavior
based on user-specified feedback and instructions (e.g., “please don’t surface disclosures related to
age”, or “this is a hypothetical situation that is not related to my personal information”). Allowing
for this sort of feedback may help reduce user frustration with model inaccuracies, especially if
future models provide fine-grained explanations. Prior work has found that user frustration can
increase when explanations are provided without giving users the ability to correct the model in
cases of disagreement [78].
7 LIMITATIONS
7.1 Model & Study Design
The disclosure spans detected by the binary and categorical disclosure variants of the model we
used as a technology probe did not surface the exact same disclosure spans, reducing our ability to
make direct comparisons between the two. We also did not counterbalance the appearance of the
models — users were always presented with the binary disclosure version of the model first. Thus
reactions to the models may be subject to order effects. As such, we avoided making any direct
statistical comparisons between the two models, instead opting to focus on why users preferred
one model’s outputs over the other from their interview responses. Future work comparing the
21Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway Krsek, et al.
two versions of the model — or alternatives with even finer-grained explanations — might consider
a between-subjects study design to eliminate concerns over priming and order effects. Due to the
length of the interviews (1.5 hours) and the sheer number of disclosure spans users were being
asked to assess, it was challenging to get the in-depth rationale for users’ decisions behind their four
ranks of each disclosure span while attempting to avoid over-fatigue on behalf of the participants.
We also note that though we did probe users on their motivations for making posts, we did not
observe any trends affecting users’ assessments of model outcomes – though this could be due to
the complexity of balancing the utility and needs for sharing with the risks. Future work could
contribute a dedicated exploration of users’ rationale for editing versus not editing disclosures that
they agreed contained disclosure risks, as well as how their posting motivation might influence
their perception of the model outcomes.
Relatedly, it is also important to note that users have differing threat models [ 33,72,95,100] that
may not align with the outputs of the model, and an important challenge exists in exploring how
to best tailor the outputs of the model to meet users needs. That said, we believe this tool can still
be particularly helpful for at-risk users (e.g. those seeking support in leaving abusive situations,
reporting violations by companies, etc.)
7.2 Recruiting & Sample Representation
The gender demographics of our exploratory user study are significantly skewed toward people
who identify as women. This gender distribution is not representative of the general population, nor
is it representative of Reddit user gender statistics [ 53]. Prior literature has well-established gender
differences in privacy perceptions and behaviors [ 41], and as such our results may not be widely
generalizable. Our participant demographics are also skewed white, with a majority of participants
below the age of 50, though these skews are more representative of Reddit demographics [ 53].
Furthermore, our sample was conducted solely with participants residing in the United States.
Though we attempted to recruit participants from the Reddit platform, we ultimately were only
able to recruit participants from Prolific. Because we had used a newly created lab account to make
recruitment posts, our posts were removed as our account “did not have enough karma”. “Karma”
is a form of social credit that is built on Reddit through commenting on others’ posts, receiving
upvotes, and awards; it is used to maintain the contribution quality of content posted to the site.
While all interviewees were verified Reddit users, it’s possible that we introduced additional biases
into our sample as crowd-sourced participants are accustomed to participating and volunteering
in research, and on the whole tend to be more tech-savvy than the general population [ 63,71].
Moreover, it’s possible that those who responded to our recruitment call were more comfortable
with sharing content that included personal disclosures online than others. Finally, our work
is highly specific to the Reddit context and, as such, our findings may not generalize to other
pseudonymous or partially pseudonymous online fora (e.g., X, Mastodon).
8 CONCLUSIONS
When posting personal information in pseudonymous online fora, like Reddit, it is difficult for users
to balance the tangible benefits of self-disclosure (e.g., providing context when seeking support)
with its comparatively abstract risks (e.g., de-anonymization by institutions or third parties). Prior
work has explored the use of NLP-based self-disclosure identification tools to help users make more
informed decisions by surfacing explicit disclosure risks in the content they plan to share online
[14,37,57]. Building on this line of work, we contribute the first comprehensive evaluation of these
tools with the users they aim to protect. Through an in-depth interview study with 21 Reddit users,
using a state-of-the-art self-disclosure detection model as a technology probe [ 27], we explore if
and how these models might be useful and usable beyond their F 1scores. Our findings suggest
22... Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway
that many users find value in NLP-powered self-disclosure detection tools, particularly in their
ability to facilitate self-reflection. We also show that these models are especially effective when
they provide users with context to interpret why detected disclosures might be risky. However,
we also identified many shortcomings in these models that must be addressed to make them more
useful and usable: for example, accounting for posting context, disclosure norms, and users’ lived
threat models. Though modern advances in AI pose many thorny privacy risks for users [ 23,51],
our work shows one way these advances may be utilized to help users protect their privacy online.
ACKNOWLEDGMENTS
This work was generously funded, in part, by the National Science Foundation under grants CNS-
2316287, IIS-2144493, and IIS-2052498. We would also like to thank our anonymous reviewers for
their helpful comments in revising this paper.