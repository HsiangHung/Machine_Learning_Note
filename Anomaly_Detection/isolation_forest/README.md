# Isolation Forest


Table of Contents:


* [3. Metrics](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Anomaly_Detection#3-metrics)
* [4. Data Preprocess](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Anomaly_Detection#4-data-preprocess)
     * [4.1 Undersample: Down-sample Majority Class](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Anomaly_Detection#41-undersample-down-sample-majority-class) 
     * [4.2 Oversample: Up-sample Minority Class](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Anomaly_Detection#42-oversample-up-sample-minority-class)
     * [4.3 Synthesize Minor Samples](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Anomaly_Detection#43-synthesize-minor-samples)





**Kappa (or Cohen’s kappa)**: Classification accuracy normalized by the imbalance of the classes in the data [[Numal Jayawardena]][How to Deal with Imbalanced Data].


**SMOTE** creates new instances of the minority class by forming convex combinations of neighboring instances. [[Devin Soni]][Dealing with Imbalanced Classes in Machine Learning] As the graphic below shows (credit: (a) from [[Devin Soni]][Dealing with Imbalanced Classes in Machine Learning] and (b,c) from [[Jason Brownlee]][SMOTE for Imbalanced Classification with Python]), it effectively draws lines between minority points in the feature space, explained in (a), and samples along these lines. This allows us to balance our data-set without as much overfitting, as we create new synthetic examples rather than using duplicates. 

![SMOTE_example](images/SMOTE_example.png)




### 5.1 Inference: Z score and Modified Z score
The z-score or standard score of an observation is a metric that indicates how many standard deviations a data point is from the sample’s mean, assuming a gaussian distribution [[Sergio Santoyo]][A Brief Overview of Outlier Detection Techniques]. The z-score of any data point can be calculated as
    
<a href="https://www.codecogs.com/eqnedit.php?latex=z&space;=&space;\frac{x-\bar{x}}{\sigma}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z&space;=&space;\frac{x-\bar{x}}{\sigma}" title="z = \frac{x-\bar{x}}{\sigma}" /></a>

The modified Z score `M` is defined as [[NIST/SEMATECH e-Handbook of Statistical Methods]][Detection of Outliers]

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{M}&space;=&space;\frac{0.6745(x-\widetilde{x})}{\textrm{MAD}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{M}&space;=&space;\frac{0.6745(x-\widetilde{x})}{\textrm{MAD}}" title="\textrm{M} = \frac{0.6745(x-\widetilde{x})}{\textrm{MAD}}" /></a>
     





## Reference


[5 SMOTE Techniques for Oversampling your Imbalance Data]: https://towardsdatascience.com/5-smote-techniques-for-oversampling-your-imbalance-data-b8155bdbe2b5
[[Cornellius Yudha Wijaya] 5 SMOTE Techniques for Oversampling your Imbalance Data](https://towardsdatascience.com/5-smote-techniques-for-oversampling-your-imbalance-data-b8155bdbe2b5)


[Dealing with Imbalanced Classes in Machine Learning]: https://towardsdatascience.com/dealing-with-imbalanced-classes-in-machine-learning-d43d6fa19d2
[[Devin Soni] Dealing with Imbalanced Classes in Machine Learning](https://towardsdatascience.com/dealing-with-imbalanced-classes-in-machine-learning-d43d6fa19d2)


[Dealing with Imbalanced Data]: https://medium.com/digital-catapult/dealing-with-imbalanced-data-8b21e6deb6cd
[[Digital Catapult] Dealing with Imbalanced Data](https://medium.com/digital-catapult/dealing-with-imbalanced-data-8b21e6deb6cd)


[How to Handle Imbalanced Classes in Machine Learning]: https://elitedatascience.com/imbalanced-classes
[[Elite Data Science] How to Handle Imbalanced Classes in Machine Learning](https://elitedatascience.com/imbalanced-classes)


[Outlier Detection with Isolation Forest]: https://towardsdatascience.com/outlier-detection-with-isolation-forest-3d190448d45e
[[Eryk Lewinson] Outlier Detection with Isolation Forest](https://towardsdatascience.com/outlier-detection-with-isolation-forest-3d190448d45e)


[SMOTE for Imbalanced Classification with Python]: https://machinelearningmastery.com/smote-oversampling-for-imbalanced-classification/
[[Jason Brownlee] SMOTE for Imbalanced Classification with Python](https://machinelearningmastery.com/smote-oversampling-for-imbalanced-classification/)


[Differences between Receiver Operating Characteristic AUC (ROC AUC) and Precision Recall AUC (PR AUC)]: http://www.chioka.in/differences-between-roc-auc-and-pr-auc/
[[log0] Differences between Receiver Operating Characteristic AUC (ROC AUC) and Precision Recall AUC (PR AUC)](http://www.chioka.in/differences-between-roc-auc-and-pr-auc/)


[DEALING WITH IMBALANCED DATA: UNDERSAMPLING, OVERSAMPLING AND PROPER CROSS-VALIDATION]: https://www.marcoaltini.com/blog/dealing-with-imbalanced-data-undersampling-oversampling-and-proper-cross-validation
[[Marco Altini] DEALING WITH IMBALANCED DATA: UNDERSAMPLING, OVERSAMPLING AND PROPER CROSS-VALIDATION](https://www.marcoaltini.com/blog/dealing-with-imbalanced-data-undersampling-oversampling-and-proper-cross-validation)


[Detection of Outliers]: https://www.itl.nist.gov/div898/handbook/eda/section3/eda35h.htm
[[NIST/SEMATECH e-Handbook of Statistical Methods] Detection of Outliers](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35h.htm)


[How to Deal with Imbalanced Data]: https://towardsdatascience.com/how-to-deal-with-imbalanced-data-34ab7db9b100
[[Numal Jayawardena] How to Deal with Imbalanced Data](https://towardsdatascience.com/how-to-deal-with-imbalanced-data-34ab7db9b100)



[What is the difference between a ROC curve and a precision-recall curve?]: https://www.quora.com/What-is-the-difference-between-a-ROC-curve-and-a-precision-recall-curve-When-should-I-use-each
[[Quora: What is the difference between a ROC curve and a precision-recall curve?] What is the difference between a ROC curve and a precision-recall curve?](https://www.quora.com/What-is-the-difference-between-a-ROC-curve-and-a-precision-recall-curve-When-should-I-use-each)


[A Brief Overview of Outlier Detection Techniques]: https://towardsdatascience.com/a-brief-overview-of-outlier-detection-techniques-1e0b2c19e561
[[Sergio Santoyo] A Brief Overview of Outlier Detection Techniques](https://towardsdatascience.com/a-brief-overview-of-outlier-detection-techniques-1e0b2c19e561)


[Learning from Imbalanced Classe]: https://www.svds.com/learning-imbalanced-classes/
[[Silicon Valley Data Science] Learning from Imbalanced Classe](https://www.svds.com/learning-imbalanced-classes/)


[Introduction to Anomaly Detection: Concepts and Techniques]: https://iwringer.wordpress.com/2015/11/17/anomaly-detection-concepts-and-techniques/
[[Srinath Perera] Introduction to Anomaly Detection: Concepts and Techniques](https://iwringer.wordpress.com/2015/11/17/anomaly-detection-concepts-and-techniques/)


[Fraud Detection Under Extreme Class Imbalance]: https://towardsdatascience.com/fraud-detection-under-extreme-class-imbalance-c241854e60c
[[Syed Sadat Nazrul] Fraud Detection Under Extreme Class Imbalance](https://towardsdatascience.com/fraud-detection-under-extreme-class-imbalance-c241854e60c)








