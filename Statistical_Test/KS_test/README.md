
# What is Kolmogorov–Smirnov test ?

`Kolmogorov–Smirnov test` (`K–S test` or `KS test`) is a **nonparametric** test of the equality of continuous, one-dimensional probability distributions that can be used to compare a sample with a **reference probability distribution** (**one-sample** K–S test), or to compare two samples (**two-sample** K–S test) [[Wiki]][Kolmogorov–Smirnov test].

The Kolmogorov–Smirnov statistic quantifies a **distance** between the **empirical distribution function of the sample** and the cumulative distribution function of the reference distribution, or between the empirical distribution functions of two samples.  The null hypothesis is the sample drawn from the reference distribution (in the one-sample case), or from the same distribution (in the two-sample case). The two-sample K–S test is sensitive to differences in both location and shape of the empirical cumulative distribution functions of the two samples. 

In the Wiki page, they defined the **empirical distribution function** (for n iid ordered observations `Xi`) as [[Wiki]][Kolmogorov–Smirnov test]

<a href="https://www.codecogs.com/eqnedit.php?latex=F_n(x)&space;=&space;\frac{1}{n}\sum^n_{i=1}&space;\textrm{I}_{[-\infty,&space;x]}(X_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F_n(x)&space;=&space;\frac{1}{n}\sum^n_{i=1}&space;\textrm{I}_{[-\infty,&space;x]}(X_i)" title="F_n(x) = \frac{1}{n}\sum^n_{i=1} \textrm{I}_{[-\infty, x]}(X_i)" /></a>


where `I(Xi)` is called the indicator function, equal to 1 if Xi ≤ x and equal to 0 otherwise. More simply speaking, given sample `{x1, . . . , xn}`, the empirical distribution function is the proportion of the data that lies below x [[S. Massa]][Kolmogorov Smirnov Test & Power of Tests], 

<a href="https://www.codecogs.com/eqnedit.php?latex=F_n(x)&space;=&space;\frac{\textrm{number&space;of&space;observations&space;below&space;}x}{\textrm{number&space;of&space;observations}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F_n(x)&space;=&space;\frac{\textrm{number&space;of&space;observations&space;below&space;}x}{\textrm{number&space;of&space;observations}}" title="F_n(x) = \frac{\textrm{number of observations below }x}{\textrm{number of observations}}" /></a>

If we order the sample observations  `x1 ≤ x2 ≤ ··· ≤ xn`, then 

<a href="https://www.codecogs.com/eqnedit.php?latex=F_n(X_i)&space;=&space;\frac{i}{n}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F_n(X_i)&space;=&space;\frac{i}{n}" title="F_n(X_i) = \frac{i}{n}" /></a>



Massa provides very good explanation about the application of KS test in her lecture [[S. Massa]][Kolmogorov Smirnov Test & Power of Tests].



# Kolmogorov distribution

# One-sample KS test


The `Kolmogorov–Smirnov statistic` for a given **cumulative distribution function** `F(x)` is

<a href="https://www.codecogs.com/eqnedit.php?latex=D_n&space;=&space;\textrm{sup}_x&space;\left&space;|&space;F_n(x)&space;-F(x)&space;\right&space;|" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D_n&space;=&space;\textrm{sup}_x&space;\left&space;|&space;F_n(x)&space;-F(x)&space;\right&space;|" title="D_n = \textrm{sup}_x \left | F_n(x) -F(x) \right |" /></a>

The null hypothesis is 

<a href="https://www.codecogs.com/eqnedit.php?latex=H_0&space;:&space;\textrm{the&space;samples&space;come&space;from&space;}&space;F_n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_0&space;:&space;\textrm{the&space;samples&space;come&space;from&space;}&space;F_n" title="H_0 : \textrm{the samples come from } F_n" /></a>


against the alternative hypothesis 

<a href="https://www.codecogs.com/eqnedit.php?latex=H_a&space;:&space;\textrm{the&space;samples&space;do&space;NOT&space;come&space;from&space;}&space;F_n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_a&space;:&space;\textrm{the&space;samples&space;do&space;NOT&space;come&space;from&space;}&space;F_n" title="H_a : \textrm{the samples do NOT come from } F_n" /></a>



# Two-sample KS test

Suppose now we have two samples, `F1` and `F2` are the empirical distribution functions of the first and the second sample respectively (subscripts`n` and `m` denote the sample size)

<a href="https://www.codecogs.com/eqnedit.php?latex=D_{n,m}&space;=&space;\textrm{sup}_x&space;\left&space;|&space;F_{1,n}(x)&space;-F_{2,m}(x)&space;\right&space;|" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D_{n,m}&space;=&space;\textrm{sup}_x&space;\left&space;|&space;F_{1,n}(x)&space;-F_{2,m}(x)&space;\right&space;|" title="D_{n,m} = \textrm{sup}_x \left | F_{1,n}(x) -F_{2,m}(x) \right |" /></a>



### ARIMA(p,d,q)

By Sunny Mewati [[Quora, 1]][What's the difference between ARMA, ARIMA, and ARIMAX, in layman's terms?], Box and Jenkins claimed (successfully) [[Box, Jenkins, Reinsel]][Time Series Analysis] that nonstationary data can be made stationary by differencing the series. This series, <a href="http://www.codecogs.com/eqnedit.php?latex=Y^*" target="_blank"><img src="http://latex.codecogs.com/gif.latex?Y^*" title="Y^*" /></a> is the input in Box-Jenkins analysis. The general model for <a href="http://www.codecogs.com/eqnedit.php?latex=Y^*" target="_blank"><img src="http://latex.codecogs.com/gif.latex?Y^*" title="Y^*" /></a> is written as







# Reference


[Kolmogorov Smirnov Test & Power of Tests]: http://www.stats.ox.ac.uk/~massa/Lecture%2013.pdf
[[S. Massa] Kolmogorov Smirnov Test & Power of Tests](http://www.stats.ox.ac.uk/~massa/Lecture%2013.pdf)




[Kolmogorov–Smirnov test]: https://en.wikipedia.org/wiki/Kolmogorov–Smirnov_test
[[Wiki] Kolmogorov–Smirnov test](https://en.wikipedia.org/wiki/Kolmogorov–Smirnov_test)

