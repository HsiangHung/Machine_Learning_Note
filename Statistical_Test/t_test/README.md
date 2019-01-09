
# t-test 

t-test is used when sample size is too small or population standard deviation is unknown. Note we have assumption the sample is approximate normal distribution.

## When to use t-test rather than Z-test

Suppose we have sample X = {X1, X2, ....Xn}, the sample mean is <a href="https://www.codecogs.com/eqnedit.php?latex=\bar{X}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{X}" title="\bar{X}" /></a> and the population standard deviation is σ. Our null and alternative hypotheses are

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{H}_0:&space;\bar{X}&space;=&space;\mu,&space;\&space;\&space;\textrm{H}_a:&space;\bar{X}&space;\ne&space;\mu" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{H}_0:&space;\bar{X}&space;=&space;\mu,&space;\&space;\&space;\textrm{H}_a:&space;\bar{X}&space;\ne&space;\mu" title="\textrm{H}_0: \bar{X} = \mu, \ \ \textrm{H}_a: \bar{X} \ne \mu" /></a>

Then the z-statistic computed from the sample is

<a href="https://www.codecogs.com/eqnedit.php?latex=z&space;=&space;\frac{\bar{X}-\mu}{\sigma/\sqrt{n}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z&space;=&space;\frac{\bar{X}-\mu}{\sigma/\sqrt{n}}" title="z = \frac{\bar{X}-\mu}{\sigma/\sqrt{n}}" /></a>

If we do not know the population variance σ, we simply replaced it with the sample standard deviation s,

<a href="https://www.codecogs.com/eqnedit.php?latex=s&space;=&space;\sqrt{\frac{1}{n-1}\sum^n_{i=1}(X_i-\bar{X})^2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s&space;=&space;\sqrt{\frac{1}{n-1}\sum^n_{i=1}(X_i-\bar{X})^2}" title="s = \sqrt{\frac{1}{n-1}\sum^n_{i=1}(X_i-\bar{X})^2}" /></a>

which is an estimate of σ from the sample.

Now we have similar format to z-statistic, t-statistic defined as

<a href="https://www.codecogs.com/eqnedit.php?latex=t&space;=&space;\frac{\bar{X}-\mu}{s/\sqrt{n}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?t&space;=&space;\frac{\bar{X}-\mu}{s/\sqrt{n}}" title="t = \frac{\bar{X}-\mu}{s/\sqrt{n}}" /></a>

The distribution of T will be **more dispersed** than that of Z. This implies that you underestimate probabilities of extreme observations, such that you compute will be too narrow confidence intervals.


## Student’s t-Distribution

William Gossett computed the distribution of the t-statistic while working for the Guiness brewery, published it under the pseudonym Student, so called Student's t-distribution. He was concerned with **small sample sizes**.

The t-distribution has a single parameter called the number of degrees of freedom; his is equal to the sample size minus 1. For large samples, typically more than 50, the sample standard deviation is very accurate, and the t-distribution is close to a normal distribution. See below [[Massa]][S. Massa, t-Test].

![](images/t-distribution.png)

For two-sided z-test and 95% confidence, the critical value of statisitic is 1.96. The t-test critical values for degree of freedoms (df) = 10 and 50 are 2.23 and 2.01, respectively. Thus we can see the t-distribution with df = 50 is quite close to a z-test.


The workflow to determine using z-test or t-test is as follows [[Massa]][S. Massa, t-Test]

![](images/t-test_flowchart.png)




## Paired t-test

The two-sample t-test is used to determine where the two samples are dependent and come in pair, like patents' reaction before and after treatment. The sample sizes are the same. For each sample observation, we need to compute the difference, and 

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{H}_0:&space;\bar{X}_d&space;=0,&space;\&space;\&space;\textrm{H}_a:&space;\bar{X}_d&space;\ne0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{H}_0:&space;\bar{X}_d&space;=0,&space;\&space;\&space;\textrm{H}_a:&space;\bar{X}_d&space;\ne0" title="\textrm{H}_0: \bar{X}_d =0, \ \ \textrm{H}_a: \bar{X}_d \ne0" /></a>

The test statistic is




## Two independent Sample t-Test


The two-sample t-test is used to determine if two population means are equal [[NIST Two-Sample t-Test]][NIST, 1.3.5.3. Two-Sample t-Test for Equal Means][[Plonsky]][M. Plonsky, Hypothesis Testing: Continuous Variables (2 Sample)]

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{H}_0:&space;\bar{X}_1&space;=&space;\bar{X}_2,&space;\&space;\&space;\textrm{H}_a:&space;\bar{X}_1&space;\ne&space;\bar{X}_2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{H}_0:&space;\bar{X}_1&space;=&space;\bar{X}_2,&space;\&space;\&space;\textrm{H}_a:&space;\bar{X}_1&space;\ne&space;\bar{X}_2" title="\textrm{H}_0: \bar{X}_1 = \bar{X}_2, \ \ \textrm{H}_a: \bar{X}_1 \ne \bar{X}_2" /></a>

If population standard deviations are known, then we have z-statistic

<a href="https://www.codecogs.com/eqnedit.php?latex=z&space;=&space;\frac{\bar{X}_1-\bar{X}_2}{\sqrt{\frac{\sigma^2_1}{n_1}&plus;\frac{\sigma^2_2}{n_2}}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z&space;=&space;\frac{\bar{X}_1-\bar{X}_2}{\sqrt{\frac{\sigma^2_1}{n_1}&plus;\frac{\sigma^2_2}{n_2}}}" title="z = \frac{\bar{X}_1-\bar{X}_2}{\sqrt{\frac{\sigma^2_1}{n_1}+\frac{\sigma^2_2}{n_2}}}" /></a>

If the population standard deviations are unknown, the t-test test statistic is

<a href="https://www.codecogs.com/eqnedit.php?latex=t&space;=\frac{\bar{X}_1-\bar{X}_2}{\sqrt{\frac{s^2_1}{n_1}&plus;\frac{s^2_2}{n_2}}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?t&space;=\frac{\bar{X}_1-\bar{X}_2}{\sqrt{\frac{s^2_1}{n_1}&plus;\frac{s^2_2}{n_2}}}" title="t =\frac{\bar{X}_1-\bar{X}_2}{\sqrt{\frac{s^2_1}{n_1}+\frac{s^2_2}{n_2}}}" /></a>

where `s1` and `s2` are the sample variances. If equal variances are assumed, the test statistic becomes

<a href="https://www.codecogs.com/eqnedit.php?latex=t&space;=&space;\frac{\bar{X}_1-\bar{X}_2}{s_p\sqrt{\frac{1}{n_1}&plus;\frac{1}{n_2}}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?t&space;=&space;\frac{\bar{X}_1-\bar{X}_2}{s_p\sqrt{\frac{1}{n_1}&plus;\frac{1}{n_2}}}" title="t = \frac{\bar{X}_1-\bar{X}_2}{s_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}" /></a>

where `sp` is the pool sample variance 

<a href="https://www.codecogs.com/eqnedit.php?latex=s_p&space;=&space;\sqrt{\frac{(n_1-1)s_1^2&plus;(n_2-1)s_2^2}{n_1&plus;n_2-2}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s_p&space;=&space;\sqrt{\frac{(n_1-1)s_1^2&plus;(n_2-1)s_2^2}{n_1&plus;n_2-2}}" title="s_p = \sqrt{\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}}" /></a>




## Correction Factor

So far we have used the following formula for the standard error:

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{SE}&space;=&space;\textrm{var}(X)&space;=&space;\frac{\sigma}{\sqrt{n}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{SE}&space;=&space;\textrm{var}(X)&space;=&space;\frac{\sigma}{\sqrt{n}}" title="\textrm{SE} = \textrm{var}(X) = \frac{\sigma}{\sqrt{n}}" /></a>

This is based on the premise that we are sampling from an infinite population [[Massa]][S. Massa, t-Test]. Usually sampling is performed from a finite population and without replacement.􏰔 In this case, if a **significant proportion of the population > 5% is sampled**, we need to use the correction factor, such that standard error becomes

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{SE}&space;=&space;\frac{\sigma}{\sqrt{n}}&space;\sqrt{\frac{N-n}{N-1}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{SE}&space;=&space;\frac{\sigma}{\sqrt{n}}&space;\sqrt{\frac{N-n}{N-1}}" title="\textrm{SE} = \frac{\sigma}{\sqrt{n}} \sqrt{\frac{N-n}{N-1}}" /></a>




## Reference



[S. Massa, t-Test]: http://www.stats.ox.ac.uk/~massa/Lecture%2010.pdf
[[Massa] S. Massa, t-Test](http://www.stats.ox.ac.uk/~massa/Lecture%2010.pdf)


[NIST, 1.3.5.3. Two-Sample t-Test for Equal Means]: https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm
[[NIST Two-Sample t-Test] NIST, 1.3.5.3. Two-Sample t-Test for Equal Means](https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm)


[M. Plonsky, Hypothesis Testing: Continuous Variables (2 Sample)]: https://www4.uwsp.edu/psych/stat/11/hyptest2s.htm
[[Plonsky] M. Plonsky, Hypothesis Testing: Continuous Variables (2 Sample)](https://www4.uwsp.edu/psych/stat/11/hyptest2s.htm)





