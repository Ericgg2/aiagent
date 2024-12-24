
In recent years, with the rapid development of the internet, the frequency of emotionally inclined texts on the web has gradually increased, making text sentiment analysis a hot research direction in the field of Natural Language Processing (NLP). For text sentiment analysis, research methods are mainly divided into three categories: methods based on sentiment dictionaries/rules, methods based on traditional machine learning, and methods based on deep learning.

#### *2.1. Sentiment Analysis Methods Based on Sentiment Dictionaries*/*Rules*

Sentiment analysis methods based on sentiment dictionaries are an early technology in the field of sentiment analysis. The core idea is to construct or use predefined sentiment dictionaries to analyze and compare the sentiment words in the input text, thereby predicting the sentiment polarity of the sentence. For example, the Chinese dictionary HowNet and the English dictionary WordNet are often used for the extension and optimization of sentiment dictionaries. However, the quality of sentiment dictionaries directly impacts the accuracy and stability of the model. Researchers have sought to improve classification performance by designing sentiment dictionaries from large-scale text data. For instance, some studies have constructed large-scale Chinese sentiment dictionaries using simple statistical methods, while others have optimized dictionaries by extending them with semantic relationships or domain-specific sentiment words based on existing dictionaries. Despite this, the applicability of sentiment dictionaries has significant limitations. For example, the meaning of sentiment words may vary in different contexts, leading to a decrease in classification accuracy. To address this issue, researchers have tried to combine sentiment dictionary methods with supervised learning. For instance, some studies have expanded sentiment dictionaries and combined them with self-supervised learning to train sentiment classifiers, significantly improving the accuracy of sentiment classification for ambiguous text. However, due to the difficulty of sentiment dictionaries in adapting to the rapid evolution of new vocabulary, their standalone application fails to meet the demands of the big data era, and research has gradually shifted towards traditional machine learning methods.[2, 3]

#### *2.2. Sentiment Analysis Methods Based on Traditional Machine Learning*

Traditional machine learning methods learn and extract text features through algorithms to determine the sentiment polarity of the text. These methods effectively avoid some of the drawbacks of sentiment dictionary-based approaches and have strong adaptability. Commonly used machine learning algorithms include Support Vector Machine (SVM), Naive Bayes, Decision Trees, K-Nearest Neighbors (KNN), and Random Forest, among others. In research, a multimodal joint sentiment topic model based on Weibo data (MJST) introduces emojis and user personality features. It analyzes users' hidden emotional characteristics and sentiment topic features using the Latent Dirichlet Allocation (LDA) model, which significantly improves the performance of unsupervised learning compared to traditional methods. Additionally, some studies have applied TF-IDF feature selection combined with the SVM model for sentiment classification of Tibetan corpus, enriching the research on Tibetan sentiment analysis. Although traditional machine learning methods outperform sentiment dictionary approaches in terms of performance, they suffer from poor transferability and high dependence on domain knowledge and manual labeling. With the development of deep learning technologies, sentiment analysis has gradually shifted towards deep learning methods.[4, 5]

#### *2.3. Sentiment Analysis Methods Based on Deep Learning*

Deep learning achieves feature extraction and learning from data through multi-layer neural networks, and in recent years, it has shown significant advantages in text sentiment analysis. Representative models include Convolutional Neural Networks (CNN) and Recurrent Neural Networks (RNN), among others.

Research has found that introducing attention mechanisms into deep learning models can significantly enhance the model's ability to identify key emotional information in text. For example, one study combined attention mechanisms with dynamic CNN and Bidirectional Gated Recurrent Units (BiGRU) to strengthen the model's ability to extract emotional features from text. Another study incorporated attention mechanisms into RNNs to further improve sentiment classification accuracy.

In recent years, pre-trained models such as BERT have driven the development of text sentiment analysis. Pre-trained models improve sentiment analysis performance by pre-training general models on large-scale unlabeled corpora and then fine-tuning them for specific tasks. For example, combining BERT with LSTM allows for more fine-grained sentiment classification. Additionally, some studies have used BERT?s dynamic representations of Weibo text, extracting contextual features and processing them with Bidirectional LSTM and attention mechanisms, while CNN captures local sentiment features to effectively perform sentiment polarity classification. To further enhance model performance, other studies have integrated semantic information from different hidden layers of BERT to generate richer feature vectors, thereby improving the model's ability to recognize sentiment tendencies.

In summary, deep learning-based sentiment analysis methods have progressively become mainstream, bringing new breakthroughs to sentiment analysis research in the realm of social networks. The introduction of pre-trained models has further expanded the boundaries of sentiment analysis technology.[6, 7]

## 3. Model Design and Construction

#### *3.1. LSTM Model Architecture*

Long Short-Term Memory (LSTM) networks are a type of Recurrent Neural Network (RNN) wellsuited for processing sequential data, capable of capturing long-term dependencies and sequence information within text data. Widely applied in natural language processing tasks, this paper opts to use an LSTM model independently for feature extraction and sentiment analysis on textual data, effectively modeling the sequential information of texts. The LSTM model primarily consists of an input layer, LSTM layer, and output layer, as illustrated in Figure 1.

The processed text sequences—having undergone tokenization and vectorization—are fed into the LSTM network. In the input layer, text data is transformed into fixed-length word vector sequences, serving as inputs to the LSTM. Through its unique gating mechanisms—the input gate, forget gate, and output gate—the LSTM network processes sequential data, effectively capturing significant contextual and temporal information within texts while avoiding the vanishing or exploding gradient problems common in traditional RNNs.

The output from the LSTM layer contains high-dimensional sequence features, which are then passed through a fully connected layer to further extract deep semantic information from the text. Finally, a Softmax classifier maps these features to a probability distribution across categories, completing the classification prediction for the sentiment analysis task. This overall model architecture is straightforward yet powerful, leveraging the advantages of LSTMs in sequence modeling to effectively mine emotional features from text data.

#### *3.2. Input Layer Structure*

The input layer of the LSTM model is responsible for converting raw text data into numerical vector representations that can be processed by the subsequent network layers. The design of the input layer involves three key steps: text preprocessing, word embedding representation, and input sequence construction.

Text Preprocessing: Raw text data undergoes tokenization, dividing it into individual words or subword units. Stopwords, special symbols, and redundant characters are removed to ensure the purity of the text data. Tokenized texts are then indexed, converting them into integer indices according to a vocabulary list.

Word Embedding Representation: Word Embedding technology, such as Word2Vec, GloVe, or randomly initialized embedding layers, maps the text data into continuous vector representations of fixed dimensions. Each input word is mapped into a low-dimensional word vector space where word vectors can capture semantic relationships and similarities between words. An embedding layer converts the indexed words into a word vector matrix with the shape (batch size, sequence length, embedding dim).

Input Sequence Construction: Text data is standardized to a uniform length by setting sequence length, padding shorter texts, and truncating longer ones. After passing through the embedding layer, the input text sequences form tensors of shape batch size,sequence length,embedding dim, which serve as inputs to the LSTM layer. Through the input layer's processing, raw text data is efficiently converted into numerical sequence representations suitable for LSTM network modeling, providing a foundation for capturing sequence features.

#### *3.3. LSTM Layer*

RNNs are particularly suited for handling linear sequence data, incorporating a recurrent structure within neural networks so that the current hidden layer is influenced not only by the input layer but also by the previous time step. To address the issues of vanishing and exploding gradients, LSTMs introduce storage and memory functions, controlling information flow through gating mechanisms, selectively forgetting some information. An LSTM unit includes an input gate, forget gate, output gate, and memory cell, as depicted in Figure 1.

![](_page_4_Figure_5.jpeg)

Figure 1: Diagram of RNN and LSTM cell structures

Forget Gate: Determines what information should be discarded from the current memory cell. The formula, translated into R-like syntax, is:

$$f_{t}=\sigma(W_{f}\cdot[h_{t-1},x_{t}]+b_{f})\tag{1}$$

![](_page_5_Figure_0.jpeg)

Figure 2: Forget Gate

Input Gate: Decides what new information should be stored in the current memory cell. The formulas, in R-like syntax, are:

$$i_{t}=\sigma(W_{i}\cdot[h_{t-1},x_{t}]+b_{i})\tag{2}$$

$$\tilde{c}_{t}=\tanh(W_{c}\cdot[h_{t-1},x_{t}]+b_{c})\tag{3}$$

Update Memory Cell: Updates the state of the current memory cell. The formula, in R-like syntax, is:

$$c_{t}=f_{t}\times c_{t-1}+i_{t}\times\tilde{c}_{t}\tag{4}$$

![](_page_6_Figure_0.jpeg)

Figure 3: ct

Output Gate: Determines what part of the current memory cell should be output. The formulas, in R-like syntax, are:

$$O_{t}=\sigma(W_{o}\cdot[h_{t-1},x_{t}]+b_{o})\tag{5}$$

$h_{t}=O_{t}\times\tanh(c_{t})$

![](_page_7_Figure_0.jpeg)

Figure 4: Output Gate

![](_page_7_Figure_2.jpeg)

Figure 5: LSTM

#### *3.4. Output Layer*

The output layer feeds the feature vectors produced by the LSTM model into a fully connected layer for dimensionality reduction. The fully connected layer then outputs the sentiment label categories, thereby completing the sentiment classification task. Finally, the Softmax function is utilized to normalize the outputs, resulting in the predicted sentiment polarity for the review texts.

#### 4. Experiments and Results Analysis

In this section, we first introduce our experiment settings including datasets, evaluation metrics and implementation details. Then we conduct a comparative analysis against state-of-the-art methods on various benchmark datasets. Finally, we perform the self-evaluations and ablation studies for our proposed model.

#### *4.1. Data Preparation*

The dataset used in this study consists of Weibo comment texts that were collected through web scraping, totaling 21,091 samples: 8,703 negative, 4,355 neutral, and 8,033 positive comments. To ensure the validity of the data, preprocessing steps were applied to the text data. This involved using regular expressions to remove punctuation, spaces, URLs, and Weibo-specific elements such as topics marked with "##" and usernames prefixed with "@"—all of which are irrelevant to sentiment analysis.

#### *4.2. Experimental Environment Setup*

The experimets were conducted using the PyTorch open-source deep learning framework on the AutoDL cloud environment(https://www.autodl.com/home).The specific experimental environment settings are shown in Table 1.

| Table 1: Experimental environment |  |
| --- | --- |
| Hardware environment |  |
| Operating system | Windows 10 64bit |
| CPU | 14 vCPU Intel(R) Xeon(R) Platinum 8362 CPU @ 2.80GHz |
| GPU | RTX 3090 (24GB) × 1 |
| Software environment |  |
| PyTorch | 1.11.0 (CUDA 11.3) |
| Python | 3.8 (Ubuntu 20.04) |
| Pandas | 2.0.3 |
| NumPy | 1.23.1 |
| scikit-learn | 1.3.2 |
| Gensim | 4.3.3 |
| TensorFlow | 2.9.0 |
| Jieba | 0.42.1 |

## *4.3. Parameter Settings*

- vocab dim = 100: This parameter sets the dimensionality of the word vectors, mapping each word to a fixed-length vector. Smaller dimensions (e.g., 50–100) result in faster training and lower memory usage but capture limited semantic information. Larger dimensions (e.g., 300) can capture richer semantic information but require longer training times. This is commonly used in word embedding models like Word2Vec and GloVe.
- n iterations = 10: This specifies the number of iterations for model training. More iterations can improve the quality of word vectors but also increase computational time.
- n exposures = 10: This sets the word frequency threshold, retaining only words that appear more than 10 times. Filtering low-frequency words reduces noise. This parameter typically corresponds to the min count parameter in Word2Vec.
- window size = 7: This controls the size of the context window, considering up to 7 words to the left and right of a target word as context. A smaller window captures local relationships, while a larger window captures broader contexts.
- n epoch = 4: This sets the number of epochs for model training. Each epoch represents one complete pass through the entire dataset. Increasing the number of epochs can enhance model performance but may introduce overfitting risks.
- input length = 100 and maxlen = 100: These parameters ensure that input sequences are fixed at length 100. Shorter texts are padded with zeros to reach the desired length, while longer texts are truncated to fit. This maintains consistency in input data, facilitating efficient computation for models like LSTM and CNN. These parameters are commonly used in Keras's Embedding layer and the pad sequences function.

## *4.4. Evaluation Metrics*

In this experiment, accuracy, precision, recall, and the F1 score are used as evaluation metrics. The confusion matrix for the prediction results is shown in Table 2.

- TP (True Positive): Indicates cases where both the predicted sentiment and the actual sentiment are positive.
- TN (True Negative): Indicates cases where both the predicted sentiment and the actual sentiment are negative.
- FP (False Positive): Indicates cases where the actual sentiment is negative but the model predicts it as positive.

- FN (False Negative): Indicates cases where the actual sentiment is positive but the model predicts it as negative.

| Table 2: Confusion Matrix |  |  |
| --- | --- | --- |
| Predicted Result |  |  |
| Actual Result Positive | Negative |  |
| Positive TP |  | FN |
| Negative FP |  | TN |

Accuracy represents the proportion of correctly predicted data out of all predictions. The formula for accuracy is:

$$A=\frac{TP+TN}{TP+TN+FP+FN}\tag{7}$$

Precision represents the proportion of correctly predicted positive instances out of all instances predicted as positive. The formula for precision is:

$$P=\frac{TP}{TP+FP}\tag{8}$$

Recall represents the proportion of correctly predicted positive instances out of all actual positive instances. The formula for recall is:

$$R=\frac{TP}{TP+FN}\tag{9}$$

The F1 score is the harmonic mean of precision and recall, giving equal weight to both. The formula for the F1 score is:

$$F1=\frac{2\cdot P\cdot R}{P+R}\tag{10}$$

*4.5. Results Analysis*

In the comparative experiments, this study selected four traditional machine learning baseline models (KNN, Random Forest, Logistic Regression, Naive Bayes), two deep learning baseline models (CNN, RNN), and two deep learning ensemble models that used the same dataset as this study (ERNIE-DAM, FastText-BGRU). These models were compared with the LSTM model used in this study. The specific results are described as follows:

From the experimental results, we can conclude the following:

- 1. Superiority of Deep Learning Models: Deep learning models can autonomously learn feature representations without requiring manual feature design and selection. They can automatically learn

| Model | Accuracy (%) | Precision (%) | Recall (%) | F1 Score (%) |
| --- | --- | --- | --- | --- |
| KNN | 55.07 | 55.65 | 69.46 | 45.75 |
| Random Forest | 74.44 | 86.96 | 57.51 | 69.23 |
| Logistic Regression | 83.23 | 83.12 | 83.38 | 83.26 |
| Naive Bayes | 83.13 | 83.10 | 83.24 | 83.10 |
| CNN | 84.80 | — | 84.90 | 84.90 |
| RNN | 86.56 | 86.53 | 86.63 | 86.58 |
| LSTM | 98.31 | 99.98 | 96.63 | 98.28 |

Table 3: Model Comparison Experimental Results

high-level, abstract features from raw data, better capturing semantic and contextual information. Traditional machine learning models typically require manual extraction and selection of appropriate features to represent text, which is a complex and labor-intensive process. Therefore, under general conditions, classification performance using deep learning algorithms outperforms traditional machine learning algorithms. In this experiment, the LSTM model showed improvements of 13% to 16% across all metrics compared to the best-performing traditional machine learning model.

- 2. Progressive Improvement in Deep Learning Baseline Models: Among the deep learning baseline models, performance improved progressively from CNN to RNN and finally to LSTM. - CNN primarily focuses on local features and lacks comprehensive consideration of context. - RNN has memory capabilities, allowing it to make predictions based on previous information. For tasks like sentiment classification, long-term context information is often more important. Thus, RNN's sentiment classification performance was 2% higher than CNN in the comparative experiments. - LSTM is an optimized variant of RNN with memory cells, input gates, forget gates, and other gating mechanisms, providing stronger expressive power and better maintenance of long-term dependencies. Therefore, in the comparative experiments, LSTM's sentiment classification results were approximately 6% higher than RNN.
#### 5. Conclusion

This paper thoroughly examines the application of LSTM (Long Short-Term Memory) models in Chinese sentiment analysis. Experimental results show that by capturing the contextual information of samples, the LSTM model significantly enhances the performance of sentiment classification. Comparative experiments demonstrate that our proposed model outperforms various classical traditional machine learning models, thereby validating its effectiveness and feasibility to some extent.

Future research can further address ambiguous comments. Specifically, for comments that contain multiple emotions, a multi-label classification approach can be employed to describe the complex emotional composition within these comments. By integrating contextual information, this method can better understand the different emotional contexts, thereby improving model performance and enhancing its generalization capability.

#### References

- [1] Z. Zhang, Q. Ye, Y. Li, A review of sentiment analysis research on internet product reviews, Journal of Management Science 13 (6) (2010) 13.
- [2] J. Liang, Y. Chai, H. Yuan, H. Zan, M. Liu, Sentiment analysis of weibo based on deep learning, Journal of Chinese Information Processing 28 (5) (2014).
- [3] G. Wang, J. Zhao, Research on sentence-level sentiment analysis based on multi-redundant labeling crfs, Journal of Chinese Information Processing 21 (5) (2007) 51–55.
- [4] X. Liu, D. Ji, Y. Ren, Product attribute sentiment analysis based on neural network models, Journal of Computer Applications 37 (6) (2017) 6.
- [5] S. Media, Research on prediction methods based on sentiment analysis of internet users (2013).
- [6] Z. Wang, W. Jiang, Y. Li, Research on extraction method of fixed collocation features in online review sentiment analysis, Journal of Engineering Management (4) (2014) 7.
- [7] L. Xie, M. Zhou, M. Sun, Multi-strategy chinese weibo sentiment analysis and feature extraction based on hierarchical structure, Journal of Chinese Information Processing 26 (1) (2012) 73–84.
