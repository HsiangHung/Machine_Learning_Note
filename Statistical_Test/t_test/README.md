
# t test 

t-test is used when sample size is too small or population standard deviation is unknown. Note we have assumption the sample is approximate normal distribution.

## When to use t-test rather than Z-test

Suppose we have sample X = {X1, X2, ....Xn}, the sample mean is <a href="https://www.codecogs.com/eqnedit.php?latex=\bar{X}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{X}" title="\bar{X}" /></a> and the population standard deviation is σ. Then the z-statistic computed from the sample is

<a href="https://www.codecogs.com/eqnedit.php?latex=z&space;=&space;\frac{\bar{X}-\mu}{\sigma/\sqrt{n}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z&space;=&space;\frac{\bar{X}-\mu}{\sigma/\sqrt{n}}" title="z = \frac{\bar{X}-\mu}{\sigma/\sqrt{n}}" /></a>

If we do not know the population variance σ, we simply replaced it with the sample standard deviation s,

<a href="https://www.codecogs.com/eqnedit.php?latex=s&space;=&space;\sqrt{\frac{1}{n-1}\sum^n_{i=1}(X_i-\bar{X})^2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s&space;=&space;\sqrt{\frac{1}{n-1}\sum^n_{i=1}(X_i-\bar{X})^2}" title="s = \sqrt{\frac{1}{n-1}\sum^n_{i=1}(X_i-\bar{X})^2}" /></a>

which is an estimate of σ from the sample.

Now we have similar format to z-statistic, defined as t-statistic

<a href="https://www.codecogs.com/eqnedit.php?latex=t&space;=&space;\frac{\bar{X}-\mu}{s/\sqrt{n}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?t&space;=&space;\frac{\bar{X}-\mu}{s/\sqrt{n}}" title="t = \frac{\bar{X}-\mu}{s/\sqrt{n}}" /></a>

The distribution of T will be **more dispersed** than that of Z. This implies that you underestimate probabilities of extreme observations, such that you compute will be too narrow confidence intervals.


## Student’s t-Distribution

William Gossett computed the distribution of the t-statistic while working for the Guiness brewery, published it under the pseudonym Student, so called Student's t-distribution. He was concerned with **small sample sizes**.

The t-distribution has a single parameter called the number of degrees of freedom; his is equal to the sample size minus 1. For large samples, typically more than 50, the sample standard deviation is very accurate, and the t-distribution is close to a normal distribution. See below [[Massa]][S. Massa, t-Test].

![](images/t-distribution.png)

For two-sided z-test and 95% confidence, the critical value of statisitic is 1.96. The t-test critical values for degree of freedoms (df) = 10 and 50 are 2.23 and 2.01, respectively. Thus we can see df = 50 is close to a z-test.

![](images/t-test_flowchart.png)



The Kolmogorov–Smirnov statistic quantifies a **distance** between the **empirical distribution function of the sample** and the cumulative distribution function of the reference distribution, or between the empirical distribution functions of two samples.  The null hypothesis is the sample drawn from the reference distribution (in the one-sample case), or from the same distribution (in the two-sample case). The two-sample K–S test is sensitive to differences in both location and shape of the empirical cumulative distribution functions of the two samples. 

There defines a the **empirical distribution function** (for n iid ordered observations `Xi`) as [[Wiki]][Wiki, Kolmogorov–Smirnov test], [[MIT]][MIT course, Kolmogorov-Smirnov Test]

<a href="https://www.codecogs.com/eqnedit.php?latex=F_n(x)&space;=&space;\frac{1}{n}\sum^n_{i=1}&space;\textrm{I}_{[-\infty,&space;x]}(X_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F_n(x)&space;=&space;\frac{1}{n}\sum^n_{i=1}&space;\textrm{I}_{[-\infty,&space;x]}(X_i)" title="F_n(x) = \frac{1}{n}\sum^n_{i=1} \textrm{I}_{[-\infty, x]}(X_i)" /></a>


where `I(Xi)` is called the indicator function, equal to 1 if Xi ≤ x and equal to 0 otherwise. More simply speaking, given sample `{X1, . . . , Xn}`, the empirical distribution function is the proportion of the data that lies below x [[Massa]][S. Massa, Kolmogorov Smirnov Test & Power of Tests], 

<a href="https://www.codecogs.com/eqnedit.php?latex=F_n(x)&space;=&space;\frac{\textrm{number&space;of&space;observations&space;below&space;}x}{\textrm{number&space;of&space;observations}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F_n(x)&space;=&space;\frac{\textrm{number&space;of&space;observations&space;below&space;}x}{\textrm{number&space;of&space;observations}}" title="F_n(x) = \frac{\textrm{number of observations below }x}{\textrm{number of observations}}" /></a>

If we order the sample observations  `X1 ≤ X2 ≤ ··· ≤ Xn`, then 

<a href="https://www.codecogs.com/eqnedit.php?latex=F_n(X_i)&space;=&space;\frac{i}{n}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F_n(X_i)&space;=&space;\frac{i}{n}" title="F_n(X_i) = \frac{i}{n}" /></a>



Massa provides very good explanation about the application of KS test in her lecture [[Massa]][S. Massa, Kolmogorov Smirnov Test & Power of Tests]. Marc-Olivier Arsenault has very nice blog to introduce the concept without math [[Marc-Olivier Arsenault]][Marc-Olivier Arsenault, Kolmogorov-Smirnov Test].



## Paired t-test

## Two independent Sample t-Test

[[NIST Two-Sample t-Test][NIST, 1.3.5.3. Two-Sample t-Test for Equal Means]





# Reference





[S. Massa, t-Test]: http://www.stats.ox.ac.uk/~massa/Lecture%2010.pdf
[[Massa] S. Massa, t-Test](http://www.stats.ox.ac.uk/~massa/Lecture%2010.pdf)


[NIST, 1.3.5.3. Two-Sample t-Test for Equal Means]: https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm
[[NIST Two-Sample t-Test] NIST, 1.3.5.3. Two-Sample t-Test for Equal Means](https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm)





