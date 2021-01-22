
# K-means Clustering 

DBSCAN, K-means, Deep Embedded Clustering (DEC) [[Yuefeng Zhang]][Deep Clustering for Financial Market Segmentation] and [[Chengwei]][How to do Unsupervised Clustering with Keras].


## Procedures

```
Randomly initialize K cluster centorids μ1, μ2,... μK

Repeat{
    1. for i = 1, ...m, each data point, assign c(i), where x(i) is closest to the i-th centroid μc.
    2. for j = 1, ...K, each centroid μ_j is determined by average of 
}
```

## Optimization Objectives (Distortion)

The cost function in K-means is also called distortion function.

<a href="https://www.codecogs.com/eqnedit.php?latex=J(c^{(1)},\cdots&space;,&space;c^{(m)},&space;\mu_1,&space;\cdots&space;,&space;\mu_K)&space;=&space;\frac{1}{m}\sum^m_{i=1}&space;||x^{(i)}-\mu_{c^{(i)}}||^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J(c^{(1)},\cdots&space;,&space;c^{(m)},&space;\mu_1,&space;\cdots&space;,&space;\mu_K)&space;=&space;\frac{1}{m}\sum^m_{i=1}&space;||x^{(i)}-\mu_{c^{(i)}}||^2" title="J(c^{(1)},\cdots , c^{(m)}, \mu_1, \cdots , \mu_K) = \frac{1}{m}\sum^m_{i=1} ||x^{(i)}-\mu_{c^{(i)}}||^2" /></a>

## Stop Criterion

The silhouette value is a measure of how similar an object is to its own cluster (cohesion) compared to other clusters (separation). The silhouette ranges from −1 to +1, where a **high** value indicates that the object is **well matched to its own cluster and poorly matched to neighboring clusters**. If most objects have a high value, then the clustering configuration is appropriate. If many points have a low or negative value, then the clustering configuration may have too many or too few clusters [[wiki]][Silhouette (clustering)].

Assume we cluster data into k clusters, for any `i` in the cluster `C_i`, we can define the mean distance `a(i)` between `i` and all other data points `j` in the same cluster, where `d(i,j)` is the distance between `i` and `j`.

<a href="https://www.codecogs.com/eqnedit.php?latex=a(i)&space;=&space;\frac{1}{|C_i|-1}&space;\sum_{j\in&space;C_{i},i\neq&space;j}d(i,j)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a(i)&space;=&space;\frac{1}{|C_i|-1}&space;\sum_{j\in&space;C_{i},i\neq&space;j}d(i,j)" title="a(i) = \frac{1}{|C_i|-1} \sum_{j\in C_{i},i\neq j}d(i,j)" /></a>

`a(i)` can be interpreted as **similarity**; the smaller value, the better the clustering.

Next we can define **dissimilarity** by considering the mean distance from `i` to all points in other clusters where `i` is not in:

<a href="https://www.codecogs.com/eqnedit.php?latex={\displaystyle&space;b(i)=\min&space;_{k\neq&space;i}{\frac&space;{1}{|C_{k}|}}\sum&space;_{j\in&space;C_{k}}d(i,j)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\displaystyle&space;b(i)=\min&space;_{k\neq&space;i}{\frac&space;{1}{|C_{k}|}}\sum&space;_{j\in&space;C_{k}}d(i,j)}" title="{\displaystyle b(i)=\min _{k\neq i}{\frac {1}{|C_{k}|}}\sum _{j\in C_{k}}d(i,j)}" /></a>

Note here we have `min`, meaning the cluster with this smallest mean dissimilarity is said to be the "neighboring cluster" of `C_i`.

We now define a silhouette (value) of one data point `i`

<a href="https://www.codecogs.com/eqnedit.php?latex=s(i)={\frac&space;{b(i)-a(i)}{\max\{a(i),b(i)\}}},&space;\textrm{if&space;}&space;|C_{i}|>1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s(i)={\frac&space;{b(i)-a(i)}{\max\{a(i),b(i)\}}},&space;\textrm{if&space;}&space;|C_{i}|>1" title="s(i)={\frac {b(i)-a(i)}{\max\{a(i),b(i)\}}}, \textrm{if } |C_{i}|>1" /></a>

From the above definition it is clear that `s(i) = [-1, 1]`.

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


[How to do Unsupervised Clustering with Keras]: https://www.dlology.com/blog/how-to-do-unsupervised-clustering-with-keras/
[[Chengwei] How to do Unsupervised Clustering with Keras](https://www.dlology.com/blog/how-to-do-unsupervised-clustering-with-keras/)


[Deep Clustering for Financial Market Segmentation]: https://towardsdatascience.com/deep-clustering-for-financial-market-segmentation-2a41573618cf
[[Yuefeng Zhang] Deep Clustering for Financial Market Segmentation](https://towardsdatascience.com/deep-clustering-for-financial-market-segmentation-2a41573618cf)




[Silhouette (clustering)]: https://en.wikipedia.org/wiki/Silhouette_(clustering)
[[wiki] Silhouette (clustering)](https://en.wikipedia.org/wiki/Silhouette_(clustering))


