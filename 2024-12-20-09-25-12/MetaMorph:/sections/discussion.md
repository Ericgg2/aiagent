In this work, we propose VPiT—a simple yet effective extension to visual instruction tuning—that enables
LLMs to predict multimodal tokens. VPiT unlocks the use of a more diverse range of instruction tuning data
than just visual question answering, such as text-to-image and pure image and video data. Through controlled
experiments, we find that visual generation ability emerges as a natural byproduct of improved visual under-
standing and requires modest additional generation data. In addition, we find that while visual understanding
and generation are mutually beneficial, adding more visual understanding data disproportionately improves
overall performance compared to adding more generation data.
Leveraging these insights, we train MetaMorph by finetuning LLaMA-3.1 8B with VPiT. With a simple
training process, MetaMorph achieves competitive performance in both visual understanding and generation.
Qualitative evaluation of our model shows that MetaMorph can leverage world knowledge and reasoning
abilities of the base LLM during visual generation. For example, it can perform multimodal tasks that typically
require multiple steps of reasoning, such as generating images of specialized proper nouns ( “Chhogori” ) or
solving visual puzzles ( “generate an image of the animal resulting from a monarch caterpillar’s metamorphosis” ).
This indicates that LLMs already possess a degree of “prior” visual knowledge which can be activated with
only minimal instruction tuning with VPiT. Overall, LLMs may have a similar representation space as unified
and multi-functional models (Huh et al., 2024). We hope the insights from this work inspire more exploration
toward developing LLMs for general intelligence.