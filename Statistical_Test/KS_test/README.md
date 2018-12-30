
# What is Kolmogorov–Smirnov test ?

`Kolmogorov–Smirnov test` (`K–S test` or `KS test`) is a **nonparametric** test of the equality of continuous, one-dimensional probability distributions that can be used to compare a sample with a **reference probability distribution** (**one-sample** K–S test), or to compare two samples (**two-sample** K–S test) [[Wiki]][Kolmogorov–Smirnov test].

The Kolmogorov–Smirnov statistic quantifies a **distance** between the **empirical distribution function of the sample** and the cumulative distribution function of the reference distribution, or between the empirical distribution functions of two samples.  The null hypothesis is the sample drawn from the reference distribution (in the one-sample case), or from the same distribution (in the two-sample case). 

The two-sample K–S test is sensitive to differences in both location and shape of the empirical cumulative distribution functions of the two samples. In Wiki page, they defined the empirical distribution function (for n iid ordered observations `Xi`) as [[Wiki]][Kolmogorov–Smirnov test]

<a href="https://www.codecogs.com/eqnedit.php?latex=F_(x)&space;=&space;\frac{1}{n}\sum^n_{i=1}&space;\textrm{I}_{[-\infty,&space;x]}(X_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F_(x)&space;=&space;\frac{1}{n}\sum^n_{i=1}&space;\textrm{I}_{[-\infty,&space;x]}(X_i)" title="F_(x) = \frac{1}{n}\sum^n_{i=1} \textrm{I}_{[-\infty, x]}(X_i)" /></a>

where `I(Xi)` is an indication function, equal to 1 if Xi ≤ x and equal to 0 otherwise.


[[S. Massa]][Kolmogorov Smirnov Test & Power of Tests] provides very good explanation about the application of KS test.


# One-sample KS test

If the series is consistently increasing over time, the sample mean and variance will grow with the size of the sample, and they will always underestimate the mean and variance in future periods. 

In addition to this, stationary processes avoid the problem of **spurious regression**. 


# Two-Sample KS test

Most business and economic time series are far from stationary when expressed in their original units of measurement, and even after deflation or seasonal adjustment they will typically still exhibit trends, cycles, random-walking, and other non-stationary behavior.



### ARIMA(p,d,q)

By Sunny Mewati [[Quora, 1]][What's the difference between ARMA, ARIMA, and ARIMAX, in layman's terms?], Box and Jenkins claimed (successfully) [[Box, Jenkins, Reinsel]][Time Series Analysis] that nonstationary data can be made stationary by differencing the series. This series, <a href="http://www.codecogs.com/eqnedit.php?latex=Y^*" target="_blank"><img src="http://latex.codecogs.com/gif.latex?Y^*" title="Y^*" /></a> is the input in Box-Jenkins analysis. The general model for <a href="http://www.codecogs.com/eqnedit.php?latex=Y^*" target="_blank"><img src="http://latex.codecogs.com/gif.latex?Y^*" title="Y^*" /></a> is written as







# Reference


[Kolmogorov Smirnov Test & Power of Tests]: http://www.stats.ox.ac.uk/~massa/Lecture%2013.pdf
[[S. Massa] Kolmogorov Smirnov Test & Power of Tests](http://www.stats.ox.ac.uk/~massa/Lecture%2013.pdf)




[Kolmogorov–Smirnov test]: https://en.wikipedia.org/wiki/Kolmogorov–Smirnov_test
[[Wiki] Kolmogorov–Smirnov test](https://en.wikipedia.org/wiki/Kolmogorov–Smirnov_test)

