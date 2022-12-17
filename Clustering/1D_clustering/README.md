
# 1D Clustering

* [1. Introduction](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Clustering/DBSCAN#1-introduction)
* [2. Hyperparameters in DBSCAN](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Clustering/DBSCAN#2-hyperparameters-in-dbscan)
     * [2.1 Choosing Epsilon](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Clustering/DBSCAN#21-choosing-epsilon)
     * [2.2 Choosing MinPt](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Clustering/DBSCAN#22-choosing-minpt)
* [3. Validation of Brutal Searching Epsilon in DBSCAN](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Clustering/DBSCAN#3-validation-of-brutal-searching-epsilon-in-dbscan)
* [4. Disadvanatge in DBSCAN](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Clustering/DBSCAN#4-disadvanatge-in-dbscan)



## 1. Kernel Density Estimate


How to use KDE for 1D clustering? see [[Stackoverflow]][How would one use Kernel Density Estimation as a 1D clustering method in scikit learn?]


Some easy rules of thumb for bandwidth [[Andrey Akinshin]][The importance of kernel density estimation bandwidth]:
* Scott’s rule of thumb: $h \sim 1.06 \sigma n^{-1/5}$
* Silverman’s rule of thumb: $h = 0.9 \min(\sigma, \frac{IQR}{1.35})n^{-1/5}$, where $IQR = (Q_3 - Q_1)/2$ [Interquartile Range](https://byjus.com/maths/interquartile-range/). Using ``` scipy.stats.iqr```


Optimization approach [[Niranjan Pramanik]][Kernel Density Estimation]:
* Maximum likelihood cross- validation (MLCV)

The Improved Sheather-Jones algorithm [[KDEpy]][KDEpy Bandwidth], [[Eduardo García-Portugués]][A Short Course on Nonparametric Curve Estimation: Bandwidth selection]

others: [[Andrey Akinshin]][The importance of kernel density estimation bandwidth], [[Crossvalidated]][Methods to Find the Best Bandwidth for Kernel Density Estimation]


### Hyperparameters in KDE

Two important hyperparameters in DBSCAN:
1. Kernel
2. bandwidth

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

GMM example [[AstroML]][1D Gaussian Mixture Example]

In the GMM model, the prior distribution on the vector $\bf{\mu}$ and $\Sigma$ of estimates given data $\bf{X}$ is 

$$ p(\bf{X}) = \sum^K_{n=1} w_n \mathcal{N}(\bf{X}|\bf{\mu}_n, \Sigma_n), $$

where index $n$ goes over distribution component, $K$ is the number of components, and $\mathcal{N}(X|\bf{\mu}_n, \Sigma_n)$ is the $n$-th component multivariate **Guassian** distribution with means $\bf{\mu_n}$ and covariance matrices $\Sigma_n$, which reads as

$$\mathcal{N}(\bf{X}|\bf{\mu}_n, \Sigma_n) = \frac{1}{ (2\pi)^{\frac{n}{2}} |\Sigma|^{\frac{1}{2}}}\exp \left( -\frac{1}{2} (\bf{X}- \bf{\mu}_n)^T \Sigma_n^{-1}(\bf{X}- \bf{\mu}_n) \right).$$


#### Reference

* [1D Gaussian Mixture Example]: https://www.astroml.org/book_figures/chapter4/fig_GMM_1D.html
[[AstroML] 1D Gaussian Mixture Example](https://www.astroml.org/book_figures/chapter4/fig_GMM_1D.html)


## 3. Meanshift
