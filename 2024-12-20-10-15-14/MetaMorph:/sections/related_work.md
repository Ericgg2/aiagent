Instruction tuning and visual instruction tuning. Instruction tuning (Wei et al., 2022a; Taori et al., 2023) finetunes
a pretrained LLM to learn the format and style of interaction. This process helps the model to effectively
convey the knowledge and capabilities acquired during pretraining (Zhou et al., 2024a). LLaVA (Liu et al.,
2023) extends instruction tuning into the multimodal domain. Since then, different lines of work focus on
improving data curation (Chen et al., 2023; Laurençon et al., 2024a,b), visual representation (Tong et al.,
2024a; Kar et al., 2025; Chen et al., 2024b), and instruction tuning strategies (Gao et al., 2024; Liu et al.,
2024b). Using only a few million multimodal instruction tuning data, this line of research (Liu et al., 2024b;
Tong et al., 2024a; Li et al., 2024a) has enabled open-source MLLMs to reach performance levels comparable
to those of proprietary models (OpenAI, 2024; Anthropic, 2024) on a number of benchmarks (Liu et al., 2024d;
Yue et al., 2024a,b) and applications (Zhai et al., 2024; Pan et al., 2024a).
From Multimodal LLMs to unified models. Recent efforts to construct unified models have primarily relied on
either extensive pretraining or heavy fine-tuning on billion-scale datasets. Some studies also use continuous
embeddings for predicting visual tokens, integrating visual regression losses (Sun et al., 2024b,a) or leveraging
diffusion-based methods (Dong et al., 2024). Other approaches (Lu et al., 2022a; Aghajanyan et al., 2022;
Team, 2024; Wu et al., 2024b; Liu et al., 2024c; Wang et al., 2024b; Lu et al., 2024) tokenize multimodal
data into discrete tokens, which are then trained using autoregressive transformers. Recent research has
also explored hybrid strategies that combine autoregressive and diffusion objectives (Zhou et al., 2024b; Xie
et al., 2024). Different from previous studies, we demonstrate that unified models can be effectively trained
in low-data regimes during instruction tuning, while also providing insights into the reciprocal relationship
between visual understanding and visual generation.