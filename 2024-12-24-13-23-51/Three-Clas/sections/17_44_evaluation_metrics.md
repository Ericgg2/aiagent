
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