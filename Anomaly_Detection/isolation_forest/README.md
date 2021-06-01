# Isolation Forest

This session is dedicated to deep understanding on isolation forest model. “Fewer and different” data points are the main idea; outliers ar more isolated than others; in other words, outliers takes less path for them to be isolated.


Table of Contents:


* [3. Metrics](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Anomaly_Detection#3-metrics)
* [4. Data Preprocess](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Anomaly_Detection#4-data-preprocess)
     * [4.1 Undersample: Down-sample Majority Class](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Anomaly_Detection#41-undersample-down-sample-majority-class) 
     * [4.2 Oversample: Up-sample Minority Class](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Anomaly_Detection#42-oversample-up-sample-minority-class)
     * [4.3 Synthesize Minor Samples](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Anomaly_Detection#43-synthesize-minor-samples)




## Isolation Forest From Scratch

The following Python follows the blog: [[Carlos Mougan]][Isolation Forest from Scratch] and [[Isolation Forest Step by Step]][Isolation Forest Step by Step].

## Isolation tree and forest

This session explains how to build an isolation forest step by step [[Isolation Forest Step by Step]][Isolation Forest Step by Step]

1. **Step 1** — Subsampling data for training

2. **Step 2** — Making binary decision tree: Suppose we have two attributes (i.e. Q1 or Q2) as shown below, random choice of an attribute and random choice of a Q1 or Q2 value between its min and max (i.e. Q1’)

3. **Step 3** — Repeat step 2 Iteratively until each data is isolated as a leaf or specified maximum depth is reached.

So far the step 1-3 can be summarized below

![](images/isolation_tree.png)

4. **Step 4** — Feeding data set and calculating anomaly score, which defines as 

<a href="https://www.codecogs.com/eqnedit.php?latex=S(d)&space;=&space;e^{-\frac{E(h)}{c(n)}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?S(d)&space;=&space;e^{-\frac{E(h)}{c(n)}}" title="S(d) = e^{-\frac{E(h)}{c(n)}}" /></a>

Given a data point, we have an anomaly score for each tree and get the final anomaly score for an entire forest by the mean value across different trees. 


5. **Step 5** - Compute anomaly score: We calculate this anomaly score for each tree and average them out across different trees and get the final anomaly score for an entire forest for a given data point

### Example

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
iForest = isolation_forest(X, n_trees=3, max_depth=100)
```
After training, we can print out the trees:
```
{'feat1 <= 2.2181214836809806': [{'feat1 <= 1.7389572375053777': [{'feat1 <= 0.18538491015441844': [{'feat2 <= 0.39944974852534676': [-0.04571121291250773, 0.4311043323198237]}, -0.3728472765820943]}, 2.8733315826978525]}, 3.5]}

{'feat2 <= 1.587423467387756': [{'feat2 <= 0.31144846892514394': [{'feat2 <= -0.12499170741512142': [-0.3728472765820943, -0.04571121291250773]}, 0.4311043323198237]}, {'feat1 <= 3.248530739825105': [2.8733315826978525, 3.5]}]}

{'feat2 <= 0.1706085041001812': [{'feat1 <= 0.21151501086291638': [-0.04571121291250773, -0.3728472765820943]}, {'feat1 <= 0.3953008359360611': [0.4311043323198237, {'feat1 <= 2.438234497822728': [2.8733315826978525, 3.5]}]}]}
```
The trees are illustrated below:
```
                  tree-1   |                    tree-2               |                 tree-3
                   ABCDE   |                    ABCDE                |                 ABCDE
feat1 < 2.22      /    \   | feat2 < 1.59      /   \                 | feat2 < 0.17   /    \
                 BCDE   A  |                  BCD   AE               |               CD    ABE
feat1 < 1.74     /   \     | feat2 < 0.31    / \    / \ feat1 > 3.25 | feat1 < 0.21  /\    / \  feat1 > 0.39           
                BCD   E    |                CD  B  E   A             |              D  C  B  AE
feat1 < 0.19   / \         | feat2 < -0.13  / \                      | feat1 < 2.44          /\
              BD  C        |               D   C                     |                      E  A
feat2 < 0.4  / \           |                                         |
            D   B          |                                         |
```


### Compute path length 

An outlier is more isolated, and have shorter path length. The path length for data `A` on each tree is [1,2,3], meaning avg path length = 2. On the other hand, path lengths `B`: [4,2,2], `C`: [3,3,2], `D`: [4,3,2], `E`: [2,2,3] are all larger than 2, which indicate normal data points.





   





## Reference


[Isolation Forest from Scratch]: https://towardsdatascience.com/isolation-forest-from-scratch-e7e5978e6f4c
[[Carlos Mougan] Isolation Forest from Scratch](https://towardsdatascience.com/isolation-forest-from-scratch-e7e5978e6f4c)


[Outlier Detection with Extended Isolation Forest]: https://towardsdatascience.com/outlier-detection-with-extended-isolation-forest-1e248a3fe97b
[[Eryk Lewinson] Outlier Detection with Extended Isolation Forest](https://towardsdatascience.com/outlier-detection-with-extended-isolation-forest-1e248a3fe97b)


[Isolation Forest Step by Step]: https://hyunsukim-9320.medium.com/isolation-forest-step-by-step-341b82923168
[[Hyunsu Kim] Isolation Forest Step by Step](https://hyunsukim-9320.medium.com/isolation-forest-step-by-step-341b82923168)


[Anomaly Detection Using Isolation Forest Algorithm]: https://medium.com/analytics-vidhya/anomaly-detection-using-isolation-forest-algorithm-8cf36c38d6f7
[[Saurabh Singh] Anomaly Detection Using Isolation Forest Algorithm](https://medium.com/analytics-vidhya/anomaly-detection-using-isolation-forest-algorithm-8cf36c38d6f7)

