Multimodal Large Language Models (MLLMs) have advanced considerably in visual understanding, progressing
from basic image captioning to complex visual inferences (Alayrac et al., 2022; Liu et al., 2023; Dai et al.,
2024). These models process multimodal inputs—primarily images and language—and generate text tokens.
Multimodal LLMs often leverage a pretrained vision encoder (Dosovitskiy et al., 2021; Radford et al., 2021),
a pretrained language model (Touvron et al., 2023; AI@Meta, 2024), and align these modalities through
connectors such as MLP (Liu et al., 2023, 2024a) or cross-attention modules (Alayrac et al., 2022; Dai et al.,
2024). Among MLLM training methods, visual instruction tuning (Liu et al., 2023) has become widely
used (Wang et al., 2024a; Agrawal et al., 2024). It treats output embeddings of pretrained vision encoders as
continuous-valued “visual tokens” and directly feeds them as inputs to pretrained LLMs.
One benefit of visual instruction tuning is that it is data and compute efficient. A pretrained LLM can be
repurposed as a Multimodal LLM by instruction tuning with modest compute and data on the order of millions
of image-text question-answer pairs (Tong et al., 2024a; Li et al., 2024a). The effectiveness of visual instruction
tuning indicates that LLMs already possess a considerable amount of inherent visual knowledge which allows
them to efficiently learn and develop visual understanding during the instruction tuning process (Zhou et al.,
2024a). Inspired by this, we investigate whether LLMs can also be finetuned to generate visual information
with comparable efficiency and effectiveness.
Current attempts toward “unified” models—models capable of both multimodal understanding and generation—
often treat visual generation as an orthogonal capability to visual understanding. They tend to require
substantialchangestotheoriginalMLLMarchitectureandsignificantmultimodalpretrainingand/orfinetuning.
Designing such methods is challenging, and past research takes different approaches including tokenizing
1arXiv:2412.14164v1  [cs.CV]  18 Dec 2024Text
HeadVision 
Head
Autoregressive 
Model
Adapter
Vision
Encoder
VPiT
Autoregressive ModelAdapted 
Diffusion 
ModelText 
HeadVision 
Head
Adapter
Encoder
Projector
Inference Examples
Generate an image of the animal resulting from a 
monarch caterpillar's metamorphosis 
Here ’s the generated image based on 
your request: < image_start ><image_end >
What’s the animal in this image?
The animal in the image is a butterfly.Figure 1 VPiT Training, Inference, and Examples of MetaMorph. Left : In Visual-Predictive Instruction Tuning (VPiT),
we finetune a pretrained LLM to generate both text and visual tokens using separate text and vision heads. Middle:
During inference, the model accepts an arbitrary input sequence of image(s) and text and outputs discrete text tokens
and continuous visual tokens. These visual tokens can be visualized via a separately finetuned diffusion model, which
is trained to condition on the pretrained vision encoder’s output. Right: An example conversation from MetaMorph
trained with VPiT. Here, the model implicitly solves a visual puzzle in order to generate the visual tokens of a butterfly.
The conversation continues with new user questions as the model continues to autoregressively process vision and text
tokens, independent of the diffusion-based visualization.
visual inputs into discrete tokens (Wu et al., 2024b; Team, 2024; Liu et al., 2024c), incorporating diffusion
objectives (Xie et al., 2024; Zhou et al., 2024b), and decoupling vision into separate understanding and
generation modes (Wu et al., 2024a). For example, approaches like LWM (Liu et al., 2024c), Show-o (Xie
et al., 2024), and Chameleon (Team, 2024) require billions of image-text pairs (Schuhmann et al., 2022; Gadre
et al., 2024) for extensive pretraining and finetuning.
In this work, we propose Visual-Predictive Instruction Tuning (VPiT)—a simple extension to visual instruction
tuning which builds upon the existing paradigm of passing continuous visual tokens as input to the LLM. VPiT
trains an LLM to output both continuous visual tokens and discrete text tokens in the finetuning stage. The
model takes pretrained vision encoder embeddings as well as text tokens as input, and outputs a combination
of text tokens and continuous visual tokens. To visualize the generated visual tokens, we finetune a diffusion
model to map the embeddings back into pixel space (see Figure 1 for an example). This framework allows us
to study the synergy between visual understanding, visual generation, and pretrained LLMs, which leads to
several intriguing findings outlined below.
First, we show that the ability to predict visual tokens emerges from understanding visual inputs and requires
minimal additional training. Similar to visual instruction tuning, VPiT efficiently and effectively morphsan
LLM into an “unified” model that understands and generates multimodal tokens. When trained jointly with
sufficient visual understanding data, this process requires as little as 200kadditional visual generation data.
We further establish that the abilities to understand and generate visual tokens are intrinsically linked and
asymmetrical . Specifically, increasing understanding data improves visual understanding (measured by higher
VQA scores) and generation performance (measured by lower FID scores). Conversely, increasing generation
data enhances generation quality and also contributes to stronger visual understanding—but to a lesser degree.
Importantly, our findings highlight an asymmetry in how training each ability impacts the model’s overall
vision performance: understanding-centric training substantially outperforms generation-centric training in
improving both visual understanding and generation.
Building upon these findings, we train a unified model called MetaMorph to predict multimodal tokens with
VPiT. We leverage diverse data sources ranging from common visual question answering datasets to pure
image and video data without text annotations. MetaMorph achieves competitive performance on both visual
understanding and visual generation benchmarks. Furthermore, we show this unified modeling approach
allows models to leverage the power of LLMs. For instance, MetaMorph can extract knowledge from the
pretrained LLM when generating visual tokens. More surprisingly, we observe that MetaMorph can implicitly
perform reasoning steps before generating visual tokens—e.g. when prompted with “the animal resulting from
a monarch caterpillar’s metamorphosis” , MetaMorph successfully generates an image of a butterfly (Figure 1).
Our results suggest that 1) training a unified model with instruction tuning is feasible, and 2) LLMs have
strong pre-existing visual capabilities which can be activated using significantly fewer samples compared
2to extensive pretraining. These insights shed light on the development of mixed-modality models. As the
community continues to improve visual understanding in Multimodal LLMs (Tong et al., 2024a; Wang et al.,
2024a; Li et al., 2024a) by advancing base LLMs, instruction tuning techniques, and data, we highlight that
these efforts may also implicitly lead to models that are better at visual generation.
2 Visual-Predictive Instruction Tuning
Visual instruction tuning as introduced by LLaVA (Liu et al., 2023) demonstrates that LLMs can be taught
to understand visual inputs. This is achieved by finetuning on million-scale data. The success of late-fusion
instruction tuning suggests that LLMs may already possess innate visual understanding ability. This ability
simply needs to be unlocked through lightweight finetuning. Analogously, we hypothesize that LLMs already
possess a degree of innate visual generation ability which just needs to be unlocked with lightweight finetuning.
Motivated by this, we present Visual-Predictive Instruction Tuning (VPiT, Figure 1)—a simple design which
extends existing instruction tuning methods to additionally generate visual tokens rather than text alone.
We use the same architecture and next-token prediction paradigm to unlock visual generation capabilities
without bells and whistles. We take a pretrained LLM and finetune it to predict both discrete text tokens
and continuous visual tokens. The visual tokens can be visualized with an adapted diffusion model.
2.1 From Unimodal to Multimodal Next-Token Prediction
The standard instruction tuning setup consists of an input sequence of conversation rounds (Wei et al., 2022a;
Taori et al., 2023): (Pi, Ri)N
i=1, where PiandRirepresent prompts and responses for the i-th round of
conversation, respectively. The model is trained to generate responses based on the prompt. VPiT adds the
following mechanisms to a standard instruction tuning setup to unlock visual understanding and generation.
Tokenizing multimodal data. We extend PiandRito include both text and images. To integrate visual data
into a pretrained LLM, we process data closely following visual instruction tuning (Liu et al., 2023):
•Text Data : Text is tokenized into discrete tokens with a standard tokenizer used by the LLM.
•Visual Data : Images are encoded with a pretrained vision encoder such as SigLIP (Zhai et al., 2023).
The output is continuous visual tokens which are then interpolated to m= 64tokens. To pass the visual
tokens as input to the LLM, we apply a trainable projection layer to align the dimensions with the LLM.
Model architecture. We take a pretrained LLM and finetune it to process arbitrary sequences of text and
visual tokens (detailed next in Section 2.2). We keep the original LLM head for text prediction, and attach a
separate vision head to the LLM for predicting visual tokens, i.e., the output tokens generated by the vision
encoder when processing images. The vision head is a projection layer that projects from the LLM’s dimension
to the vision encoder’s dimension. All response tokens can then be trained and predicted autoregressively,
with prompt tokens as context.
Unlike conventional visual instruction tuning, in VPiT, visual tokens are also outputs of the LLM—not just
inputs. To make the LLM aware of the presence of visual tokens, we introduce special tokens ⟨image_start ⟩
and⟨image_end ⟩to indicate the boundaries of visual token sequences and when to use the vision head.
Loss functions . The language head outputs a probability distribution over the vocabulary and is trained with
cross-entropy loss for next-token prediction. Visual prediction uses cosine similarity loss between the LLM’s
predicted visual tokens and those from the vision encoder. Consistent with instruction tuning practices, the
model only makes predictions and incurs loss on response tokens.
2.2 Using Broad Types of Data
Because VPiT enables the model to predict both text and visual tokens in its responses, it allows the use of
a broader range of training data. Traditional visual instruction tuning, on the other hand, primarily relies
on question-and-answer pairs. The majority of our dataset is publicly available, and we categorize it into
three major categories below. This categorization enables us to systematically study the model, as detailed in
3Section 3 and Section 4. All data types are formatted as instruction tuning style prompt & response pairs.
See further details in Appendix C.2.
1.Visual Understanding Data : This category includes data that takes image(s) or video as input and outputs
text responses. See Figure 1 for an example. We use:
•ImageQA: Cambrian-7M (Tong et al., 2024a). The model answers questions based on input image(s).
Pi∈ {⟨visual tokens ⟩,⟨text prompt ⟩}
Ri∈ {⟨text response ⟩}
•VideoQA: VideoStar (Zohar et al., 2024) and ShareVideo (Zhang et al., 2024). The model answers
questions based on the input video. For videos in VideoQA, we process frames at 1 FPS.
Pi∈ {⟨visual tokens ⟩,···,⟨visual tokens ⟩,⟨text prompt ⟩}
Ri∈ {⟨text response ⟩}
2.Visual Generation Data : MetaCLIP (Xu et al., 2024). The model predicts visual tokens based on an image
description. We using at most 5 million pairs. We curate the data into question-answering formats.
Pi∈ {⟨text prompt ⟩}
Ri∈ {⟨text response ⟩,⟨visual tokens ⟩}
We prompt the model to generate visual tokens with instructions like “Generate an image of...” . The
text responses are “Here is an image based on your request...” . See Figure 1 for an example.
3.Other Visual Data : This category includes data that requires the model to predict visual tokens given
interleaved input visual tokens and text tokens. We use:
•Video Data: SomethingSomethingV2 (Goyal et al., 2017b) and HowTo100M (Miech et al., 2019).
The model predicts frames in a sequential order. We design different question-answer pairs to
probe into the video, such as asking about future frames, past frames, and reordering frames.
Pi∈ {⟨visual tokens ⟩,···,⟨visual tokens ⟩,⟨text prompt ⟩}
Ri∈ {⟨visual tokens ⟩,···,⟨visual tokens ⟩}
•Visual Thinking Data: Visualization-of-Thought (Shao et al., 2024) and VStar (Wu and Xie, 2024).
The model predicts multimodal tokens in its response before addressing problems. For instance, it
predicts a zoomed-in view of an image before generating textual responses.
Pi∈ {⟨visual tokens ⟩,⟨text prompt ⟩}
Ri∈ {⟨text response ⟩,⟨visual tokens ⟩,⟨text response ⟩}
In the response, the model will output “I will think about it visually” , followed by visual tokens
representing a zoomed-in segment of the image, and then proceed to answer the question.
•Image-to-Image Data: InstructPix2Pix (Brooks et al., 2023) and Aurora (Krojer et al., 2024). The
model generates a transformed image conditioned on a text description and an input image.
Pi∈ {⟨visual tokens ⟩,⟨text prompt ⟩}
Ri∈ {⟨visual tokens ⟩}
2.3 Mapping Tokens to Images through Diffusion
Because models trained with VPiT learn to predict continuous visual tokens, we need to map the predicted
tokens back into pixel space. We leverage the concept of a “Diffusion Autoencoder” (Bordes et al., 2022;
Preechakul et al., 2022; Pan et al., 2024b; Koh et al., 2024; Li et al., 2024c) in which the diffusion model
can be adapted to condition on image embeddings rather than text embeddings. Specifically, we finetune an
existing diffusion model to condition on outputs from the vision encoder using held-out training data.
At inference time, if the tag token ⟨image_start ⟩is generated, the model begins outputting visual tokens until
⟨image_end ⟩. We then plug the generated visual tokens into the diffusion model to visualize the prediction in
pixel space. We use standard latent diffusion model training procedures. Details on the hyperparameters and
training setup are provided in Appendix A.2.
43 Findings on Unlocking Visual Generation
We study the following questions about the effects and synergy of visual understanding and generation, under
our VPiT framework:
§3.1Can visual generation be unlocked through lightweight tuning, or does it require extensive data?
§3.2Are visual understanding and generation mutually beneficial or orthogonal?
§3.3 Howmuchdoesmorevisualunderstandingorgenerationdatacontributetounderstandingandgeneration
quality?
§3.4Which visual understanding tasks correlate the most with generation performance?
Evaluation settings. We use 9 ImageQA benchmarks (MMBench, Seed, VStar, MMVP, MMMU, ChartQA,
TextVQA, ScienceQA, RealWorldQA) to evaluate different aspects of the model. For image generation, we
use the finetuned diffusion model to visualize generated visual tokens and measure FID score (lower is better)
and CLIP score (higher is better) on the COCO-30K dataset. Unless otherwise specified, we use LLaMA-3
8B (AI@Meta, 2024) / SigLIP ViT-SO400M-14@384 (Zhai et al., 2023) as the pretrained LLM / vision
encoder. We also study the effect of different LLMs in Section 3.2. We use instruction tuned versions of
the LLMs. We pretrain the adapter between the vision encoder and the LLM following visual instruction
tuning (Liu et al., 2023, 2024a). For experiments in this section, we provide training details in Appendix A
and include the full results in Appendix B.
3.1 Visual Generation Can Be Unlocked Efficiently by Joint Training with Visual Understanding
We start by investigating the number of image-text samples required to teach a language model to generate
high-quality visual tokens. To this end, we randomly sample {1k, 5k, 10k, 50k, 200k, 1M, 3M, 5M} image-text
pairs from our generation data (MetaCLIP dataset (Xu et al., 2024)). We explore two settings: (1) finetuning
the LLM using only visual generation data, and (2) joint training visual generation with visual understanding
and the rest of data types described in Section 2.2.
In Figure 2, we see that training solely on visual generation performs significantly worse than joint training
with all other data. With over 3 million image-text pairs, the model struggles to generate high-quality visual
images ( ∼40 FID score), and performance remains inferior to joint training with 5 million pairs. This suggests
that training solely on visual generation data is significantly less sample efficient. This finding aligns with a
prior study (Zhang et al., 2023) which also suggests that LLMs cannot be easily tuned to generate visual
tokens when trained with only generation data. In contrast, joint training with other datasets substantially
improves generation performance. The model generates effective visual tokens with just 5kgeneration data,
and performance stabilizes around 200ksamples. This indicates that visual generation is not an orthogonal
capability but rather an ability that benefits from other tasks and emerges more effectively with joint training.
/uni00000014/uni00000013/uni00000016/uni00000014/uni00000013/uni00000017/uni00000014/uni00000013/uni00000018/uni00000014/uni00000013/uni00000019
/uni00000031/uni00000058/uni00000050/uni00000045/uni00000048/uni00000055/uni00000003/uni00000052/uni00000049/uni00000003/uni0000002a/uni00000048/uni00000051/uni00000048/uni00000055/uni00000044/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni00000027/uni00000044/uni00000057/uni00000044/uni00000003/uni0000000b/uni0000002f/uni00000052/uni0000004a/uni00000003/uni00000036/uni00000046/uni00000044/uni0000004f/uni00000048/uni0000000c/uni00000015/uni00000013/uni00000017/uni00000013/uni00000019/uni00000013/uni0000001b/uni00000013/uni00000014/uni00000013/uni00000013/uni00000014/uni00000015/uni00000013/uni00000029/uni0000002c/uni00000027/uni00000003/uni00000036/uni00000046/uni00000052/uni00000055/uni00000048/uni00000003/uni0000000b /uni0000000c
/uni0000002a/uni00000048/uni00000051/uni00000048/uni00000055/uni00000044/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni00000027/uni00000044/uni00000057/uni00000044/uni00000003/uni00000024/uni0000004f/uni00000052/uni00000051/uni00000048 /uni0000002d/uni00000052/uni0000004c/uni00000051/uni00000057/uni00000003/uni00000037/uni00000055/uni00000044/uni0000004c/uni00000051/uni0000004c/uni00000051/uni0000004a/uni00000003/uni0000005a/uni0000004c/uni00000057/uni0000004b/uni00000003/uni00000024/uni0000004f/uni0000004f/uni00000003/uni00000032/uni00000057/uni0000004b/uni00000048/uni00000055/uni00000003/uni00000027/uni00000044/uni00000057/uni00000044
Figure 2 Generation-only training vs. Joint training
with other data. Training solely on generation data
results in inferior performance. Joint training with
additional data enables visual generation with only
5k generation data and yields high-quality outputs
with 200k generation data.
/uni00000013 /uni00000018/uni00000013 /uni00000014/uni00000013/uni00000013
/uni00000029/uni0000002c/uni00000027/uni00000003/uni00000036/uni00000046/uni00000052/uni00000055/uni00000048/uni00000003/uni0000000b /uni0000000c
/uni00000024/uni0000004f/uni0000004f/uni00000003/uni00000047/uni00000044/uni00000057/uni00000044/uni0000002a/uni00000048/uni00000051/uni00000048/uni00000055/uni00000044/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni0000000e/uni00000003/uni0000002c/uni00000050/uni00000044/uni0000004a/uni00000048/uni00000003/uni00000034/uni00000024/uni0000002a/uni00000048/uni00000051/uni00000048/uni00000055/uni00000044/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni0000000e/uni00000003/uni00000039/uni0000004c/uni00000047/uni00000048/uni00000052/uni00000003/uni00000034/uni00000024/uni0000002a/uni00000048/uni00000051/uni00000048/uni00000055/uni00000044/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni0000000e/uni00000003/uni00000033/uni00000058/uni00000055/uni00000048/uni00000003/uni00000039/uni0000004c/uni00000047/uni00000048/uni00000052/uni0000002a/uni00000048/uni00000051/uni00000048/uni00000055/uni00000044/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni0000000e/uni00000003/uni00000039/uni0000004c/uni00000056/uni00000058/uni00000044/uni0000004f/uni00000003/uni00000037/uni0000004b/uni0000004c/uni00000051/uni0000004e/uni0000004c/uni00000051/uni0000004a/uni0000002a/uni00000048/uni00000051/uni00000048/uni00000055/uni00000044/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni0000000e/uni00000003/uni0000002c/uni00000050/uni00000044/uni0000004a/uni00000048/uni00000010/uni00000057/uni00000052/uni00000010/uni0000002c/uni00000050/uni00000044/uni0000004a/uni00000048/uni0000002a/uni00000048/uni00000051/uni00000048/uni00000055/uni00000044/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni00000032/uni00000051/uni0000004f/uni0000005c
/uni00000013 /uni00000014/uni00000013 /uni00000015/uni00000013
/uni00000026/uni0000002f/uni0000002c/uni00000033/uni00000003/uni00000036/uni00000046/uni00000052/uni00000055/uni00000048/uni00000003/uni0000000b /uni0000000c
Figure3 Impactofdifferentdatatypesonvisualgeneration. Thebaseline
of training on only visual generation data is red; Joint training with
other data is yellow; Joint training with visual understanding data
is green; and all data is blue. Joint training with additional data
improves the baseline, with visual understanding tasks contributing
the most to enhancing visual generation.
5/uni00000017/uni00000018/uni00000011/uni00000013 /uni00000017/uni0000001a/uni00000011/uni00000018 /uni00000018/uni00000013/uni00000011/uni00000013 /uni00000018/uni00000015/uni00000011/uni00000018 /uni00000018/uni00000018/uni00000011/uni00000013
/uni00000039/uni00000034/uni00000024/uni00000003/uni00000024/uni00000046/uni00000046/uni00000058/uni00000055/uni00000044/uni00000046/uni0000005c/uni00000003/uni0000000b /uni0000000c
/uni00000014/uni0000001b/uni00000015/uni00000013/uni00000015/uni00000015/uni00000015/uni00000017/uni00000015/uni00000019/uni00000015/uni0000001b/uni00000029/uni0000002c/uni00000027/uni00000003/uni00000036/uni00000046/uni00000052/uni00000055/uni00000048/uni00000003/uni0000000b /uni0000000c
/uni00000017/uni00000018/uni00000011/uni00000013 /uni00000017/uni0000001a/uni00000011/uni00000018 /uni00000018/uni00000013/uni00000011/uni00000013 /uni00000018/uni00000015/uni00000011/uni00000018 /uni00000018/uni00000018/uni00000011/uni00000013
/uni00000039/uni00000034/uni00000024/uni00000003/uni00000024/uni00000046/uni00000046/uni00000058/uni00000055/uni00000044/uni00000046/uni0000005c/uni00000003/uni0000000b /uni0000000c
/uni00000014/uni00000019/uni00000014/uni0000001b/uni00000015/uni00000013/uni00000015/uni00000015/uni00000026/uni0000002f/uni0000002c/uni00000033/uni00000003/uni00000036/uni00000046/uni00000052/uni00000055/uni00000048/uni00000003/uni0000000b /uni0000000c
/uni00000015/uni00000013/uni00000013/uni0000004e/uni00000003/uni0000002a/uni00000048/uni00000051/uni00000048/uni00000055/uni00000044/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni00000027/uni00000044/uni00000057/uni00000044/uni00000003/uni0000002d/uni00000052/uni0000004c/uni00000051/uni00000057/uni0000004f/uni0000005c/uni00000003/uni00000037/uni00000055/uni00000044/uni0000004c/uni00000051/uni00000048/uni00000047/uni00000003/uni0000005a/uni0000004c/uni00000057/uni0000004b
/uni00000014/uni00000030/uni00000003/uni00000039/uni00000034/uni00000024
/uni00000015/uni00000030/uni00000003/uni00000039/uni00000034/uni00000024/uni00000016/uni00000030/uni00000003/uni00000039/uni00000034/uni00000024
/uni00000017/uni00000030/uni00000003/uni00000039/uni00000034/uni00000024/uni00000018/uni00000030/uni00000003/uni00000039/uni00000034/uni00000024
/uni00000019/uni00000030/uni00000003/uni00000039/uni00000034/uni00000024/uni0000001a/uni00000030/uni00000003/uni00000039/uni00000034/uni00000024Figure 4 VQA Performance vs. Generation Performance with
generation data controlled at 200k. Increasing understand-
ing data improves VQA and generation performance.
/uni00000015/uni00000013/uni00000011/uni00000013 /uni00000015/uni00000015/uni00000011/uni00000018 /uni00000015/uni00000018/uni00000011/uni00000013 /uni00000015/uni0000001a/uni00000011/uni00000018
/uni00000029/uni0000002c/uni00000027/uni00000003/uni00000036/uni00000046/uni00000052/uni00000055/uni00000048/uni00000003/uni0000000b /uni0000000c
/uni00000017/uni00000019/uni00000017/uni0000001a/uni00000017/uni0000001b/uni00000017/uni0000001c/uni00000018/uni00000013/uni00000018/uni00000014/uni00000018/uni00000015/uni00000039/uni00000034/uni00000024/uni00000003/uni00000024/uni00000046/uni00000046/uni00000058/uni00000055/uni00000044/uni00000046/uni0000005c/uni00000003/uni0000000b /uni0000000c
/uni00000014/uni00000019 /uni00000014/uni0000001b /uni00000015/uni00000013 /uni00000015/uni00000015
/uni00000026/uni0000002f/uni0000002c/uni00000033/uni00000003/uni00000036/uni00000046/uni00000052/uni00000055/uni00000048/uni00000003/uni0000000b /uni0000000c
/uni00000017/uni00000019/uni00000017/uni0000001a/uni00000017/uni0000001b/uni00000017/uni0000001c/uni00000018/uni00000013/uni00000018/uni00000014/uni00000018/uni00000015/uni00000039/uni00000034/uni00000024/uni00000003/uni00000024/uni00000046/uni00000046/uni00000058/uni00000055/uni00000044/uni00000046/uni0000005c/uni00000003/uni0000000b /uni0000000c
/uni00000014/uni00000030/uni00000003/uni00000039/uni00000034/uni00000024/uni00000003/uni00000027/uni00000044/uni00000057/uni00000044/uni00000003/uni0000002d/uni00000052/uni0000004c/uni00000051/uni00000057/uni0000004f/uni0000005c/uni00000003/uni00000037/uni00000055/uni00000044/uni0000004c/uni00000051/uni00000048/uni00000047/uni00000003/uni0000005a/uni0000004c/uni00000057/uni0000004b
/uni00000015/uni00000013/uni00000013/uni0000004e/uni00000003/uni0000002a/uni00000048/uni00000051/uni00000048/uni00000055/uni00000044/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni00000027/uni00000044/uni00000057/uni00000044
/uni00000018/uni00000013/uni00000013/uni0000004e/uni00000003/uni0000002a/uni00000048/uni00000051/uni00000048/uni00000055/uni00000044/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni00000027/uni00000044/uni00000057/uni00000044/uni00000014/uni00000030/uni00000003/uni0000002a/uni00000048/uni00000051/uni00000048/uni00000055/uni00000044/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni00000027/uni00000044/uni00000057/uni00000044
/uni00000015/uni00000030/uni00000003/uni0000002a/uni00000048/uni00000051/uni00000048/uni00000055/uni00000044/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni00000027/uni00000044/uni00000057/uni00000044/uni00000016/uni00000030/uni00000003/uni0000002a/uni00000048/uni00000051/uni00000048/uni00000055/uni00000044/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni00000027/uni00000044/uni00000057/uni00000044
/uni00000017/uni00000030/uni00000003/uni0000002a/uni00000048/uni00000051/uni00000048/uni00000055/uni00000044/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni00000027/uni00000044/uni00000057/uni00000044Figure 5 Generation Performance vs. VQA Performance with
VQA data controlled at 1M. Increasing generation data im-
proves generation and VQA performance.
To better understand how each type of data contributes to visual generation, we conduct a controlled
experiment using 200k visual generation data, joint training individually with each data type defined in
Section 2.2. We also compare them with training all the data together. We show results in Figure 3. While
all data types enhance the model’s visual generation, the degree of improvement varies. Visual understanding
data, such as ImageQA and VideoQA, significantly boost the model’s visual generation capabilities, even
when the amount of generation data is kept constant at 200k. This indicates a strong link between the ability
to understand visual content and generate visual tokens. Additionally, combining all data types in training
further improves performance, suggesting that the benefits from different data types can be additive.
Finding 1: The ability to generate visual tokens can be unlocked with significantly less generation data
when the model is jointly trained with visual understanding data, in contrast to training only on
generation data.
3.2 Visual Understanding and Generation are Mutually Beneficial
More understanding data leads to better understanding and generation. Building upon findings from the previous
subsection, we perform a controlled experiment to investigate how visual understanding ability correlates with
visual generation ability. We ablate our model using a fixed set of 200k generation data while varying VQA
data from 1M to 7M samples from Cambrian-7M to develop different levels of visual understanding. The
results presented in Figure 4 indicate that stronger VQA ability correlates with better generation performance.
More generation data leads to better understanding and generation. Here, we investigate the reverse direction:
does enhancing the model’s visual generation capability also relate to higher VQA performance? To explore
this, we conduct a controlled experiment using 1M fixed VQA samples as the baseline for understanding. We
then vary the amount of generation data ({200k, 500k, 1M, 2M, 3M, 4M}) to adjust generation capacity while
joint training with the fixed 1M VQA data. We present results in Figure 5. Within the 1M VQA setting,
stronger generation ability is correlated with improved VQA performance. This implies that increasing the
amount of generation data not only enhances generation but also positively impacts VQA performance.
This synergy scales across different LLMs. We examine whether the findings transfer across various LLM
backbones. Using a data composition of 7M VQA samples and 1M generation data, we train VPiT on
LLaMA-3 8B, LLaMA-3.1 8B, and LLaMA-3 70B. Figure 6 shows the scaling behavior across different LLMs.
Finding 2: Visual understanding and generation are synergistic. Increasing data for either capability
enhances both simultaneously.
6/uni00000018/uni00000017 /uni00000018/uni00000019 /uni00000018/uni0000001b /uni00000019/uni00000013 /uni00000019/uni00000015
/uni00000039/uni00000034/uni00000024/uni00000003/uni00000024/uni00000046/uni00000046/uni00000058/uni00000055/uni00000044/uni00000046/uni0000005c/uni00000003/uni0000000b /uni0000000c
/uni00000014/uni00000016/uni00000011/uni00000013/uni00000014/uni00000016/uni00000011/uni00000018/uni00000014/uni00000017/uni00000011/uni00000013/uni00000014/uni00000017/uni00000011/uni00000018/uni00000014/uni00000018/uni00000011/uni00000013/uni00000029/uni0000002c/uni00000027/uni00000003/uni00000036/uni00000046/uni00000052/uni00000055/uni00000048/uni00000003/uni0000000b /uni0000000c
/uni0000002f/uni0000002f/uni00000044/uni00000030/uni00000024/uni00000010/uni00000016/uni00000003/uni0000001b/uni00000025
/uni0000002f/uni0000002f/uni00000044/uni00000030/uni00000024/uni00000010/uni00000016/uni00000011/uni00000014/uni00000003/uni0000001b/uni00000025
/uni0000002f/uni0000002f/uni00000044/uni00000030/uni00000024/uni00000010/uni00000016/uni00000003/uni0000001a/uni00000013/uni00000025
/uni00000018/uni00000017 /uni00000018/uni00000019 /uni00000018/uni0000001b /uni00000019/uni00000013 /uni00000019/uni00000015
/uni00000039/uni00000034/uni00000024/uni00000003/uni00000024/uni00000046/uni00000046/uni00000058/uni00000055/uni00000044/uni00000046/uni0000005c/uni00000003/uni0000000b /uni0000000c
/uni00000015/uni00000019/uni00000011/uni00000018/uni00000015/uni0000001a/uni00000011/uni00000013/uni00000015/uni0000001a/uni00000011/uni00000018/uni00000026/uni0000002f/uni0000002c/uni00000033/uni00000003/uni00000036/uni00000046/uni00000052/uni00000055/uni00000048/uni00000003/uni0000000b /uni0000000c
/uni0000002f/uni0000002f/uni00000044/uni00000030/uni00000024/uni00000010/uni00000016/uni00000003/uni0000001b/uni00000025/uni0000002f/uni0000002f/uni00000044/uni00000030/uni00000024/uni00000010/uni00000016/uni00000011/uni00000014/uni00000003/uni0000001b/uni00000025/uni0000002f/uni0000002f/uni00000044/uni00000030/uni00000024/uni00000010/uni00000016/uni00000003/uni0000001a/uni00000013/uni00000025Figure 6 Comparison between different language backbones.
We jointly train 7M VQA and 1M Generation data on
different language backbones (LLaMA-3 8B, LLaMA-3.1
8B, LLaMA-3 70B). We observe that the synergy between
understanding and generation transfer across LLMs.
/uni00000014/uni00000030 /uni00000017/uni00000030 /uni0000001a/uni00000030
/uni00000039/uni00000034/uni00000024/uni00000003/uni00000027/uni00000044/uni00000057/uni00000044/uni00000015/uni00000013/uni00000013/uni0000002e
/uni00000018/uni00000013/uni00000013/uni0000002e
/uni00000014/uni00000030
/uni00000015/uni00000030
/uni00000016/uni00000030
/uni00000017/uni00000030/uni0000002a/uni00000048/uni00000051/uni00000048/uni00000055/uni00000044/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni00000027/uni00000044/uni00000057/uni00000044/uni00000024/uni00000059/uni00000048/uni00000055/uni00000044/uni0000004a/uni00000048/uni00000003/uni00000039/uni00000034/uni00000024/uni00000003/uni00000036/uni00000046/uni00000052/uni00000055/uni00000048
/uni00000014/uni00000030 /uni00000017/uni00000030 /uni0000001a/uni00000030
/uni00000039/uni00000034/uni00000024/uni00000003/uni00000027/uni00000044/uni00000057/uni00000044/uni00000029/uni0000002c/uni00000027/uni00000003/uni00000036/uni00000046/uni00000052/uni00000055/uni00000048
/uni00000014/uni00000030 /uni00000017/uni00000030 /uni0000001a/uni00000030
/uni00000039/uni00000034/uni00000024/uni00000003/uni00000027/uni00000044/uni00000057/uni00000044/uni00000026/uni0000002f/uni0000002c/uni00000033/uni00000003/uni00000036/uni00000046/uni00000052/uni00000055/uni00000048
/uni00000017/uni0000001b/uni00000018/uni00000013/uni00000018/uni00000015/uni00000018/uni00000017/uni00000018/uni00000019
/uni00000014/uni00000018/uni00000015/uni00000013/uni00000015/uni00000018
/uni00000014/uni0000001a/uni00000011/uni00000018/uni00000015/uni00000013/uni00000011/uni00000013/uni00000015/uni00000015/uni00000011/uni00000018/uni00000015/uni00000018/uni00000011/uni00000013Figure 7 Heatmap visualization of Average VQA Score, FID
Score, andCLIPScoreacrossvaryingamountsofVQAdataand
generationdata. Darkercolorsindicatebetterperformance.
Increasing VQA data is more effective for improving both
understanding and generation capabilities.
3.3 Understanding Data Contributes More
We investigate whether understanding and generation data contribute equally. Here, we jointly train different
scales of VQA data {1M, 4M, 7M} and generation data {200k, 500k, 1M, 2M, 3M, 4M}. Figure 7 summarizes
these findings, with the x-axis representing VQA data, and the y-axis representing generation data. Results
are visualized on heatmaps using darker colors for better performance.
The results indicate that increasing VQA data yields the most significant improvements in all three metrics.
When VQA data is relatively low (1M), increases in generation data lead to noticeable improvements, as
reflected by the gradual darkening in the plot. However, as the VQA data scales up (from 1M to 4M to 7M),
the impact of VQA data becomes more pronounced, demonstrated by a sharp color transition in the heatmap.
Ultimately, with 7M VQA data, increases in generation data contribute minimally. These results demonstrate
the critical role of understanding data in enhancing both understanding and generation performance.
Finding 3: While increasing data improves performance overall, the impact of visual understanding
data is significantly higher than the impact of visual generation data.
3.4 Certain Understanding Tasks Correlate More with Generation Performance
Given the diverse nature of understanding tasks such as OCR, Vision-Centric tasks, and Knowledge-based
tasks, we investigate which tasks most strongly correlate with generation ability. Inspired by Cambrian-1, we
categorize VQA tasks into five groups: General, Text&Chart, High-Resolution, Knowledge, and Vision-Centric
VQA. Using the results from our earlier experiments, which jointly train various VQA data scales with different
amounts of generation data, we plot each benchmark’s VQA performance against generation performance in
Figure 8. We also calculate the Pearson correlation ( ρ) between VQA scores and FID/CLIP Scores.
/uni00000014/uni00000018 /uni00000015/uni00000013 /uni00000015/uni00000018/uni00000019/uni00000015/uni00000011/uni00000018/uni00000019/uni00000018/uni00000011/uni00000013/uni00000019/uni0000001a/uni00000011/uni00000018/uni0000001a/uni00000013/uni00000011/uni00000013
/uni00000036/uni00000048/uni00000048/uni00000047
/uni00000003/uni00000020/uni00000003/uni00000013/uni00000011/uni0000001c/uni00000017
/uni00000014/uni00000018 /uni00000015/uni00000013 /uni00000015/uni00000018/uni00000019/uni00000013/uni00000019/uni00000018/uni0000001a/uni00000013/uni0000001a/uni00000018
/uni00000030/uni00000030/uni00000025/uni00000048/uni00000051/uni00000046/uni0000004b
/uni00000003/uni00000020/uni00000003/uni00000013/uni00000011/uni0000001b/uni00000019
/uni00000014/uni00000018 /uni00000015/uni00000013 /uni00000015/uni00000018/uni00000018/uni00000013/uni00000018/uni00000015/uni00000018/uni00000017/uni00000018/uni00000019/uni00000018/uni0000001b
/uni00000035/uni00000048/uni00000044/uni0000004f/uni0000003a/uni00000052/uni00000055/uni0000004f/uni00000047/uni00000034/uni00000024
/uni00000003/uni00000020/uni00000003/uni00000013/uni00000011/uni0000001b/uni0000001b
/uni00000014/uni00000018 /uni00000015/uni00000013 /uni00000015/uni00000018/uni00000015/uni00000018/uni00000016/uni00000013/uni00000016/uni00000018/uni00000017/uni00000013/uni00000017/uni00000018
/uni00000030/uni00000030/uni00000039/uni00000033
/uni00000003/uni00000020/uni00000003/uni00000013/uni00000011/uni0000001b/uni00000018
/uni00000014/uni00000018 /uni00000015/uni00000013 /uni00000015/uni00000018
/uni00000026/uni0000002f/uni0000002c/uni00000033/uni00000003/uni00000036/uni00000046/uni00000052/uni00000055/uni00000048/uni00000003/uni0000000b /uni0000000c
/uni00000015/uni00000013/uni00000015/uni00000018/uni00000016/uni00000013/uni00000016/uni00000018
/uni00000026/uni0000004b/uni00000044/uni00000055/uni00000057/uni00000034/uni00000024
/uni00000003/uni00000020/uni00000003/uni00000013/uni00000011/uni0000001c/uni00000015
/uni00000014/uni00000018 /uni00000015/uni00000013 /uni00000015/uni00000018/uni00000018/uni00000013/uni00000018/uni00000018/uni00000019/uni00000013
/uni00000037/uni00000048/uni0000005b/uni00000057/uni00000039/uni00000034/uni00000024
/uni00000003/uni00000020/uni00000003/uni00000013/uni00000011/uni0000001b/uni0000001a
/uni00000014/uni00000018 /uni00000015/uni00000013 /uni00000015/uni00000018/uni00000016/uni0000001b/uni00000017/uni00000013/uni00000017/uni00000015/uni00000017/uni00000017
/uni00000039/uni00000036/uni00000057/uni00000044/uni00000055
/uni00000003/uni00000020/uni00000003/uni00000013/uni00000011/uni0000001a/uni00000014
/uni00000014/uni00000018 /uni00000015/uni00000013 /uni00000015/uni00000018/uni0000001a/uni0000001c/uni0000001b/uni00000013/uni0000001b/uni00000014/uni0000001b/uni00000015
/uni00000036/uni00000046/uni0000004c/uni00000048/uni00000051/uni00000046/uni00000048/uni00000034/uni00000024
/uni00000003/uni00000020/uni00000003/uni00000013/uni00000011/uni00000019/uni00000015
/uni00000014/uni00000018 /uni00000015/uni00000013 /uni00000015/uni00000018/uni00000016/uni00000019/uni00000016/uni0000001b/uni00000017/uni00000013
/uni00000030/uni00000030/uni00000030/uni00000038
/uni00000003/uni00000020/uni00000003/uni00000010/uni00000013/uni00000011/uni00000015/uni00000019
/uni00000014/uni00000018 /uni00000015/uni00000013 /uni00000015/uni00000018/uni00000019/uni00000015/uni00000019/uni00000017/uni00000019/uni00000019/uni00000019/uni0000001b/uni0000001a/uni00000013
/uni00000003/uni00000020/uni00000003/uni00000010/uni00000013/uni00000011/uni0000001c/uni00000018
/uni00000014/uni00000018 /uni00000015/uni00000013 /uni00000015/uni00000018/uni00000019/uni00000013/uni00000019/uni00000018/uni0000001a/uni00000013/uni0000001a/uni00000018
/uni00000003/uni00000020/uni00000003/uni00000010/uni00000013/uni00000011/uni0000001b/uni00000019
/uni00000014/uni00000018 /uni00000015/uni00000013 /uni00000015/uni00000018/uni00000018/uni00000013/uni00000018/uni00000015/uni00000018/uni00000017/uni00000018/uni00000019/uni00000018/uni0000001b
/uni00000003/uni00000020/uni00000003/uni00000010/uni00000013/uni00000011/uni0000001b/uni00000018
/uni00000014/uni00000018 /uni00000015/uni00000013 /uni00000015/uni00000018/uni00000015/uni00000018/uni00000016/uni00000013/uni00000016/uni00000018/uni00000017/uni00000013/uni00000017/uni00000018
/uni00000003/uni00000020/uni00000003/uni00000010/uni00000013/uni00000011/uni0000001b/uni0000001a
/uni00000014/uni00000018 /uni00000015/uni00000013 /uni00000015/uni00000018
/uni00000029/uni0000002c/uni00000027/uni00000003/uni00000036/uni00000046/uni00000052/uni00000055/uni00000048/uni00000003/uni0000000b /uni0000000c
/uni00000015/uni00000013/uni00000015/uni00000018/uni00000016/uni00000013/uni00000016/uni00000018
/uni00000003/uni00000020/uni00000003/uni00000010/uni00000013/uni00000011/uni0000001c/uni00000015
/uni00000014/uni00000018 /uni00000015/uni00000013 /uni00000015/uni00000018/uni00000018/uni00000013/uni00000018/uni00000018/uni00000019/uni00000013
/uni00000003/uni00000020/uni00000003/uni00000010/uni00000013/uni00000011/uni0000001b/uni0000001a
/uni00000014/uni00000018 /uni00000015/uni00000013 /uni00000015/uni00000018/uni00000016/uni0000001b/uni00000017/uni00000013/uni00000017/uni00000015/uni00000017/uni00000017
/uni00000003/uni00000020/uni00000003/uni00000010/uni00000013/uni00000011/uni0000001a/uni00000015
/uni00000014/uni00000018 /uni00000015/uni00000013 /uni00000015/uni00000018/uni0000001a/uni0000001c/uni0000001b/uni00000013/uni0000001b/uni00000014/uni0000001b/uni00000015
/uni00000003/uni00000020/uni00000003/uni00000010/uni00000013/uni00000011/uni00000019/uni00000016
/uni00000014/uni00000018 /uni00000015/uni00000013 /uni00000015/uni00000018/uni00000016/uni00000019/uni00000016/uni0000001b/uni00000017/uni00000013
/uni00000003/uni00000020/uni00000003/uni00000013/uni00000011/uni00000015/uni00000016
Figure 8 Correlation analysis between generation and various understanding benchmarks. Results are collected by joint
training different amounts of VQA data combined with varying quantities of generation data. Each subplot shows the
correlation ( ρ) with a fitted regression line. Stars represent data points. We analyze General VQA, Vision-Centric
VQA, Text&Chart VQA, High-Resolution VQA, and Knowledge VQA. For most tasks, generation performance and
VQA performance are strongly correlated: higher VQA performance indicates better generation and vice versa. Only
knowledge-intensive and high-resolution VQA tasks exhibit weaker correlations with generation performance.
7Figure 8 shows that General, Vision-Centric, and Text&Chart VQA tasks strongly correlate with generation
performance, each with a Pearson correlation coefficient ( ρ) above 0.85. High-Resolution VQA exhibits
moderate correlation, with ρaround 0.7. In contrast, Knowledge VQA tasks, such as MMMU, show weak
correlation with generation performance. These findings suggest that generation ability aligns more closely
with the model’s vision capabilities rather than knowledge-specific tasks.
Finding 4: General, vision-centric, and text understanding VQA tasks exhibit strong correlations with
visual generation, whereas knowledge-based VQA tasks do not.
4 MetaMorph Model
Based on the insights in Section 3, we train our unified model, MetaMorph, based on LLaMA-3.1 8B (AI@Meta,
2024), using VPiT with the data curated in Section 2.2. We present our experimental results in three parts:
quantitative performance (Section 4.1), evidence of MetaMorph leveraging LLM knowledge in visual generation
(Section 4.2), and implicit reasoning skills in multimodal contexts (Section 4.3).
Image QA Video QA Generation
Method Base LLM
MMBenchEN
SEED
RealworldQA
MMVP
SQA
MMMU
VStar
ChartQA
TextVQA
MV-Bench
COCO (FID)
Visual Understanding Only
GPT-4V* 75.8 69.1 61.4 50.0 75.7 56.8 55.0 78.5 78.0 43.5 -
Visual Generation Only
Stable Diffusion 1.5∗- - - - - - - - - - 9.6
Dalle 2∗- - - - - - - - - - 10.4
Imagen∗- - - - - - - - - - 7.3
Unified Models
EMU-3∗58.5 68.2 57.4 36.6†89.2 31.6 51.8†68.6 64.7 - 12.8
Janus∗DeepSeek 1.3B 69.4 63.7 - - - 30.5 - - - - 8.5
VILA-U 256†LLaMA-2 7B 66.6 57.1 46.6 22.0 67.1 32.2 38.7 11.4 48.3∗40.8 19.6
Transfusion∗- - - - - - - - - - 6.7
Chameleon-7B†35.7 27.2 19.6 0.0 50.3 28.4 37.1 0.0 0.0 - 26.7∗
MetaMorph (ours) LLaMA-3.1 8B 75.271.858.348.383.241.844.037.160.5 48.8 11.8
Table 1 Comparison of MetaMorph with other unified models. MetaMorph offers competitive performance compared to
other leading unified models. Models in gray are understanding-only or generation-only. Unified models without a
base LLM are trained from scratch.∗We use numbers reported in original papers.†We obtain results using official
open-sourced model weights.
4.1 Competitive Performance in Understanding and Generation
We compare MetaMorph with other unified models and summarize results in Table 1. Since these models are
trained on different datasets and base LLMs (or pretrained from scratch), an apples-to-apples comparison
is difficult. Nevertheless, MetaMorph demonstrates competitive performance and outperforms other unified
models on most benchmarks—even when prior models may have been trained on more data. Compared to
models trained from scratch, such as EMU-3 (Wang et al., 2024b) and Chameleon (Team, 2024), MetaMorph
leverages the strengths of the latest pretrained LLMs and achieves competitive understanding and generation
performance. MetaMorph highlights that unified models can be developed effectively from pretrained LLMs.
8“Chhogori”“view of 
Chizarira ”
SD-3.58B
MetaMorphGround Truth 
/ Examples 
Janus
“A glass 
without water”“Slightly tall 
building”
“A bookshelf 
with few books”
 “Oncilla”“A bookshelf 
with many books”“A glass filled 
withwater”“Very tall 
building”
Professional Knowledge Addressing Semantic NuancesFigure 9 Examples of MetaMorph leveraging LLMs to generate visual tokens. Left : MetaMorph can leverage knowledge from
the LLM to generate visual tokens for professional terms that need domain-specific understanding. Right: MetaMorph
also avoids common mistakes seen in T2I models that condition on text embeddings (e.g., Stable Diffusion-3.5 8B).
4.2 MetaMorph can Leverage LLM Knowledge for Visual Generation
MetaMorph effectively leverages the world knowledge embedded in pre-trained LLMs. We show examples on
the left side of Figure 9. We prompt the model to generate concepts requiring non-trivial and specialized
knowledge. Examples include “Chhogori” (the world’s second-highest mountain), “Oncilla” (a small wildcat
from South America), and “Chizarira” (an isolated wilderness area in Zimbabwe).
MetaMorph successfully translates domain-specific knowledge into accurate visual tokens, thereby displaying
the ability to leverage world knowledge from LLMs . In contrast, the latestText-to-Image (T2I) model, Stable
Diffusion-3.5 8B, struggles to generate the correct concept despite producing high-quality images. This issue
may stem from the text embedding models it uses—–CLIP (Radford et al., 2021) and T5 (Roberts et al.,
2019)—–which fail to properly encode these specialized terms (Yuksekgonul et al., 2022).
On the right side of Figure 9, we demonstrate how MetaMorph handles common semantic challenges more
effectively than text embedding models such as CLIP and T5. These challenges include negation and
subjectivity, using prompts with common failure patterns identified in Multimon (Tong et al., 2024b).
MetaMorph differentiates semantic nuances such as “slightly” versus “very”, “few” versus “many”, and “without”
versus “with”, which are common failures in existing text-to-image systems.
4.3 Reasoning in Multimodal Generation
In Figure 10, we present examples where the model generates images in response to puzzle prompts such as
“The national flag of the country where Yellowstone National Park is located” . For each puzzle, we directly use
the prompt “Generate an image of {puzzle}” , without calling any Chain-of-Thought (CoT) (Wei et al., 2022b)
in the prompts. MetaMorph generates the correct image from prompts that require multi-step reasoning.
For example, when answering the question “A musical instrument, this instrument is often played by the
scientist who formulated the theory of special relativity” , the model needs to implicitly complete three reasoning
steps: it identifies Albert Einstein as the scientist formulated the theory of special relativity, recognizes that
his preferred instrument is the violin, and then directly generates correct visual tokens—a violin—without
explicitly separating these steps during the generation process. This result implies that MetaMorph implicitly
solves the puzzle and generates correct visual tokens immediately following the prompt. These results align
with the findings in Physics of LLMs (Ye et al., 2024; Allen-Zhu, 2024), where the authors suggest that LLMs
precompute reasoning graphs before autoregressively generating subsequent tokens. Here, we demonstrate
that this capability transfers to the unified multimodal model setting even when decoding visual tokens.
9SD3.5 -8B MetaMorphSolution
Examples Janus
Yellowstone National Park’s Location 
➟America 
➟American Flag
Sushi's Origin 
➟Japan 
➟Flower in Spring Festivals in Japan 
➟Cherry Blossom (Sakura)
Constellation Associated with the 
Northern Sky 
➟Ursa Major
➟Ursa (Latin for 'Bear’) 
➟Large Mammal Named 'Bear'Prompt
Scientist Who Formulated Special 
Relativity
➟Albert Einstein 
➟Instrument Often Played by Einstein 
➟Violin
Step -by-Step Logic Chain
(For Reference)
2+7
➟9 
➟Animal Believed to Have 9 lives 
➟Cat
“The national flag ofthecountry
where Yellowstone National Park
islocated”
“The flower celebrated inspring
festivals inthe country where
sushioriginated”
“The large mammal that shares
itsname with aconstellation
often visible inthenight skyand
associated with thenorthern part
oftheworld”
“A musical instrument, this
instrument isoften played bythe
scientist who formulated the
theory ofspecialrelativity”
“The animal associated with
having (2+7)lives”Figure 10 Examples of MetaMorph solving reasoning problems in visual generation. We design puzzles that require multi-step
reasoning. We include reference logic chains needed to solve the puzzles, and reference solution examples . When
prompting each model, we directly feed in the puzzle without any CoT hints or logic chains. MetaMorph has the
ability to implicitly solve these puzzles and generate the correct image without explicitly creating or processing a logic
chain. It demonstrates that the implicit reasoning skills in text-only LLMs can transfer to unified multimodal models.