
Sentiment analysis methods based on sentiment dictionaries are an early technology in the field of sentiment analysis. The core idea is to construct or use predefined sentiment dictionaries to analyze and compare the sentiment words in the input text, thereby predicting the sentiment polarity of the sentence. For example, the Chinese dictionary HowNet and the English dictionary WordNet are often used for the extension and optimization of sentiment dictionaries. However, the quality of sentiment dictionaries directly impacts the accuracy and stability of the model. Researchers have sought to improve classification performance by designing sentiment dictionaries from large-scale text data. For instance, some studies have constructed large-scale Chinese sentiment dictionaries using simple statistical methods, while others have optimized dictionaries by extending them with semantic relationships or domain-specific sentiment words based on existing dictionaries. Despite this, the applicability of sentiment dictionaries has significant limitations. For example, the meaning of sentiment words may vary in different contexts, leading to a decrease in classification accuracy. To address this issue, researchers have tried to combine sentiment dictionary methods with supervised learning. For instance, some studies have expanded sentiment dictionaries and combined them with self-supervised learning to train sentiment classifiers, significantly improving the accuracy of sentiment classification for ambiguous text. However, due to the difficulty of sentiment dictionaries in adapting to the rapid evolution of new vocabulary, their standalone application fails to meet the demands of the big data era, and research has gradually shifted towards traditional machine learning methods.[2, 3]