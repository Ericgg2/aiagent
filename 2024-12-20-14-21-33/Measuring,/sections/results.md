To answer RQ1, our findings indicate that users found value in using our model to detect self-
disclosure risks, with the majority (17/21) expressing a desire to use it outside of the study or
recommend it to others. In particular, users appreciated the self-reflection the model encouraged,
finding value in its ability to: (i) catch risky disclosures they were previously unaware of or missed
in the process of writing, (ii) broaden their conception of risky disclosure, and (iii) help them come
to a decision on information they were unsure about disclosing. However, we also found that users
required support in navigating how to rephrase and de-risk the content that they wrote in a manner
that preserved the semantic meaning of their original post. To answer RQ2, our results suggest
that the granularity of information offered alongside text that the model detected as risky may
have had an impact on users’ acceptance of disclosure detection spans (the text that the models
determined may contain self-disclosure risks). Users described the categorical disclosure version of
the model’s category labels as helping them understand why a disclosure span was detected as a
privacy risk. Finally, to answer RQ3, our results indicate that participants found the model least
useful when its outputs failed to account for their own risk mitigation strategies (e.g., hypothetical
situations, intentional lies users made to preserve their anonymity), conflicted with the disclosure
norms and requirements of their posting context, and surfaced risks that were misaligned with
the threat models they most cared about. We also highlight categories of risky disclosure that the
model failed to capture, but which participants felt were important to detect.
Descriptive Statistics on Users’ Reactions to the Self-Disclosure Detection Spans Surfaced by the
Model. Among the 851 total self-disclosure spans that the model detected across all our participants,
participants accepted 58% (495 total) as containing risky self-disclosures, and rejected the other
41.8% (356 total) (see Table 3). In response to seeing the detected disclosures, about 15% (127/851)
of all disclosure spans were ultimately altered by participants, while 3.5% (30/851) left participants
undecided on what to do; the remaining 81.5% (694/851) were not altered by participants.
When only looking at the disclosure spans that were accepted by users (495), the alteration rate
of disclosure spans was only slightly higher (114/495 = 23%), with the majority still deciding not to
alter the disclosure span (357/495 = 72%); participants were unsure whether or how they would
alter the remaining accepted disclosure spans (23/495 = 5%).
To explore whether participants’ decisions to alter the content of detected disclosure spans were
influenced by mistakes made by the model, we further examined the 72% of non-altered disclosure
spans that participants accepted as containing self-disclosures (357). For these detected disclosures,
12... Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway
we calculated the rates at which participants reported different mistakes by the models. We found
that very few of the non-altered disclosure spans were reported to have contained mistakes made by
the model (10/357 = 3.2%). Only about 7 (7/357 = 2.2%) were identified by participants as misaligned
with users’ preferences for what to disclose, while only 3 (3/357 = 1%) had mistakes pertaining to
post-context (e.g., the model flagging disclosures that users were required to share per subreddit
rules). The majority of non-altered but accepted disclosure spans contained no explicit mistakes
identified by users (305/357 = 85%).
Rather, participants’ decisions to alter text seemed related to their perceptions of the disclosure
span’s helpfulness, importance, and perceived riskiness. While there is debate over how to analyze
Likert scale data, past work in statistics has shown that two-sample t-tests and Mann-Whitney U
tests produce nearly equal false-positive rates when performed on Likert scale data [ 25], and are
close in significance level target. Given this reported equivalence we conducted a Welch’s t-test in
order to examine whether the medians of the altered (114) and non-altered (357) disclosure spans
that participants agreed with (495) differed significantly across scores of helpfulness, importance,
sensitivity, and riskiness (as it accounts for unequal variances, and is considered to be more
conservative than student t-tests and Mann-Whitney U [ 29]); we found significant differences
across all four scales (see Table 2).2
From our tests, we found that the content of non-altered disclosure spans was perceived as
more “important” to include for the context of the participant’s post than that of altered spans
(t(155)=7.244, p < 0.0001, Cohen’s d = -0.4545076). In contrast, the content of altered spans was
considered more “sensitive” (Welch’s: (t(182)=8.928, p < 0.0001, Cohen’s d = 0.5217734))) and “risky”
by participants (t(168)=8.7505, p < 0.0001, Cohen’s d = 0.5287747) than that of non-altered spans.
Unsurprisingly, therefore, the model highlights for altered spans were perceived as being more
“helpful” (t(201)=6.9965, p < 0.0001, Cohen’s d = 0.2475993) than the highlights for unaltered spans.
We use the subsection on RQ3 below to extend our discussion of the reasons participants gave for
rejecting disclosure spans output by the model.
5.1 RQ1: How Interaction with an NLP Model Can Benefit Users’ Awareness of Risky
Self-Disclosures and Mitigation Behaviors
While the model was clearly imperfect, when reflecting on their overall opinion of the tool, partici-
pants’ reactions to the model were largely positive: The vast majority of participants (17/21) either
expressed that they would want to use it personally when making online posts (14/21), or that they
would want to recommend its use to others they know 2/21. That latter group felt like they already
had appropriate strategies for mitigating self-disclosure risks in their posts without the model, but
suggested it might be especially useful for users with less experience in mitigating disclosure risks
online. P19, for example, recounted: “I don’t know that I necessarily need it. I do think it’d be a
good idea for like tweens and teens, like people who are new to the internet. Just kind of give them
an idea of stuff that they really shouldn’t be sharing.”
Users perceived several benefits from their interaction with the model, with most describing its
value as a tool for reflection (12/21), even for circumstances where the model’s outputs made little
sense in isolation. Participant’s responses revealed that a core value of the model lay in its potential
for catching mistakes and double-checking one’s writing for potential privacy risks: “What it
grabs prompts you to think more thoroughly about whether you actually want to include that
information, and whether that information could be used to identify you. Specifically, in terms of
2As a robustness check, we also performed a Mann-Whitney U test, another non-parametric test of statistical difference
often used on Likert data and obtained the same results. Conducting both tests in assessing Likerts is understood to be
helpful in cementing confidence in purported significance levels [25]. See Appendix Section A.5 for a full analysis.
13Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway Krsek, et al.
SUMMARY STATISTICS FOR ACCEPTED SELF-DISCLOSURE SPANS OUTPUT BY THE MODELS
Accepted Altered Disclosure Spans
(114)Accepted Non-Altered Disclosure Spans
(357)Welch’s T-Test Results
M SD M SD p-value Cohen’s d
Helpfulness 4.14 1.24 3.15 1.44 1.52702e-10*** 0.24
Importance 2.58 1.53 3.74 1.25 7.728284e-11*** 0.45
Sensitivity 3.95 1.36 2.62 1.39 1.884628e-15*** 0.52
Riskiness 3.61 1.47 2.22 1.35 8.741327e-15*** 0.52
Table 2. Welch T-test results for disclosure spans accepted by participants to explain nuances in when
participants altered and did not alter their posts in response to seeing the model outputs. The outcomes of the
test show significant differences in the median scores of disclosure spans between those accepted and altered
compared to those accepted but not altered by participants across helpfulness, importance, sensitivity, and
riskiness. P-values for both tests have been adjusted for multiple-hypothesis testing.
Helpfulness, Importance, Sensitivity, and Riskiness all range from 1 (“Not at all...”) to 5 (“Very...”)
*p<0.05, ** p<0.01, *** p<0.001
M = Mean, SD = Standard Deviation
r/AmItheAsshole3posts — the number of times I’ve seen people edit their post with ’so and so
found it’...” (P8)
Other participants mentioned the utility of the model as a “tie-breaker” when deciding whether
or not to disclose specific information, as evidenced by the following reflection from P20: “it would
help me make the decision of ‘do I want to take this out, or change it, or is it fine’...”.
Finally, other participants mentioned the model’s potential to challenge and subsequently expand
users’ conception of what constitutes a risky self-disclosure: “It catches very detailed things that
people may write that they may not even think about as being risky, like things about location that
people reveal not even realizing that they’re revealing it sometimes. Sometimes we’re not even
realizing it could be risky.” (P5)
5.2 RQ2: The Impact of Classification Granularity
To assess how the granularity of classification labels might impact the utility of the disclosure
detection spans from the model to users, we also assessed the differences in users’ reactions to a
binary disclosure model (where text spans are classified as risky self-disclosures or not) versus as a
categorical disclosure model (where these spans were also labeled with a category describing the
kind of sensitive disclosure made).
Overall, we found that higher-granularity classifications resulted in greater user acceptance of
model outputs: outputs from the binary disclosure model were rejected (54%) more often than they
were accepted (46%), while outputs from the categorical disclosure model were accepted (65%) more
often than they were rejected (35%).
However, greater acceptance of disclosure spans did not necessarily result in markedly different
disclosure behaviors. We define the “alteration rate” of a model as the number of detected disclosures
that users decided to alter, divided by the total number of disclosures detected by that model. The
alteration rates for both the categorical disclosure (91/557 = 16.4%) and binary disclosure (36/289 =
12.5%) models were both similar ( 𝜒2(1, 𝑁=846)=1.9, 𝑝=0.16) and low overall. Note, however,
3r/AmItheAsshole is a subreddit that Reddit users post to in order to get outside perspective on conflicts they’ve experienced,
and whether the way that the author handled that conflict was justified.
14... Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway
BARPLOT OF ACCEPTED VS. REJECTED DISCLOSURE DETECTION SPANS, BY MODEL TYPE
Fig. 5. A horizontal bar graph depicting the percentage of disclosure detection spans that participants
accepted vs. rejected as containing self-disclosure risks, by model type. The percentage of disclosure spans
that were accepted output from the binary disclosure version of the model (46%) was lower than those
accepted (54%). Compared to the binary disclosure version, we see that for the categorical disclosure version
of the model disclosure spans were accepted more often, with the majority of participants (65%) agreeing
they contained self-disclosure risks.
that the detected disclosures identified by the binary disclosure model and the categorical disclosure
model were not always the same, so we cannot make direct comparisons at the text-span level
between the models.
Higher-granularity labels in the categorical disclosure model helped participants (10/21) recognize
the disclosure risks of a detected text span. The presence of these categories helped surface why
a span of text was detected by the model, which was instructive in situations where participants
may have not been aware of a specific type of risk. As P21 stated, “I would have never thought
that would have been...identifiable information...but gender is...I mean, obviously with outliers, but
there’s the binary of gender in terms of sex of birth which you’ve now basically taken off the table. ”
The average “helpfulness” and “riskiness” scores that participants assigned to detected spans also
differed slightly between the two models. Recall that participants were asked to rate the perceived
helpfulness and riskiness of each detected span on a 5-point Likert scale (ranging from “not at all... ”
to “Very...”). The detected spans of the categorical disclosure model were, on average, perceived
as “slightly helpful”/“helpful” and “slightly risky”. In contrast, the detected spans of the binary
disclosure model were perceived as “slightly helpful”, but “not at all” risky. P19 discussed how
the higher granularity of the categorical disclosure model outputs may have contributed to the
improved perceptions of helpfulness and agreement of risk: “I think that [the categories] would be
very helpful...it might not be obvious why something is considered a disclosure. Like, why would
they highlight this? What? What’s revealing about this, and maybe having the category would be
like that? Oh, yeah, I guess I see the point.” In this way, the categorical disclosure labels can be
seen as a kind of “coarse” explanation for model outputs.
Relatedly, the majority of users expressed a desire for more granular explanations for model
outputs (16/21). Participants wanted explanations that spoke to why a detected disclosure was
considered a risk, how sensitive or risky was the detected disclosure, and worst-case scenarios or
examples of how the information in the detected disclosure could be used to harm them. Participants
15Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway Krsek, et al.
also expressed a desire for feedback on how to modify the detected disclosure to reduce risk while
retaining enough context for their desired audience to understand their posts.
Participants discussed wanting the model to take their history of disclosures across posts into
consideration when detecting and explaining potential risks (6/21). As P14 stated: “It might be also
important to point out like ‘combined with other information in your posts plus other information
that may be in your profile on previous posts, this sort of thing may be identifiable!”’ (P14). P20
also expressed a desire to contextualize model outputs based on how other users have historically
responded to similar outputs: “It could tell me like statistics about other users and like tell me what
other people decided based on the information that it like gathered for them. Maybe that would
help me make the decision of do I want to take this out or change it or it’s fine” (P20).
SUMMARY OF MODEL DISCLOSURE SPAN DETECTION ISSUES
Disclosure Detection Span Issues Accepted Spans ( 495, 58% ) Rejected Spans ( 356, 41.8% )Total Occurrences ( 868)
Didn’t Make Sense 1 (0.2%) 115 (30.8%) 116 (13.4%)
Missing Context 5 (1%) 28 (7.5%) 33 (3.8%)
Misaligned with User Preference 8 (1.6%) 152 (40.8%) 160 (18.4%)
** Incorrect Category Tag 33 (6.7%) 46 (12.3%) 79 (9.1%)
** Needs Multiple Category Tags 2 (0.4%) 0 2 (0.2%)
Other (under/over-detected) 19 (3.8%) 9 (2.5%) 28 (3.3%)
Table 3. This table summarizes the frequency of issues with disclosure detection spans that were reported by
participants in our interviews. The disclosure detection spans are separated by whether they were ultimately
accepted (495, 58%) or rejected (356, 41.8%) by participants as containing self-disclosures. The remaining
486 (57.1%) of tags that contained no mistakes are not listed in this table. The most common issues among
rejected tags were that they misaligned with users’ understanding of sensitive information (40.8%), and/or
were identified as being nonsensical (30.8%). While incorrect categorization was also an issue (affecting 9.1%
of all disclosure spans), it did not always lead to the rejection of a disclosure span (6.7% were accepted). Note:
Because there were overlaps in issues, the numbers for individual issues are greater than the number of
tags (851). The total rates of accepted versus rejected highlights are adjusted based on this, while the total
percentages of each mistake are based on a total number of occurrences (868).
**These issues are only relevant to the multi-class version of the model since the binary version did not
contain disclosure categories.
5.3 RQ3: Where AI-powered Disclosure Detection Tools Can Fall Short And Be
Improved
We next analyzed our data to identify where participants felt our models fell short in order to identify
opportunities for improvement. Our results surfaced many ways that automated disclosure detection
tools — like the models we developed in this work — could be adjusted to better accommodate
users’ needs.
Misalignment of risk conception. One of the most common reasons users rejected model outputs
was that participants disagreed that a disclosure detected by the model was actually risky (see Table
3), and didn’t mind disclosing that information resulting in a misalignment with user preference.
This preference misalignment was the most common reason for rejection among nine of the
seventeen disclosure categories detected by our model: i.e., “relationship status”, “pet”, “finance”,
16... Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway
“age”, “occupation”, “education”, “appearance”, “husband/BF”, and “wife/GF” (see Table C in Appendix
for the full summary of acceptance and rejection rates by category).
For some detected disclosures, participants believed that the flagged disclosure could not actually
be used to narrow down their identity to the extent that they could be re-identified: “Okay, the
next [disclosure span], ‘I’ve been happily monogamously remarried. Now just had our 15-year
anniversary.’ I don’t think that’s identifiable at all. I think you know, lots of people have been
married for 15 years. And nobody could really identify me from that specific information.” (P7) This
quote reaffirms the need for more granular explanations — absent these explanations, users may fill
the void with their own conception of attack possibilities which may not be fully representative of
all possibilities. In this case, for example, while there may be many couples who have been married
for 15 years (the absolute risk remains small), the number of people who were married exactly
15 years ago is much smaller than the number of, e.g., Reddit users as a whole (the relative risk
is high). Combined with other identifying disclosures, the risk of re-identification may be higher
than expected.
Yet, it is also important to not be overly prescriptive and to allow participants to exercise
their own judgment. Even if there is an objective increase in risk and it is communicated well,
sometimes participants viewed said risk as a necessary cost to communicate intent. As P4 states:
“I’m comfortable with what I’ve shared in the past and what I intend on sharing in the future...it
adds value to my post, but in a way that doesn’t personally identify me by any past nor any future
posts that I intend to make.” Any tool that aims to help users account for disclosure risks should
allow users to make informed decisions — not try to prevent users from taking any risks.
Missing disclosure categories. Participants also pointed out several kinds of disclosures that the
model overlooked. Disclosures about illegal or abusive activities — such as harassment and substance
abuse — was one such category. In cases of harassment, for example, participants were worried that
being too specific could open them up to re-identification by a perpetrator they were discussing.
Referring to a post in which they were describing a situation with an estranged family member, P6
stated: “I’ve been trying to keep my distance from him as much as possible and this seems like an
invitation for him to go on a big rant defending himself, so I wouldn’t want him to find it either...He
would probably just try everything he could to contact me...and I already have him blocked on
everything personal so he’d probably just message me a lot on this Reddit account and I might be
tempted to just delete the account, or prevent him from contacting me forever.”
Participants also mentioned the importance of detecting disclosures related to addiction and
substance use . When discussing others’ addictions — e.g., in the case of a user seeking advice on how
to help their spouse — a primary concern was that the subject of the post might identify themselves
if descriptions were too specific. On the other hand, when describing one’s own addictions or
substance-use habits, participants were more concerned that personal connections who knew of
their account(s) might see this information attached to their profile via their posting history.
Ancestry and ethnicity also came up as a category for disclosure detection models to identify. For
example, one participant made a detailed post asking about a small town where her parent was born.
They mentioned wanting this detected as a disclosure risk to protect themselves or others they
discuss in their posts from further unwanted or unanticipated connections with past relationships:
“So somebody who had grown up there or had family who grew up there might know my family
and be interested in more identifying information...it might be someone my dad doesn’t like, and
they might try to track him down and bother him further.” (P19) They also mentioned concerns
over other internet users reacting negatively when discussions around ethnicity arise: “people do
tend to get upset when ethnicity comes up. Discussions get heated...”
17Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway Krsek, et al.
Temporal and situational details about specific events (e.g. graduations, birthday parties), dates
and times, instances of conflict (e.g., arguments about specific events), as well as direct quotes (from
text messages, emails, or conversations on other platforms) were all also considered to be important
categories of disclosures for the model to identify. These details can add a level of specificity to
posts that made participants believe that any individuals involved in those events would easily be
able to re-identify the post’s author using those details.
In sum, these missing categories, and participants’ rationales for their inclusion, underscore
the need for disclosure detection models to account for participants’ lived threat models — some
disclosures may be more risky for interpersonal threats (e.g., friends and relations learning personal
information that the participant would rather keep private), others for third-party threats (e.g.,
strangers using disclosures to doxx an individual), and still others for institutional threats (e.g., law
enforcement inferring illicit or illegal activities).
Accounting for disclosure norms and posting context. The third most common reason participants
rejected model outputs — accounting for about 7.5% of all rejections (see Table 3) — was that
the model failed to consider posting context. Several participants discussed situations where the
detected disclosures were rendered irrelevant in light of the norms within the subreddit they were
making the post: a common example was participants seeing location disclosures flagged when
posting in a subreddit specifically about that location (e.g. “my car was stolen from Tacoma, WA”
in r/Tacoma). Another example was detecting a disclosure about a poster’s medical condition
in a subreddit explicitly about that condition (e.g., sharing that one has Cushing’s syndrome in
r/Cushings). In other circumstances, certain personal disclosures were required by the subreddit’s
community guidelines, as was the case for P1 who had to disclose the name and age of her pet
when posting to a subreddit about mourning family pets.
Distinguishing between factual and non-factual disclosures. Our results also surfaced the impor-
tance of distinguishing between disclosures that were factual (e.g., about real people and situations)
versus those that were not (e.g., when users intentionally perturbed identifying information, dis-
cussed hypotheticals, or discussed fictional characters). P10 shared: “I mentioned...’suppose I had
an office visit with a doctor’...it was clear that it wasn’t even a real office visit, it was a hypothetical
office visit to set the stage for the question to follow.” This misunderstanding extended to other situ-
ations as well, such as when participants posted about games they were playing, with discussions of
fictional characters being flagged with self-disclosure risks (e.g., the “occupation” of this character).
Participants also described lying about details such as gender and age in their posts as a tactic
for privacy risk management; in these cases, the model failed to account for these strategies and
detected disclosure risks that participants already mitigated. P10 later reflected that this failure to
distinguish between factual and non-factual disclosures was the model’s most significant drawback:
“The biggest downside for these tools is that they’re dumb. No awareness of context, no awareness
of what I was actually trying to do in this post.”
Classification accuracy. Model accuracy was an overarching concern that often led to users’
rejecting detected disclosures — disclosure spans that did not make sense and erroneous category
labels were the second most common reason users rejected model outputs (30.8%) (see Table 3).
Many erroneous disclosure spans, for example, consisted of one-off words such as “the”, “I”, or
“him”. Other errors included disclosures being mislabeled with the wrong class. We note, however,
that among the 79 disclosures that were mislabeled with the wrong class, participants accepted
42% of them (see Table 3, “Incorrect Category Tag” row). It is possible that even when the detected
disclosure was mislabeled, it may have still brought users’ attention to potentially risky disclosures
that participants felt important to reconsider.
18... Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway
Calibrating detection frequency. Finally, over-detecting and under-detecting was also an issue
for a minority (4/21) of participants, accounting for about 3.3% (28/851) of all model outputs (see
Table 3). In the over-detecting case, these participants expressed frustration that the model surfaced
text that was irrelevant to what participants identified as the disclosure, suggesting the disclosure
spans be cut down the keywords that needed to be altered to improve the preservation of their
anonymity (e.g. “with her daughter in the back seat” should be cut down to “her daughter”). For
under-detected passages, this occurred when participants considered them in the context of the
sentence rather than in isolation. However, when discussing their overall outlook on the model,
these issues did not always result in detected disclosures being rejected by participants — only
about 2.5% (9/356) of detected disclosures that were considered redundant were ultimately rejected
by participants (see Table 3).