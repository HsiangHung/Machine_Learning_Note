
# Unsupervised Clustering 

DBSCAN, K-means, Deep Embedded Clustering (DEC) [[Yuefeng Zhang]][Deep Clustering for Financial Market Segmentation].


## Metric

### Silhouette Score

The silhouette value is a measure of how similar an object is to its own cluster (cohesion) compared to other clusters (separation). The silhouette ranges from −1 to +1, where a **high** value indicates that the object is **well matched to its own cluster and poorly matched to neighboring clusters**. If most objects have a high value, then the clustering configuration is appropriate. If many points have a low or negative value, then the clustering configuration may have too many or too few clusters [[wiki]][Silhouette (clustering)].

Assume we cluster data into k clusters, for any `i` in the cluster `C_i`, we can define the mean distance `a(i)` between `i` and all other data points `j` in the same cluster, where `d(i,j)` is the distance between `i` and `j`.

<a href="https://www.codecogs.com/eqnedit.php?latex=a(i)&space;=&space;\frac{1}{|C_i|-1}&space;\sum_{j\in&space;C_{i},i\neq&space;j}d(i,j)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a(i)&space;=&space;\frac{1}{|C_i|-1}&space;\sum_{j\in&space;C_{i},i\neq&space;j}d(i,j)" title="a(i) = \frac{1}{|C_i|-1} \sum_{j\in C_{i},i\neq j}d(i,j)" /></a>

`a(i)` can be interpreted as **similarity**; the smaller value, the better the clustering.

Next we can define **dissimilarity** by considering the mean distance from `i` to all points in other clusters where `i` is not in:

<a href="https://www.codecogs.com/eqnedit.php?latex={\displaystyle&space;b(i)=\min&space;_{k\neq&space;i}{\frac&space;{1}{|C_{k}|}}\sum&space;_{j\in&space;C_{k}}d(i,j)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\displaystyle&space;b(i)=\min&space;_{k\neq&space;i}{\frac&space;{1}{|C_{k}|}}\sum&space;_{j\in&space;C_{k}}d(i,j)}" title="{\displaystyle b(i)=\min _{k\neq i}{\frac {1}{|C_{k}|}}\sum _{j\in C_{k}}d(i,j)}" /></a>

Note here we have `min`, meaning the cluster with this smallest mean dissimilarity is said to be the "neighboring cluster" of `C_i`.

We now define a silhouette (value) of one data point `i`

<a href="https://www.codecogs.com/eqnedit.php?latex=s(i)={\frac&space;{b(i)-a(i)}{\max\{a(i),b(i)\}}},&space;\textrm{if&space;}&space;|C_{i}|>1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s(i)={\frac&space;{b(i)-a(i)}{\max\{a(i),b(i)\}}},&space;\textrm{if&space;}&space;|C_{i}|>1" title="s(i)={\frac {b(i)-a(i)}{\max\{a(i),b(i)\}}}, \textrm{if } |C_{i}|>1" /></a>

Which can be also written as s(i) = (1) 1-a(i)/b(i) if a(i) < b(i), (2) s(i) = 0 if a(i) = b(i), (3) s(i) = b(i)/a(i)-1 if a(i) > b(i). From the above definition it is clear that -1 \le s(i) \le 1.



![inter_class_variance](images/inter_class_variance.png)






## Reference





[Deep Clustering for Financial Market Segmentation]: https://towardsdatascience.com/deep-clustering-for-financial-market-segmentation-2a41573618cf
[[Yuefeng Zhang] Deep Clustering for Financial Market Segmentation](https://towardsdatascience.com/deep-clustering-for-financial-market-segmentation-2a41573618cf)




[Silhouette (clustering)]: https://en.wikipedia.org/wiki/Silhouette_(clustering)
[[wiki] Silhouette (clustering)](https://en.wikipedia.org/wiki/Silhouette_(clustering))


