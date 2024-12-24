With the rapid development of computer technology and the internet, information dissemination has increasingly become dominated by the internet, with social networks serving as key platforms for users to express opinions and emotions. On social media and short video platforms, user engagement has been continuously increasing. By the end of the first quarter of 2023, the number of monthly active users on Weibo reached 593 million, with 255 million daily active users. Especially during sudden public events, user interaction frequency on Weibo has significantly increased, forming a public opinion sphere in a short time. Moreover, Weibo, as an amplifier for information dissemination, has also enhanced the influence of online public opinion.

However, with the vast amount of comment data available, it is becoming increasingly difficult to manually analyze the potential direction and impact of public opinion on hot topics. Therefore, extracting key information from billions of comment texts and accurately analyzing users' emotional trends to provide refined public opinion guidance has become a significant challenge in the current research field.

Text sentiment analysis technology can extract valuable information from massive social media data, greatly improving the efficiency of user sentiment analysis. Although there have been significant advances in sentiment analysis research that combines deep learning in recent years, sentiment analysis of social media comment data still faces three major challenges: 1. Diversity of comment forms: Comments on different social platforms often present in multimodal forms, requiring consideration of the fusion of different modal features. 2. Informality of sentences and fast updates of new words: User comments are often informal, with low grammatical standards, and frequently use emerging popular terms, making sentiment analysis methods based on dictionaries or rules difficult to handle. 3. Complexity of sentiment word parts of speech: In Chinese corpora, a significant proportion of sentiment words are contained in verbs and nouns, but lowfrequency key noun sentiment words are often overlooked, making it difficult for sentiment word extraction or feature extraction models to capture the core emotional information in sentences.

This paper conducts experiments on Weibo comment texts, analyzing users' attention to hot public opinion events and their emotional attitudes. To effectively address the above challenges, this paper proposes a three-class sentiment analysis method based on Long Short-Term Memory (LSTM). LSTM captures the contextual semantics of texts and performs sentiment classification tasks. At the same time, the LSTM model demonstrates high accuracy and robustness in the comment sentiment classification task. This research not only validates the effectiveness of combining multimodal features but also provides a reference for further exploration in the field of sentiment analysis.