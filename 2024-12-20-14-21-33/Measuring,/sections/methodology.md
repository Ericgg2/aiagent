To explore how AI-assisted identification of self-disclosure spans might impact users’ awareness
of self-disclosure risks and their writing behaviors, we conducted a 75-minute interview study
with 21 Reddit users. We asked participants to share two of their self-authored Reddit posts with
researchers which were subsequently run through our NLP model. We then asked participants
questions, using the NLP model outputs as a guide, to determine how the model affected users’
awareness of potential self-disclosure risks (RQ1), how feedback from the model should be framed
to maximize utility to participants (RQ2), and where these tools might be altered to better align
with users’ preferences (RQ3).
1https://microsoft.github.io/presidio/
8... Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway
4.1 Recruitment
We recruited a total of 21 Reddit users through Prolific, an on-demand participant recruitment
platform. Participants were screened to ensure that they: had a Reddit account at the time of the
study, made at least three posts on Reddit, resided in the U.S., and were 18 years of age or older.
Eligible participants were subsequently asked to provide links to two text-based Reddit posts they
had made; one with which they had privacy concerns and another with which they did not. From
about 158 who took the pre-study survey, we invited 33 Reddit users to participate in the interview
based on the Reddit posts they shared with which they had privacy concerns. Participants were
only invited to participate after researchers ensured their shared posts were majority text-based,
and contained personal disclosures, and after ensuring that the model we used was able to detect
potentially identifying disclosures in the post. More specifically, participants were filtered out of
the study if the posts that they shared were inaccessible, removed, contained no text (e.g. only an
image), or if they reported not having made a post that meets those criteria (e.g., if they answered
with “N/A” or “I have not done this” when asked to share a Reddit post they drafted over which
they had privacy concerns). While we did reach out to participants who shared invalid links, none
of them responded to our request for an alternative post. From the total 158 users who took the
pre-study survey, we invited 33 Reddit users to participate in the interview based on the Reddit
posts they shared with which they had privacy concerns. Of those 33 participants, 21 followed
up on our request to schedule interviews. Given the average sample size for studies within the
CHI community is 12 participants [ 13], and the rich body of work demonstrating that anywhere
between 6-12 participants is enough for high saturation [ 32,38–40,56,60], we did not run any
additional recruitment attempts.
The collected demographic data is displayed in the Appendix (see Table A in section A). The
sample was slightly skewed female, with 12 participants identifying as female. 16 of the 21 partici-
pants were below the age of 50, and 15 participants held a bachelor’s degree or higher certificate of
education. Data collection occurred in the summer of 2023, and participants received $17 compen-
sation for their participation in the interview and pre-study survey. Our study design was approved
by an institutional review board.
4.2 Pre-study Survey
Participants were first directed to an online survey that included screening questions to ensure
eligibility. Those who didn’t meet the requirements were automatically removed from the survey
at this stage. Afterward, participants were presented with a consent form in the survey. Those
who agreed to participate provided their preferred email address for future communication and to
schedule a Zoom-based interview. Participants were then requested to share links to two Reddit
posts they had made; one with which they had privacy concerns and another with which they did
not. As mentioned prior, participants were filtered out of the study if the posts that they shared
were inaccessible, removed, contained no text (e.g., had only an image), or if they reported not
having made a post that met our criteria.
In the final section of the pre-study survey, participants answered questions about their Reddit
usage and behaviors, their perception of self-anonymity on Reddit, as well as their tendency
to disclose information publicly using validated scales adapted from prior work on perceived
anonymity in online social support communities [ 99]. Additionally, participants were asked about
their demographics and their general attitudes towards security and privacy using the SA-13 scale
[30]. We collected these data because prior research has found that differences in end-user security
attitudes, demographic characteristics, and perceived audiences when sharing content online can
shape users’ online S&P decision-making [15].
9Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway Krsek, et al.
Fig. 3. Image depicting how the disclosure detection spans of both versions of the model were presented to
participants. On the left is the binary disclosure version, and on the right is the categorical disclosure version.
4.3 Interview
User Assessment of Model Output on Their Posts. We conducted 75-minute semi-structured in-
terviews to gather feedback on the model’s outputs and understand participants’ views on online
anonymity risks and how those risks are influenced by subreddit community norms. The interviews
began with general questions about participants’ Reddit usage and the disclosure norms they
followed for the subreddits in which they were active. We also asked about their posting behaviors
and differences in disclosure norms across subreddits in order to account for posting practices that
might interfere with the outputs of the model (RQ1, RQ3). Prior to showing participants the model
outputs on their posts, we discussed the posts participants shared with us in the pre-study survey.
We started with the post they reported feeling less comfortable sharing with people they know in
the physical world, probing them on what personal disclosures they thought they included in the
post, as well as the threats they perceived to their anonymity, who they were concerned might
identify them, and why. We then asked participants to either (a) share a post from a burner account
they had privacy concerns with, or (b) draft a post that they’d previously hesitated to share on
Reddit for reasons related to privacy or sensitivity. After doing this, we then probed participants
on all the same questions as the first post. As opposed to the first post, asking them to share/draft
an additional post allowed us to assess the model’s utility in providing feedback on posts that users
hesitated to share from their main accounts.
In the next stage of the interview, we analyzed participants’ posts using both the binary and
categorical disclosure versions of the disclosure detection model (RQ2). Participants first saw the
output of the binary disclosure model on both of their posts and assessed those. We then showed
participants the output of the categorical disclosure model on their posts for assessment. When
evaluating the model’s outputs on self-authored posts, we also asked participants to assess each
of the disclosure spans detected by the model; we asked whether they agreed or disagreed that
the detected disclosure span contained self-disclosure and why, as well as whether and how they
would want to change their post as a result. Participants then rated each detected disclosure span
on four aspects using a 5-point Likert scale (from “not at all...” (1) to “very... ”(5)): 1) the “helpfulness”
of the disclosure span in surfacing a privacy risk, 2) the “importance” of disclosing the information
in the disclosure span for communicating the context of the post, 3) their perceived “sensitivity” of
the information in the disclosure span, and 4) the “riskiness” of disclosing that information in their
online post. Because these scales were delivered verbally in during the interview, we also probed
participants on the reasoning behind their rankings. We present our analysis of their reasoning
in the results section alongside rankings. Finally, we asked participants whether they would feel
comfortable posting the modified second post to their main Reddit account based on the model
outputs, and any changes they would make as a result (RQ1, RQ2, RQ3).
10... Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway
In the next stage of the interview, in order to get a baseline user assessment for each of the category
labels for disclosure spans produced by the categorical disclosure model, we asked participants
to assess the disclosure detection outputs of the model on a selection of public posts sourced
from Reddit (RQ2). We selected six such posts where the model performed reasonably well; each
participant was randomly shown one of the 6. Upon being presented with the disclosure detections
from the model on the public post, participants then answered all the same questions they were
asked in their assessment of the model output on their self-authored posts.
Lastly, after completing all assessments of the model outputs we asked participants to share their
overall opinions on the model (both positive and negative) (RQ1), what changes could be made to
improve its utility (RQ2), and whether or not they would use it themselves and why (RQ1, RQ3).
INTERVIEW METHODOLGY FLOWCHART
Fig. 4. Flowchart depicting the interview methodology flow. Participants first answered general questions
about self-disclosure on Reddit and were asked to share a post from a burner account or draft a post that
they considered making but hesitated to due to privacy concerns. They then moved onto the model output
assessment stage where they provided their thoughts on the model’s output across the two posts they shared
and ranked them on helpfulness, importance, riskiness, and sensitivity – first assessing the outputs of the
binary disclosure model, and then the categorical disclosure model. Finally, the participants then moved to
the exit stage of the interview, being probed on their overall thoughts on the model and concerns, as well as
desired areas for improvement.
4.4 Data Analysis
We used an inductive thematic analysis approach to coding our interviews with participants [ 66],
leveraging affinity diagramming to uncover themes within the work. This analysis was conducted
by two researchers who actively collaborated in reviewing 5 transcripts to develop a codebook with
40 codes, containing a mixture of general reactions to the model, disclosure detection preferences,
and their reasons for each. The same two researchers then used this codebook to identify emergent
patterns and themes across the full set of interview transcripts. The researchers also collaborated
in affinity diagramming the codes in order to reveal sub-themes in the work. For a subset of the
study sessions (23% of the data) which were coded independently by two researchers, we achieved
11Accepted for publication at CSCW ’25, October 18 — 22, 2025, Bergen, Norway Krsek, et al.
a Cohen’s Kappa of 0.98 — an inter-rater reliability value generally considered to represent high
agreement [31, 48, 90].
In order to analyze how participants’ reactions to the disclosure detections surfaced by each
model differed, we compared: The rate at which participants agreed that the detected disclosure
span contained a sensitive self-disclosure; the reasons participants provided for disagreeing with or
rejecting a disclosure span; whether participants altered what they wrote based on the disclosure
detection by the model; and, the rating of each detected disclosure span in terms of its helpfulness
(of the disclosure detection span in surfacing a privacy risk), importance (of including in the post
for context), sensitivity of the information disclosed, and the riskiness of sharing that information.
To explore whether participants’ rankings (of helpfulness, importance, sensitivity, and riskiness)
differed significantly across altered and non-altered disclosure spans that were accepted by partici-
pants as containing self-disclosure, we employed both a two-sample t-test and Mann-Whitney test
to ensure the results agreed to account for any power differences. The p-values reported are from
the two-sample t-test. We ran all statistical comparisons in R.