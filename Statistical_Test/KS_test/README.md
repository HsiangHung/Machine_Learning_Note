
# What is Kolmogorov–Smirnov test ?

`Kolmogorov–Smirnov test` (`K–S test` or `KS test`) is a **nonparametric** test of the equality of continuous, one-dimensional probability distributions that can be used to compare a sample with a **reference probability distribution** (**one-sample** K–S test), or to compare two samples (**two-sample** K–S test) [[Wiki]][Kolmogorov–Smirnov test].

The Kolmogorov–Smirnov statistic quantifies a **distance** between the **empirical distribution function of the sample** and the cumulative distribution function of the reference distribution, or between the empirical distribution functions of two samples.  The null hypothesis is the sample drawn from the reference distribution (in the one-sample case), or from the same distribution (in the two-sample case). 

The two-sample K–S test is sensitive to differences in both location and shape of the empirical cumulative distribution functions of the two samples. In Wiki page, they defined the empirical distribution function (for n iid ordered observations `Xi`) as [[Wiki]][Kolmogorov–Smirnov test]

<a href="https://www.codecogs.com/eqnedit.php?latex=F_n(x)&space;=&space;\frac{1}{n}\sum^n_{i=1}&space;\textrm{I}_{[-\infty,&space;x]}(X_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F_n(x)&space;=&space;\frac{1}{n}\sum^n_{i=1}&space;\textrm{I}_{[-\infty,&space;x]}(X_i)" title="F_n(x) = \frac{1}{n}\sum^n_{i=1} \textrm{I}_{[-\infty, x]}(X_i)" /></a>


where `I(Xi)` is an indication function, equal to 1 if Xi ≤ x and equal to 0 otherwise.



[[S. Massa]][Kolmogorov Smirnov Test & Power of Tests] provides very good explanation about the application of KS test.


# One-sample KS test


The `Kolmogorov–Smirnov statistic` for a given cumulative distribution function `F(x)` is

<a href="https://www.codecogs.com/eqnedit.php?latex=D_n&space;=&space;\textrm{sup}_x&space;\left&space;|&space;F_n(x)&space;-F(x)&space;\right&space;|" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D_n&space;=&space;\textrm{sup}_x&space;\left&space;|&space;F_n(x)&space;-F(x)&space;\right&space;|" title="D_n = \textrm{sup}_x \left | F_n(x) -F(x) \right |" /></a>




# Two-sample KS test

Suppose now we have two samples, F
F_{1,n} and 
F
2
,
m
{\displaystyle F_{2,m}} are the empirical distribution functions of the first and the second sample respectively, and 

<a href="https://www.codecogs.com/eqnedit.php?latex=D_{n,m}&space;=&space;\textrm{sup}_x&space;\left&space;|&space;F_{1,n}(x)&space;-F_{2,m}(x)&space;\right&space;|" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D_{n,m}&space;=&space;\textrm{sup}_x&space;\left&space;|&space;F_{1,n}(x)&space;-F_{2,m}(x)&space;\right&space;|" title="D_{n,m} = \textrm{sup}_x \left | F_{1,n}(x) -F_{2,m}(x) \right |" /></a>



### ARIMA(p,d,q)

By Sunny Mewati [[Quora, 1]][What's the difference between ARMA, ARIMA, and ARIMAX, in layman's terms?], Box and Jenkins claimed (successfully) [[Box, Jenkins, Reinsel]][Time Series Analysis] that nonstationary data can be made stationary by differencing the series. This series, <a href="http://www.codecogs.com/eqnedit.php?latex=Y^*" target="_blank"><img src="http://latex.codecogs.com/gif.latex?Y^*" title="Y^*" /></a> is the input in Box-Jenkins analysis. The general model for <a href="http://www.codecogs.com/eqnedit.php?latex=Y^*" target="_blank"><img src="http://latex.codecogs.com/gif.latex?Y^*" title="Y^*" /></a> is written as







# Reference


[Kolmogorov Smirnov Test & Power of Tests]: http://www.stats.ox.ac.uk/~massa/Lecture%2013.pdf
[[S. Massa] Kolmogorov Smirnov Test & Power of Tests](http://www.stats.ox.ac.uk/~massa/Lecture%2013.pdf)




[Kolmogorov–Smirnov test]: https://en.wikipedia.org/wiki/Kolmogorov–Smirnov_test
[[Wiki] Kolmogorov–Smirnov test](https://en.wikipedia.org/wiki/Kolmogorov–Smirnov_test)

