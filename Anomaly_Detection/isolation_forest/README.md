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

We show how the isolation forest works step by step using the above code. Suppose we have five 2D data instances like

| | feat1 | feat2|
|:-:|:-:| :-:|
|A|  3.300000 | 3.500000 |
|B| -0.397208 | 0.431104 |
|C|  0.749262 |-0.372847 |
|D|  0.167278 |-0.045711 |
|E|  1.752083 | 2.873332 |

Obviously `A` is the outlier and others are normal.

Next we train 3 isolation trees in the forest:
```Python 
iForest = isolation_forest(X[:5], n_trees=3, max_depth=100)
```
We will have three trees:
```
                    tree-1 

                     ABCDE
feat1 < 2.218       /    \
                   BCDE   A
feat1 < 1.739     /   \
                BCD    E
feat1 < 0.185   / \
               BD  C
feat2 < 0.399 / \
             D  B
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

