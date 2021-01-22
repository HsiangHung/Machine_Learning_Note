
# K-means Clustering 




## A. Procedures

Assume there are `m` data points

```
For each K{

    Randomly initialize K cluster centorids μ1, μ2,... μK,

    Repeat{
          a. for i = 1, ...m, each data point, assign c(i), where the centroid μc is the closest to x(i).
          b. for j = 1, ...K, each centroid μj is updated by average of data points which are labeled to c(j)
          }
}
```

### Stop Criterion

See [[Azika Amelia]][K-Means Clustering: From A to Z] and [[Pulkit Sharma]][The Most Comprehensive Guide to K-Means Clustering You’ll Ever Need]:
1. The datapoints assigned to specific cluster remain the same.
2. Centroids remain the same ([Stanford course](https://stanford.edu/~cpiech/cs221/handouts/kmeans.html) used this criterion).
3. The distance of datapoints from their centroid is minimum.
4. Fixed number of iterations have reached (insufficient iterations → poor results, choose max iteration wisely).


### Randomly Initialize Centroids

For each K, randomly initial centroids many times to avoid K-means traps in local optima (see below examples, credit from Andrew Ng's ML class), and pick clustering profile with lowest cost `J(..)`.

![local_optima](images/kmeans_localoptima.png)


## B. Optimization Objectives (Distortion)

The cost function in K-means is also called **distortion** function. The distortion function is helpful to understand if K-means converges in learning curves. 

<a href="https://www.codecogs.com/eqnedit.php?latex=J(c^{(1)},\cdots&space;,&space;c^{(m)},&space;\mu_1,&space;\cdots&space;,&space;\mu_K)&space;=&space;\frac{1}{m}\sum^m_{i=1}&space;||x^{(i)}-\mu_{c^{(i)}}||^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J(c^{(1)},\cdots&space;,&space;c^{(m)},&space;\mu_1,&space;\cdots&space;,&space;\mu_K)&space;=&space;\frac{1}{m}\sum^m_{i=1}&space;||x^{(i)}-\mu_{c^{(i)}}||^2" title="J(c^{(1)},\cdots , c^{(m)}, \mu_1, \cdots , \mu_K) = \frac{1}{m}\sum^m_{i=1} ||x^{(i)}-\mu_{c^{(i)}}||^2" /></a>

K-means is an algorithm to minimize `J(..)`:

* The above procedure a is the cluster assignment step, to minimize `J(..)` by updating c(1), c(2),.. ,c(m).
* The above procedure b is the move centroid step, to minimize `J(..)` by updating μ1, μ2,... μK.


## C. Some Notes

It’s important to preprocess your data before performing K-Means. You would have to convert your dataset into numerical values if it is not already, so that calculations can be performed. Also, applying feature reduction techniques would speed up the process, and also improve the results. These steps are important to follow because **K-Means is sensitive to outliers**, just like every other algo that uses average/mean values. Following these steps alleviate these issues.

Since clustering algorithms including kmeans use distance-based measurements to determine the similarity between data points, it’s recommended to standardize the data.

### Chooseing the value of K
Elbow method (credit from Andrew Ng's ML class)

![elbow_method](images/kmeans_elbow.png)

The right panel is hard to determine value of K. Then we can evaluate cluster quality.

Sometimes K-means is used to helpful to give business purpose, e.g. if we decide to make T-shirt in 5 sizes, the size range:

![business_purpose](images/kmeans_purpose.png)

### Evaluating the cluster quality 

see [[Azika Amelia]][K-Means Clustering: From A to Z] and [[Pulkit Sharma]][The Most Comprehensive Guide to K-Means Clustering You’ll Ever Need]

1. **Inertia**: Inertia actually calculates the sum of distances of all the points within a cluster from the centroid of that cluster. Therefore, a small of inertia is aimed for. The range of inertia’s value starts from zero and goes up.

2. **Silhouette score**: Silhouette score tells how far away the datapoints in one cluster are, from the datapoints in another cluster. The range of silhouette score is from -1 to 1. Score should be closer to 1 than -1.

### Drawbacks

Kmeans algorithm is good in capturing structure of the data if clusters have a **spherical-like shape**. It always try to construct a nice spherical shape around the centroid. That means, the minute the clusters have a complicated geometric shapes, kmeans does a poor job in clustering the data. We’ll illustrate three cases where kmeans will not perform well.


## D. K-Means++
K-Means++ is a smart centroid initialization technique and the rest of the algorithm is the same as that of K-Means [[Satyam Kumar]][Understanding K-Means, K-Means++ and, K-Medoids Clustering Algorithms]. The [coursera course, Machine Learning: Clustering & Retrieval](https://www.coursera.org/lecture/ml-clustering-and-retrieval/smart-initialization-via-k-means-T9ZaG) has better explanation about the procedures:

* Pick the first centroid point (`C1`) randomly.
* Compute distance of all points in the dataset from the centroid. The data point which has the maximum distance to `C1` will be second centroid.  Now we have `(C1, C2)`.
* Compute distances of all points from the respective nearest centroids. For example, assume we have `(x1,.., x6)` in dataset. The closest centroid to `(x1, x3, x6)` is `C1` and `x6` is the farthest point to `C1` with distance = `d(6,1)`. The closest centroid to `(x2, x4, x5)` is `C2` and `x4` is the farthest point to `C2` with `d(4,2)`. We assign `x4` as the third centroid if `d(4,2) > d(6,1)`. Now we have `(C1, C2, C3)`.
* Repeat the above step till you find K centroids.

In summary, the new centroid is determined by maximum probability proportional to distance sqaure where the distance is the distance bwtween a data point and its nearest centroid:

<a href="https://www.codecogs.com/eqnedit.php?latex=C_{n&plus;1}&space;=&space;x_i,&space;\&space;\textrm{if}&space;\&space;d_i&space;=&space;\max_{&space;C_j&space;\textrm{closest&space;to&space;}x_i&space;}&space;||x_i&space;-&space;C_j||^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C_{n&plus;1}&space;=&space;x_i,&space;\&space;\textrm{if}&space;\&space;d_i&space;=&space;\max_{&space;C_j&space;\textrm{closest&space;to&space;}x_i&space;}&space;||x_i&space;-&space;C_j||^2" title="C_{n+1} = x_i, \ \textrm{if} \ d_i = \max_{ C_j \textrm{closest to }x_i } ||x_i - C_j||^2" /></a>




## Reference


[K-Means Clustering: From A to Z]: https://towardsdatascience.com/k-means-clustering-from-a-to-z-f6242a314e9a
[[Azika Amelia] K-Means Clustering: From A to Z](https://towardsdatascience.com/k-means-clustering-from-a-to-z-f6242a314e9a)


[K-means Clustering: Algorithm, Applications, Evaluation Methods, and Drawbacks]: https://towardsdatascience.com/k-means-clustering-algorithm-applications-evaluation-methods-and-drawbacks-aa03e644b48a#:~:text=Since%20clustering%20algorithms%20including%20kmeans,units%20of%20measurements%20such%20as
[[Imad Dabbura] K-means Clustering: Algorithm, Applications, Evaluation Methods, and Drawbacks](https://towardsdatascience.com/k-means-clustering-algorithm-applications-evaluation-methods-and-drawbacks-aa03e644b48a#:~:text=Since%20clustering%20algorithms%20including%20kmeans,units%20of%20measurements%20such%20as)


[The Most Comprehensive Guide to K-Means Clustering You’ll Ever Need]: https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/
[[Pulkit Sharma] The Most Comprehensive Guide to K-Means Clustering You’ll Ever Need](https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/)


[Understanding K-Means, K-Means++ and, K-Medoids Clustering Algorithms]: https://towardsdatascience.com/understanding-k-means-k-means-and-k-medoids-clustering-algorithms-ad9c9fbf47ca
[[Satyam Kumar] Understanding K-Means, K-Means++ and, K-Medoids Clustering Algorithms](https://towardsdatascience.com/understanding-k-means-k-means-and-k-medoids-clustering-algorithms-ad9c9fbf47ca)
