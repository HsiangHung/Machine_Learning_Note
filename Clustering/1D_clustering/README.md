
# 1D Clustering

* [1. Kernel Density Estimate (KDE)](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Clustering/1D_clustering#1-kernel-density-estimate)
* [2. Gaussina Mixture Model (GMM)](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Clustering/1D_clustering#2-gaussina-mixture-model-gmm)
* [3. Validation of Brutal Searching Epsilon in DBSCAN](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Clustering/DBSCAN#3-validation-of-brutal-searching-epsilon-in-dbscan)




## 1. Kernel Density Estimate (KDE)


How to use KDE for 1D clustering? Mainly refer the stackoverflow post: [Stackoverflow: How would one use Kernel Density Estimation as a 1D clustering method in scikit learn?](https://stackoverflow.com/questions/35094454/how-would-one-use-kernel-density-estimation-as-a-1d-clustering-method-in-scikit).

First fit the 1D density using KDE:
```Python
from sklearn.neighbors.kde import KernelDensity
a = array([10,11,9,23,21,11,45,20,11,12]).reshape(-1, 1)
kde = KernelDensity(kernel='gaussian', bandwidth=3).fit(a)
```
Then prepare profile based on the data range to identfiy local minima and maxima:
```Python
from scipy.signal import argrelextrema
s = linspace(np.min(a), np.max(a))
e = kde.score_samples(s.reshape(-1,1))
mi, ma = argrelextrema(e, np.less)[0], argrelextrema(e, np.greater)[0]
```
`mi` returns `[17.34693878, 33.67346939]`. 

Then we can simply clustering the data as 
1. `a[a < mi[0]]` (a < 17.347)
2. `a[(a >= mi[0]) * (a <= mi[1])]` (17.347 < a < 33.673)
3. `a[a >= mi[1]]` (a > 33.673)

### Hyperparameters in KDE

Two important hyperparameters in KDE:
1. Kernel
2. bandwidth

The 1D clustering using KDE is sensitive to bandwidth selection.

There are some easy rules of thumb for determining bandwidth [[Andrey Akinshin]][The importance of kernel density estimation bandwidth]:
* Scott’s rule of thumb: $h \sim 1.06 \sigma n^{-1/5}$
* Silverman’s rule of thumb: $h = 0.9 \min(\sigma, \frac{IQR}{1.35})n^{-1/5}$, where $IQR = (Q_3 - Q_1)/2$ [Interquartile Range](https://byjus.com/maths/interquartile-range/). Using ``` scipy.stats.iqr```


Optimization approach [[Niranjan Pramanik]][Kernel Density Estimation]:
* Maximum likelihood cross- validation (MLCV)

The Improved Sheather-Jones algorithm [[KDEpy]][KDEpy Bandwidth], [[Eduardo García-Portugués]][A Short Course on Nonparametric Curve Estimation: Bandwidth selection]

others: [[Andrey Akinshin]][The importance of kernel density estimation bandwidth], [[Crossvalidated]][Methods to Find the Best Bandwidth for Kernel Density Estimation]


#### Reference

* [The importance of kernel density estimation bandwidth]: https://aakinshin.net/posts/kde-bw/
[[Andrey Akinshin] The importance of kernel density estimation bandwidth](https://aakinshin.net/posts/kde-bw/)

* [Kernel Density Estimation]: https://medium.com/analytics-vidhya/kernel-density-estimation-kernel-construction-and-bandwidth-optimization-using-maximum-b1dfce127073
[[Niranjan Pramanik] Kernel Density Estimation](https://medium.com/analytics-vidhya/kernel-density-estimation-kernel-construction-and-bandwidth-optimization-using-maximum-b1dfce127073)


* [KDEpy Bandwidth]: https://kdepy.readthedocs.io/en/latest/bandwidth.html
[[KDEpy] KDEpy Bandwidth](https://kdepy.readthedocs.io/en/latest/bandwidth.html)

* [A Short Course on Nonparametric Curve Estimation: Bandwidth selection]: https://bookdown.org/egarpor/NP-EAFIT/dens-bwd.html
[[Eduardo García-Portugués] A Short Course on Nonparametric Curve Estimation: Bandwidth selection](https://bookdown.org/egarpor/NP-EAFIT/dens-bwd.html)

* [Methods to Find the Best Bandwidth for Kernel Density Estimation]: https://stats.stackexchange.com/questions/229743/methods-to-find-the-best-bandwidth-for-kernel-density-estimation
[[Crossvalidated] Methods to Find the Best Bandwidth for Kernel Density Estimation](https://stats.stackexchange.com/questions/229743/methods-to-find-the-best-bandwidth-for-kernel-density-estimation)


* [How would one use Kernel Density Estimation as a 1D clustering method in scikit learn?]: https://stackoverflow.com/questions/35094454/how-would-one-use-kernel-density-estimation-as-a-1d-clustering-method-in-scikit
[[Stackoverflow] How would one use Kernel Density Estimation as a 1D clustering method in scikit learn?](https://stackoverflow.com/questions/35094454/how-would-one-use-kernel-density-estimation-as-a-1d-clustering-method-in-scikit)

## 2. Gaussina Mixture Model (GMM)

The example to use GMM to perform 1D clustering is described in: [[AstroML]][1D Gaussian Mixture Example]

In the GMM model, the prior distribution on the vector $\bf{\mu}$ and $\Sigma$ of estimates given data $\bf{X}$ is 

$$ p(\bf{X}) = \sum^K_{n=1} \omega_n \mathcal{N}(\bf{X}|\bf{\mu}_n, \Sigma_n), $$

where index $n$ goes over distribution component, $K$ is the number of components, and $\mathcal{N}(X|\bf{\mu}_n, \Sigma_n)$ is the $n$-th component multivariate **Guassian** distribution $\mathcal{N}_n$ with means $\bf{\mu_n}$ and covariance matrices $\Sigma_n$, which reads as

$$ \mathcal{N}_n = \mathcal{N}(\bf{X}|\bf{\mu}_n, \Sigma_n) = \frac{1}{ (2\pi)^{\frac{n}{2}} |\Sigma|^{\frac{1}{2}}}\exp \left( -\frac{1}{2} (\bf{X}- \bf{\mu}_n)^T \Sigma_n^{-1}(\bf{X}- \bf{\mu}_n) \right).$$

Given a predetermining parameter, $K$, the number of Gaussian distributions, we perform iterative processes, called Expectation–maximization (EM) algorithm. 

At first we initialize the weights $\omega_n = 1/K$ and split points which define the range of Gaussian distrubutions, e.g. x < $s^0$ for $\mathcal{N}_0$, $s^0 \ge$ x < $s^1 $ for $\mathcal{N}_1$ ... etc. Then from data, we can determine means $\mu_n$ and covariance matrices $\Sigma_n = \mathcal{N}(\bf{X}|\bf{\mu}_n, \Sigma_n)$ as well as  $\mathcal{N}_n$ for each component $n$.

Next step is to compute new weight as 

$$ \omega_n^{\textrm{new}} = \frac{1}{N} \sum^N_{n=1} \frac{\mathcal{N}(\bf{X}|\bf{\mu}_n, \Sigma_n)}{\sum^K \mathcal{N}(\bf{X}|\bf{\mu}_n, \Sigma_n)}, $$

and the new means and covariance matrices 

$$ \mu^{\textrm{new}}_n = \sum^N_{i=1} p(\bf{X}_i) \bf{X}_i = $$

Here is a introductionary youtube: [Unsupervised Learning: Gaussian Mixture Model (1D GMM)](https://www.youtube.com/watch?v=fVsmnZqrBUs).


#### Reference

* [1D Gaussian Mixture Example]: https://www.astroml.org/book_figures/chapter4/fig_GMM_1D.html
[[AstroML] 1D Gaussian Mixture Example](https://www.astroml.org/book_figures/chapter4/fig_GMM_1D.html)


## 3. Meanshift

**Mean shift** is an unsupervised learning algorithm that is mostly used for clustering. It is widely used in real-world data analysis (e.g., image segmentation)because it’s **non-parametric** and doesn’t require any predefined shape of the clusters in the feature space.

Simply speaking, “mean shift” is equal to “shifting to the mean” in an iterative way.
