Studies have underscored how, regardless of the recent breakthrough
and swift advances in AI research, even state-of-the-art Large Language
models (LLMs) continue to struggle when performing logical and math-
ematical reasoning. The results seem to suggest that LLMs still work as
(highly advanced) data pattern identifiers, scoring poorly when attempt-
ing to generalise and solve reasoning problems the models have never
previously seen or that are not close to samples presented in their train-
ing data. To address this compelling concern, this paper makes use of the
notion of critical questions from the literature on argumentation theory ,
focusing in particular on Toulmin’s model of argumentation. We show
that employing these critical questions can improve the reasoning capa-
bilities of LLMs. By probing the rationale behind the models’ reasoning
process, the LLM can assess whether some logical mistake is occurring and
correct it before providing the final reply to the user prompt. The un-
derlying idea is drawn from the gold standard of any valid argumentative
procedure: the conclusion is valid if it is entailed by accepted premises.
Or, to paraphrase such Aristotelian principle in a real-world approxima-
tion, characterised by incomplete information and presumptive logic, the
conclusion is valid if not proved otherwise. This approach successfully
steers the models’ output through a reasoning pipeline, resulting in better
performance against the baseline and its Chain-of-Thought (CoT) imple-
mentation. To this end, an extensive evaluation of the proposed approach
on the MT-Bench Reasoning and Math tasks across a range of LLMs is
provided.