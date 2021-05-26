# Isolation Forest

This session is dedicated to deep understanding on isolation forest model.

Table of Contents:


* [3. Metrics](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Anomaly_Detection#3-metrics)
* [4. Data Preprocess](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Anomaly_Detection#4-data-preprocess)
     * [4.1 Undersample: Down-sample Majority Class](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Anomaly_Detection#41-undersample-down-sample-majority-class) 
     * [4.2 Oversample: Up-sample Minority Class](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Anomaly_Detection#42-oversample-up-sample-minority-class)
     * [4.3 Synthesize Minor Samples](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Anomaly_Detection#43-synthesize-minor-samples)




## Isolation Forest From Scratch

The following Python follows the blog: [[Carlos Mougan]][Isolation Forest from Scratch].

We used the above code to build an isolation forest. Suppose the five input data instances are

| | feat1 | feat2|
|:-:|:-:| :-:|
|0|  3.300000 | 3.500000 |
|1| -0.522788 | 0.269247 |
|2| -0.016005 |-0.028487 |
|3|  0.056282 |-0.458942 |
|4| -0.828018 |-1.886786 |

and we put 3 trees in the forest:
```
iForest = isolation_forest(X[:5], n_trees=3, max_depth=100)
```

**SMOTE** creates new instances of the minority class by forming convex combinations of neighboring instances. [[Devin Soni]][Dealing with Imbalanced Classes in Machine Learning] As the graphic below shows (credit: (a) from [[Devin Soni]][Dealing with Imbalanced Classes in Machine Learning] and (b,c) from [[Jason Brownlee]][SMOTE for Imbalanced Classification with Python]), it effectively draws lines between minority points in the feature space, explained in (a), and samples along these lines. This allows us to balance our data-set without as much overfitting, as we create new synthetic examples rather than using duplicates. 

![SMOTE_example](images/SMOTE_example.png)




### 5.1 Inference: Z score and Modified Z score
The z-score or standard score of an observation is a metric that indicates how many standard deviations a data point is from the sample’s mean, assuming a gaussian distribution [[Sergio Santoyo]][A Brief Overview of Outlier Detection Techniques]. The z-score of any data point can be calculated as
    
<a href="https://www.codecogs.com/eqnedit.php?latex=z&space;=&space;\frac{x-\bar{x}}{\sigma}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z&space;=&space;\frac{x-\bar{x}}{\sigma}" title="z = \frac{x-\bar{x}}{\sigma}" /></a>

The modified Z score `M` is defined as [[NIST/SEMATECH e-Handbook of Statistical Methods]][Detection of Outliers]

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{M}&space;=&space;\frac{0.6745(x-\widetilde{x})}{\textrm{MAD}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{M}&space;=&space;\frac{0.6745(x-\widetilde{x})}{\textrm{MAD}}" title="\textrm{M} = \frac{0.6745(x-\widetilde{x})}{\textrm{MAD}}" /></a>
     





## Reference


[Isolation Forest from Scratch]: https://towardsdatascience.com/isolation-forest-from-scratch-e7e5978e6f4c
[[Carlos Mougan] Isolation Forest from Scratch](https://towardsdatascience.com/isolation-forest-from-scratch-e7e5978e6f4c)

