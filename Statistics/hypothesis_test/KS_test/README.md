
# Kolmogorov–Smirnov test 

For z-test and t-test, we have a strong assumption: the sample distribution is normal distribution. What about if you sample is not? 

## What is Kolmogorov–Smirnov test?

Kolmogorov–Smirnov test (`K–S test` or `KS test`) is a **nonparametric** test of the equality of continuous, one-dimensional probability distributions that can be used to compare a sample with a **reference probability distribution** (**one-sample** K–S test), or to compare two samples (**two-sample** K–S test) [[Wiki]][Wiki, Kolmogorov–Smirnov test]. The KS-test has the advantage of making no assumption about the distribution of data [[Kirkman]][Kirkman T. W., Kolmogorov-Smirnov Test]. 

The Kolmogorov–Smirnov statistic quantifies a **distance** between the **empirical distribution function of the sample** and the cumulative distribution function of the reference distribution, or between the empirical distribution functions of two samples.  The null hypothesis is the sample drawn from the reference distribution (in the one-sample case), or from the same distribution (in the two-sample case). The two-sample K–S test is sensitive to differences in both location and shape of the empirical cumulative distribution functions of the two samples. 

There defines a the **empirical distribution function** (for n iid ordered observations `Xi`) as [[Wiki]][Wiki, Kolmogorov–Smirnov test], [[MIT]][MIT course, Kolmogorov-Smirnov Test]

<a href="https://www.codecogs.com/eqnedit.php?latex=F_n(x)&space;=&space;\frac{1}{n}\sum^n_{i=1}&space;\textrm{I}_{[-\infty,&space;x]}(X_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F_n(x)&space;=&space;\frac{1}{n}\sum^n_{i=1}&space;\textrm{I}_{[-\infty,&space;x]}(X_i)" title="F_n(x) = \frac{1}{n}\sum^n_{i=1} \textrm{I}_{[-\infty, x]}(X_i)" /></a>


where `I(Xi)` is called the indicator function, equal to 1 if Xi ≤ x and equal to 0 otherwise. More simply speaking, given sample `{X1, . . . , Xn}`, the empirical distribution function is the proportion of the data that lies below x [[Massa]][S. Massa, Kolmogorov Smirnov Test & Power of Tests], 

<a href="https://www.codecogs.com/eqnedit.php?latex=F_n(x)&space;=&space;\frac{\textrm{number&space;of&space;observations&space;below&space;}x}{\textrm{number&space;of&space;observations}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F_n(x)&space;=&space;\frac{\textrm{number&space;of&space;observations&space;below&space;}x}{\textrm{number&space;of&space;observations}}" title="F_n(x) = \frac{\textrm{number of observations below }x}{\textrm{number of observations}}" /></a>

If we order the sample observations  `X1 ≤ X2 ≤ ··· ≤ Xn`, then 

<a href="https://www.codecogs.com/eqnedit.php?latex=F_n(X_i)&space;=&space;\frac{i}{n}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F_n(X_i)&space;=&space;\frac{i}{n}" title="F_n(X_i) = \frac{i}{n}" /></a>



Massa provides very good explanation about the application of KS test in her lecture [[Massa]][S. Massa, Kolmogorov Smirnov Test & Power of Tests]. Marc-Olivier Arsenault has very nice blog to introduce the concept without math [[Marc-Olivier Arsenault]][Marc-Olivier Arsenault, Kolmogorov-Smirnov Test].



## Kolmogorov distribution and Kolmogorov–Smirnov statistic

The Kolmogorov distribution is the distribution of the random variable

<a href="https://www.codecogs.com/eqnedit.php?latex=K&space;=&space;\lbrace&space;X_1,&space;X_2,&space;\cdots,&space;X_n&space;\rbrace&space;=&space;\textrm{sup}_{x&space;\in&space;[0,1]}&space;\left&space;|&space;B(x)&space;\right&space;|" target="_blank"><img src="https://latex.codecogs.com/gif.latex?K&space;=&space;\lbrace&space;X_1,&space;X_2,&space;\cdots,&space;X_n&space;\rbrace&space;=&space;\textrm{sup}_{x&space;\in&space;[0,1]}&space;\left&space;|&space;B(x)&space;\right&space;|" title="K = \lbrace X_1, X_2, \cdots, X_n \rbrace = \textrm{sup}_{x \in [0,1]} \left | B(x) \right |" /></a>

where B(x) is the [Brownian bridge](https://en.wikipedia.org/wiki/Brownian_bridge). The cumulative distribution function of K is given by [[Wiki]][Wiki, Kolmogorov–Smirnov test]

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{Pr}(K&space;\le&space;x)&space;=&space;\frac{\sqrt{2&space;\pi}}{x}&space;\sum^{\infty}_{k=1}&space;e^{-(2k-1)^2&space;\pi^2/(8&space;x^2)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{Pr}(K&space;\le&space;x)&space;=&space;\frac{\sqrt{2&space;\pi}}{x}&space;\sum^{\infty}_{k=1}&space;e^{-(2k-1)^2&space;\pi^2/(8&space;x^2)}" title="\textrm{Pr}(K \le x) = \frac{\sqrt{2 \pi}}{x} \sum^{\infty}_{k=1} e^{-(2k-1)^2 \pi^2/(8 x^2)}" /></a>


Given a null hypothesis, we reject the null hypothesis at level α (α = 0.05, for example), if Kolmogorov–Smirnov statistic `Dn` satisfies

<a href="https://www.codecogs.com/eqnedit.php?latex=D_n&space;>&space;D_{\textrm{crit},&space;n}&space;=&space;\frac{K_{\alpha}}{\sqrt{n}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D_n&space;>&space;D_{\textrm{crit},&space;n}&space;=&space;\frac{K_{\alpha}}{\sqrt{n}}" title="D_n > D_{\textrm{crit}, n} = \frac{K_{\alpha}}{\sqrt{n}}" /></a>

where <a href="https://www.codecogs.com/eqnedit.php?latex=D_{\textrm{crit},&space;n}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D_{\textrm{crit},&space;n}" title="D_{\textrm{crit}, n}" /></a> is the critical value and <a href="https://www.codecogs.com/eqnedit.php?latex=K_{\alpha}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?K_{\alpha}" title="K_{\alpha}" /></a> is from <a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{Pr}(K&space;\le&space;K_{\alpha})&space;=&space;1&space;-\alpha" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{Pr}(K&space;\le&space;K_{\alpha})&space;=&space;1&space;-\alpha" title="\textrm{Pr}(K \le K_{\alpha}) = 1 -\alpha" /></a>.





## One-sample KS test


The `Kolmogorov–Smirnov statistic` for a given **cumulative distribution function** (reference) `F(x)` is

<a href="https://www.codecogs.com/eqnedit.php?latex=D_n&space;=&space;\textrm{sup}_x&space;\left&space;|&space;F_n(x)&space;-F(x)&space;\right&space;|" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D_n&space;=&space;\textrm{sup}_x&space;\left&space;|&space;F_n(x)&space;-F(x)&space;\right&space;|" title="D_n = \textrm{sup}_x \left | F_n(x) -F(x) \right |" /></a>,

where the KS statistic is determined by the maximal distance between `F` and `Fn`. The null hypothesis is 

<a href="https://www.codecogs.com/eqnedit.php?latex=H_0&space;:&space;\textrm{the&space;samples&space;come&space;from&space;}&space;F_n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_0&space;:&space;\textrm{the&space;samples&space;come&space;from&space;}&space;F_n" title="H_0 : \textrm{the samples come from } F_n" /></a>


against the alternative hypothesis 

<a href="https://www.codecogs.com/eqnedit.php?latex=H_a&space;:&space;\textrm{the&space;samples&space;do&space;NOT&space;come&space;from&space;}&space;F_n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_a&space;:&space;\textrm{the&space;samples&space;do&space;NOT&space;come&space;from&space;}&space;F_n" title="H_a : \textrm{the samples do NOT come from } F_n" /></a>

As we described previously, when 

<a href="https://www.codecogs.com/eqnedit.php?latex=D_n&space;>&space;D_{\textrm{crit},&space;n}&space;=&space;\frac{K_{\alpha}}{\sqrt{n}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D_n&space;>&space;D_{\textrm{crit},&space;n}&space;=&space;\frac{K_{\alpha}}{\sqrt{n}}" title="D_n > D_{\textrm{crit}, n} = \frac{K_{\alpha}}{\sqrt{n}}" /></a>

we reject the null hypothesis.

As an example given by Massa [[Massa]][S. Massa, Kolmogorov Smirnov Test & Power of Tests], suppose we have data and are wondering if it comes from a normally distributed `N(0,1)`. In her lecture, we first order the data to form the empirical distribution function `Fn`, and prepare the CDF of `N(0,1)` as `F`. Then we compute all `|Fn-F|` and determine the KS statistic `Dn` is 0.092 (maximal difference). For significant level `α=0.05`, <a href="https://www.codecogs.com/eqnedit.php?latex=K_{\alpha}&space;=&space;1.36" target="_blank"><img src="https://latex.codecogs.com/gif.latex?K_{\alpha}&space;=&space;1.36" title="K_{\alpha} = 1.36" /></a>, such that the critical value is 1.36/10 = 0.136 if sample size `n=100`. As a consequence,

<a href="https://www.codecogs.com/eqnedit.php?latex=D_{n}&space;=&space;0.092&space;<&space;D_{\textrm{crit},&space;n}&space;=&space;\frac{1.36}{\sqrt{100}}&space;=&space;0.136" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D_{n}&space;=&space;0.092&space;<&space;D_{\textrm{crit},&space;n}&space;=&space;\frac{1.36}{\sqrt{100}}&space;=&space;0.136" title="D_{n} = 0.092 < D_{\textrm{crit}, n} = \frac{1.36}{\sqrt{100}} = 0.136" /></a>

and we retain the null hypothesis. 


## Two-sample KS test

Suppose now we have two samples, `F1` and `F2` are the empirical distribution functions of the first and the second sample respectively (subscripts`n` and `m` denote the sample size), then the KS statistic is

<a href="https://www.codecogs.com/eqnedit.php?latex=D_{n,m}&space;=&space;\textrm{sup}_x&space;\left&space;|&space;F_{1,n}(x)&space;-F_{2,m}(x)&space;\right&space;|" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D_{n,m}&space;=&space;\textrm{sup}_x&space;\left&space;|&space;F_{1,n}(x)&space;-F_{2,m}(x)&space;\right&space;|" title="D_{n,m} = \textrm{sup}_x \left | F_{1,n}(x) -F_{2,m}(x) \right |" /></a>


The null hypothesis is rejected at level α if

<a href="https://www.codecogs.com/eqnedit.php?latex=D_{n,m}&space;>&space;C(\alpha)&space;\sqrt{\frac{1}{n}&plus;\frac{1}{m}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D_{n,m}&space;>&space;C(\alpha)&space;\sqrt{\frac{1}{n}&plus;\frac{1}{m}}" title="D_{n,m} > C(\alpha) \sqrt{\frac{1}{n}+\frac{1}{m}}" /></a>

`C(α)` is a function of α; for α = 0.05, `C(α) = 1.224` and for α = 0.01, `C(α) = 1.517`.







# Reference


* [Kirkman T. W., Kolmogorov-Smirnov Test]: http://www.physics.csbsju.edu/stats/KS-test.html
[[Kirkman] Kirkman T. W., Kolmogorov-Smirnov Test](http://www.physics.csbsju.edu/stats/KS-test.html)
* [Marc-Olivier Arsenault, Kolmogorov-Smirnov Test]: https://towardsdatascience.com/kolmogorov-smirnov-test-84c92fb4158d
[[Marc-Olivier Arsenault] Marc-Olivier Arsenault, Kolmogorov-Smirnov Test](https://towardsdatascience.com/kolmogorov-smirnov-test-84c92fb4158d)
* [S. Massa, Kolmogorov Smirnov Test & Power of Tests]: http://www.stats.ox.ac.uk/~massa/Lecture%2013.pdf
[[Massa] S. Massa, Kolmogorov Smirnov Test & Power of Tests](http://www.stats.ox.ac.uk/~massa/Lecture%2013.pdf)
* [MIT course, Kolmogorov-Smirnov Test]: https://ocw.mit.edu/courses/mathematics/18-443-statistics-for-applications-fall-2006/lecture-notes/lecture14.pdf
[[MIT] MIT course, Kolmogorov-Smirnov Test](https://ocw.mit.edu/courses/mathematics/18-443-statistics-for-applications-fall-2006/lecture-notes/lecture14.pdf)
* [Statistics How To, Kolmogorov-Smirnov Goodness of Fit Test]: https://www.statisticshowto.datasciencecentral.com/kolmogorov-smirnov-test/
[[Statistics How To] Statistics How To, Kolmogorov-Smirnov Goodness of Fit Test](https://www.statisticshowto.datasciencecentral.com/kolmogorov-smirnov-test/)
* [Wiki, Kolmogorov–Smirnov test]: https://en.wikipedia.org/wiki/Kolmogorov–Smirnov_test
[[Wiki] Wiki, Kolmogorov–Smirnov test](https://en.wikipedia.org/wiki/Kolmogorov–Smirnov_test)

