
# Classification 




## Metric

### Precision and Recall

In most cases, there are no perfect classifiers. A good common question is which metric should we use for model selection, precision or recall? Classifier to have high True Positive Rate (TPR) or False Positive Rate (FPR)? It depends on domain and our business goal.

Call the definition:

```
           Truth
 _______ | Pos | Neg |
Pred Pos | TP  | FP  |
Pred Neg | FN  | TN  |
```
The relevant metrics are 
```
precision = TP/(TP+FP), recall = TP/(TP+FN)
```
and
```
TPR = recall, FPR = FP/(FP+TN)
```
Each probability threshold in classifier determiones a set of the above metrics. Also we can define review rate 
```
review rate = N(prob > threshold)/N
```
where `N` is the number of data points.

Here is the post to list some examples whrn precision is important and when recall is important ? [[StackExchange]][When is precision more important over recall?]. Depends on whhcih we want to minimize, FP or FN? Here I just summarize my understanding and list in the following:

1. For rare cancer data modeling, a false negative is usually more disastrous than a false positive for preliminary diagnoses. We want to minimize FN to have higher recall. So **Recall** is a better measure than precision.




<a href="https://www.codecogs.com/eqnedit.php?latex=a(i)&space;=&space;\frac{1}{|C_i|-1}&space;\sum_{j\in&space;C_{i},i\neq&space;j}d(i,j)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a(i)&space;=&space;\frac{1}{|C_i|-1}&space;\sum_{j\in&space;C_{i},i\neq&space;j}d(i,j)" title="a(i) = \frac{1}{|C_i|-1} \sum_{j\in C_{i},i\neq j}d(i,j)" /></a>

`a(i)` can be interpreted as **similarity**; the smaller value, the better the clustering.

Next we can define **dissimilarity** by considering the mean distance from `i` to all points in other clusters where `i` is not in:

<a href="https://www.codecogs.com/eqnedit.php?latex={\displaystyle&space;b(i)=\min&space;_{k\neq&space;i}{\frac&space;{1}{|C_{k}|}}\sum&space;_{j\in&space;C_{k}}d(i,j)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\displaystyle&space;b(i)=\min&space;_{k\neq&space;i}{\frac&space;{1}{|C_{k}|}}\sum&space;_{j\in&space;C_{k}}d(i,j)}" title="{\displaystyle b(i)=\min _{k\neq i}{\frac {1}{|C_{k}|}}\sum _{j\in C_{k}}d(i,j)}" /></a>



The silhouette score can be computed using Scikit-learn. [The sklearn page](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html) shows an excellent example. From our bare eyes, the best outcome is given by 4 clusters. We can visualize silhouette score `s(i)` for each data point in different clusters:

![silhouette_n_2](images/silhouette_n2.png)
![silhouette_n_3](images/silhouette_n3.png)
![silhouette_n_4](images/silhouette_n4.png)
![silhouette_n_5](images/silhouette_n5.png)
![silhouette_n_6](images/silhouette_n6.png)

and we see the 4 clusters (execpet for 2 clusters) certainly gives the highest silhouette score from the page.
```
For n_clusters = 2 The average silhouette_score is : 0.7049787496083262 
For n_clusters = 3 The average silhouette_score is : 0.5882004012129721
For n_clusters = 4 The average silhouette_score is : 0.6505186632729437
For n_clusters = 5 The average silhouette_score is : 0.56376469026194
For n_clusters = 6 The average silhouette_score is : 0.4504666294372765
```



## Reference


[When is precision more important over recall?]: https://datascience.stackexchange.com/questions/30881/when-is-precision-more-important-over-recall
[[StackExchange] When is precision more important over recall?](https://datascience.stackexchange.com/questions/30881/when-is-precision-more-important-over-recall)



