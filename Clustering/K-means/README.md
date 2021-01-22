
# K-means Clustering 




## Procedures

```
For each K{

    Randomly initialize K cluster centorids μ1, μ2,... μK,

    Repeat{
          a. for i = 1, ...m, each data point, assign c(i), where the i-th centroid μc is the closest to x(i).
          b. for j = 1, ...K, each centroid μj is updated by average of data points where are labeled to c(j)
          }
}
```

## Optimization Objectives (Distortion)

The cost function in K-means is also called distortion function. The distortion function is helpful to understand if K-means converges. 

<a href="https://www.codecogs.com/eqnedit.php?latex=J(c^{(1)},\cdots&space;,&space;c^{(m)},&space;\mu_1,&space;\cdots&space;,&space;\mu_K)&space;=&space;\frac{1}{m}\sum^m_{i=1}&space;||x^{(i)}-\mu_{c^{(i)}}||^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J(c^{(1)},\cdots&space;,&space;c^{(m)},&space;\mu_1,&space;\cdots&space;,&space;\mu_K)&space;=&space;\frac{1}{m}\sum^m_{i=1}&space;||x^{(i)}-\mu_{c^{(i)}}||^2" title="J(c^{(1)},\cdots , c^{(m)}, \mu_1, \cdots , \mu_K) = \frac{1}{m}\sum^m_{i=1} ||x^{(i)}-\mu_{c^{(i)}}||^2" /></a>

The above procedure a, cluster assignment step is to minimize `J(..)` by updating c(1), c(2),.. ,c(m).

The above procedure b, move centroid step is to minimize `J(..)` by updating μ1, μ2,... μK.


## Some Points:

### Stop Criterion

See [[Azika Amelia]][K-Means Clustering: From A to Z]:
1. The datapoints assigned to specific cluster remain the same (takes too much time).
2. Centroids remain the same (time consuming).
3. The distance of datapoints from their centroid is minimum (the thresh you’ve set).
4. Fixed number of iterations have reached (insufficient iterations → poor results, choose max iteration wisely).

### Randomly Initialize Centroids

For each K, randomly initial centroids many times to avoid K-means traps in local optima (see below example). Pick clustering with lowest cost `J(..)`.

![local_optima](images/kmeans_localoptima.png)


The silhouette score can be computed using Scikit-learn. [The sklearn page](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html) shows an excellent example. From our bare eyes, the best outcome is given by 4 clusters. We can visualize silhouette score `s(i)` for each data point in different clusters:





## Reference


[K-Means Clustering: From A to Z]: https://towardsdatascience.com/k-means-clustering-from-a-to-z-f6242a314e9a
[[Azika Amelia] K-Means Clustering: From A to Z](https://towardsdatascience.com/k-means-clustering-from-a-to-z-f6242a314e9a)



