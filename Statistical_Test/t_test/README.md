
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

For two-sided z-test and 95% confidence, the critical value of statisitic is 1.96. The t-test critical values for degree of freedoms (df) = 10 and 50 are 2.23 and 2.01, respectively. Thus we can see the t-distribution with df = 50 is quite close to a z-test.


The workflow to determine using z-test or t-test is as follows

![](images/t-test_flowchart.png)




## Paired t-test

## Two independent Sample t-Test

[[NIST Two-Sample t-Test][NIST, 1.3.5.3. Two-Sample t-Test for Equal Means]





# Reference





[S. Massa, t-Test]: http://www.stats.ox.ac.uk/~massa/Lecture%2010.pdf
[[Massa] S. Massa, t-Test](http://www.stats.ox.ac.uk/~massa/Lecture%2010.pdf)


[NIST, 1.3.5.3. Two-Sample t-Test for Equal Means]: https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm
[[NIST Two-Sample t-Test] NIST, 1.3.5.3. Two-Sample t-Test for Equal Means](https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm)





