This section summarizes the fundamental ideas and context related to fatigue, its effects, and measurement methods. Subsequently, it reviews the systematic literature search approach to find pertinent studies on wearable and AI-based fatigue monitoring.

#### *2.1. Fatigue Background*

Fatigue is a multifaceted condition characterized by a decline in physical, cognitive, or mental performance due to prolonged activity or stress (see Figure 2) . This section explores the various types of fatigue and the impact of AI in detecting and managing fatigue, as well as reviews related studies that contribute to our understanding of this issue.

Fatigue occurs when one does not get enough sleep, works for an extended period at a high mental or physical intensity, or does the same mundane duties repeatedly [27]. A tired individual may not recognize their condition. Therefore, this could potentially create risk and has to be managed [28]. Suppose the fatigue condition of an individual can be diagnosed in time, and a corresponding early warning can be supplied. In that case, [28], there may be a significant reduction in the incidence of an accident due to fatigue. For instance, the Transport Accident Commission in Australia [29] reports that fatigue is a significant factor in 20%-30% of fatal road accidents in Australia. Also, research indicates that fatigue is directly responsible for 30% of all fatal accidents in the manufacturing sector [30]. Workers who are very drowsy or exhausted are 70% more likely to be engaged in industrial mishaps than attentive and well-rested workers [31]. There are two main types of fatigue physical and cognitive [32]. Each type could be then divided into three levels according to the severity of fatigue: acute, normative, and chronic, as shown in Figure 3. Acute fatigue is a normal response to physical or mental activity and typically lasts for a short period, for example, after a long day or a hard workout. Rest, sleep, and other forms of relaxation can help with acute fatigue.

![](_page_3_Figure_1.jpeg)

Figure 2: Identified two main types of fatigue.

Chronic fatigue is a more severe and long-term type of fatigue. It is characterized by persistent feelings of exhaustion that are not relieved by rest and sleep. Underlying medical conditions, such as anemia, diabetes, thyroid disorders, and certain infections, can cause chronic fatigue. Lifestyle factors, such as poor nutrition, lack of exercise, and chronic stress, can also cause it. Normative fatigue is a type of fatigue that is considered normal and acceptable. It is a normal part of aging, familiar in healthy people with demanding jobs, children, or other responsibilities. Normative fatigue is a state of tiredness that can be managed with good sleep hygiene and healthy lifestyle habits, but it doesn't require medical attention.

There is a growing interest in detecting and monitoring mental and physical fatigue using wearables and artificial intelligence [28] [33] [34] [35] [36] [37]. According to a recent search of Engineering Village ©, more than 8,000 articles have been published between 2015 and 2024 on the topic of fatigue measurement and detection based on human medical or physiological data (see Fig. 4). Fatigue is subjective to be reliably measured; however, it depends on many other physical, mental, and environmental multidimensional factors [38]. A growing body of evidence suggests that lifestyle, social, psychological, and general wellness difficulties, rather than a pre-existing medical illness, are primary contributors to fatigue. It is essential to differentiate mental fatigue from neuromuscular fatigue (muscle fatigue). Muscle or neuromuscular fatigue results from repeated muscle actions [39]. In contrast, mental fatigue is the inability to execute mental activities involving self-motivation and internal signals without physical reason.

Human fatigue may be better understood by using physiological signals. These signals may aid in early diagnostics and therapeutics by estimating essential biomarkers, which can reveal the fatigue state formed in the human body. To create a fully automated detection system, studies of physiological signals have undergone significant evolution in recent years [40]. There are a variety of techniques available for identifying signs of fatigue.

Recent studies have shown that methods for identifying static muscle fatigue are relatively advanced [37]. Sensing devices are often used for signal collection. The subjective and objective levels of human fatigue are used to determine the muscular exhaustion state, and various classification techniques are developed [37]. However, there are still many obstacles to overcome when studying fatigue-detecting technologies. There is currently no clear-cut solution for measuring fatigue objectively. Various methods have been proposed, including self-report questionnaires, physiological measures, and performance-based tests, but each has limitations and may not provide a comprehensive assessment of fatigue. Additionally, fatigue is a complex and multidimensional phenomenon that can be influenced by various factors, such as physical and mental demands, sleep quality, and overall health, making it difficult to quantify accurately. Therefore, it is essential to consider multiple measures and approaches when assessing fatigue [41].

![](_page_3_Figure_7.jpeg)

Figure 3: Three forms of fatigue are identified.

Advances in wearable and consumer electronics have significantly improved physiological signal measurements. Wearable devices such as smartwatches, fitness trackers, and bright clothing can now monitor various physiological parameters, including heart rate, respiration, and body temperature. Additionally, many devices now include sensors that can measure other necessary physiological signals, such as electrodermal activity, which can provide insight into stress levels, and EMG, which can provide information about muscle activity. Consumer electronics like smart glasses and head-mounted displays are also being used for physiological signal measurements in research settings like EEG [42], ECG [43] , [44], PPG [45], EOG [46], EEG [47] and many others. These devices are becoming increasingly sophisticated, with many now including advanced algorithms and machine learning capabilities to provide more accurate and detailed data. This allows for monitoring physiological signals in real-time, providing new opportunities for research, healthcare, and personal use.

On the other hand, the availability of edge and cloud computing has dramatically expanded the capabilities for processing and analyzing data [48]. Edge computing refers to using resources close to the data source, such as on a device or at the network edge, allowing for real-time data processing and analysis [49]. With cloud computing, data can be easily stored, shared, and analyzed by multiple users and devices [50]. This has led to the development of cloud-based platforms and services for data

analysis and machine learning, making it easier for organizations and individuals to gain insights from their data [51]. Together, edge and cloud computing provide a powerful combination of capabilities that can be leveraged to process and analyze data in various applications.

Power BI Desktop

![](_page_4_Figure_1.jpeg)

Sum of Published studies - Human f…

Figure 4: Published studies between 2015 and 2024 related to fatigue detection using physiological data (as per a search conducted on Engineering Village©).

AI and wearables for fatigue monitoring have numerous applications, but they are still in their infancy. The ability to continuously monitor physiological signals in real-time using wearable [52] and analyze the data using AI algorithms can revolutionize how we understand and manage fatigue [53]. However, despite the potential, the field of fatigue monitoring using AI and wearable is still in its early stages, and a lot of work needs to be done to develop robust and validated methods. The physiological markers of fatigue are poorly understood, and the algorithms used to analyze the data are still being developed and refined [54]. Additionally, the wearable used for monitoring must be validated for accuracy and reliability. Despite these challenges, the potential benefits of using AI and wearable for fatigue monitoring make it a promising area of research and development.

In light of what has been said before, According to a recent search of Engineering Village©, between 2015 and 2024, 8,121 scholarly articles were published on fatigue measurement and detection based on human medical or physiological data (see Figure 4).

#### *2.2. Literature Search Strategy*

This section outlines the systematic literature review methodology, including the databases used, search parameters, and inclusion criteria. A four-phase flowchart of the literature search and selection procedure is illustrated in Figure 5 , providing a clear and organized representation of the steps taken in the literature selection process. This framework shows the sequential steps from searching databases, screening, ensuring the relevance of articles, and final inclusion of research papers for a

systematic review of articles related to fatigue monitoring using wearable technologies and AI.

#### *2.2.1. Search Methods*

For this review, four major databases were utilized to identify and select relevant studies on fatigue monitoring using wearable technologies and AI: Google Scholar, IEEE Xplore Digital Library, Web of Science (WoS), and Scopus. Google Scholar was included due to its broad coverage of academic sources across multiple disciplines. IEEE Xplore Digital Library was selected for its focus on high-quality, peer-reviewed technical and engineering research, particularly in AI and wearable technologies. Scopus was used for its extensive coverage of citations and abstracts from international peer-reviewed literature, while WoS provided access to comprehensive bibliometric analysis and citation metrics.

The following keywords were used in the search process: "Fatigue Monitoring," "Wearable Technology," "Artificial Intelligence," "Machine Learning," "Deep Learning," "Physiological Signals," "ECG," "EEG," "EMG," "PPG," and "EOG." Boolean logical operators were used to combine search terms such as "Fatigue Monitoring" AND "Wearable Technology" to target relevant articles. Additionally, terms like "Artificial Intelligence" OR "Machine Learning" were combined to ensure the inclusion of articles that addressed AI in fatigue monitoring. To broaden the scope, we also included physiological signal modalities like "ECG," "EEG," "EMG," and "PPG."

#### *2.2.2. Inclusion and Exclusion Criteria*

We included original research articles written in English that focused on fatigue monitoring through wearable technologies and AI, with an emphasis on fields such as computer science, engineering, and healthcare. No restrictions were placed on publication dates, given the recent advancements in AI and wearable technologies. Secondary studies, reviews, book chapters, editorials, patent documents, and conference papers were excluded to ensure a focus on primary research. This strategy ensured that our review centered on the most relevant and high-quality studies directly addressing our research questions.

#### *2.2.3. Data Extraction and Structured Meta-analysis*

During the first screening stage, titles and abstracts were carefully reviewed to identify papers related to fatigue monitoring using wearable technologies and AI. Multiple reviewers independently conducted full-text screening, with disagreements resolved through discussion. Data extraction was managed using Google Sheets, which recorded details of inclusion or exclusion, enabling systematic data management. The extracted data focused on critical issues such as wearables, AI methodologies, and physiological signal types in fatigue monitoring. Studies that lacked transparent methodologies or did not explicitly focus on fatigue detection through AI or wearables were excluded. Tabulation techniques supported the data extraction process, guaranteeing that the study's outcomes were consistent with the research objectives. Methodological approaches from the selected articles were evaluated, and those with vague definitions or unclear methods were disqualified.

![](_page_5_Figure_0.jpeg)

Figure 5: PRISMA flowchart used for our systematic review.

The final data was systematically organized, allowing for a structured meta-analysis and presentation of findings in this review. Each article's methodological data were thoroughly assessed and organized to ensure relevance to the research focus on fatigue monitoring using AI and wearables.

#### 3. Datasets Availability for Fatigue Monitoring

High-quality datasets are essential for advancing the efficacy of fatigue monitoring systems that leverage wearable technologies and AI. They help to improve the accuracy of detecting fatigue through physiological signals like ECG, EMG, EEG, PPG, and EOG. This section summarizes significant publicly accessible datasets pertinent to the study of fatigue detection.

#### *3.1. Physiological Signal-Based Datasets*

Datasets based on physiological signals concentrate on the acquisition of vital physiological indicators, which play a significant role in identifying fatigue and examining the body's reactions to physical and mental stress.

#### *3.1.1. PhysioNet*

PhysioNet is an extensive repository that provides access to various physiological signal datasets, encompassing ECG, EEG, and PPG [55]. It is extensively utilized in numerous healthrelated investigations, particularly fatigue monitoring. PhysioNet provides a wide range of data that can be used to create

fatigue detection models by combining different physiological signals [56]. This makes the models more accurate and valuable in healthcare and fitness.

#### *3.1.2. DREAMER*

The DREAMER dataset includes EEG and ECG signals [57]. Initially created for emotion recognition, it is also a valuable resource for fatigue detection. This tool effectively records physiological responses across various cognitive and emotional tasks, an essential resource for exploring mental fatigue and cognitive workload [58]. The dataset uses machine learning and deep learning models to evaluate mental states like fatigue.

#### *3.1.3. SEED*

The SJTU Emotion EEG Dataset (SEED) comprises EEG data collected during cognitive tasks and is commonly utilized to detect mental fatigue [59]. The dataset comprises recordings from participants engaged in emotionally stimulating tasks, facilitating an analysis of the effects of fatigue on cognitive functions. Although the main emphasis is on mental fatigue, SEED is an essential resource for investigating cognitive workload [60].

#### *3.1.4. SPhysio*

SPhysio encompasses various physiological signals, such as ECG and PPG, which are instrumental in investigating physical fatigue in exercise and fitness environments [61]. This dataset facilitates the development of models to detect and manage fatigue

in environments characterized by physical demands, including sports and labor-intensive occupations.

#### *3.2. Behavioral and Video-Based Datasets*

Datasets that encompass behavioral and video-based elements are designed to capture visual and behavioral markers of fatigue, including facial expressions, eye movements, and yawning. These datasets are frequently utilized in real-time fatigue detection systems, leveraging computer vision and AI methodologies.

#### *3.2.1. YawDD*

The Yawning Detection Dataset (YawDD) [62] comprises a series of video recordings designed to document yawning behaviors, which have been gathered to detect driver fatigue. The dataset comprises labeled yawning events, significant markers of drowsiness within driving scenarios [63]. This dataset is often utilized alongside computer vision methodologies to create systems for real-time fatigue detection by analyzing facial expressions.

#### *3.2.2. CEW*

The Closed Eyes in the Wild (CEW) dataset comprises images depicting individuals with both open and closed eyes, serving as a resource for detecting drowsiness in practical environments [64]. The detection of fatigue is particularly significant in contexts where eye closure may serve as an indicator of diminished alertness, notably in driving scenarios. This dataset serves as a valuable resource for the training of deep learning models that utilize facial cues to evaluate levels of drowsiness and fatigue.

#### *3.3. Multi-Modal Datasets*

#### *3.3.1. Driver Fatigue*

The Driver Fatigue Dataset comprises EEG, EOG, and behavioral data from drivers engaged in extended driving sessions [65]. The development of fatigue detection systems in automotive safety is of significant importance, particularly due to the necessity for real-time monitoring to mitigate the risk of accidents resulting from drowsiness. This dataset facilitates the investigation of machine learning algorithms aimed at identifying early indicators of fatigue through the analysis of neural and ocular activities.

#### *3.3.2. DROZY*

The DROZY dataset includes different types of multi-modal data, like EEG, ECG, EOG, and video recordings that were collected in certain ways to make people sleepy [66]. This dataset has a lot of potential for studies that look at how to detect fatigue, especially when it comes to situations where combining physiological signals and behavioral data is important for making accurate predictions about fatigue levels [67]. This approach frequently assesses machine learning models for realtime fatigue monitoring within practical applications.

Although various datasets are accessible, there are ongoing challenges related to data quality, the applicability of data in realtime scenarios, and the need for standardization across different

studies. Numerous datasets exhibit inconsistencies that hinder the development of generalizable models. Variations in sensor quality, participant characteristics, and experimental conditions may restrict their applicability across different domains. Furthermore, numerous datasets are structured for static or short-term investigations, which poses challenges for ongoing observation in practical settings.

#### 4. Fatigue Measurement Methods

This section focuses on the diverse methodologies for assessing fatigue, including subjective self-reports, performancerelated tests, bio-mathematical models, behavioral observations, and physiological signal-based approaches. Each offers unique insights into the detection and quantification of fatigue.

The term "fatigue measurement" is used to describe the process of determining how tired a person is. Self-report surveys, physiological markers, and performance assessments are just a few ways fatigue may be evaluated. Lack of sleep, strenuous activity, stress, and medical problems, including depression and chronic fatigue syndrome, are all potential contributors to tiredness. Work schedule, shift work, and poor sleep quality are other causes of fatigue. Recognizing and addressing the root causes of tiredness is crucial because of its detrimental effects on people's safety, productivity, and quality of life.

Although several methods have been presented for fatigue diagnosis and monitoring, there is currently no agreed-upon method for quantifying fatigue [68]. Figure 6 demonstrates the most common methods used for fatigue monitoring. In this section, we briefly discuss these methods.

#### *4.1. Subjective Measure*

Subjective fatigue measurements analyse an individual's fatigue perception [69]. Self-report questionnaires or surveys ask people to assess their exhaustion on various scales. Visual analog scales, numerical rating scales, and multi-item fatigue inventories assess subjective exhaustion. These scales may ask people to score their fatigue level, frequency, duration, or associated symptoms like drowsiness or energy. Subjective fatigue measurements may reveal an individual's reported exhaustion and monitor changes over time. However, they are biased and may not appropriately reflect fatigue levels. Therefore, subjective fatigue assessments should be combined with objective performance measures or physiological indicators to provide a complete picture of an individual's fatigue levels [70].

#### *4.2. Performance Related Methods*

Methods based on performance depend on the observation that people's mental and, by extension, physical capacity to carry out a set of activities reflects their degree of exhaustion. Neuro-behavioral tasks are used in these approaches to evaluate a subject's cognitive abilities (such as alertness, hand-eye coordination, sustained attention, and response time). Although performance-related procedures may be standardized with relative ease, they cannot be utilized to identify the onset of fatigue in time to avoid an accident.

![](_page_7_Figure_0.jpeg)

Figure 6: Common techniques and frameworks used in literature for fatigue measurement and monitoring.

![](_page_7_Figure_2.jpeg)

Figure 7: Common techniques and frameworks used in [68] for fatigue measurement and monitoring.

# *4.3. Bio-mathematical Models*

In line with [68], subjects' fatigue levels are predicted by biomathematical models using data on their sleep-wake schedules, work-rest patterns, and circadian rhythms. The aviation industries of both the military and the civilian sectors are frequently employed to evaluate the danger of fatigue. These models are the product of research on the effects of both partial and complete sleep deprivation. Wrist-mounted actigraphy has replaced subjective reporting to improve the accuracy of sleep and waking time estimations.

Several bio-mathematical models have been developed to measure fatigue, each with advantages and limitations. Some of the most commonly used models include:

- The Fatigue Severity Scale (FSS): This is a self-report questionnaire that measures the impact of fatigue on various aspects of daily life, such as work, social activities, and mental health. It is a widely used tool for assessing fatigue in various medical conditions, including chronic fatigue syndrome and cancer-related fatigue.
- The Chalder Fatigue Scale (CFQ): This is another selfreport questionnaire that measures fatigue in 11 items. It is widely used in clinical research and in primary care to diagnose chronic fatigue syndrome.
- The Piper Fatigue Scale (PFS): This self-report questionnaire measures the frequency and severity of different types

of fatigue. It is widely used in cancer-related fatigue research and in primary care.

1

- The Fatigue Impact Scale (FIS): This is a self-report questionnaire that measures the impact of fatigue on various aspects of daily life, such as physical, emotional and social functioning.
- The Multidimensional Assessment of Fatigue (MAF): This is a self-report questionnaire that measures the frequency, severity and impact of fatigue on various aspects of daily life, such as physical, emotional, and cognitive functioning.

These models are widely used in various fields, including research and clinical practice, to evaluate fatigue and its impact on quality of life. They can be used in different conditions as a way of measuring the fatigue levels of patients, but ultimately, the choice of the right tool depends on the condition, population, and goals of the assessment.

#### *4.4. Behavioural-Based Methods*

Behavioral-based methods for fatigue monitoring involve observing and measuring an individual's behavior to detect signs of fatigue. As per authors in [68] [45] [71] [72], external symptoms of exhaustion, such as yawning, sighing, eyelids closing, or head nodding, are observed and accounted for using behaviorallybased procedures (see Figure 7). Therefore, metrics associated with eye movements, head motion, and facial expression are often used as input characteristics in technologies belonging to this class.

#### *4.5. Physiological Signal-based Methods*

Fatigue monitoring using physiological signals involves measuring an individual's physiological responses to detect signs of fatigue. Some commonly used physiological signals for fatigue monitoring include EEG, ECG, EMG, and EOG. These methods are highly accurate, non-invasive, and can objectively measure fatigue. They are widely used in various fields, such as transportation, aviation, and shift work, to monitor fatigue levels and prevent accidents. Choosing the right physiological signals to monitor fatigue depends on the context, population, and assessment objectives (see Section 6 for a comprehensive review of these methods).

Figure 8 shows the overall AI/ML pipeline for fatigue monitoring using physiological signals. Once wearables collect the data, pre-processed, filtered, and then cleaned. Then an AI/ML model is developed, optimized, and validated to predict the response variable (here fatigue). This model is then fully tested and deployed for real-world applications.

#### 5. Physiological Signals for Fatigue Monitoring

Physiological signs are often used as a reliable and noninvasive technique to determine the level of fatigue [73]. unfortunately, most other non-physiological signal-based techniques primarily concentrate on accuracy rather than forecasts for fatigue effectiveness. The resulting procedures are less reliable

and accurate, making them inappropriate for fatigue diagnosis and monitoring. To solve this problem, the research world has proposed magnificent, complete frameworks for the early identification of fatigue by modeling data collected from wearables, relying on physiological signal-based approaches. Below are the core benefits of utilizing an approach based on physiological signals.

#### *5.1. Data-driven (objective vs subjective)*

As a quantitative record of the human body's dynamic physiological processes, physiological-driven data provides an accurate and impartial snapshot of the human body in its present setting [38]. Researchers can better identify and predict fatigue using physiological data-driven methods because they can act on the most relevant information at the most relevant moment. Furthermore, data-driven is a cornerstone of predictive analytics. Physiological data as objective-driven data should allow for a neutral and evidence-based evaluation of fatigue. Important judgments should not be made solely on subjective data for recognizing fatigue since it requires making assumptions and interpretations based on non-data observations without verified facts.

### *5.2. Real-Time Monitoring*

Collection of physiological signals allows the end user to monitor fatigue in real time [42] [46] [74] [75] [76]. Realtime fatigue monitoring using physiological signals can provide several benefits, including improved safety, increased efficiency, better understanding of fatigue, better treatment, and greater performance.

#### *5.3. Edge Processing*

Edge computing improves the speed and accuracy of fatigue detection using physiological data. Think about the possibility of using the analysis of sensor physiological data collected at the distant wearable's application cloud to keep tabs on the wearable's health. Such wearables have the potential to generate dozens, if not millions, of data points each second. Raw data transmission to a faraway data center may be excessively timeconsuming and resource-intensive without pre-processing at the edge to remove irrelevant information. This is particularly true if the network link is unreliable.

# *5.4. Using Advanced AI and DL*

The AI revolution for processing physiological signals for human performance monitoring has been driven by the emergence of wearables, big data, and the ability to perform real-time analysis. The availability of advanced AI/ML techniques for data processing has greatly expanded in recent years, enabling organizations to gain insights from a wide range of data sources, including time series data and multi-source data. These techniques include machine learning, deep learning, natural language processing (NLP), and computer vision. These techniques are widely used in various industries, such as healthcare, finance, transportation, and manufacturing, and are available through various commercial and open-source software platforms and

libraries. Furthermore, with the ongoing research and development in the field, new techniques and improvements are continually being developed, making them even more powerful and accessible, especially with the fast data processing capabilities that are now possible. This allows individuals to quickly gain insights from large and complex datasets (here, mainly time-series of physiological signals), which can be used to make data-driven decisions and improve operations (see Fig. 8 for the pipeline).

In addition to commercial software platforms and libraries, there are also a number of open-source Python packages, such as sci-kit-learn and Pytorch, that are widely used for processing physiological data. These packages provide a wide range of tools for data analysis, machine learning, and deep learning and are widely used by researchers and practitioners in the field. They are also very flexible and can be easily integrated with other tools and packages, making them a popular choice for physiological data analysis.

#### 6. Fatigue Monitoring using Wearables and AI

The goal of fatigue monitoring using wearables and AI is to employ cutting-edge technology to reliably and continually evaluate an individual's state of fatigue [68]. Refer to Figure 8, Smart-watches, fitness trackers, and sleep monitors are all examples of wearable technology that may give continuous, objective data on physiological and behavioural indicators of fatigue, such as heart rate, activity levels, and sleep patterns [77]. Next, artificial intelligence systems may examine these records to glean useful insights about a person's fatigue.

One of the key benefits of fatigue monitoring using wearables and AI is the provision of continuous real-time data on an individual's degrees of fatigue [78]. This paves the way for early diagnosis of fatigue-related concerns, including lower performance or increased accident risk, and may guide actions to enhance health and happiness. Also, those at a greater risk for fatigue-related problems, such as shift workers, truck drivers, and athletes, may have their muscle fatigue tracked using wearables and AI.

Although wearables and AI have many potential benefits for fatigue monitoring, they are not without their drawbacks. There are several variables, such as an individual's degree of physical activity, might distort the data obtained by wearables, making it possible that they do not always provide an accurate reflection of a person's genuine fatigue levels. The quality of the data, the complexity of the algorithm, and the existence of outliers or noise in the data may all impact the accuracy of AI algorithms while evaluating the data [79]. Therefore, before deploying wearables and AI-based fatigue monitoring systems in the wild, testing and assessing their efficacy is crucial.

Figure 9 shows the overall process of using wearables and AI to monitor the performance of an individual. An individual's wearables passively measure physiological data such as heart rate, skin temperature, and movement patterns. This data is then processed and cleaned to remove noise or irrelevant information. After the data is cleaned, AI algorithms such as machine learning and deep learning are used to model the data. These AI models are then used for prediction, providing insights to the

![](_page_9_Figure_0.jpeg)

Figure 8: The overall AI/ML pipeline for processing physiological data measured by wearables.

end-users on fatigue level, sleep quality, and stress level. This process allows for non-invasive and continuous monitoring of an individual's physiological state, providing valuable insights for healthcare professionals, researchers, and individuals to improve their overall health and well-being.

Wearable sensor fatigue monitoring is a method in which tiny, portable devices are worn on the body to gather information on several physiological and behavioral indicators of exhaustion, such as heart rate, activity levels, and sleep patterns [80]. Smartwatches, fitness trackers, and sleep monitors are all examples of wearable sensors that may collect data via EEG, ECG, EMG, and PPG.

Figure 10 shows a detailed workflow of the entire process of physiological signal management, starting from patient preparation, where the patient is readied for signal data acquisition. The raw physiological signals are then captured and undergo initial signal processing to extract and label key features indicative of cardiac activity. The processed signals are further transformed through feature extraction techniques, preparing them for advanced analysis. These features are subsequently mapped into a high-dimensional space using deep learning methods, which facilitate the detailed modeling of the signals. The model is finetuned to maximize the similarity between the extracted features and known patterns of various conditions. The final step involves using this trained model to predict specific heart conditions from new signals, categorizing them into Low, Moderate, High, or Very High fatigue conditions. This streamlined depiction emphasizes integrating clinical practices with advanced computational techniques to enhance diagnostic accuracy in fatigue.

#### *6.1. ECG-based Methods*

Fatigue detection utilizing ECG and AI technologies incorporates complex machine learning algorithms to conduct a detailed analysis of an individual's HRV. This method involves examining the temporal variations in heart rate, capturing and analyzing the minutiae of its fluctuation patterns. Decreased HRV, indicated by fewer variations between consecutive heartbeats, serves as a critical biomarker for fatigue. It reflects diminished activity and adaptability of the autonomic nervous system, particularly the sympathetic and parasympathetic branches, under stress or fatigue. By mapping these variations and linking them to physiological responses, this approach provides an insightful,

quantifiable indicator of an individual's fatigue levels over time (See Figure 10).

The AI-based ECG analysis process begins with patient preparation and collection of raw ECG signals, which are then preprocessed to remove noise and artifacts. After pre-processing, important heart wave parts like atrial depolarization waves, ventricular depolarization complexes, and ventricular re-polarization waves are found. This wave information is then refined and prepared to produce labeled ECG data. The next step involves feature extraction, where deep learning techniques map significant features from the ECG signals into a high-dimensional space. The model is subsequently tuned to enhance similarity with known cardiac conditions, optimizing its predictive accuracy. The labeled data is analyzed in the detection and labeling phase to identify cardiac abnormalities, such as arrhythmias and ischemic events. Finally, healthcare professionals display the labeled ECG data for further analysis and review. This comprehensive process ensures accurate and efficient ECG analysis, leveraging advanced AI techniques to develop robust prediction models that can accurately identify conditions such as normal heart function (NORM), myocardial infarction (MI), congestive heart failure (CHF), and hypertrophy (HYP), showcasing the efficacy of AI in improving cardiac diagnostics and patient outcomes (See Figure 11).

Current research in fatigue assessment highlights the critical role of ECG in advancing automated and objective monitoring methods. Wearable ECG devices have been shown to continuously and non-invasively monitor HRV indicators, which are essential for figuring out how tired someone is in real time without getting in the way of daily life [81]. Researchers have shown that ECG signals can accurately pick up on different levels of driver hyper-vigilance, such as drowsiness and cognitive inattention, using advanced classifiers [43]. The integration of ECG with video signals has shown significant promise in educational settings, achieving detection accuracies as high as 99.6%, making it a powerful tool for identifying fatigue [82]. Using R-R intervals from ECG data in a new way has helped find tired drivers, and advanced statistical models like AR-GARCH are good at spotting changes from alert to tired states [83]. Realtime fatigue detection using short-time period ECG signals has also been validated, demonstrating practical application potential [35]. Using machine learning models to find mental fa-

![](_page_10_Figure_0.jpeg)

Figure 9: The overall pipeline of fatigue monitoring using wearable and AI.

tigue using ECG has been successful over 94.5% of the time, showing that ECG features could be used for accurate fatigue monitoring [84]. Techniques such as wavelet transform have further improved the accuracy of driver drowsiness detection by minimizing noise interference [85]. High accuracy in driver drowsiness detection using wrist-worn ECG devices underscores the potential for integrating ECG technology into consumer devices and vehicles [86]. Smart bracelets with ECG sensors have effectively assessed driving fatigue levels, demonstrating their practical application [76]. Predicting exhaustion thresholds using ECG features and artificial neural networks has shown high accuracy, benefiting athletes through precise monitoring [87]. The integration of ECG in FDA-approved wearable devices for heart health monitoring further underscores its potential to revolutionize healthcare through continuous and personalized data analysis [75]. Additionally, research has identified specific ECG parameters correlating with fatigue, providing valuable insights for clinical diagnosis and highlighting gender differences in fatigue characteristics [81]. These advancements collectively underscore the indispensable role of ECG in developing reliable, objective, and interpretable methods for fatigue assessment.

In addition to being non-invasive and ideal for continuous monitoring in various settings, this cost-effective approach reduces consumables and medical personnel expenses. It enhances patient comfort and compliance, particularly in long-term monitoring, and is easier to use, requires less training, and facilitates broader adoption. The absence of invasive procedures also minimizes the risk of infections and other complications, enhancing safety. Moreover, non-invasive devices tend to be portable, allowing for monitoring in diverse environments, including homes and remote areas, and they can be seamlessly integrated with other health technologies. Furthermore, the rich data generated from continuous, real-time monitoring is well-suited for integration with future AI advancements, enhancing the potential for predictive analytics and adaptive learning algorithms to improve health outcomes over time. This combination of features makes non-invasive ECG monitoring a valuable tool for comprehensive health management and positions it favorably for future technological integrations.

While non-invasive ECG monitoring offers numerous benefits, it also has significant disadvantages, including its inability to distinguish between fatigue and other conditions that affect

HRV, such as sleep apnea, potentially leading to false positives and confusion or misdiagnosis. Additionally, elements like the person's general health, the caliber of the ECG signal, and the particular machine learning algorithm used can impair the detection accuracy. Other challenges include sensitivity to external noise and interference, which can compromise reading accuracy. The variability in signal quality due to individual anatomical differences, such as skin thickness and body fat percentage, may lead to inconsistent results. Non-invasive ECG may not provide the detailed data necessary for diagnosing more complex cardiac conditions and relies heavily on the accuracy of underlying algorithms for signal interpretation, which can result in inaccuracies or missed diagnoses. Continuous wear-ability can also be inconvenient or uncomfortable over long periods, affecting patient compliance and data reliability. Moreover, the continuous transmission and storage of health data raise significant privacy and security concerns, necessitating robust protections to ensure patient confidentiality. These limitations highlight the need for continuous improvement and careful integration with other diagnostic approaches in comprehensive cardiac care.

Regarding practicality, fatigue detection using ECG and AI has wide applications across several industries, notably enhancing safety and efficiency. In the transportation industry, this technology is crucial for monitoring the fatigue levels of drivers, pilots, and train operators, significantly improving safety by potentially preventing accidents caused by drowsiness. Beyond transportation, its utility extends to industrial settings, where continuous monitoring of employees can greatly enhance operational safety. In healthcare, the technology can monitor patients with chronic illnesses, while in athletics, it assesses athletes' fatigue levels, potentially preventing over-training and aiding in optimized performance.

Other potential application areas include the technology and entertainment industries, where managing fatigue can increase productivity and mitigate health-related liabilities during extensive computer use or production activities. Despite these promising applications, it is important to note that further research is needed to enhance the accuracy and reliability of the detection methods before they can be widely adopted. This includes developing robust and accurate algorithms, studying the physiological and psychological changes that occur with fatigue, and establishing normative data for different population groups.

![](_page_11_Figure_0.jpeg)

![](_page_11_Figure_1.jpeg)

Figure 11: AI-based ECG analysis: cleans raw data, identifies wave components, refines and labels conditions, and displays results for review.

These steps are critical to ensure the efficacy and practicality of ECG and AI in fatigue detection across diverse industries.

Authors in [75] [88] [84] [82] [81] [86] [85] [43] [87] [35] [76] [83] [89] have used EEG signals and AI methods for identifying fatigue in subjects in the lab and real-world settings. Further information about the performance of AI methods for fatigue monitoring using EEG signals can be found in Table 1.

#### *6.2. EMG-based Methods*

Fatigue detection using electromyography (EMG) is a method for identifying signs of fatigue in individuals by analyzing the electrical activity of their muscles. This is typically done by measuring the electrical activity of the muscles via surface electrodes and analyzing the resulting EMG signals using machine learning algorithms or other analytical methods. The use of EMG for fatigue detection offers a non-invasive and practical approach to monitoring muscle function in real-time, making it valuable in various applications such as sports performance, rehabilitation, occupational health, and driver safety. Recent advancements have significantly enhanced the accuracy and reliability of fatigue detection by integrating advanced signalprocessing techniques and machine-learning models. We used support vector machines (SVM), convolutional neural networks (CNN), and extended short-term memory networks (LSTM) along with the time-domain and frequency-domain properties of EMG signals to find the essential parts. This helped researchers make strong models that accurately tell the difference between different levels of muscle fatigue.

One of the main advantages of this approach is that it can provide a direct measure of muscle activity related to muscle fatigue. Additionally, EMG can be used with other physiological measures, such as HRV or electroencephalography (EEG), to provide a more complete picture of fatigue. These innovations contribute to a better understanding of muscle physiology and offer practical solutions to preventing fatigue-related injuries and optimizing performance in various settings.

The paper [40] developed an automated muscle fatigue detection system by analyzing cyclostationary properties of sEMG signals under dynamic muscle fatiguing contractions, achieving high accuracy using geometric features and machine learning models. Similarly, [90] suggested a better wavelet threshold method to clean up sEMG signals, improving the accuracy of feature extraction and classification using a CNN-SVM algorithm. The study [90] combined time-frequency analysis, ICA, and neural networks to classify muscle fatigue from EMG signals, demonstrating effective handling of non-stationary EMG signals and achieving over 90% accuracy. In [91], an LSTM-based model, combined with an improved wavelet packet threshold function, was used to classify muscle fatigue with high accuracy, showcasing the potential of advanced signal processing and deep learning models. The paper [92] utilized EMG and GSR signals to detect driver fatigue, with an SVM classifier achieving high accuracy, indicating the practicality of mobile-based fatigue detection solutions. The study [93] introduced a novel F-GRU model for sEMG-based muscle fatigue detection, achieving over 98% classification accuracy by leveraging feature extraction and deep learning techniques. The review [94] discussed how sEMG

can measure exercise-induced fatigue. It focused on signal processing, feature extraction, and how sEMG can be combined with other physiological signals to get a complete picture of fatigue.

In the study [95], machine learning and high-resolution timefrequency methods were used to sort sEMG signals into groups based on muscle fatigue. This shows that combining these methods works well. The paper [96] integrated EMG data from wearable sensors with subjective user reports, using machine learning to develop a model for physical fatigue detection, achieving high accuracy with a Gradient-boosting classifier. The study [97] examined how to tell if someone is tired during rehabilitation after a stroke using sEMG signals and advanced machine learning algorithms. HMM and ANN classifiers were used to get very good results. Also, [98] used sEMG signals to figure out how the elbow moved when it was fatigued in different ways. They trained a machine learning model to guess joint angles even when the fatigue level changed correctly. This shows that sEMG could be used for real-time monitoring and evaluation in sports performance and rehabilitation. These studies collectively emphasize the efficacy of integrating advanced signal processing and machine learning techniques for reliable and accurate muscle fatigue detection using EMG and sEMG signals.

There are also several challenges associated with using EMG for fatigue monitoring. Movement of the muscle or noise from outside the body can change EMG signals. This lowers the quality of the signals and makes it harder to accurately measure muscle activity, which requires cleaning and filtering the data in a way that takes a lot of time and effort. Muscle fatigue levels vary significantly between individuals, complicating the establishment of normative data across different population groups, and different muscles may fatigue at different rates, complicating the assessment of overall muscle fatigue. Additionally, EMG is typically used to measure activity in specific muscle groups and is not well-suited for monitoring overall body fatigue levels. The electrodes required for EMG can be uncomfortable for subjects, particularly if worn for extended periods. The accuracy of EMG in measuring muscle fatigue is limited, and the correlation between EMG signals and fatigue levels is not always clear. Furthermore, EMG equipment can be bulky and requires a power source, making it difficult to use in portable or mobile settings. To address these challenges, researchers have developed alternative methods, such as wireless EMG systems, which enhance comfort and allow for greater freedom of movement.

It is important to note that in many cases, EMG is used to complement other techniques, such as HRV or electroencephalography (EEG), as it can provide a more complete picture of the subject's fatigue. For example, the combination of EEG and EMG can be used for fatigue monitoring in drivers, where the EEG measures the cognitive load and the EMG measures muscle fatigue.

EMG signals and AI approaches have been employed by the authors of [40] [90] [91] [92] [93] [94] [95] [96] [97] [98]

#### *6.3. EEG-based Methods*

Fatigue detection using electroencephalography (EEG) combined with artificial intelligence (AI) represents a sophisticated

method for identifying fatigue in individuals through the analysis of brain activity. This technique involves placing electrodes on the scalp to measure the brain's electrical activity, producing EEG signals. These signals are then subjected to advanced machine learning algorithms, which process and analyze the data to detect patterns indicative of fatigue. The integration of AI allows for the development of complex models capable of interpreting the nuanced and often subtle variations in EEG signals that correspond to different fatigue levels. This method provides a reliable and efficient approach to real-time fatigue assessment, which is critical for applications in high-stakes environments such as transportation, aviation, and occupational health. This technology uses AI-driven analysis to make fatigue detection more accurate and make it easier to start early intervention plans that lower the risks of impairments caused by fatigue.

Studies highlight significant advancements in EEG-based fatigue detection and drowsiness monitoring. In the paper [99], an innovative iterative cross-subject negative-unlabeled (NU) learning algorithm is described. It achieves an average accuracy of 93.77% using a dry wearable EEG headband and shows negative correlations with beta and alpha bands, improving driver safety by preventing accidents related to fatigue. In the same way, [100] uses several different feature extraction methods and deep learning models, such as AlexNet and VGGNet, along with the tunable Q-factor wavelet transform (TQWT) for sub-band decomposition to get a 94.31% success rate in detecting driver sleepiness. The study [101] explores a highly wearable in-ear EEG sensor, achieving feasible automatic light sleep classification with accuracies between 80.0% and 82.9%, beneficial for out-of-clinic drowsiness monitoring in various operators. In [38], a simulated driving experiment using EEG signals and advanced classifiers like PSO-H-ELM achieved the highest accuracy, underscoring the potential of EEG-based real-time fatigue detection systems to enhance road safety. The paper [102] combines kernel principal component analysis (KPCA) and Hidden Markov Model (HMM) with complexity parameters to estimate mental fatigue, achieving an accuracy of 84%, highlighting the efficacy of complexity parameters and KPCA-HMM. In [103], TQWT-based features effectively distinguish between alertness and drowsiness states, with the extreme learning machine (ELM) classifier achieving an accuracy of 91.842%. The study [104] tackles noise interference in EEG signals due to vehicle vibrations, providing a reliable measure of driving workload by analyzing frequency components, contributing to traffic safety. Finally, [105] provides a comprehensive review of EEG-based MF detection systems, emphasizing the importance of preprocessing, feature extraction, and various classification algorithms, recommending the Kernel Partial Least Squares - Discrete Linear Regression (KPLS-DLR) model for its outstanding performance and minimal intrusiveness, suggesting opportunities for deep learning models and online implementations for broader applications. Collectively, these studies demonstrate the robust and efficient use of EEG in detecting and monitoring fatigue and drowsiness, paving the way for enhanced safety in various fields.

One of the primary advantages of using EEG is its ability to provide a more direct measure of brain activity compared to other methods, such as self-reported fatigue or physiological measures like HRV. Moreover, EEG-based monitoring can offer real-time assessment, enabling the identification of fatigue at its early stages before it escalates into a significant issue.

However, the presence of artifacts in the EEG signal due to muscle activity and other movements presents a significant challenge when using EEG for fatigue detection in mobile subjects. These artifacts can compromise the accuracy of brain activity measurements, potentially leading to false positives or false negatives in fatigue detection.

Another significant issue is the sensitivity of EEG electrodes to movement. If the subject moves excessively, these electrodes can become dislodged, degrading the quality of the EEG signal. Additionally, movement can cause discomfort for the subject, reducing their compliance with the measurement process.

Furthermore, subjects' need to remain seated or still during EEG measurement can be restrictive and impractical, particularly in applications involving physical activity such as transportation, sports, and industrial work. This limitation underscores the need for advancements in EEG technology that can accommodate movement without compromising data integrity.

Researchers have developed alternative methods to overcome these issues, such as wireless EEG systems, which can be more comfortable for the subject and allow for greater freedom of movement. Additionally, advanced signal processing techniques such as independent component analysis (ICA) can remove artifacts caused by movement from the EEG signal.

Regarding the EEG, the authors in [100] [106] [107] [99] [102] [104] [105] [103] [38] [101] have employed EEG data and AI algorithms to detect weariness in participants in both laboratory and real-world scenarios. Table 1 and Table 2 provide more details on the efficacy of AI approaches for fatigue monitoring using EEG data.

#### *6.4. PPG-based Methods*

Photoplethysmography (PPG) is an invaluable physiological signal for monitoring and detecting fatigue, leveraging its technical prowess to provide detailed cardiovascular insights. PPG operates by emitting light onto the skin and measuring the variations in light absorption and reflection, which correspond to changes in blood volume. This method is particularly effective for real-time heart rate monitoring and calculating other cardiovascular parameters such as HRV.

PPG sensors, often embedded in wearable devices, capture these fluctuations in blood volume with high precision, offering a non-invasive means to track physiological changes continuously. Unlike electroencephalography (EEG), which monitors electrical activity in the brain, PPG focuses on peripheral cardiovascular metrics. When used together, PPG and EEG provide complementary data that delivers a holistic view of an individual's physiological state, enhancing the accuracy of fatigue detection systems. The integration of PPG sensors in wearable technology facilitates continuous, real-time monitoring, making it possible to detect early signs of fatigue, manage stress, and improve overall cardiovascular health. This synergy of PPG with other sensors underscores its critical role in advancing health monitoring technologies, particularly in applications requiring

accurate, non-intrusive, and continuous physiological assessments.

One of the primary advantages of utilizing photoplethysmography (PPG) to measure fatigue is its noninvasive nature, ease of use, and integration capability with various devices such as smartwatches and smartphones. PPG facilitates continuous monitoring of cardiovascular activity, making it particularly valuable in contexts where fatigue poses significant safety risks, such as for drivers, pilots, and other professionals whose performance may be compromised by fatigue.

PPG is highly effective in measuring HRV, a crucial indicator of autonomic nervous system activity. HRV provides insights into the balance between the sympathetic and parasympathetic nervous systems, with variations in HRV reflecting changes in fatigue levels. Specifically, low HRV is associated with increased fatigue and stress, making it a reliable metric for assessing fatigue.

Additionally, PPG can measure blood oxygenation levels, offering further information about an individual's physiological state. Monitoring blood oxygenation helps detect changes due to fatigue, providing a comprehensive view of the individual's health status. The integration of PPG in wearable technology thus enables real-time, continuous assessment of cardiovascular health and fatigue, enhancing safety and performance in various high-stakes environments.

The following studies provide robust support for the integration and efficacy of photoplethysmography (PPG) sensors in various applications related to fatigue research, highlighting significant advancements and practical implementations in wearable technology. The paper [108] presents a driver condition recognition system that utilizes Support Vector Machine (SVM) classifiers to detect driver drowsiness by analyzing heart rate and RR interval data obtained from a PPG sensor embedded in a wearable device. The system achieved an impressive classification accuracy of 96.3%, with data preprocessing steps including segmentation and normalization to remove noise and standardize data. Similarly, [109] extends this application by integrating PPG sensors with additional physiological and motionrelated data such as galvanic skin response (GSR), temperature (TEM), acceleration (ACCEL), and gyroscope (GYRO) data. The study implemented preprocessing steps to segment data into 10-second intervals and filter out noise, achieving an accuracy of 68.31% for distinguishing between normal, stressed, fatigued, and drowsy states, which improved to 84.46% when fatigue and drowsiness were combined into a single class.

The Cardiopulmonary Care Platform (C2P) described in [110] utilizes a smartwatch equipped with PPG sensors to capture HRV and respiratory cycles, addressing the challenge of noise and motion artifacts by incorporating data from the smartwatch's accelerometer and applying zero-phase forward-reverse filtering with a Butterworth IIR filter. The system achieved a high correlation with Pearson's correlation coefficient, averaging 0.987 across sessions for breathing cycles and demonstrated accuracies of 84.2% and 94% for detecting stair climbing and brisk walking, respectively. In [111], a PPG-based system for real-time heart rate monitoring during running exercises utilizes an easy pulse plug-in PPG sensor placed on the user's fingertips, with heart rate

data processed by an Arduino microcontroller and transmitted to an Android smartphone via Bluetooth. The system calculates heart rate by detecting intervals between successive peaks in the PPG signal, providing alerts when the heart rate exceeds predefined thresholds. The experimental setup demonstrated a high accuracy of 95.923% in heart rate detection, ensuring user safety through timely alerts.

Additionally, the innovative Activity-Aware Recurrent Neural Network (AcRoNN) framework in [112] integrates PPG sensors with accelerometers and electrodermal activity (EDA) sensors to enhance cognitive fatigue assessment. The system processes signals using stationary wavelet transform (SWT) and convex optimization (cvxEDA) techniques to remove noise and motion artifacts. The AcRoNN model, designed in two stages, involves feature extraction, activity recognition, and initial cognitive fatigue scoring based on gestural and postural activities, followed by refinement using an LSTM with Consistency Self-Attention (LSTM-CSA) model. This approach achieved up to a 19% improvement in accuracy over baseline models, demonstrating the effectiveness of integrating PPG data with other sensor signals. Collectively, these studies underscore the potential of PPG sensors to provide accurate, real-time monitoring of fatigue, stress, and other physiological states, significantly contributing to safety and productivity in various domains. However, it is worth noting that PPG has some limitations for fatigue monitoring. PPG signals can be affected by various factors such as motion, skin pigmentation, and hydration level, which can introduce noise and bias into the measurements. Additionally, PPG is not able to provide information about the neural or cognitive aspects of fatigue, which may be important in certain situations.

In lab and real-world situations, authors in [108] [109] [110] [111] [112] have employed PPG data and AI to detect exhaustion in people. Table 1 and Table 2 show the performance of AI techniques for fatigue monitoring using PPG signals.

#### *6.5. EDA-based Methods*

Fatigue detection through electrodermal activity (EDA) is an advanced method for identifying signs of fatigue by analyzing the electrical conductance changes in the skin. This approach involves the use of electrodes to measure the skin's electrical activity, capturing fluctuations caused by the sympathetic nervous system's activation of sweat glands. These EDA signals are then subjected to sophisticated signal processing techniques and machine learning algorithms to detect and quantify fatigue correctly. By leveraging these advanced analytical methods, EDA-based fatigue detection provides a non-intrusive, real-time assessment of physiological states. This capability is crucial for early identification and management of fatigue, enhancing safety and performance in high-stakes environments such as driving, aviation, and demanding workplace settings. The continuous monitoring enabled by EDA offers critical insights into the autonomic nervous system's functioning, making it an invaluable tool for comprehensive fatigue management and overall health monitoring.

One of the primary advantages of using electrodermal activity (EDA) for measuring fatigue is its ability to provide a noninvasive measure of changes in the sympathetic nervous system,

which are directly related to fatigue. EDA sensors capture the electrical conductance of the skin, reflecting the activity of sweat glands controlled by the sympathetic nervous system. This physiological measure can be particularly valuable for monitoring fatigue because it directly correlates with the body's stress and arousal responses. Moreover, EDA can be effectively combined with other physiological measures, such as HRV or electroencephalography (EEG), to provide a comprehensive assessment of fatigue. This multimodal approach enhances the accuracy and reliability of fatigue detection, offering a more complete picture of an individual's physiological state and improving the potential for timely interventions.

However, the use of EDA in measuring fatigue also presents several disadvantages. One significant challenge is the susceptibility of EDA signals to artifacts such as sweat, motion, or other external noise sources, which can degrade the quality of the signal. This necessitates rigorous data cleaning and filtering processes to remove these artifacts, which can be time-consuming and complex. Furthermore, EDA is influenced by various factors, including emotional state, stress, and other physiological conditions, which can complicate the interpretation of results. These factors can introduce variability and potential confounders into the EDA data, making it difficult to isolate fatigue-specific signals. Despite these challenges, advancements in signal processing and machine learning techniques continue to enhance the robustness and reliability of EDA-based fatigue assessment, making it a valuable tool in the field of physiological monitoring.

The advancements in electrodermal activity (EDA) signal processing and its applications in fatigue assessment are comprehensively reviewed in several studies, underscoring the critical role of EDA in real-time physiological monitoring. The paper titled [113] highlights innovations in EDA devices and signal processing techniques that enhance measurement accuracy, even amidst artifacts and noise, making it possible to derive sophisticated measures from EDA signals. These advancements enable the assessment of cognitive and physical states by quantifying sudomotor activity linked to the sympathetic nervous system's response to fatigue, thus facilitating real-time fatigue monitoring through changes in skin conductance responses (SCRs) and skin conductance levels (SCL). Complementing this, the study [114] demonstrates the high accuracy (approximately 89%) of a wearable EDA device in classifying emotional states such as calm and distress, highlighting its utility in non-intrusive monitoring of arousal, stress, and fatigue. Addressing the challenge of motion artifacts, [115] develops an advanced framework for detecting and mitigating these artifacts in EDA signals, achieving a remarkable mean accuracy of 94.82% with the GradBoost classifier, thereby enhancing the reliability of EDA-based fatigue measurements in real-world settings. Additionally, [116] leverages EDA alongside other physiological sensors in a multimodal approach to induce and detect cognitive and physical fatigue, with the integration of EDA data significantly contributing to high classification accuracies using Random Forest and LSTM models. Lastly, [117] integrates EDA with functional near-infrared spectroscopy (fNIRS), ECG, respiratory inductance plethysmography (RIP), and accelerometers to refine cognitive fatigue detection, achieving an average classification accuracy of 70.91%, with some

models exceeding 80%. Collectively, these studies underscore the pivotal role of EDA in delivering a comprehensive, nonintrusive approach for real-time monitoring and assessment of fatigue, demonstrating its efficacy and potential for practical applications in various high-stakes environments.

In terms of practicality, fatigue detection using EDA has potential applications in transportation, industrial, and sports settings, as well as healthcare. However, it is important to note that further research is needed to improve the accuracy and reliability of the detection method before it can be widely adopted in practical settings. This includes developing robust and accurate algorithms, studying the physiological and psychological changes that occur with fatigue, and establishing normative data for different population groups.

It is important to note that in many cases, EDA is used to complement other techniques, such as HRV or electroencephalography (EEG), as it can provide a more complete picture of the subject's fatigue. For example, the combination of EEG and EDA can be used for fatigue monitoring in drivers, where the EEG measures the cognitive load and the EDA measures the physiological changes caused by fatigue.

Regarding the EDA-Based methods, the authors in [113] [114] [115] [116] [117] have employed EDA to detect weariness in participants in both laboratory and real-world scenarios. Table 1 provides more details on the efficacy of AI approaches for fatigue monitoring using EDA sensors.

#### *6.6. IMU-based Methods*

Fatigue detection using inertial measurement units (IMUs) is a sophisticated method for identifying signs of fatigue in individuals by analyzing biomechanical changes in body movements and postures. This method typically involves measuring angular and linear acceleration, angular velocity, and magnetic field strength via devices embedded with one or more IMUs, such as smartwatches or accelerometers attached to the body. The high-resolution data captured from these IMUs are then subjected to advanced machine learning algorithms or other analytical techniques to identify and quantify signs of fatigue accurately. Recent research highlights the critical role of IMUs in enabling real-time, continuous monitoring of physical fatigue by capturing detailed motion data and identifying subtle variations indicative of fatigue onset. These advancements have facilitated the development of robust predictive models that integrate IMU data with sophisticated analytical frameworks, achieving high accuracy in fatigue detection. This methodological approach offers significant practical applications across various high-stakes environments, including sports, industrial safety, and occupational health, enhancing managing fatigue proactively and improving overall safety, performance, and productivity.

Recent research highlights the significant progress in employing Inertial Measurement Unit (IMU) sensors for fatigue assessment, emphasizing their pivotal role in real-time physiological monitoring. The academic paper [118] systematically reviews the application of IMUs in sports performance, emphasizing their role in capturing and analyzing detailed motion data, such as acceleration, velocity, and jerk, to detect subtle changes in movement patterns indicative of fatigue. Complementing this,

the study [119] demonstrates a robust data-driven methodology to develop a model capable of detecting physical fatigue by analyzing IMU data from the lower back, identifying key features like gait maximum acceleration and mean back rotational position, with a classification accuracy of 88%. In an industrial context, the paper [120] explores the use of a Smart Safety Helmet (SSH) equipped with IMU and EEG sensors to detect fatigue-related head motions and assess accident risks, providing precise measurements of acceleration and orientation to identify fatigue-induced movements. Additionally, [121] introduces an innovative system that uses forearm IMU sensors to continuously monitor construction workers' fatigue by predicting the aerobic fatigue threshold (AFT) through the analysis of muscle activity and motion data, achieving superior accuracy in fatigue evaluation compared to traditional metrics. Finally, the research [122] presents an AI model that integrates IMU-generated data to predict fatigue and stamina in athletes, effectively capturing triaxial acceleration, angular velocity, and magnetic orientation to train machine learning models like Random Forest, Gradient Boosting Machines, and LSTM networks, showing high predictive accuracy and enabling timely interventions. Collectively, these studies highlight the practicality, reliability, and effectiveness of IMU technology for continuous fatigue monitoring across various fields, enhancing safety, performance, and productivity through precise and real-time fatigue assessment.

One of the main advantages of using inertial measurement units (IMUs) for measuring fatigue is that they provide a noninvasive means of capturing changes in body movements and postures related to fatigue. IMUs can continuously monitor and record angular and linear acceleration, angular velocity, and magnetic fields, offering high-resolution data that reflect the physical state of an individual. Furthermore, IMUs can be integrated with other physiological measures, such as HRV or electroencephalography (EEG), to provide a comprehensive assessment of fatigue. This multimodal approach enhances the robustness and reliability of fatigue detection by combining biomechanical data with physiological indicators.

However, this approach also has several disadvantages. One significant challenge is the susceptibility of IMU data to artifacts, such as muscle movements or external noise sources, which can degrade the signal quality and complicate the accurate measurement of body movements and postures. Addressing these artifacts requires extensive data cleaning and filtering, which can be time-consuming and complex. Additionally, the accuracy of fatigue detection using IMUs may be influenced by factors such as the placement of the sensors, the specific machine learning algorithms employed, and individual variations in biomechanics. These variables can introduce variability and potential inaccuracies in the fatigue assessment, necessitating careful calibration and validation to ensure reliable results.

Researchers in [118] [119] [120] [121] [[122] have applied IMU signals and AI techniques to detect fatigue in humans in both laboratory and real-world scenarios.

#### *6.7. EOG-based Methods*

EOG stands for Electrooculography, a technique used to measure the electrical potential difference between the front and

back of the human eye. It is commonly used in research and clinical settings for monitoring eye movements and detecting changes in the electrical activity of the eye, including fatigue.

The technique works by placing electrodes around the eyes and measuring the electrical activity generated by the eye muscles as they move. Changes in this electrical activity can indicate changes in the state of the eye, including fatigue. EOG can be used to monitor fatigue in various settings, including in drivers, pilots, and other individuals whose performance may be affected by fatigue.

Recent research papers have showcased significant progress in fatigue detection through the use of Electrooculography (EOG) sensors. The paper [123] introduces a novel wearable system that combines EOG sensors and a three-axis gyroscope to monitor fatigue and provide timely wake-up interventions through physical stimuli like music. The system utilizes a single-lead electrode for EOG signal collection and gyroscope data to analyze blink and head posture characteristics using a Backpropagation (BP) neural network, effectively identifying fatigue-related features and ensuring real-time monitoring suitable for high-vigilance environments.

In [124], the study employs EOG sensors to assess driver hypo-vigilance, including fatigue, drowsiness, visual inattention, and cognitive inattention. The research uses a rigorous experimental protocol to collect EOG data from ten participants during simulated driving sessions. Seventeen significant features are extracted and analyzed using advanced machine learning algorithms such as Support Vector Machine (SVM), k-nearest neighbor (KNN), and ensemble classifiers, achieving a maximum accuracy of 98.7% for binary classification and 90.9% for five-class detection. Principal component analysis (PCA) is used for feature reduction, enhancing classification performance.

Similarly, [125] provides a comprehensive review of EOGbased driver fatigue detection, highlighting the integration of EOG with other physiological signals to improve detection accuracy. The review discussed the development of a multi-feature fusion technique and advanced pre-processing methods like wavelet transforms and singular spectrum analysis to address challenges such as baseline drift and signal noise. Machine learning classifiers like SVM, Artificial Neural Networks (ANN), and Extreme Learning Machines (ELM) are emphasized for their high classification accuracy in detecting fatigue states.

The paper [126] focuses on office environments, developing an algorithm to detect fatigue through EOG signal analysis during a 60-minute N-back task with 24 participants. The study captures and analyzes blink duration, amplitude, and the time between blinks, achieving an average classification accuracy of 93% in user-dependent mode and 89% in user-independent mode. Sophisticated preprocessing techniques ensure the accuracy and reliability of the detected signals, providing a practical solution for real-time fatigue management in repetitive task environments.

In [127], EOG glasses are used to continuously monitor fatigue in real-world settings over a two-week period with 16 participants. The study collects over 2,860 hours of EOG recordings and 1,047 ground truth assessments using Psychomotor Vigilance Tasks (PVT). The results demonstrate a statistically significant positive correlation between increased blink frequency and longer reaction times, validating using EOG glasses as a practical and unobtrusive tool for real-time fatigue monitoring. The development of a robust predictive model based on continuous EOG data allows for accurate detection of fatigue-related changes in alertness, enhancing user safety and performance.

Finally, [128] proposes a multimodal signal fatigue detection method employing deep learning techniques to identify driver fatigue effectively states using both EOG and EEG sensors. Convolutional autoencoders (CAE) are used to fuse EEG and EOG signal features, while convolutional neural networks (CNN) maintain spatial locality. The fused features are input into a recurrent neural network (RNN) for fatigue recognition, achieving superior performance with an RMSE/COR of 0.08/0.96 compared to single modality features. This multimodal approach significantly enhances the accuracy and robustness of fatigue detection systems, demonstrating practical applications in improving road safety through timely and accurate fatigue monitoring.

Collectively, these studies underscore the versatility, reliability, and practical applications of EOG-based fatigue monitoring systems across various environments, offering comprehensive solutions for enhancing safety and performance. One of the main advantages of EOG is that it is non-invasive and relatively easy to use. It can be used to monitor fatigue in real-time, which can be useful in situations where fatigue is a potential safety concern. Additionally, EOG can be used with other techniques, such as EEG, to provide a more complete picture of an individual's level of fatigue.

However, there are also some limitations to using EOG for fatigue monitoring. The technique is sensitive to head movements, making it difficult to use in specific settings. Additionally, EOG may not be able to detect all types of fatigue, particularly those not caused by changes in the state of the eye. Regarding practicality, EOG is still mainly used in clinical or laboratory settings and is not yet a widely available technology in practical applications, such as cars or airplanes. The cost and complexity of the equipment and lack of standardization in the techniques used to analyze the data obtained by EOG could be some of the reasons behind this. However, as technology is advancing, it is possible that EOG will become more widely used in the future.

Authors in [123] [124] [125] [126] [127] [128] utilised EOG signals and AI to detect fatigue. Tables 1 and 2 provide information on AI fatigue monitoring approaches utilising EOG signals.

#### *6.8. Hybrid Models*

Hybrid methods for fatigue monitoring combine multiple physiological signals and camera images to provide a more comprehensive assessment of an individual's level of fatigue. These methods aim to overcome the limitations of using a single physiological signal or camera image by combining the strengths of multiple techniques.

One example of a hybrid method for fatigue monitoring is the combination of electroencephalography (EEG) and electrooculography (EOG) to measure brain activity and eye movements, respectively. EEG can provide information about brain activity

and fatigue, while EOG can provide information about eye movements and changes in the state of the eye. By combining these two techniques, researchers can get a more complete picture of an individual's level of fatigue.

Another example is using physiological signals such as electrocardiography (ECG) and photoplethysmography (PPG) combined with camera images to monitor fatigue. ECG and PPG can provide information about heart rate and blood flow, respectively, while camera images can provide information about facial expressions, head movements and blink rate. The combination of these signals can provide a more accurate assessment of an individual's level of fatigue, and other factors that may be related to fatigue, such as stress.

Additionally, using a combination of physiological signals and camera images can allow for the monitoring of fatigue in real-time and in naturalistic settings without the need for the individual to wear a lot of equipment. However, it is worth noting that the combination of multiple signals and images also increases the complexity of the system and the need for sophisticated algorithms for data analysis. Additionally, it may also increase the cost of the system and the need for trained personnel to operate and interpret the results.

The recent body of research demonstrates remarkable progress in the field of fatigue detection through the integration of multimodal sensors and sophisticated machine learning algorithms. The study [28] leverages Electroencephalography (EEG) and Electrooculography (EOG) signals, employing a fast Support Vector Machine (FSVM) algorithm to process features such as power spectral density (PSD) and differential entropy from EEG and blink characteristics and independent component analysis (ICA) derived features from EOG, achieving superior recognition accuracy in real-time driver fatigue detection. Similarly, [129] develops a real-time fatigue monitoring system using lightweight Convolutional Neural Network (CNN) architectures on EEG and EOG signals, extracting features such as PSD and saccades and achieving 94% classification accuracy on the Jetson TX2 platform while utilizing IoT technology for enhanced road safety.

The study [130] integrates multiple sensors, including Electrocardiography (ECG), Electromyography (EMG), Electrodermal Activity (EDA), and EEG, to monitor cognitive and physical fatigue. The system employs machine learning models such as Random Forest (RF) and Long Short-Term Memory (LSTM) networks, achieving 80.5% accuracy for physical fatigue and 84.1% for cognitive fatigue, demonstrating the efficacy of multimodal sensor fusion. In [72], driver sleepiness detection is enhanced using Continuous Wavelet Transform (CWT) to extract time-frequency features from EEG and EOG signals and augmented with Generative Adversarial Networks (GAN) to overcome data limitations, resulting in a mean accuracy of 98% with LSTM networks.

The study [131] focuses on miner fatigue detection by integrating ECG and EMG signals, employing Principal Component Analysis (PCA) and Grey Relational Analysis (GRA) for feature optimization, and utilizing machine learning models such as XG-Boost, SVM, and Random Forest (RF), with XG-Boost achieving the highest accuracy of 89.47%. Similarly, [132]

uses a multi-feature information fusion approach, combining ECG, EMG, pulse, blood pressure, reaction time (RT), and vital capacity (VC) signals, and employs SVM and RF classifiers, achieving 90% accuracy with RF for fatigue detection in extreme conditions.

The study [36] explores fatigue detection in Pilates rehabilitation by fusing ECG and surface EMG (sEMG) signals, using an Improved Particle Swarm Optimization-SVM (IPSO-SVM) classifier to achieve an average recognition rate of 93.58% across relaxed, transition, and tired states. This approach demonstrates the complementary nature of ECG and sEMG in monitoring muscle fatigue accurately. Lastly, [71] introduces an IoT-based multimodal fatigue monitoring system combining EEG, EOG, and facial data, using deep learning models such as Convolutional Neural Networks (CNNs) and Long Short-Term Memory (LSTM) networks to classify eye and mouth states with accuracies of 99.01% and 99.5%, respectively, significantly enhancing real-time driver fatigue detection and road safety.

These studies show that multimodal sensor systems and advanced machine learning techniques can provide complete, realtime solutions for monitoring fatigue in many areas, such as healthcare, transportation, workplace safety, and rehabilitation. Therefore, the hybrid methods for fatigue monitoring that combine physiological signals with camera images can provide a more comprehensive assessment of an individual's level of fatigue. However, when implementing these methods, it is important to consider practical issues such as cost and complexity.

Authors in [28] [36] [71] [72] [129] [131] [132] [130] have used a hybrid model for identifying fatigue. Further information about the performance of AI methods for fatigue monitoring using hybrid models can be found in Table 1 and Table 2.

Power BI Desktop Count of Reference by Experiement

26

Count of Reference by Modality

8 8

SVM

Hybrid

20

Modality

PPG-Based Method

EDA-Based Method

Count of Reference by Machine Learning Methods

Other

LSTM

DT

3 3

GPS-Based Method

2

IMUs

ELM

MLPNN RF A…

ANN AR-… BT CC…

NU QDA

H… M… MPF

XG…

DNN F_GRU FMIW…

BPNN CNN GB KNN

1 1

EOG-Based Method

7 5

EMG-Based Method

#### *6.9. Discussion* Lab

Figure 12 illustrates the popularity of various physiological signals and data sources used for fatigue monitoring in different studies. EEG and ECG are the most commonly used signals, with a significant proportion of studies utilizing them. On the other hand, EDA/GSR is the least used source for fatigue monitoring among the options presented. This highlights the trend towards using EEG and ECG in fatigue monitoring research while using EDA/GSR remains limited. 0 10 20 Count of Reference Experiement Simulation Field Real-world Hybrid 19 6 5 2 0 5 10 15 20 Count of Reference Hybrid ECG-Based MethodsEMG-Based MethodEEG-Based Method

![](_page_17_Figure_12.jpeg)

Figure 12: The popularity of different physiological signals used for fatigue monitoring.

Figure 13 shows the count of field and lab tests for fatigue monitoring using physiological signals. Most studies utilize lab tests, rather than field tests, for monitoring fatigue. This is likely due to the convenience and practicality of conducting lab tests and the ability to collect data in a controlled environment. However, field tests are still used in a few studies and may provide more practical solutions for measuring fatigue. This representation demonstrates that field and lab tests are used to monitor fatigue using physiological signals, but lab tests are more commonly used. EEG-Based Method EOG-Based Meth… EDA-Based … GPS-Based …

Power BI Desktop Count of Reference by Experiement

19

26

ECG-Based Meth…

0 10 20

Hybrid sEMG-Based Method

6 5

2

Sum of Reference by Modality

Count of Reference

![](_page_18_Figure_1.jpeg)

Experiement

Experiement

Lab Simulation Field Real-world Hybrid

0 10 20

Hybrid sEMG-Based Method

6 5

2

Sum of Reference by Modality

Experiement

Lab Simulation Field Real-world Hybrid

Count of Reference

EEG-Based Method

26

ECG-Based Meth…

EOG-Based Meth…

19

0 10 20 Count of Reference Figure 13: The count of environment studies conducted for fatigue monitoring using wearables and physiological signals.

Sum of Reference by Modality Hybrid sEMG-Based Method EEG-Based Method ECG-Based Meth… EOG-Based Meth… According to Figure 14, the hybrid approach is more prevalent among other AI methods for measuring fatigue using wearables. A hybrid model, which combines multiple approaches, may provide a more robust and comprehensive measurement of fatigue. ECG-based methods are in the second rank. ECG is a suitable method for monitoring fatigue because it can provide information about the heart rate and rhythm, which fatigue can affect. One important measure that can be obtained from ECG is HRV, which is the variation in time between heartbeats. HRV can indicate the body's ability to adapt to stressors; lower HRV has been associated with increased fatigue. Power BI Desktop Count of Reference by Experiement

![](_page_18_Figure_4.jpeg)

Count of Reference by Modality

SVM

Modality EMG-Ba… PPG-… Count of Reference by Machine Learning Methods Figure 14: Popular AI methods for fatigue monitoring using wearables and physiological signals.

Other

ELM

EDA-Based … GPS-Based … Hybrid LSTM DT BPNN CNN GB DNN F_GRU Figure 15 shows that Support Vector Machine (SVM) has emerged as the most popular model for modeling and identifying fatigue. This is due to the excellent capabilities of SVM for handling large amounts of data, versatility (being able to process both linear and nonlinear samples), and excellent generalization power (robust to noise). Other popular methods for fatigue monitoring are kNN, RF, and DL models.

KNN FMIW… Ultimately, the analysis highlights significant trends and methodologies in fatigue monitoring research. EEG and ECG signals emerge as the most widely utilized modalities, offering crucial insights into physiological parameters like heart rate variability and brain activity. In contrast, methods leveraging

![](_page_18_Figure_8.jpeg)

Figure 15: Popular AI models for fatigue monitoring.

0 5 3 3 2 1 1 EDA/GSR remain less explored, suggesting opportunities for further investigation in this area.

Modality Hybrid ECG-Based Method sEMG-Based Method EEG-Based Method EOG-Based Method EMG-Based Method PPG-Based Method EDA-Based Method GPS-Based Method IMUs EMG-Ba… PPG-… Count of Reference by Machine Learning Methods Lab-based studies dominate the field, highlighting the preference for controlled environments that enable precise data collection. Nonetheless, the inclusion of simulation, field, and hybrid approaches reflects a growing interest in extending research to more realistic and diverse settings, striking a balance between control and ecological validity.

EDA-Based … GPS-Based … SVM Hybrid Other LSTM DT ELM BPNN CNN GB KNN MLPNN RF A… ANN AR-… BT CC… DNN F_GRU The increasing prevalence of hybrid models, which integrate multiple modalities and machine learning methods, demonstrates the push toward comprehensive and robust fatigue assessment systems. Support Vector Machines (SVM) are the leading AI method due to their adaptability and robustness, while deep learning approaches such as CNNs and LSTMs, along with hybrid frameworks, are gaining traction for their effectiveness in processing complex, multimodal datasets.

H… M… MPF

XG…

NU QDA

FMIW… These findings underscore the evolution of fatigue monitoring research, emphasizing the role of advanced machine learning techniques, diverse experimental frameworks, and multimodal physiological data in developing reliable and effective solutions.

#### 7. Research Challenges

10 15

Count of Reference by Modality

20

EMG-Ba… PPG-…

Hybrid

ECG-Based Method

sEMG-Based Method

EEG-Based Method

8 8

EOG-Based Method

7 5

EMG-Based Method

Count of Reference

8 8

Modality

PPG-Based Method

EDA-Based Method

Count of Reference by Machine Learning Methods

3 3

GPS-Based Method

2

IMUs

1 1

7 5

#### *7.1. Access to Real- Time Data*

MLPNN RF A… ANN AR-… BT CC… H… M… MPF NU XG… The data transmission needed for fatigue assessment is a multistep procedure that might take a lengthy time. The first step is to sync the wearable gadget and upload the data. Suppose this device is on a mobile network. In that case, the data must go via that network provider's infrastructure and out onto the internet before ending up in the service provider's network, potentially through the cloud. The data might arrive at its destination later than expected if access to the Cloud [133] is disrupted or if an internet outage happens. Mobile networks [134] are not guaranteed to be constantly accessible. If mobile users can't connect to the internet for routine tasks, that's a problem; but when someone's life is on the line, as it may be in a dangerous situation, information must be sent quickly and accurately [135] [129].

QDA

| Re fer en ce | M o da | l ity | M ac h ine Le arn | ing M et ho ds | Sa le S ize mp | Fe atu re Co un t | Ex er im en t p | Pe r for ma nc e Re su lt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [ 3 5 ] | E C G- Ba se d | Me t ho d | S V M |  | 1 2 | 4 | S im u lat ion | Ac cur = 8 3. 9 % acy |
| 3 7 | EM G- Ba | d Me t ho d | C N N |  | 6 4 | 2 | La b | Ac cur = 9 1. 3 8 % ( 6 0 °/s ) acy |
| [ ] | s se |  |  |  |  |  |  | 1 Ac cur = 8 9. 8 7 % ( 8 0 °/s ) acy |
|  |  |  |  |  |  |  |  | Ac cur = 9 4. 0 9 % acy |
| 4 0 [ ] | EM G- s Ba se | d ho d Me t | EL M |  | 5 8 | 7 | b La | F- Sc 9 3. 7 5 % ore = |
|  |  |  |  |  |  |  |  | Re l l 9 3. 3 3 % ca = |
|  |  |  |  |  |  |  |  | Pre is ion 6 9. 4 0 % c = |
| 4 [ 2] | EM G- Ba d se | Me t ho d | G B |  | 1 0 | 2 6 | La b | F- Sc 7 6. 6 0 % ore = |
|  |  |  |  |  |  |  |  | Re l l = 7 4. 1 0 % ca |
| [ 4 3 ] | E C G- Ba d se | Me t ho d | br i d Hy |  | 1 0 | 2 0 | S im lat ion u | Ac = 1 0 0 % cur acy |
| [ 7 6 ] | E C G- Ba d se | Me t ho d | BP N N |  | 9 | 8 | S im lat ion u | N / A |
| 8 3 [ ] | E C G- Ba d se | Me t ho d | AR -G AR | C H | 1 0 | 1 | F ie l d | N / A |
|  |  |  |  |  |  |  |  | Ac 8 8. 3 % Fo les |
| 8 5 [ ] | E C G- Ba d se | Me t ho d | KN N |  | 2 5 | 3 2 | La b | cur acy = ( r ma ) Ac = 8 5. 7 % ( Fo fem les ) cur acy r a |
| [ 8 7 ] | E C G- Ba d se | Me t ho d | AN N |  | 5 | 5 6 | La b | Ac = 8 9. 3 % cur acy |
| 8 9 [ ] | br Hy | i d | ME RF |  | 2 1 | 5 8 | Re l-w l d a or | N / A |
|  |  |  |  |  |  |  |  | Ac 8 9. 47 % cur acy = |
| [ 1 3 1] | Hy br | i d | X G- Bo | ost | 5 5 | 2 3 | F ie l d | Pre is ion = 8 0 % c F- Sc ore = 8 8. 8 9 % |
|  |  |  |  |  |  |  |  | Re ca l l = 1 0 0 % |
|  |  |  |  |  |  |  |  | AU D = 0. 9 |
|  |  |  |  |  |  |  |  | Ac cur = 9 6 % acy |
| 1 1 9 [ ] | br Hy | i d | RF |  | 2 4 | 4 3 | La b | Pre is ion 9 3 % c = F- Sc 9 3 % |
|  |  |  |  |  |  |  |  | ore = Re l l 9 2 % |
|  |  |  |  |  |  |  |  | = ca |
| 1 3 6 [ ] | EM G- Ba d se | Me t ho d | ML PN | N | 1 4 | N A / | La b | Ac 9 1 % cur acy = Re l l = 9 3 % ca |
|  |  |  |  |  |  |  |  | Ac = 9 2 % cur acy |
| [ 1 3 7 ] | br Hy | i d | S V M |  | 6 | 1 0 | La b | Pre c is ion = 9 0 % |
| [ 1 3 8 ] | s EM G- Ba se | d Me t ho d | F_ G RU |  | 8 | 9 | S im u lat ion | Ac cur = 9 8 % acy |
| [ 3 8 ] | EE G- Ba d se | Me t ho d | EL M |  | 6 | 9 6 | S im lat ion u | Ac = 9 1. 7 8 % cur acy |
|  |  |  |  |  |  |  |  | Ac = 9 6. 3 % cur acy |
| [ 4 5 ] | PP G- Ba se d | Me t ho d | S V M |  | 1 0 | 2 | La b | Pre c is ion = 9 7. 8 0 % |
|  |  |  |  |  |  |  |  | Re ca l l = 9 4. 7 0 % |
| [ 4 6 ] | E O G- Ba se d | Me t ho d | C C N F |  | 3 0 | 3 6 | Hy br i d | N / A |
| [ 7 2] | br | i d | L S TM |  | 1 2 | N / A | S im lat ion | Ac cur = 9 8 % acy |
|  | Hy |  |  |  |  |  | u | F- Sc ore = 9 5 % |
| [ 1 0 9 ] | Hy br | i d | S V M |  | 2 8 | 3 8 | S im u lat ion | Ac cur = 9 8. 4 3 % acy |
| [ 9 9 ] | EE G- Ba se d | Me t ho d | N U |  | 2 9 | 9 6 | S im u lat ion | Ac cur = 9 3. 7 7 % acy |
| [ 1 0 |  |  |  |  |  |  |  | Ac 8 2. 9 % |
| 0 ] | EE G- Ba se d | Me t ho d | L S TM |  | 1 6 | 4 1 0 0 | S im u lat ion | Ac cur = 9 4. 3 1 % acy |
| [ 1 0 1] | EE G- Ba se d | Me t ho d | S V M |  | 2 3 | 6 0 | La b | cur = acy Pre c is ion = 8 4. 4 0 % |
|  |  |  |  |  |  |  |  | Re ca l l = 6 6. 4 0 % |

| Tab |
| --- |
| le |
| 1: Sum |
| ma ry |
| of |
| fati |
| gue |
| mo |
| nit |
| ori |
| ng |
| tec |
| hni |
| que |
| s |
| usi |
| ng |
| EC |
| G, |
| ED |
| A, |
| EE |
| G, |
| EM |
| G, |
| EO |
| G, |
| GP |
| S, |
| PP |
| G, IM |
| Us , |
| sEM |
| G, |
| and |
| hy |
| bri d |
| me |
| tho |
| ds. |

| Re fer en ce | M o da l ity | M ac h ine Le arn ing M et ho ds | Sa le S ize mp | Fe atu re Co un t | Ex er im en t p | Pe r for ma nc e Re su lt |
| --- | --- | --- | --- | --- | --- | --- |
| [ 1 0 3 ] | EE G- Ba se d Me t ho d | EL M | N / A | 5 | La b | Ac cur = 9 1. 8 4 % acy F- Sc ore = 9 3. 3 % |
|  |  |  |  |  |  | Re l l 9 6. 5 0 % ca = |
| 1 3 9 [ ] | br i d Hy | C N N | 6 | N A / | S im lat ion u | Ac 7 0 % for E C G cur acy = Ac 6 4 % for PP G cur = |
| 1 4 0 [ ] | br i d Hy | FM IW PT | 3 1 | N A / | S im lat ion u | acy Ac 9 5 % 9 7 % cur acy = - |
| 8 | br i d | br i d | 3 5 DR O ZY ( ) | N A | La b | Ac 9 9. 6 % DR O ZY cur acy = ( ) |
| [ 2] | Hy | Hy | 9 2 Se l f- Co l lec te d Da tas ( | / et ) | Ac cur | 9 1. 8 % Se l f- Co l lec te d Da tas et acy = ( ) |
|  |  |  |  |  |  | Ac 7 5. 5 % cur acy = |
| 8 [ 1] | E C G- Ba d Me t ho d se | KN N | 3 5 | 6 | La b | AU C = 0. 7 4 |
|  |  |  |  |  |  | Ac 9 4. 5 % cur acy = |
| 8 [ 4] | E C G- Ba d Me t ho d se | RF | 6 0 | 9 | La b | F- Sc = 9 5 % ore |
| [ 1 4 1] | EM G- Ba d Me t ho d se | MP F | 1 0 | N / A | S im lat ion u | N / A |
|  |  |  |  |  |  | Ac = 8 4 % cur acy |
| [ 1 0 2] | EE G- Ba d Me t ho d se | br i d Hy | 5 0 | 1 0 | La b | Pre c is ion = 8 3 % |
|  |  |  |  |  |  | Re ca l l = 8 4 % |
| [ 1 0 7 ] | Hy br i d | BT | 1 2 | 2 1 | S im u lat ion | Ac cur = 8 2. 6 % acy |
|  |  |  |  |  |  | Ac cur = 9 5. 1 8 % acy |
| [ 9 1] | s EM G- Ba se d Me t ho d | L S TM | 2 0 | 4 | La b | Pre c is ion = 9 6. 6 5 % |
|  |  |  |  |  |  | Re ca l l = 9 4. 0 8 % |
| [ 9 8 ] | s EM G- Ba se d Me t ho d | ML PN N | 3 0 | 2 | La b | Ac cur = 6 0. 1 2 % acy |
| [ 9 7 ] | s EM G- Ba se d Me t ho d | HM M | 6 | 8 | La b | Ac cur = 9 5. 3 % acy |
| [ 1 27 ] | E O G- Ba se d Me t ho d | Ot he r | 1 6 | 1 | Re a l-w or l d | N / A |
| [ 1 2 8 ] | Hy br i d | Hy br i d | 2 3 | N / A | S im u lat ion | N / A Ac 9 3 % den |
|  |  |  |  |  | Ac | cur = (us er- dep en t ) acy cur = 8 9 % (us er- in dep en den t ) acy |
| [ 1 2 6 ] | E O G- Ba se d Me t ho d | Q D A | 2 4 | 3 | Re a l-w or l d | Pre c is ion = 8 6 % |
|  |  |  |  |  |  | Re l l 9 2 % ca = |
|  |  |  |  |  |  | AU C 0. 9 4 = |
| 1 [ 2] | br i d Hy | Ac Ro N N | 5 | 5 3 | Re l-w l d a or | N A / |
| 1 1 [ 1] | PP G- Ba d Me ho d se t | Ot he r | 7 | 1 | La b | Ac 9 5. 9 2 % cur acy = |
| 1 1 0 [ ] | PP G- Ba d Me ho d se t | Ot he r | 1 9 | 3 | br i d Hy | N A / |
|  |  |  |  |  |  | Ac RF 8 0. 5 % cur acy = : |
| 1 3 0 [ ] | br i d Hy | br i d Hy | 3 2 | 2 6 9 | La b | Ac L S TM 8 4. 1 % cur acy = : |
|  |  |  |  |  |  | Re l l = 9 0 % ( L S TM ) ca |
|  |  |  |  |  |  | Re ca l l = 8 8 % ( RF ) Ac = 9 4. 7 % cur acy |
| [ 1 1 5 ] | ED A- Ba se d Me t ho d | G B | 2 0 | 4 0 | La b | F- Sc ore = 9 1. 6 1 % |
|  |  |  |  |  |  | Re ca l l = 9 2. 9 0 % |
| 1 1 | ED A- Ba d Me t ho d | DT | 5 0 | 3 6 | La b | Ac cur = 8 9. 1 8 % acy Re l l 9 3. 9 % D istr |
| [ 4] | se |  |  |  |  | ca = ( ess ) Re l l 8 5. 3 6 % Ca lm ca = ( ) |

| Re | fer | M | da | l | ity | M | h | ine | Le | ing | M | ho | ds | Sa | le | S | ize | Fe | Co | Ex | im | Pe | for | Re | lt | et | atu | t | t | en | ce | o | ac | arn | mp | re | un | p | er | en | r | ma | nc | e | su | 5 | Ac | 8 | 9. | % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cur | acy | = | Re | l | l | 1 | 0 | 0 | % |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ca | = | [ | 1 | 4 | 2] | Hy | br | i | d | DT | 1 | 9 | 3 | S | im | lat | ion | u | AU | C | 0. | 8 | 3 | 3 | ( | No | ) | tem | tur |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| se | p | era | e | = | AU | C | 0. | 9 | 5 | ( | ist | ) | 7 | W | tem | tur |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| r | p | era | e | = | 6 | Ac | 8. | 3 | 1 | % | ( | Fo | ) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| sta | tes | cur | acy | ur | = | br | i | d | im | lat | ion | [ | 7 | 4] | Hy | S | V | M | 2 | 8 | 1 | 9 | 0 | S | u | Ac | 8 | 4. | 4 | 6 | % | ( | T | hre | ) | sta | tes |  |  |  |  |  |  |  |  |  |  |  |  |  |
| cur | acy | e | = | [ | 1 | 4 | 3 | ] | G | P | S- | Ba | d | Me | ho | d | Ot | he | 3 | 0 | 6 | F | ie | l | d | N | / | A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| t | se | r | Ac | 8 | 5- | 9 | 0 | % |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| cur | acy | = | is | ion | Pre | 9 | 0 | % |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| c | = | 5. | [ | 1 | 3 | 2] | Hy | br | i | d | Hy | br | i | d | 4 | 5 | 9 | 0 | F | ie | l | d | F- | Sc | 8 | 7 | 1 | % |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ore | = | Re | l | l | 8 | 8. | 8 | 9 | % |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ca | = | AU | C | 0. | 8 | 5 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| = |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ac | 9 | 9. | 5 | % | ( | h | ) | Mo | ut | cur | acy | = | Ac | 9 | 9. | 0 | 1 | % | ( | Ey | ) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| cur | acy | e | = | 5 | [ | 7 | 1] | Hy | br | i | d | DN | N | N | / | A | N | / | A | S | im | lat | ion | Pre | is | ion | 9 | 8. | 1 | % | ( | Ey | ) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| u | c | e | = | Re | l | l | 9 | 9. | 8 | 1 | % | ( | Ey | ) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ca | e | = | AU | C | 0. | 9 | 9 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| = |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ac | 9 | 6 | % | cur | acy | = | is | ion | Pre | 9 | 3 | % |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| c | = | br | i | d | b | [ | 1 | 1 | 9 | ] | Hy | RF | 2 | 4 | 4 | 3 | La | F- | Sc | 9 | 3 | % |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ore | = | Re | l | l | 9 | 2 | % |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ca | = | Ac | 9 | 6 | % |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| cur | acy | = | is | ion | 9 | 3 | % | Pre |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| c | = | 1 | 2 | 2] | S | 1 | 9 | / | A | ie | l | d | [ | IM | Us | L | TM | N | F | F- | Sc | 9 | 2 | % |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ore | = | Re | l | l | 9 | 3 | % |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ca | = | Ac | 9 | 2. | 3 | 1 | % |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| cur | acy | = | br | i | d | ie | l | d | Sc | 9 | 2. | 4 | 0 | % | [ | 1 | 2 | 1] | Hy | DT | 1 | 0 | 1 | 2 | F | F- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ore | = | l | l | Re | 1 | 0 | 0 | % |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ca | = | [ | 1 | 0 | 4] | EE | G- | Ba | d | Me | ho | d | Ot | he | 3 | 0 | 2 | Re | l-w | l | d | N | / | A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| t | se | r | a | or | [ | 9 | 0 | ] | EM | G- | Ba | d | Me | ho | d | S | V | M | 2 | 0 | 5 | La | b | Ac | 8 | 6. | 6 | 9 | % |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| t | s | se | cur | acy | = | 9 | 5 | G- | d | ho | d | br | i | d | 5 | 2 | 4 | b | Ac | 9 | 1. | 3 | 9 | % | [ | ] | EM | Ba | Me | Hy | La |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| t | se | cur | acy | s | = | las | det | ion | Ac | 9 | 8. | 7 | % | ( | Tw | ) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ect | cur | acy | o-c | s | = | Ac | 9 | 0. | 9 | % | ( | F | ive | las | det | ion | ) | ect |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| cur | acy | -c | s | = | 1 | 2 | 4] | O | G- | d | ho | d | br | i | d | 1 | 0 | 1 | 6 | S | im | lat | ion | Pre | is | ion | 8 | 1. | 6 | 0 | % | [ | E | Ba | Me | Hy | t |  |  |  |  |  |  |  |  |  |  |  |  |  |
| se | c | u | = | Sc | 8 | 0. | 6 | 0 | % | F- |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ore | = | l | l | 9. | 8 | 0 | % | Re | 7 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ca | = | d | ho | d | b | [ | 1 | 2 | 3 | ] | E | O | G- | Ba | Me | BP | N | N | 2 | 4 | 8 | La | N | / | A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| t | se | S | EE | D- | V | I | G | dat |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| t | ase | [ | 2 | 8 | ] | Hy | br | i | d | S | V | M | N | / | A | S | im | lat | ion | Ac | 9 | 5. | 17 | % | u | cur | acy | = | S | im | lat | d | dr | iv | ing | dat |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| e | a | u |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

| fer | ity | ine | ing | Sa | S | ize | Co | im | for | Re | M | da | l | M | h | Le | M | ho | ds | le | Fe | Ex | Pe | Re | lt | et | atu | t | t | en | ce | o | ac | arn | mp | re | un | p | er | en | r | ma | nc | e | su | Ac | 9 | 3. | 5 | 8 | % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cur | acy | = | is | ion | 9 | 4. | 2 | 5 | % | ( | lax | d | Sta | ) | Pre | Re | te |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| c | e | = | is | ion | 9 | 2. | 2 | 5 | % | ( | it | ion | Sta | ) | Pre | Tra | te |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| c | ns | = | is | ion | 5 | ire | d | Pre | 9 | 4. | 2 | % | ( | T | Sta | ) | te |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| c | = | F- | Sc | 9 | 4. | 2 | 5 | % | ( | Re | lax | d | Sta | ) | te |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ore | e | = | [ | 3 | 6 | ] | Hy | br | i | d | S | V | M | 2 | 0 | 7 | La | b | F- | Sc | 9 | 2. | 2 | 5 | % | ( | Tra | it | ion | Sta | ) | te |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ore | ns | = | Sc | 9 | 4. | 2 | 5 | % | ( | ire | d | Sta | ) | F- | T | te |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ore | = | l | l | 9 | 4. | 2 | 5 | % | ( | lax | d | Sta | ) | Re | Re | te |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ca | e | = | l | l | 5 | it | ion | Re | 9 | 2. | 2 | % | ( | Tra | Sta | ) | te |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ca | ns | = | Re | l | l | 9 | 4. | 2 | 5 | % | ( | T | ire | d | Sta | ) | te |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ca | = |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

| Re fer en ce | Stu dy | Dr | Pa To ic p er p iv Fa t Ev lua t ion ing ig | Pr d M et ho d op ose Su ort Ve cto Ma h ine S V M de l ( ) | Ov l l Pe for era r ma nc e E f fe ct ive fat det ect ion in l-t im it h 5-s d ig |
| --- | --- | --- | --- | --- | --- |
|  |  | on | ue a | p p r c mo | ue rea e w eco n |
| [ 3 5 ] | ste Sy | Ba m | d S ho rt T im Pe io d se on e r | it h RB F ker l, ing w ne us | E C G int ls, h iev ing h ig h d to erv a ac acc ura cy com p are |
|  |  |  | E C G S ig na l | HR V t im e- fre ue do ma in fea tur es q ncy | lon er io d E C G me t ho ds g- p |
| [ 3 7 ] | Re Va | sea rc h r iou s | on t he Re co n it ion o f g Mu sc le Fa t ig ue Sta tes in | Co nv o lut ion a l Ne ura l Ne tw or k ( C N N ) mo de l, Mu lt i- S V M, Mu lt i-L D A | C N N ac h iev e d t he h ig he st acc ura an d AU C, cy ou tp er for m ing Mu lt i- S V M an d Mu lt i-L D A in fat ig ue |
|  | Au | Re s ist tom ate Fa t ig | anc e Str en t h Tra in ing g d De tec t ion o f Mu sc le Co d it ion ue n s Us ing | Ex h ine EL M tre me Le arn ing Ma c ( ), | rec n it ion acr oss fou r fat ig ue lev e ls. og EL M mo de l w it h eom etr ic fea tur es dem on str ate d g |
| 4 0 [ ] | Cy | los c tat | ion -ba d Ge ic ary se om etr | Mu lt i Pe ML P lay er rce p tro n ( ) | h h d F-s f fe ive for ig acc ura cy an cor e, p rov ing e ct le fat det ect ion mu sc ig ue . |
|  | P hy | Fe ica l s | atu f EM G res o s Fa t De tec t ion Us ig ue ing | L ine S V S V M it h RB F ker ar M, w ne l, Gr d ien t Bo ost ( G B ), a ing | Be st for h iev d it h Gr d ien t Bo ost G B p er ma nc e ac e w a ing ( ), |
| [ 4 2] | EM A To | G We ara Ma c h wa r ds | b les an d Us er Re ort s - p ine Le arn ing Ap roa c h p A dap t ive Re ha b i l ita t ion | Ex tra -Tr ees ( ET ), Ra n do m Fo res ts ( RF ), w it h ost roc ess ing us ing p -p me d ian f i lte r ing an d tem ora l rou ing | ort e d by ost roc ess ing for tem ora l acc ura sup p p -p p cy im rov em ent F 1 Sc ore im rov e d fro m in it ia l p . p 6 7. 2 % to 7 6. 6 % w it h ost roc ess ing p -p |
| 4 3 | De | ion tec t | d An is f Dr ive an a ly s o r | p g p Su ort Ve cto r Ma c h ine ( S V M ), p p K- Ne Ne h bo KN N | En sem b le c las s i f ie r ac h iev e d t he h ig he st acc ura for cy las du d 5 8. 3 % in f iv las tw o-c s sta tes ; re ce acc ura cy ( ) e-c s |
| [ ] | Sta te | it h w | E lec d E C G tro car iog ram ( ) | are st ig rs ( ), En b le C las i f ie sem s r | det ion dro fat isu l ina ion ect (no rm a l, ws y, ig ue v a tte nt , , it ive ina tte nt ion co g n ) |
| [ 7 6 ] | Le | Re sea rc l Us ve | h Dr iv Fa t on ing ig ue E C G S l fro ing ig na m | BP Ne l Ne tw k for dat sat ion ura or a com p en , lt i- in dex fus ion t he mu ory | BP Ne l Ne tw k d P C A fu l d ist is he d ura or an suc ces s ly ing u fou fat lev ls i de ke i l der |
|  |  | Mo de l | Sm art Br ace let ing an d Re co n it ion o f g | w it h r inc ip a l com on ent an a ly s is ( P C A ) p p AR 1 G AR C H 1 de l for im ies | r ig ue e (w aw a m d, mo ate sev ere ) , , E f fe ive det ion f fat it h it ion de |
| [ 8 3 ] | on | Dr iv ing R- R | Fa t ig ue Sta te Ba se d Int erv a ls o f E C G Da ta | ( )- ( 1, ) mo t e ser an a ly s is Su ort Ve cto r Ma c h ine ( S V M ) an d | ct ect o ig ue w a rec n lay og o f les s t ha n 5 m inu tes for a l l dr ive rs |
| 8 5 [ ] | A lg or | ive Dr r it hm s | ine ion Dr ow s ss De tec t Us E lec d ing tro car iog ram | p p h bo K- Ne are st Ne ig rs ( KN N ) it h Wa let Tra for W T d w ve ns m ( ) an | it h let for h iev d he h he KN N w Wa ve Tra ns m ac e t ig st dem im d det ion for acc ura cy, on str at ing p rov e ect p er ma nc e |
|  |  |  | Da ta An is a ly s | S ho rt Fo ier Tra for S TF T ur ns m ( ) for fea tur ext t ion e rac | ot he t ho ds. ov er r me |
|  | Pre d | ict ion | f Ex ha ust ion T hre ho l d o s | Ar t i f ic ia l Ne l Ne tw k ( AN N ) ura or | AN N de l f fe ct ive d ict ha ust ion t hre ho l d mo e ly p re s ex s |
| [ 8 7 ] | Ba | se d on | E C G Fe atu res Us ing | w it h Le ven be Ma ua r dt rg- rq | w it h h ig h cor re lat ion to Bo sca le an d rg |
|  | Ar t | i f ic ia l | Ne ura l Ne tw or k ( AN N ) | ( tra in lm ) tra in ing a lg or it hm | t im e to ex ha ust ion ( TT E ) in d ica tor s. |
|  |  | To wa r | ds Au tom ate d Fa t ig ue | Ra n do m Fo res t M ixe d- E f fe cts Mo de l ( ME RF ) | T he ME RF mo de l dem on str ate d im rov e d er for ma nc e p p |
| [ 8 9 ] |  | As ses | sm ent Us ing We ara b le | us ing e an d BM I c lus ter ing ag , | by inc ora t ing dem h ic fac tor s, orp og rap |
|  |  | Se ns ing | d M ixe d- E f fe an cts Mo de ls | do d Ra n m Fo res t, an L ine Re ion for iso ar g res s com p ar n | h iev he low d h he lat ion ac ing t est err or an ig st cor re he ho ds d. am on g t me t tes te |
|  | In for ste sy | ion ma t for m m | fus ion d lt i-c las i f ie an mu s r ine fat it ion in r ig ue rec og n | Su Ve Ma h ine S V M p p ort cto r c ( ), Ra do Fo t RF n m res ( ), d Ex tre Gr d ien t Bo ost ( X G- Bo ost ), an me a ing us ing | T h is h h h l hts t ha t t he X G- Bo ost de l it h res ear c ig ig mo w |
| [ 1 3 1] | p e lec tro | lat eau car d iog | env iro nm ent s ba se d on hy an d e lec tro hy rap my og rap s ig na ls | Pr inc ip a l Co on ent An a ly s is ( P C A ) an d mp Gr Re lat ion a l An a ly s is ( G R A ) for ey fea tur e se lec t ion | P C A- ba se d fea tur e fus ion ac h iev e d t he be st res lts u , ec ia l ly in a h ig h-a lt itu de m in ing con tex t. esp |

| Re fer en | Pa ce p | To ic er p | Pr d M et ho d op ose | Ov l l Pe for era r ma nc e |
| --- | --- | --- | --- | --- |
|  | A dat dr ive a- n Fa t ig ue Ma na g | h to P ica l ap p roa c hy s em ent Us ing We ara b le | Ra do Fo t RF n m res ( ), Ar t i f ic ia l Ne ura l Ne tw or k ( AN N ), | T h is res ear c h ac h iev e d re l ia b le fat ig ue c las s i f ic at ion |
| [ 1 1 9 ] | Se nso rs for C las | Fo ur Fa t ig ue Le ve ls s i f ic at ion | S V M, De c is ion Tre e ( DT ), K- Ne are st Ne ig h bo rs ( KN N ), ist ic ion LR Lo Re | in wa l k ing tas ks w it h t he RF mo de l us ing re du ce d fea tur e set s, w h ic h he lp e d t im ize mo de l er for ma nc e. op p |
|  | Mu le Fa sc t ig ue | De ion in EM G tec t | g g res s ( ) i-L l k Mu lt er Pe rce tro n Ne ura Ne tw or ( ML PN N ) ay p ine d it h Le be Ma dt L- M d tra w ven rg– rq ua r ( ) an | T he h dem d he f fe ive f res ear c on str ate t e ct ne ss o im fre ho ds b ine d it h t e- q ue ncy me t com w |
| 1 3 6 [ ] | Us T im ing e– I C A, an d | Fre Me t ho ds, q ue ncy Ne ura l Ne tw or ks | Gr d ien t De nt G D A it hm a sce ( ) a lg or t im fre is d us ing e- q ue ncy an a ly s an In dep en den t Co on ent An a ly s is ( I C A ) mp | l tw ks for det ect le fat neu ra ne or ing mu sc ig ue , art icu lar ly it h C W T roc ess ing an d p w p rep L- M a lg or it hm . |
|  | Mo b i le- Ba se | d We ara b le- Ty e p | for fea tur e ext rac t ion Su ort Ve cto r Ma c h ine ( S V M ) c las s i f ie r w it h p p | T he res ear c h dem on str ate s t ha t EM G an d G S R dat a roc ess e d t hro h a mo b i le- ba se d S V M p ug |
| [ 1 3 7 ] | Dr ive r Fa t ig ue an | De tec t ion by G S R d EM G | in fre ue -do ma fea tur e an a ly s is for q ncy EM G d G S R an | las i f ie f fe ive det fat h iev c s r can e ct ly ect ig ue ac ing , h h |
|  | Mu le Fa sc t ig | De ion Us ue tec t ing | G RU Ga d Re Un it de l for F_ ( te cur ren t ) mo | ig acc ura cy. T h is h h h l hts he f fe ive f he res ear c ig ig t e ct ne ss o t |
| 1 3 8 [ ] | Fe atu Ex re Le | tra ct ion d De an ep arn ing | fat las i f ic at ion it h fea tur ext t ion ig ue c s w e rac , fro t im d fre do ins m e an q ue ncy ma | F_ G RU de l for h h-a l-t im mo ig ccu rac y, rea e le fat det ect ion mu sc ig ue . |
| [ 3 8 ] | C las s i fy ing Us ing | Dr iv ing Fa t ig ue EE G S ig na ls | Pa rt ic le Sw t im iza t ion br i d Ex tre arm Op Hy me Le arn ing Ma c h ine ( P S O- H- EL M ), Su ort Ve cto r Ma c h ine ( S V M ), p p | T he h in d ica tes t ha t t he P S O- H- EL M res ear c c las s i f ie r er for me d be tte r t ha n tra d it ion a l p me t ho ds for dr iv ing fat ig ue det ect ion us ing EE G. |
| 25 | Se nso r- ba se d it ion rec n us | dr ive r con d it ion ing ort vec tor | K- Ne are st Ne ig h bo rs ( KN N ) Su ort Ve cto r Ma c h ine ( S V M ) c las s i f ie r p p | T h is res ear c h dem on str ate d t he h ig h e f fe ct ive ne ss f S M it h PP G dat fro b le o us ing V w a m a we ara |
| 4 5 [ ] | og h ine for he ma c t dro | sup p det ion f dr ive ect o r ine ws ss | it h dat l iza ion d ion w a no rm a t an seg me nta t for ha d las i f ic at ion en nc e c s | dev ice ize dro ine in l le d to rec og n ws ss a con tro dr iv im lat ion iro ent ing s u env nm . |
| [ 4 6 ] | V i lan Es ig ce We ara b le E O Dr iv ing | t im at ion Us ing a G De v ice in Re a l En v iro nm ent s | Co nt inu Co d it ion l Ne l F ie l d ( C C N F ) ou s n a ura an d Co nt inu ou s Co n d it ion a l Ra n do m F ie l d ( C C RF ) for tem ora l mo de l ing o f v ig i lan ce sta tes p | T h is h h h l hts t he f fe ct ive f res ear c ig ig e ne ss o a b le E O G dev ice for t inu i lan we ara con ou s v ig ce mo n ito r ing in rea l-w or l d an d s im u lat e d env iro nm ent s, w it h h ig h cor re lat ion va lue s in d ica t ing acc ura te |
| [ 7 2] | Dr ive r S lee p EE G d E O an | ine ss De tec t ion fro m G S ls ig na Us ing | Lo S ho rt- Te rm Me mo ( L S TM ) ne tw or ks, ng ry d it h Co d it ion l Wa in G AN C W G AN | v ig i lan ce est im at ion . T h is Re sea rc h use d C W G AN to en ha nc e tra in ing dat a for L S TM h iev h h in dro ine ac ing ig acc ura cy ws ss , |
|  | G AN d L an We b le De ara v | S TM Ne ks tw or ice -B d ase Sy ste m to | aug me nte w n a sse rst e ( ) Su Ve Ma h ine S V M las i f ie it h p p ort cto r c ( ) c s r w | det ion ito ha in EE G d E O G. ect by mo n r ing a lp wa ve s an T h is h dem he f fe ive f res ear c on str ate s t e ct ne ss o us ing |
| 1 0 9 [ ] | Mo ito Dr ive 's n r r Dr | Str Fa t d ess ig ue an , , ine ow s ss | fea tur lec t ion AN O V A d e se us ing an Se nt ia l F loa t Fo d Se lec t ion ( S FF S ) q ue ing rw ar | b le it h S V M las i f ic at ion for we ara sen sor s w c s ito dr ive sta tes in im lat d iro ent mo n r ing r a s u e env nm . |
| [ 9 9 ] | Ite rat ive Cr -Su b oss j Le arn ing A lg or it hm | ect Ne at ive -U la be le d g n for Qu ant i fy ing Pa ss ive | Ne at ive -U la be le d ( N U ) Le A it hm g n arn ing lg or us ing Su ort Ve cto r Ma c h ine ( S V M ) w it h an p p | T h is h h h l hts t he f fe ct ive res ear c ig ig e ne ss o f t he N U lea rn ing roa c h for cro ss- su b j ect ap p |
|  |  | Fa t ig ue | RB F ker ne l Hy br i d mo de l com b in ing s ig na l-p roc ess ing -ba se d | ass ive fat ig ue det ect ion p . T h is res ear c h com b ine s tra d it ion a l s ig na l |
| [ 1 0 0 ] | An E f fe ct ive Hy br i Dr ow s | d Mo de l for EE G- Ba se d ine ion ss De tec t | fea tur es an d de lea rn ing -ba se d fea tur es, us ing ep ho d Lo S rt- Te rm Me mo ( L S TM ) an ng ry | roc ess ing an d de lea rn ing fea tur es, p ep ho h h for ba d s w ing ig acc ura EE G- se cy |
|  |  |  | de lut ion l ks A lex Ne d V G G Ne ep con vo a ne tw or ( t an t ) | dro ine det ion ws ss ect . |

| Pr ose d M et ho d Ov era l l Pe r for ma nc e op T h is res ear c h con f irm s t he fea s i b i l ity o f us ing Au tom at ic De tec t ion o f Dr ow s ine ss Us ing 0 1] Su ort Ve cto r Ma c h ine ( S V M ) w it h RB F ker ne l in- ear EE G for dro ws ine ss det ect ion ac h iev ing p p , In- Ea r EE G bst ia l in l le d su ant acc ura cy a con tro set t ing . Tu na b le Q- Fa cto r Wa ve let Tra ns for m ( T Q W T ) for fea ion d iou las i f ie T h is Re h f irm he f fe ive f tur e ext rac t an var s c s rs sea rc con s t e ct ne ss o Fe Ex ion Me ho d for C las i f ic ion atu re tra ct t s at De is ion Tre Lo ist ic Re ion T W T- ba d fea tur in d ist is h be tw ( c e, g g res s Q se es ing u ing een , 0 3 f A ler tne d Dr ine Sta tes in ] o ss an ow s ss F ine Ga ian S V M, ler tne d dro ine h iev h h uss a ss an ws ss, ac ing ig EE G S ig na ls We ig hte d KN N, En sem b le Bo ost e d Tre c las s i f ic at ion er for ma nc e w it h EL M es, p . Ex tre me Le arn ing Ma c h ine ) T h is res ear c h h ig h l ig hts t he e f fe ct ive ne ss o f Us ing We ara b le E C G / PP G Se nso rs Co nv o lut ion a l Ne ura l Ne tw or k ( C N N ) w it h t hre e us ing rec urr en ce lot s w it h C N N for dro ws ine ss p for Dr ive r Dr ow s ine ss De tec t ion ty es o f Re cur ren ce P lot s ( B in- RP Co nt- RP Re LU -R P ) p , , det ion in irtu l dr iv E C ect a v a ing set up us ing Ba d Re P lot for fea ion d dro ine las i f ic ion se on cur ren ce s tur e ext rac t an ws ss c s at d PP G dat an a. T h is h dev d fuz ba res ear c e lop e a zy -en tro p y- Dr ive Dr ine C las i f ic ion Fu Mu l In for ion Wa let Pa ke Tra for FM IW PT r ow s ss s at zzy tua ma t ve c t ns m ( ) let ke ts tra for for dr ive dro ine wa ve p ac ns m r ws Us Fu Wa let -Pa ke t- Ba d for fea tur ext t ion b ine d it h iou las i f ie LD A, ing zzy ve c se e rac com w var s c s rs ( , las i f ic at ion h iev h h in c s ac ing ig acc ura cy , Fe atu re- Ex tra ct ion A lg or it hm kN N, LI BL IN E AR LI B S V M ) , s im u lat e d con d it ion s. Da ta- dr ive n lea rn ing fat ig ue det ect ion T h is res ear c h com b ine s E C G an d v i de o dat a to ste m: A mu lt im o da l fus ion roa c h X G Bo ost c las s i f ie r w it h a hy br i d o f ha n dcr a fte d an d sy ap p h ig h det ect ion acc ura in d i f fe ren t fat ig ue con d cy o f E C G (e lec tro car d iog ram ) an d v i de o de lea rn ing fea tur es fro m E C G an d v i de o dat a ep l i h va dat ing t he roa c acr oss dat ase ts. ap p ls s ig na | Re fer [ 1 1 [ | en ce Pa er To ic p p |  |
| --- | --- | --- | --- |
| 3 9 ] G d se ss 4 0 ] ac h iev e 2] it ion s, h is h l i dat he f ba d fea T res ear c va es t use o HR V- se tur es De ion f Me l Fa Sta HR V He Ra Va ia b i l in d ica d it h tec t o nta t ig ue te ( art te r ity ) tor s use w fro b le E C G dev ice for l fat det ion 1] m we ara s me nta ig ue ect , | [ 1 1 [ [ 8 8 [ |  | 26 |
| it h We b le E C G De ice las i f ie S V KN Na ïve Ba Lo ist ic Re ion w ara v s c s rs ( M, N, y es, g g res s ) h iev ta b le it h t he KN N las i f ie ac ing no acc ura cy w c s r. Pr inc l Co ent An is P C A for fea tur lec t ion T h is h dem str ate f fe ct ive nta l fat ip a mp on a ly s ( ) e se res ear c on s e me ig ue , E C G S l Fe atu C las i f ic at ion for Ra do Fo t ( RF ), K- Ne st Ne h bo ( KN N ), det ect ion E C G fea tur d h ine lea ig na res s n m res are ig r us ing es an a ma c rn ing 4] Me nta l Fa t Re it ion L ine D isc im ina nt An is LD A d las i f ic at ion de l, it h h h h iev d | [ 8 |  |  |
| ig ue co n ar r a ly s ( ), an c s mo w ig acc ura ac e g cy De c is ion Tre e ( DT ) c las s i f ie rs t hro h t he RF c las s i f ie r. ug E lec tro h ica l Ma n i fes tat ion s o f EM G fre ue an d am l itu de an a ly s is w it h my og rap q ncy p T h is res ear c h lor es EM G- ba se d fat ig ue in d ica tor s exp Mu sc le Fa t ig ue Du r ing D i f fe ren t Le ve ls res s ion an a ly s is to me asu re fat ig ue reg 4 1] in low -in ten s ity ma nu a l tas ks, h ig h l ig ht ing t ha t mu sc le f S im lat d L ht l As b low -in d it ion Ma tw ten | [ 1 |  |  |
| o u e ig nu a sem ly ov er o s ity con s fat be det d hro h MP F de ks ig ue can ect e t ug cre ase s acr oss tas . Wo k 8 % d 1 2 % MV C r ( an ) EE G- Ba d Es im ion f Me l Fa Ke l Pr inc l Co An is KP C A T h is h f fe ive b ine KP C A d HM M se t at o nta t ig ue rne ip a mp on ent a ly s ( ) res ear c e ct ly com s an 0 Us KP C A– HM M d Co lex b ine d it h H i d den Ma ko Mo de l HM M for det ect nta l fat lev lex 2] ing an mp ity com w r v ( ) ing me ig ue era g ing com p ity , Pa for l fat las i f ic ion las i fat it h h h | 1 [ |  |  |
| ete nta at to sta tes ram rs me ig ue c s me asu res c s fy ig ue w ig acc ura cy. Bo ost d tre las i f ie io ica l T h is h fou d t ha t ito k in tem tur e e c s r us ing p hy s log res ear c n mo n r ing s p era e Mo ito Fa t in Co nst t ion n r ing ig ue ruc 0 7 ] fea tur es fro m he art rat s k in tem era tur fro m t he tem le ion wa s art icu lar ly e f fe ct ive e, p e, p reg p , Wo r ker s Us ing P hy s io log ica l Me asu rem ent s an d EE G me asu rem ent s to c las s i fy fat ig ue lev e ls ac h iev ing h ig he r acc ura t ha n he art rat e a lon e. cy L S TM ( Lo S ho rt- Te rm Me mo ) ne tw or k, T h is res ear c h s ho wc ase s a h ig h-a ccu rac mu sc le | [ 1 |  |  |
| ng ry y A Mu sc le Fa t ig ue C las s i f ic at ion Mo de l Ba se d 1] Im rov e d Wa ve let Pa c ke t T hre s ho l d fun ct ion fat ig ue det ect ion mo de l w it h L S TM lev era ing p , g on L S TM an d Im rov e d Wa ve let Pa c ke t T hre s ho l d p for den is ls ha d l den is hro h let hn o ing s EM G s ig na en nc e s ig na o ing t wa ve tec iq ue s. ug Es t im at ion o f E l bo w K ine ma t ics Un der Mu lt i- lay ere d Pe rce tro n Ne ura l Ne tw or k ( ML PN N ), T h is res ear c h att em ts to est im ate e l bo w mo vem ent p p | [ 9 |  |  |
| Fa d No n-F Co d it ion foc IEM G d Ze Cr Z C d las i fat d it ion h iev der t ig ue an at ig ue n s us ing on an ro oss ing ( ) as an c s fy ig ue con s, ac ing mo ate 8 ] Us ML PN Ne tw k Ba d fea tur for l bo k ine t ics d it h ML PN N ba d i f ic t im do in ing or se on key es e w ma an acc ura cy w se on sp ec e- ma fat las i f ic at ion EM G fea tur ig ue c s s es. | 9 [ | EM G S l s ig na |  |

| d M et ho d Ov l l Pe for ion for fat ig ue sta tus c las s i f ic at ion exe rc ise s. Ey e b l in k fre ue an a ly s is to ass ess T h is res ear c h ut i l ize s E O G- ba se d e b l in k fre ue in a q ncy ey q ncy Co nt inu ou s A ler tne ss As ses sm ent s Us ing fat ig ue lev e ls; me asu rem ent s cor re lat e d w it h we ara b le dev ice to con t inu ou s ly mo n ito r a ler tne ss lev e ls 27 ] E O G G las ses to Un o btr us ive ly Mo n ito r Fa t ig ue Ps ho V i lan Ta k PV T ion in l-w l d ho lat ion be y c mo tor ig ce s ( ) rea ct rea or set t ing s, s w ing a cor re tw een Le ls In- T he -W i l d ve im d h for ler lev ls inc d b l in k fre d de d ler t es as a g rou n tru t a tne ss e rea se q ue ncy an cre ase a tne ss. Fa Dr iv De ion Me ho d Ba d Co lut ion l Au der C AE for fea fus ion d T h is h dem he f fe ive f lt im da l t ig ue ing tec t t se on nv o a toe nc o ( ) tur e an res ear c on str ate s t e ct ne ss o mu o 2 8 T im -Fr Fe atu f Mu lt im da l Co lut ion l Ne l Ne tw k C N N fo l low d EE G d E O G fea tur fus ion in det ect fat ] e- Sp ace eq ue ncy res o o nv o a ura or ( ) e an e ing ig ue , S ig ls by Lo S ho rt- Te Me ( L S TM ) for las i f ic at ion it h str for tr ics ing C AE d B i-L S TM na ng rm mo ry c s w on g p er ma nc e me us an . Qu dra t ic D isc im ina nt An is ( Q D A ) las i f ie a r a ly s c s r, T h is h dem str ate t he ote nt ia l for ing E O G ig ls res ear c on s p us s na Fa t ig ue De tec t ion Ca use d by O f f ic e Wo r k w it h fea tur es ba se d on b l in k an a ly s is, 2 6 ] to mo n ito r fat ig ue in an o f f ic e env iro nm ent w it h h ig W it h t he Us e o f E O G S ig na l inc lu d ing b l in k du rat ion b l in k am l itu de , p , c las s i f ic at ion acc ura cy. an d t im e be tw een b l in ks T h is res ear c h dev e lop s a no ve l Ac Ro N N mo de l inc orp Ac t iv ity -A wa re De Co n it ive Fa t ig ue Ac t iv ity -A wa re Re cur ren t Ne ura l Ne tw or k ( Ac Ro N N ) ep g iv for it ive fat 2] act ity -aw are ne ss mo re acc ura te co g n ig As Us We b les it h L S TM d Co ist Se l f- At ion ses sm ent ing ara w tw o-s tag e an ns en cy ten t im ion est at acr oss var y ing con tex ts. He Ra Mo ito Du An dro i d- ba d l ica ion it h T h is h int du l-t im he ito art te n r ing Sy ste m r ing se ap p t w an res ear c ro ces a rea e art rat e mo n r 1 P ica l Ex ise for Fa t Wa Us Ea Pu lse PP G for l-t im ito ste it h t i f ic at ion ba d t hre ho l d l 1] hy s erc ig ue rn ing ing sy sen sor rea e mo n r ing sy m w wa rn ing no s se on s , No n-I ive We b le Se it h ler ts i de d ba d he art rat t hre ho l ds to he fat du ise nv as ara nso r w a p rov se on e s lp ma na g e ig ue r ing exe rc . He art rat d bre at h att ext t ion T h is h lev PP G d ot he art tc h e an ing p ern rac res ear c era g es an r sm wa sen An Un btr ive Sm art tc h-B d P lat for o us wa ase m 1 0 ] fro m PP G, act iv ity det ect ion us ing to mo n ito r fat ig ue un o btr us ive ly, va l i dat ing hy s io log p for Au tom at ic Ba c kg rou n d Mo n ito r ing o f Fa t ig ue acc e ler om ete r an d res sur e sen sor s ma r ker s w it h h ig h cor re lat ion to est a b l is he d too ls. p | en ce er ose era r ma nc e p p op H i d den Ma ko Mo de l ( HM M ) d T h is stu dem str ate t he f fe ct ive f HM M r v an dy on s e ne ss o Fa t ig ue Sta tus Re co n it ion in a Po st- Str o ke g 7 ] Ar t i f ic ia l Ne ura l Ne tw or k ( AN N ) for acc ura te fat ig ue det ect ion in ost -st ro ke re ha b i l ita t p Re ha b i l ita t ion Ex erc ise w it h s EM G S ig na l | Re fer Pa To ic [ 9 [ 1 1 [ | Pr |
| --- | --- | --- | --- |
| h ora t ing ue ing im its sor s ica l Ra n do m Fo res t ( RF ) for hy s ica l fat ig ue ( PF ) T h is res ear c h lev era es a com re he ns ive mu lt im o da l set p g p up |  | [ 1 [ 1 1 [ [ 1 27 |  |
| As ses s ing Fa t ig ue w it h Mu lt im o da l 3 0 ] det ect ion an d L S TM for co n it ive fat ig ue ( C F ) to ass ess hy s ica l an d co n it ive fat ig ue dem on str at ing h ig h g p g , |  | [ 1 |  |
| We ara b le Se nso rs an d Ma c h ine Le arn ing det ion it h for d for ect acc ura w RF PF an L S TM C F. cy |  |  |  |
| Au tom at ic Mo t ion Ar t i fac t De tec t ion in Gr a d ien t Bo ost ing ( Gr a d Bo ost ) c las s i f ie r, T he res ear c h em ha s ize s h ig h acc ura an d F 1 Sc ore in p cy |  |  |  |
| 1 5 E lec der l Ac iv Da Us lua d it h Le -O -Su b -O L O S O det ion i fac it h in ED A dat bu it do ] tro ma t ity ta ing eva te w ave ne j ect ut ( ) ect ing mo t art ts w a, t es no t |  | 1 [ |  |
| Ma h ine Le l i dat ion i de i f ic lue for Pre is ion AU C. c arn ing cro ss- va p rov a sp ec va c or |  |  |  |
| T h is h b le ED A- ba d dev ice las i res ear c use s a we ara se to c s fy E lec tro der l Ac t iv Se for Sta t ist ica l is d las i f ic at ion ma ity nso r an a ly s an c s us ing lm d istr sta tes It dem str ate t he dev ice 's h h ca ver sus ess on s ig . 1 4] C las i f ic at ion f Ca lm / D istr tre ba d de l; Str at i f ie d s o ess a e- se mo |  | [ 1 |  |
| acc ura ma k ing it su ita b le for rea l-t im lon ter m me nta l e, |  |  |  |
| cy, g- Co n d it ion 1 0- fo l d cro ss- va l i dat ion he a lt h mo n ito r ing l ica t ion s. |  |  |  |
| ap p De c is ion tre e c las s i f ic at ion ba se d on |  |  |  |
| Fe atu re Ex tra ct ion an d Ev a lua t ion for T h is res ear c h lor es us ing t he rm ore u lat c ha es to det ect exp g ory ng |  |  |  |
| c ha es in no se an d wr ist tem era tur e ng p |  |  |  |
| 4 2] Dr ive r Dr ow s ine ss De tec t ion Ba se d on dr ive r dro ws ine ss in s im u lat ion s, s ho w ing t he ote nt ia l o f p an d he art rat us ing s lop es in |  | [ 1 |  |
| e, T he lat ion ba d det ion for ito dro ine rm ore g u tem p era tur e- se ect mo n r ing ws ss. |  |  |  |
| d HR ds tem p era tur e an tre n |  |  |  |
| Su Ve Ma h ine S V M las i f ie p p ort cto r c ( ) c s r |  |  |  |
| We b le De ice -B d T h is h b le for l-t im ito ara v ase Sy ste m to res ear c p rop ose s a we ara sy ste m rea e mo n r ing |  |  |  |
| it h for ise du ion d w p rep roc ess ing no re ct an Mo ito Dr ive 's Str Fa t d f dr ive d it ion h iev t ica l for d ist is h 4] n r a r ess ig ue an o r con s, ac ing p rac acc ura cy ing u ing , , |  | 7 [ |  |
| t im l fea tur lec t ion AN O V A d op a e se us ing an Dr ine str fat d dro ine sta tes ow s ss ess ig ue an ws ss . , , |  |  |  |
| Se ue nt ia l F loa t ing Fo rw ar d Se lec t ion ( S FF S ) q |  |  |  |
| T h is h int du C N N- G RU -ba d de lea ing res ear c ro ces a se rn | ep A De Le arn ing Ap roa c h for Fa t ig ue Co nv o lut ion a l Ne ura l Ne tw or k ( C N N ) w it h ep p |  |  |
| ent , | mo de l to re d ict fat ig ue t hro h G P S-t rac ke d mo vem p ug 4 3 ] Pre d ict ion in Sp ort s Us ing G P S Da ta Ga te d Re cur ren t Un its ( G RU ), na me d Fa t ig ue Ne t, | [ 1 |  |
| ing l l on ma nu a RP E dat a co lec t ion . | rov i d ing ins ig hts int o fat ig ue mo n ito r ing w it ho ut re ly p an d Ra te o f Pe rce ive d Ex ert ion for t im e-s er ies re d ict ion ba se d on G P S dat a fea tur es p |  |  |

| Re | fer | Pa | To | ic | Pr | d | M | ho | d | Ov | l | l | Pe | for | et | en | ce | p | er | p | op | ose | era | r | ma | nc | e | ho | hy | io | log | ica | l | ive | ion | it | h | lat | ion | Ps | Da | Dr | Fe | Pe |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ta- | atu | ext | t | c | p | s | n | re | rac | ars | on | cor | re | y | w | , | T | h | is | h | dem | h | ig | h-a | h | str | ate | res | ear | c | on | s | a | ccu | rac | y | ap | p | roa | c | lt | i-F | for | ion | ion | d | d | O | C | ly | is. | Mu | In | Fu | R | eat | t | t-te | sts |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ure | ma | s | an | an | an | a | s | , | 1 | 3 | 2] | for | i | den | i | fy | ing | ine | fat | ig | by | b | in | ing | hy | io | log | ica | l | [ | t | m | r | ue | com | p | s | it | ion | f | ine | ig | las | i | f | ic | ion | ing | h | ine | Re | M | Fa | Su | Ve | Ma | ( | S | V | M | ) | t | at | ort | cto |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| co | g | n | o | r | ue | c | s | us | p | p | r | c | fac | in | ha | l | len | ing | iro | tor | ent | s | c | g | env | nm | s. | in | H | ig | h- | A | lt | itu | de | d | Co | l | d | Ar | d | Ra | do | Fo | ( | RF | ) | de | ls | t |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| an | eas | an | n | m | res | mo | Fu | l | ly | Co | lut | ion | l | Re | De | Ne | l | Ne | k | T | h | is | h | h | ig | h-a | fat | ig | ito | ing |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| t | tw | nv | o | a | cur | ren | ep | ura | or | res | ear | c | p | rop | ose | s | a | ccu | rac | y | ue | mo | n | r | ds | Sa | fer | ds | A | ing | d | ( | C | ) | it | h | ba | d | h | ite | for | ing | d | de | lea | ing | for | ha | d | dr | ive | fet | To | Ro | De | Le | -B | F | R- | DN | N | Io | T- | Io | T | ctu | ste |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| wa | r | a | : | ep | arn | ase | se | arc | re | sy | m | us | an | ep | rn | en | nc | e | r | sa | w | y | 1] | [ | 7 | lt | im | da | l | ig | ito | ing | Sy | l-t | im | ito | ing | l | le | l | C | d | by | det | ing | fat | ig | in | d | ica | hro | h | fac | ia | l | fea | d | Mu | Fa | Mo | N | N | t | ste | ect | tor | t | tur |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| o | ue | n | r | m | rea | e | mo | n | r | ; | p | ara | an | ue | s | ug | es | an | L | S | TM | lay | for | d | h | las | i | f | ic | ion | hy | io | log | ica | l | dat | ut | at |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ers | ey | e | an | mo | c | s | p | s | a. | T | h | is | h | h | ig | h | l | ig | hts | h | ig | h-a | h | for |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| res | ear | c | a | ccu | rac | y | ap | p | roa | c | ive | h | hy | ica | l | ig | ion | fro | d | dat | A | Da | Dr | Ap | P | Fa | Fe | IM | U | EM | G | ta- | to | t | atu | ext | t | n | p | roa | c | s | ue | re | rac | m | an | a; | ing | hy | ica | l | fat | ig | hro | h | b | le | t |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ma | na | g | p | s | ue | ug | we | ara | sen | sor | s | [ | 1 | 1 | 9 | ] | Ma | Us | ing | We | b | le | Se | las | i | f | ic | ion | ing | Ra | do | Fo | ( | RF | ) | ent | to | at | t | na | g | em | ara | nso | rs | c | s | us | n | m | res | as | d | h | ine | lea | ing | it | h | i | f | ic | foc |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| an | ma | c | rn | w | a | sp | ec | us | on | , | C | las | i | fy | Fo | D | iag | ic | Fa | ig | Sta | he | im | l | de | l | st | t | tes | t | t | s | ur | no | ue | op | a | mo | ha | b | i | l | ita | ion | d | ise | int | ity | l. | t | tro |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| re | an | exe | rc | en | s | con | AI | de | l | int | ing | Ra | do | Fo |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| rat | t, | mo | eg | n | m | res | h | is | h | ha | ize | AI | -dr | ive | l-t | im | fat | ig | d | T | res | ear | c | em | p | s | s | n, | rea | e | ue | an | AI | -A | ist | d | Fa | ig | d | Sta | ina | Co | l | for | Gr | d | ien | Bo | ing | Ma | h | ine | d | t | ntr | t | ost |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ss | e | ue | an | m | o | a | c | s, | an | ina | ito | ing | in | h | let | ing | lt | iva | iat | im | ies | sta | at | t | m | mo | n | r | es | us | mu | r | e | e | ser | for | Sp | Ge | d | S | ks | for | fat | ig | d | ina | d | ict | ion | [ | 1 | 2 | 2] | Pe | IM | U- | L | TM | ort | ate | tw | sta |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| r | ma | nc | e | s | on | ner | ne | or | ue | an | m | p | re | , | fro | IM | Us | foc | ing | ing | in | ing | d | im | iz | ing | ent | ert | t | m | us | on | p | rev | ov | ra | an | op | lt | iva | iat | im | Se | ies | it | h | l-t | im | fee | d | ba | k | loo | for | , | Mu | T | Da | tas | ets |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| r | e | e | r | w | rea | e | c | p | s | for | p | er | ma | nc | e. | dap | ive | in | ing | d | j | t | tra | ust | nts |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| a | a | me | Ae | b | ic | Fa | ig | T | hre | ho | l | d | ( | AF | T | ) | d | ict | ion |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| t | ro | ue | s | p | re | d | d | Co | inu | ig | h | is | h | l | i | dat | l-t | im | fat | ig | ito | ing | in | Au | Fa | T | tom | ate | nt | t | ste | an | ou | s | ue | res | ear | c | va | es | a | rea | e | ue | mo | n | r | sy | m | ing | B | iL | S | TM | -ba | d | l | k; | ent | tw |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| us | se | rec | urr | neu | ra | ne | or | ito | ing | in | ion | ker | ing | ion | f | fe | ive | ly | ing | for | d | dat | [ | 1 | 2 | 1] | Mo | Co | Wo | Us | EM | G | IM | U | nst | t | str | t | ct | n | r | ruc | r | s | con | uc | e | us | ear | m | an | a | , | is | ion | las | i | f | ie | d | for | De | Tre |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| c | e | c | s | r | use | Fo | EM | G | d | IM | U | We | b | le | Se | for | inu | fat | ig | du | ing | la | bo | int | ive | ks | t | nt | tas | rea | rm | an | ara | nso | rs | con | ou | s | ue | ass | ess | me | r | r- | en | s | fat | ig | lev | l | las | i | f | ic | ion | . | at |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ue | e | c | s | T | h | is | h | l | ho | d | i | fy | dr | iv | ing |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| t | to | nt | res | ear | c | p | rop | ose | s | a | no | ve | me | q | ua | ise | l | ing | l | f | ion | No | Ha | β- | t | rem | ov | a | wa | ve | cor | rec | us | ; | 28 | H | ig | h | ly | Re | l | ia | b | le | Dr | iv | ing | Wo | k | loa | d | An | ly | is | k | loa | d | ing | EE | G | by | iso | lat | ing | ine | i | bra | ion | ise | d | t |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| r | a | s | wo | r | us | en | g | v | no | an | ist | ica | l | ly | is | f | d | lcu | lat | β | sta | t | to | an | a | s | o | α | an | wa | ve | s | ca | e | 1 | 0 | 4] | Us | ing | Dr | ive | E | lec | ha | log | ( | EE | G | ) | ly | ing | d | It | dem | ig | i | f | ic | f | in | d | ing | [ | β | tro | str | ate | ant |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| r | en | cep | ram | an | a | an | wa | ve | s. | on | s | s | n | s | z | α | EE | G | iv | ity | ire | d | ly | dr | iv | ing | act | t-te | sts | to | ; | p | a | an | a | ze | Ac | iv | it | ies | ing | iv | ing | d | ing | inc | d | k | loa | d | du | ing | le | ft-t | dr | iv | ing | Du | Dr | t |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| r | reg | ar | rea | se | wo | r | r | urn | k | loa | d | d | i | f | fe | d | t | ty | wo | r | acr | oss | ren | roa | p | es | d | ig | ht | dr | iv | ing | to | str |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| com | p | are | a | . | Im | d | let | hre | ho | l | d | for | EM | G | den | is | ing | T | h | is | h | bu | ho | d | for | EM | G | ig | l |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| t | st | t | p | rov | e | wa | ve | s | s | o | ; | res | ear | c | p | rop | ose | s | a | ro | me | s | s | na | Re | it | ion | f | Mu | le | Fa | ig | Sta | Ba | d | fea | ion | ( | RM | S, | IEM | G, | MF | MP | F, | B | S | E | ); | den | is | ing | d | fat | ig | las | i | f | ic | ion | int | ing | let | t | tus | tur | ext | t | at | rat |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| co | g | n | o | sc | ue | se | e | rac | o | an | ue | c | s | eg | wa | ve | , | , | [ | 9 | 0 | ] | d | let | hre | ho | l | d | d | C | S | las | i | f | ic | ion | ing | C | S | S | S | O- | S | hre | ho | l | d | ing | it | h | C | S | for | im | d | for | Im | Wa | T | N | N- | V | M | N | N- | V | M, | V | M, | P | V | M, | N | N- | V | M | at | t |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| on | p | rov | e | ve | s | an | c | s | us | s | p | rov | e | p | er | ma | nc | e | w | d | C | in | i | den | i | fy | ing | le | fat | ig | N | N. | t | sta | tes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| an | mu | sc | ue | . | ig | h-r | lut | ion | im | fre | ly | is | ing | H |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| t | eso | e- | q | ue | ncy | an | a | s | us | S-t | for | B- | d | istr | i | bu | ion | ( | BD | ), | d | t |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ran | s | m, | an | Su | fac | lec | hy | d | le | h | is | h | ha | ize | he | b | i | l | ity | f | h | ig | h-r | lut | ion | E | -B | Mu | T | tro | t | r | e | my | og | rap | ase | sc | res | ear | c | em | p | s | s | cap | a | o | eso | Ex | de | d | Mo | d | i | f | ie | d | B- | D | istr | i | bu | ion | ( | EM | BD | ); | ten | t |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ig | ion | ing | ig | h-R | lut | ion | im | fre | ho | ds, | icu | lar | ly | in | det | ing | Fa | De | Us | H | EM | BD | t | tec | t | t | t | art | ect | ue | eso | e- | q | ue | ncy | me | p | , | 5 | fea | lec | ion | ia | Ge | ic | A | lg | it | hm | ( | G | A | ) | d | [ | 9 | ] | tur | t | t | e | se | ne | or | an | v | T | im | Fre | Me | ho | ds | d | dy | ic | le | fat | ig | it | h | h | ig | h | f | fe | ing | bu | t | st | e- | q | ue | ncy | an | na | m | mu | sc | ue | w | acc | ura | cy, | o | r | ro |
| ina | ic | le | Sw | Op | im | iza | ion | ( | S | O | ); | B | Pa | BP | rt | t | t | ry | arm | Ma | h | ine | Le | ing | A | lg | it | hm | l | ica | ion | for | ics | d | ha | b | i | l | ita | ion | t | ort | t | c | arn | or | s | ap | p | s | sp | s, | erg | on | om | an | re | las | i | f | ic | ion | ing | do | d | , | . | S | V | M, | Ra | Fo | at | t, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| c | s | us | n | m | res | an | Ro | ion | Fo | tat | t |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| res | Pre | ing | ing | Bu | h | f | i | lte | ( | 0. | 1– | 3 | 0 | Hz | ); |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| tte | ort | p | roc | ess | us | rw | r | T | h | is | h | dem | he | f | f | ic | f | E | O | G | ig | ls | str | ate | t | res | ear | c | on | s | e | acy | o | s | na | An | lec | -O | log | ( | O | G | ) | Se | 's | fea | ion | ( | 1 | 6 | fea | ist | ica | l, | h | ig | he | der | E | E | tro | tur | ext | t | tur | sta | t |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| cu | ram | nso | r | e | rac | es: | r-o | r | in | det | ing | dr | ive | hy | ig | i | lan | lt | ip | le | ect | r | p | ov | ce | acr | oss | mu | b | i | l | ity | ive | ig | i | lan | ist | ics | l | ine | ); | fea | lec | ion | ia | [ | 1 | 2 | 4] | A | De | Dr | Hy | to | tec | t | sta | t | tur | t |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| r | p | ov | ce | no | n- | ar | e | se | v | , | be | hav | ior | l | it | h | En | b | le | las | i | f | ie | f | fe | ing | sta | tes | a | w | sem | c | s | rs | o | r | , | Us | ing | Ma | h | ine | Le | ing | AN | O | V | A | d | P | C | A; | las | i | f | ie | d | inc | lu | de |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| c | arn | an | c | s | rs | use | he | be | for | for | lt | ic | las | det | ion | t | st | ect | p | er | ma | nc | e | mu | s | . | S | V | M, | KN | N, | d | En | b | le | ho | ds | t |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| an | sem | me |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

| Re | fer | Pa | To | ic | Pr | d | M | ho | d | Ov | l | l | Pe | for | et | en | ce | p | er | p | op | ose | era | r | ma | nc | e | O | G | ig | l | is | it | ion | ing | hre | lec | de | E |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t | tro | s | na | acq | us | e | e | s; | u | T | h | is | h | int | du | b | le | b | in | ing | ste | res | ear | c | ro | ces | a | we | ara | sy | m | com | ig | ito | ing | d | Aw | ke | ing | Sy | he | d | det | ion | ia | Fa | Mo | t | ste | ost | ect |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ue | n | r | an | a | n | m | a | p | ure | v | g | y | ros | cop | e | sen | sor | ; | E | O | G | d | he | d | ly | is | for | fat | ig | det | ion | ent | ect | an | a | mo | vem | an | a | s | ue | d | lec | ica | l | d | d | fat | ig | lev | l | las | i | f | ic | ion | ing | [ | 1 | 2 | 3 | ] | Ba | Ey | E | He | Mo | tr | ent | at |
| se | on | e | an | a | vem | ue | e | c | s | us | d | int | ion | l | i | dat | d | hro | h | lee | dep | iva | ion | ent | t | t | an | erv | va | e | ug | s | p | r | , | Pa | Mo | ito | ing | BP | Ne | l | Ne | k; | ke | int | ion | ete | tw | ent |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ram | rs | n | r | ura | or | wa | -up | erv | im | d | du | l-ta | k | for | ent | tes | ts. | exp | er | s | an | a | s | p | er | ma | nc | e | ia | ic | d | hy | ica | l | im | lat | ion | st |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| v | mu | s | an | p | s | u | ing | ise | f | i | lte | ing | d | ion | Pre | No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ext | t | p | roc | ess | : | r | an | rac | f | Sp | l | ity | ( | S | ) | d | Po | De | P | D | ect |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| o | we | r | ra | ns | an | D | i | f | fe | ia | l | En | ( | DE | ) | fea | fro | T | h | is | h | l-t | im | fat | ig | det | ion | t | tro | tur | ent | ect |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ren | p | y | es | m | res | ear | c | p | res | s | a | rea | e | ue | A | l | ig | iv | ing | Sta | it | ion | No | Fa | Dr | Re | t | te | ve | ue | co | g | n | EE | G | ig | ls, | d | In | dep | den | Co | An | ly | is | d | ing | b | in | ing | EE | G | d | E | O | G | ig | ls, | t | ent | ste |  |  |  |  |  |  |  |  |  |
| s | na | an | en | mp | on | a | s | an | wa | rn | sy | m | com | an | s | na | d | ing | ho | d | d | G | d | O | G | [ | 2 | 8 | ] | Wa | Me | Ba | EE | E | t | an | rn | se | on | an | ( | I | C | A | ) | fro | E | O | G | ig | ls. | l | i | dat | d | in | im | lat | d | dr | iv | ing | d | it | ion | d | lev | ing |  |  |
| m | s | na | va | e | s | u | e | con | s | an | era | g | S | ig | ls | na | C | las | i | f | ic | ion | hn | log | for | ler | d | iss | ina | ion | Io | T | at | tec | t | t |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| s | : | o | a | em | y | . | Su | h | ine | ( | S | ) | Fa | Ve | Ma | F | V | M | st | ort | cto |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| p | p | r | c | it | h | fea | lev | l | fus | ion | tur | w | e- | e |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| . | Fe | ion | fro | E | C | G | d | EM | G | ing |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| atu | ext | t | re | rac | m | an | s | us | im | do | in, | fre | -do | in, | d | dv | d | T | h | is | h | dem | he | ia | l | f | b | in | ing | t | str | ate | t | ote | nt |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| e- | ma | q | ue | ncy | ma | an | a | anc | e | res | ear | c | on | s | p | o | com | Re | h | Ex | ise | Fa | ig | Es | im | ion | t | t | at | sea | rc | on | erc | ue | de | it | ion | hn | iq | C | las | i | f | ic | ion | ing | C | G | d | G | dat | for | fat | ig | det | ion | in | E | EM | tec | at | te | ect |  |  |  |  |  |  |  |
| com | p | os | ue | an | a | acc | ura | ue | s. | s | us | s | 3 | 6 | Me | ho | d | in | P | i | lat | Re | ha | b | i | l | ita | ion | Ba | d | [ | ] | t | t | es | se | on | d | ic | le | im | iza | ion | ha | b | i | l | ita | ion | ing | he | for | fer | d | f | fe | ive | Im | Pa | Sw | Op | rt | t | t | t | t | ct |  |  |  |
| p | rov | e | arm | re | p | av | wa | y | sa | an | mo | re | e | , | E | C | G | d | EM | G | Fe | Fu | ion | atu | an | s | re | s | Su | Ve | Ma | h | ine | ( | IP | S | O- | S | V | M | ) | h | ine | int | fac | ort | cto | p | p | r | c | ma | n-m | ac | er | es. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| det | hre | Re | lax | d, | Tra | it | ion | d | T | ire | d. | to | ect | t | sta | tes | e | : | e | ns | an | , |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

#### *7.2. Ergonomics and Portability*

When it comes to wearable devices, ergonomics and comfort are of utmost significance, particularly if they are to be worn for When it comes to wearable devices, ergonomics and comfort are of utmost significance, particularly if they are to be worn for extended periods. The ideal degree of comfort would prevent the user from ever noticing that they have anything extra attached to their body. Industrial design may achieve such a high degree of ergonomics and comfort by experimenting with various forms and shapes until they are just right and then improving the design depending on user input. To prevent issues like irritation or allergies, the device's materials should be carefully selected [144].

Most healthcare wearables are either single-use or have replaceable batteries that cannot be recharged. For this reason, mobility and size are being compromised by the battery's strict overall form-factor requirements. The battery capacity of wearable devices is usually limited. Therefore, making effective use of available battery life is crucial for the devices to function for a fair period [144].

#### *7.3. Unobtrusiveness*

When it comes to fatigue monitoring, there are a variety of scenarios in which prolonged monitoring of a user (for either immediate evaluation or a more in-depth ongoing watch) is both essential and beneficial. Additionally, it is preferable, particularly for long-term fatigue monitoring, that the selected equipment has a minimum effect on the user [145]. To be considered unobtrusive, a wearable gadget must not interfere with the user's normal activities. This may be accomplished via minimalism in size and style or by disguising the item as commonplace [145]. The bulkiness of the equipment being worn is also a key issue. Users seldom welcome large, bulky, and cumbersome-to-use wearables. The development of chip-scale integrated circuit packaging is notoriously difficult and is often reserved for large corporations or production runs.

Unobtrusive wearable devices like wristbands, phones, and glasses have been the focus of much recent research in wireless physiological sensing and monitoring. Recently, advanced smart apparel (fabric/textile as a sensor) has also received attention as one of the best unobtrusive data collection [146] [147].

#### *7.4. Continuous Monitoring*

The remote monitoring platform should exist and provide individualized monitoring plans for each kind of wearable to guarantee obtaining sufficient data while keeping linked to a person, which is necessary for effective fatigue management and monitoring. Patients will be under constant and active supervision with a smart ecosystem that connects the Wearables and the might of Artificial Intelligence. In the event of any unexpected or developing fatigue, this might even save their lives [148].

#### *7.5. Data Quality*

Patient-reported exhaustion outcome metrics have become more popular in fatigue monitoring, reflecting the complex interdependence of many variables. Considering the importance

of accurately measuring and monitoring fatigue, data acquired by patient-reported fatigue data must be of high quality. The subjective character of the data on fatigue raises concerns about the reliability of the results because of the many confounding variables that might affect patients' replies. This might happen during the making and using of the instrument, or it could result from the patient's reaction patterns. Such considerations are crucial for producing reliable fatigue monitoring results based on data that accurately represents patients' assessments [149].

Data accuracy is essential for monitoring and analysing fatigue levels. False information cannot assist in diagnosing weariness and developing a remedy for it since it does not provide a realistic picture. Data inaccuracies may be traced back to several causes, such as missing data, corrupted measurements owing to noise or data Inconsistency and significant drops for mobile users when using wearable devices.

#### 8. Research Gaps and Future Opportunities

The use of AI and wearables to track fatigue has a lot of unexplored potentials. Despite progress in these areas, numerous obstacles must be overcome before viable fatigue monitoring systems can be developed, validated, and deployed. The absence of standardized ways for assessing fatigue, the limited accuracy of existing wearables, and the need for more robust and adaptive AI algorithms are all mentioned in this section as examples of research gaps. The use of wearables and AI to monitor fatigue raises ethical and privacy problems that must also be addressed.

#### *8.1. Predictive Accuracy*

The intricacy of the fatigue concept necessitates that the research community comprehend how the offered AI algorithms could enhance fatigue monitoring. Most AI methods have a long way to go before they can reliably generalise, much alone be clinically applicable, for most forms of fatigue monitoring data [150]. There is concern that blind spots in artificial intelligence would reinforce biases already present in the performance of the current methods, leading to inaccurate predictions about fatigue monitoring. Although there are presently few instances of fatigue monitoring, In the research domain, AI approaches for fatigue monitoring are being proposed with positive results but still, A lot of effort has to go into creating a framework for reliable fatigue monitoring in the clinical domain [150].

Testing an AI system using sufficiently substantial datasets obtained from institutions other than those that contributed the data for model training is an integral part of external validation and is necessary for the accurate evaluation of real-world clinical performance linked to fatigue monitoring.

Methods, such as independent test sets, need to be developed to allow for direct comparisons of AI systems. It is crucial for those working on AI algorithms to keep an eye out for the danger posed by a lack of fatigue datasets [150].

#### *8.2. Multimodal Information Fusion*

In the context of fatigue monitoring, multimodal information fusion is a method of combining data from multiple sources to accurately detect and monitor fatigue. This can include physiological data such as heart rate and eye movement, as well as behavioural data and reaction time. Multimodal information fusion allows for more robust and reliable detection of fatigue than using a single modality alone. The AI algorithms can also continuously learn and adapt to changes in the data, making the system more accurate over time. The usage of this technology can potentially improve fatigue monitoring [151].

Wearables are being used to gather many modalities for fatigue monitoring since a single modality may not be enough for capturing the whole scope of fatigue. For that, we need to apply more research into the model's interpretability, exploration of the correlation distribution between features and classification outcomes, break the black box barrier, and demonstrate the model's decision-making mechanism's rationality in the task of muscle fatigue detection as well as algorithm optimisation [152]. For that, we need to deepen our fatigue detection framework by fusing environmental and psychophysiological signals with optical data for a comprehensive assessment of the overall fatigue detection framework design.

#### *8.3. Explainable AI for Fatigue Measurements*

Explainable AI (XAI) has become one of the most important topics in the field of AI and its applications in the real world. For instance, AI algorithms applied for medical diagnosis and prediction must be fully explicable and generated by transparent AI models (rather than black boxes) [152]. The simplest AI model cannot properly explain the logic of how they process data/features and reach a decision. The nonconvexity problem of AI algorithms further justifies the requirement for explainability. AI models developed for fatigue measurement and monitoring must be able to simply yet accurately describe how they make detection and prediction. It is especially required if those AIempowered devices for fatigue monitoring will be approved by relevant authorities in different countries. For instance, there are a set of guidelines issued by the US Federal Trade Commission related to the explainability of AI systems [152]. To the best of our knowledge, the current literature related to using AI for fatigue monitoring fully ignores this path. Explainability for fatigue monitoring could be partially addressed using recently developed tools such as SHAP could be used for this purpose [153].

To improve the explainability and readability of AI/ML models, researchers have developed a technique called SHAP values (Shapley Additive exPlanations) [154] that is based on cooperative game theory. SHAP displays the relevance or contribution of each feature to the model's prediction, but it does not assess the accuracy of the forecast. Authors in [155] used SHAP and gradient boosting methods for predictive fatigue monitoring in drivers (Figure 16 and Figure 17). The importance of a feature in a model refers to how much it contributes to the model's output or prediction. The more important a feature is, the more impact it has on the model's output. The model's performance can be improved by focusing on the most important features and giving them more weight in the model. Conversely, features with little or no impact on the model's output can be removed or given less weight. It's also important to note that feature importance can

change as the dataset changes, so it's important to monitor and adapt the feature selection process constantly.

![](_page_30_Figure_6.jpeg)

Figure 16: SHAP values describing the contribution and importance.

#### *8.4. Uncertainty Quantification and Trust*

Fatigue definition and measurement are intrinsically fuzzy and uncertain. Experts from different fields can't agree on how AI algorithms and signals from wearables can be used to define and measure fatigue in a precise way. All AI techniques applied in literature for fatigue estimation fully ignore issues related to predictive uncertainties associated with AI models. There are two types of uncertainty associated with predictions generated by AI models for fatigue monitoring. These are aleatoric and epistemic uncertainties [156]. Aleatoric uncertainty is irreducible and caused by noise in recordings or sample mislabelling. The lack of data in different regions of input space causes epistemic (knowledge) uncertainty. It is of practical importance to quantify these uncertainties and flag uncertain outcomes/decisions/predictions generated by AI models for fatigue monitoring. Ignoring uncertainties could lead to misleading results, as AI models could easily make wrong decisions when confronted with unknown or noisy samples [157].

There are also important questions about how AI models can be trusted, how fair they are, and how reliable they are. These issues are the focus of AI deployment for mission-critical applications including autonomous vehicles, cyber-security, and healthcare [158] [159]. These issues are also required to be theoretically and practically considered when designing fatigue monitoring systems.

![](_page_31_Figure_0.jpeg)

Figure 17: SHAP Waterfall Plot showing the contribution of features to the model's prediction.

#### *8.5. Edge Computing*

Processing multimodal datasets at scale on edge using limited computing resources. In the context of future research, answers to how can one distinguish mental exhaustion from physical exhaustion, what factors could lead to exhaustion, and what implications learning fatigue has on mental performance are essential to be explored. A comprehensive review of edge computing technologies for wearables can be found in [160].

Research gaps related to fatigue monitoring include information perception, sensing, storage, and computing. The study presented a detailed methodology for detecting driver hypovigilance using ECG data analysis. ECG signals were meticulously recorded and pre-processed to remove noise and artifacts, ensuring accurate HRV analysis—a key factor in monitoring driver states[7][13]. Twenty distinct features were extracted from the ECG data, including time-domain linear features like mean and median heart rates and frequency-domain nonlinear features such as Approximate Entropy[24][25]. The relevance of each feature was statistically evaluated using one-way ANOVA, and feature reduction was performed using PCA[26][27]. The processed features were then classified using advanced machine learning techniques: SVM, KNN, and Ensemble methods[28][29].

The results indicated high accuracy rates for the two-class detection model, which distinguished between normal and hypovigilant states, including drowsiness and visual or cognitive inattention, faring better than the five-class detection approach[30]. The success of the two-class model, particularly with the Ensemble classifier that achieved accuracies of up to 100%, underscores the effectiveness of the selected features and the potential of the proposed methodology in practical, real-world applications[31].

These findings highlight the viability of ECG data in the development of robust driver monitoring systems and suggest further enhancement of the classification algorithms for improved detection of hypovigilance states[32].

The study's constraints were noted, particularly the artificial simulation of fatigue through problem-solving tasks and the need for broader research to encompass diverse populations and physical activity levels [161]. Nonetheless, the findings support the viability of wearable ECG devices in monitoring mental fatigue effectively, emphasizing the promise of such technology in mobile health (m-health) applications [162]. The research concluded that a select number of HRV indicators could be sufficient for effective mental fatigue prediction, indicating the

potential for employing low-cost wearable devices for efficient data processing and fatigue state detection in real-time [163].

The study on wrist-worn wearable sensors for detecting driver drowsiness [86] utilized a detailed methodology within a highfidelity driving simulator to gather physiological data crucial for assessing drowsiness. A key focus of the methodology was the extraction and analysis of HRV from data collected via wrist-worn devices, using sophisticated algorithms designed to isolate relevant HRV metrics indicative of drowsiness [164]. This included time-domain measures such as mean heart rate and standard deviations of RR intervals, along with frequencydomain measures like low and high-frequency components of the HRV spectrum, which reflect autonomic nervous system activity [165].

![](_page_31_Figure_10.jpeg)

1

Figure 18: Existing research efforts on edge computing for wearable technologies.

The efficacy of several machine learning classifiers—Support Vector Machines (SVM), Random Forests, and Decision Trees—was rigorously evaluated in both user-dependent and user-independent frameworks. These classifiers underwent thorough testing for accuracy in predicting drowsiness states based on the extracted features, with training using crossvalidation techniques to ensure robustness and prevent overfitting [166][167].

The results revealed that the wearable sensors achieved high accuracy rates, showcasing their potential as viable alternatives to more traditional, invasive methods such as electrocardiography (ECG) [141][143]. This high level of precision underscores the capability of wearable technologies in the real-time monitoring and detection of driver drowsiness, highlighting significant advancements in driver safety and automated monitoring systems [168]. The operational viability of such wearable devices in practical applications not only confirms their effectiveness but also paves the way for their integration into automotive safety systems to enhance road safety by effectively monitoring driver states [169].

This paper [170] introduces a proposed model for fatigue detection using multimodal data—ECG and video signals. The model stands out for its integration of various feature extraction techniques and the application of machine learning to precisely classify fatigue states. During the ECG processing phase, the

study extracts both traditional handcrafted features and advanced deep learning (DL) features from ECG signals [81][171]. The handcrafted features encompass time, frequency, and nonlinear domain metrics, providing a comprehensive view of the physiological indicators of fatigue [86][172]. The advanced DL features are derived from a cascaded network that includes a convolutional neural network (CNN) and a bidirectional long short-term memory (BiLSTM) with an attention mechanism [173], which together enhance the temporal analysis of ECG data. For video processing, the research utilizes a hybrid attention cascade network to extract facial expression features [174], incorporating spatial features with ResNet-50 and applying hybrid attention and a gated recurrent unit (GRU) for temporal feature extraction. The model's classifier module employs an XGBoost classifier that synergizes the features from both ECG and video data [175]. After a detailed feature fusion and selection process, the classifier proficiently categorizes the subject's state into alert, normal, or tired. Validated on the DROZY public dataset and a self-collected dataset, the model demonstrates substantial superiority over existing methods, achieving 99.6% accuracy on the DROZY dataset [175] and 91.8% accuracy on the self-collected dataset [176], underpinning its potential for reliable application in real-world scenarios (see Figure 18).

#### *8.6. Lessons Learned and Novel Insights*

This article offers valuable insights into the current technological advancements and methodologies employed for fatigue monitoring, emphasizing the incorporation of wearable technologies and AI. One of the significant insights gained is the efficacy of integrating various physiological signals, including ECG, EEG, EMG, and PPG, with machine learning and deep learning frameworks. Integrating multi-modal data fusion significantly improves the precision of fatigue detection systems by providing a more holistic perspective on mental and physical fatigue. This combination has demonstrated significant utility in high-demand environments, including aviation and manufacturing, where real-time monitoring is essential for ensuring safety and optimizing performance. The findings indicate that this trend will likely persist as advancements in AI and wearable technology progress, facilitating the development of increasingly sophisticated and precise fatigue detection systems.

Another important discovery is the potential for unobtrusive and real-time fatigue monitoring made possible by wearable technology, such as smartwatches, fitness trackers, and specialized sensors. Research highlights the significance of ongoing observation conducted in a non-intrusive way, enabling fatigue evaluation while preserving the user's workflow and daily routines. The transition towards seamlessly incorporating monitoring technologies into daily life presents novel opportunities for proactive fatigue management across various sectors, including sports, healthcare, and transportation. Nonetheless, a significant challenge persists regarding the variability in the quality and availability of real-time data. This situation necessitates the development of more standardized protocols and dependable sensing technologies to achieve consistent and actionable outcomes.

Even though the results of current methods are promising, there is still a lot of room for improvement in making AI models that can be explained and that give more accurate and understandable information about fatigue detection. Furthermore, the progression of edge computing is essential for facilitating realtime data processing on wearable devices, thereby minimizing reliance on cloud-based systems and enhancing response times. Addressing these gaps is essential to developing advanced fatigue monitoring solutions that exhibit accuracy and real-time capabilities while being portable, scalable, and tailored to meet individual requirements.
