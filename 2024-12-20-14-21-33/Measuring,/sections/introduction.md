Every day, millions of people log onto pseudonymous online fora like Reddit to access a seemingly
safe space to vent, seek support, and connect with like-minded others without the additional
baggage of their offline identity. Unsurprisingly, prior work has also found that users in these
pseudonymous fora are more likely to disclose highly sensitive information [ 98]. While the benefits
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee
provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the
full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored.
Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires
prior specific permission and/or a fee. Request permissions from permissions@acm.org.
Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway
©2024 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 978-1-4503-XXXX-X/18/06
https://doi.org/XXXXXXX.XXXXXXX
1arXiv:2412.15047v1  [cs.HC]  19 Dec 2024Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway Krsek, et al.
Fig. 1. AI-powered, span-level self-disclosure detection helps users in reviewing their posts to improve privacy.
of these self-disclosures are apparent to users, the potential harms are more abstract and difficult
to reason about. This asymmetry can lead to uninformed sharing that can result in regrets [ 76,93],
self-censorship [ 22,77], and/or risks of de-anonymization [ 3,67,79]. As such, a defining dilemma
of modern social networking is helping users balance the social benefits they reap through online
self-disclosure with the privacy risks associated with those disclosures.
Recent work [ 4,14,37,57,104] has explored the use of natural language processing (NLP)
tools to help users identify potentially risky self-disclosures. However, to date, these tools have
not been evaluated with the actual users that they aim to protect. Rather, most of this work has
focused on improving model performance in detecting personal disclosures against benchmarks and
accuracy metrics that cannot be confidently correlated with what users want [ 14,37,57]. Without
considering user intentions, needs, and contexts of use, NLP-powered disclosure detection tools run
the risk of running headlong into Ackerman’s social-technical gap [ 1]: i.e., the gap between what is
possible technically and what is necessary socially. Users often disclose personal information online
intentionally: e.g., when seeking emotional or informational support [ 24,70,101], and to build
relationships [ 24,47]. A disclosure-detection tool that fails to consider why users are disclosing
personal information, and what threats they’re most concerned about in sharing that information,
may fall short of helping users make informed decisions.
Driven by this hypothesis, we ask: How can NLP-based disclosure detection tools be designed to
help users make informed decisions about online self-disclosures? Taking cues from prior work in
the domain of usable security & privacy, we formulate three sub-questions to better understand
how users perceive the outputs of existing models, and how they might be improved:
•RQ1: Given the tension between the need for self-disclosure and the risks, how can interaction
with an NLP model make users aware of potential self-disclosure risks? [2, 43]
•RQ2: How should the feedback from the NLP model be framed? What level of textual granu-
larity is helpful in communicating the abstract risks of users’ disclosures? [12, 92]
•RQ3: Where do NLP self-disclosure detection models fall short, and how might they be further
improved to better align with users’ preferences? [21, 46, 81]
Guided by these RQs, we conducted an in-depth interview study with 21 Reddit users. We had our
participants use a state-of-the-art NLP-based disclosure detection model from prior work by Dou
et al. [27] on two self-authored posts made on and for Reddit. We chose this model because, unlike
other similar models that operate at the post or sentence level [ 17,88], Dou et al.’s model operates
at the text-span level: i.e., it is capable of identifying specific segments of text in a broader post
that constitutes a potentially risky self-disclosure (see Fig.1). This higher-level of granularity let us
localize user feedback to the specific words in their posts that the model estimated as constituting
2... Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway
disclosure risk. Moreover, the model has two versions: a multi-class version (which we refer to as
thecategorical disclosure model ) which is capable of detecting 19 different self-disclosure categories
(see Table 1), and a binary version that flags content as self-disclosures or not (which we refer to as
thebinary disclosure model ). To answer our RQs, we asked users questions about how they viewed
and accepted the model’s outputs for their posts (RQ1), differences in perceptions of model utility
between the categorical and binary versions of the model (RQ2), and — when users rejected model
outputs — why they rejected the outputs and where they felt the model failed more broadly (RQ3).
While the model was imperfect at identifying self-disclosures (with users accepting 58% of all
detected disclosures overall), the majority of participants reacted positively to the model. 82% of
our participants stated that they wanted to use the model outside of the study or would recommend
it to others. Participants described the model’s utility as encouraging self-reflection, catching users’
mistakes, raising risks they were previously unaware of, and in making decisions about content
users were uncertain of sharing. However even when agreeing with the model’s output, participants
generally did not act to alter the disclosure detection spans the model identified (15% of all detected
disclosure spans were altered). Participants rated detected disclosures that they did not alter as
being especially important to convey meaning. Conversely, participants rated detected disclosures
that they did alter as being especially risky. In short, our results suggest that model outputs — even
if imperfect — can help participants make informed decisions: sometimes the risk is warranted,
while other times it is not.
We also found that participants preferred the more granular outputs of the categorical disclosure
model, as the category labels added clarity to why the model detected some disclosures as risky.
Category labels served as a kind of “coarse” explanation, which participants appreciated. Participants
expressed a desire for additional explanation, such as threat severity rankings, worst-case scenarios
for how disclosures could be used against users, as well as suggested rephrasings that reduce
disclosure risk while retaining the semantic context required for a user’s audience.
Finally, our results indicate many opportunities for future improvements to such models. For
example, participants expressed a need for models to understand posting context and disclosure
norms (e.g., disclosures about a specific location may be less relevant when posting to a subreddit
about that location), to differentiate between factual and non-factual disclosures (e.g., hypotheticals),
to account for users’ existing privacy management strategies (e.g., perturbing their age, gender,
and location when sharing content), and to customize outputs to relevant threat models (e.g.,
some information may be more exploitable by a stalker than an institution and vice versa). Our
findings also surface additional forms of self-disclosure that users found important to detect such
as disclosures regarding illegal or abusive activities, substance addiction, and situational details
(e.g., dates, times, specific events).
In summary, this paper makes the following novel research contributions:
•An examination of how a self-disclosure detection NLP model can raise users’ awareness of
potential re-identification risks that stem from what they post online in pseudonymous fora.
•An analysis of how to present model outputs to users to appropriately convey risk in a
manner that allows users to make informed decisions about how to weigh the benefits and
risks of disclosure when seeking informational and/or emotional support.
•Design considerations for researchers and practitioners exploring the use of NLP-powered
disclosure detection tools in reducing self-disclosure-based privacy risks.
3Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway Krsek, et al.