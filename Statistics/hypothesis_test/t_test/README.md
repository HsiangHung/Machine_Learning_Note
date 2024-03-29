
# 1. T-Test 

t-test is used **when sample size is too small or population standard deviation is unknown**. Note we have assumption the sample is approximate normal distribution.

## When to use t-test rather than z-test

Suppose we have sample X = {X1, X2, ....Xn}, the sample mean is <a href="https://www.codecogs.com/eqnedit.php?latex=\bar{X}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{X}" title="\bar{X}" /></a> and the population standard deviation is σ. Our null and alternative hypotheses are

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{H}_0:&space;\bar{X}&space;=&space;\mu,&space;\&space;\&space;\textrm{H}_a:&space;\bar{X}&space;\ne&space;\mu" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{H}_0:&space;\bar{X}&space;=&space;\mu,&space;\&space;\&space;\textrm{H}_a:&space;\bar{X}&space;\ne&space;\mu" title="\textrm{H}_0: \bar{X} = \mu, \ \ \textrm{H}_a: \bar{X} \ne \mu" /></a>

Then the z-statistic computed from the sample is

<a href="https://www.codecogs.com/eqnedit.php?latex=z&space;=&space;\frac{\bar{X}-\mu}{\sigma/\sqrt{n}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z&space;=&space;\frac{\bar{X}-\mu}{\sigma/\sqrt{n}}" title="z = \frac{\bar{X}-\mu}{\sigma/\sqrt{n}}" /></a>

If we **do not know the population variance σ**, we simply replaced it with the sample standard deviation s,

<a href="https://www.codecogs.com/eqnedit.php?latex=s&space;=&space;\sqrt{\frac{1}{n-1}\sum^n_{i=1}(X_i-\bar{X})^2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s&space;=&space;\sqrt{\frac{1}{n-1}\sum^n_{i=1}(X_i-\bar{X})^2}" title="s = \sqrt{\frac{1}{n-1}\sum^n_{i=1}(X_i-\bar{X})^2}" /></a>

which is an estimate of σ from the sample.

Now we have similar format to z-statistic, called t-statistic, defined as

<a href="https://www.codecogs.com/eqnedit.php?latex=t&space;=&space;\frac{\bar{X}-\mu}{s/\sqrt{n}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?t&space;=&space;\frac{\bar{X}-\mu}{s/\sqrt{n}}" title="t = \frac{\bar{X}-\mu}{s/\sqrt{n}}" /></a>

The distribution of T will be **more dispersed** than that of Z. This implies that you underestimate probabilities of extreme observations, such that what you compute have too narrow confidence intervals.


## Student’s t-Distribution

William Gossett computed the distribution of the t-statistic while working for the Guiness brewery, published it under the pseudonym Student, so called Student's t-distribution. He was concerned with **small sample sizes**.

The t-distribution has a single parameter called the number of degrees of freedom; his is equal to the sample size minus 1. For large samples, typically more than 50, the sample standard deviation is very accurate, and the t-distribution is close to a normal distribution. See below [[Massa]][S. Massa, t-Test].

![](images/t-distribution.png)

For two-sided z-test and 95% confidence, the critical value of statisitic is 1.96. The t-test critical values for degree of freedoms (df) = 10 and 50 are 2.23 and 2.01, respectively. Thus we can see the t-distribution with df = 50 is quite close to a z-test.


The workflow to determine using z-test or t-test is as follows [[Massa]][S. Massa, t-Test]

![](images/t-test_flowchart.png)

from [[Javier Fernandez]][From the Central Limit Theorem to the Z- and t-distributions]
![](images/t-test_flowchart_2.png)


## Paired t-test

The two-sample t-test is used to determine where the two samples are dependent and come in pair, like patents' reaction before and after treatment. The sample sizes are the same. For each sample observation, we need to compute the difference, and 

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{H}_0:&space;\bar{X}_d&space;=0,&space;\&space;\&space;\textrm{H}_a:&space;\bar{X}_d&space;\ne0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{H}_0:&space;\bar{X}_d&space;=0,&space;\&space;\&space;\textrm{H}_a:&space;\bar{X}_d&space;\ne0" title="\textrm{H}_0: \bar{X}_d =0, \ \ \textrm{H}_a: \bar{X}_d \ne0" /></a>

The test statistic is




## Two independent sample t-test


The two-sample t-test is used to determine if two population means are equal [[NIST Two-Sample t-Test]][NIST, 1.3.5.3. Two-Sample t-Test for Equal Means], [[Plonsky]][M. Plonsky, Hypothesis Testing: Continuous Variables (2 Sample)]


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


## The t-test and robustness to non-normality

Even though population is not skewed but if sample size is large (`n > 30`), we can still use t-test due to central limit theorem [[Javier Fernandez]][From the Central Limit Theorem to the Z- and t-distributions], [[Jonathan Bartlett]][The t-test and robustness to non-normality], [[The Role of Probability]][Central Limit Theorem]. However, if small sample size, we can use boostrapping to generate boostrapping distribution and evaluate the confidence interval [Coursera-Bootstrapping](https://www.coursera.org/learn/inferential-statistics-intro/lecture/u3k1n/bootstrapping).


# 2. Z-Test


## Single proportion z-test

For comparing a sample proportion with the population proportion. Assume <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{p}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{p}" title="\hat{p}" /></a> is the sample proportion, like number of clicks divided by number of lands, and <a href="https://www.codecogs.com/eqnedit.php?latex=p_0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_0" title="p_0" /></a> is the population proportion. The sample size is still `n`. The null and alternative hypotheses are separately

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{H}_0:&space;\hat{p}&space;=&space;p_0,&space;\&space;\textrm{H}_a:&space;\hat{p}&space;\ne&space;p_0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{H}_0:&space;\hat{p}&space;=&space;p_0,&space;\&space;\textrm{H}_a:&space;\hat{p}&space;\ne&space;p_0" title="\textrm{H}_0: \hat{p} = p_0, \ \textrm{H}_a: \hat{p} \ne p_0" /></a>

The test statistic is z-test, defined as [[Stattrek: Hypothesis Test for a Proportion]][Stattrek, Hypothesis Test for a Proportion]

<a href="https://www.codecogs.com/eqnedit.php?latex=z&space;=&space;\frac{\hat{p}-p_0}{\sqrt{p_0(1-p_0)/n}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z&space;=&space;\frac{\hat{p}-p_0}{\sqrt{p_0(1-p_0)/n}}" title="z = \frac{\hat{p}-p_0}{\sqrt{p_0(1-p_0)/n}}" /></a>


## Two proportion z-test


For comparing two independent sample proportions [[Stattrek: Difference Between Proportions]][Stattrek, Hypothesis Test: Difference Between Proportions], [[PSU, 1]][Penn State, Applied Statistic: Comparing Two Population Proportions with Independent Samples], [[PSU, 2]][Penn State, Probability Theory and Mathematical Statistics: Comparing Two Proportions].
Assume two samples have 'success' proportions, 

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{p}_1&space;=&space;x_1/n_1&space;\&space;\textrm{and}&space;\&space;\hat{p}_2&space;=&space;x_2/n_2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{p}_1&space;=&space;x_1/n_1&space;\&space;\textrm{and}&space;\&space;\hat{p}_2&space;=&space;x_2/n_2" title="\hat{p}_1 = x_1/n_1 \ \textrm{and} \ \hat{p}_2 = x_2/n_2" /></a>

the test statistic is

<a href="https://www.codecogs.com/eqnedit.php?latex=z&space;=&space;\frac{(\hat{p}_1-\hat{p}_2)-0}{\sqrt{\hat{p}(1-\hat{p})\Big(\frac{1}{n_1}&plus;\frac{1}{n_2}\Big)}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z&space;=&space;\frac{(\hat{p}_1-\hat{p}_2)-0}{\sqrt{\hat{p}(1-\hat{p})\Big(\frac{1}{n_1}&plus;\frac{1}{n_2}\Big)}}" title="z = \frac{(\hat{p}_1-\hat{p}_2)-0}{\sqrt{\hat{p}(1-\hat{p})\Big(\frac{1}{n_1}+\frac{1}{n_2}\Big)}}" /></a>

where 

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{p}&space;=&space;\frac{x_1&plus;x_2}{n_1&plus;n_2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{p}&space;=&space;\frac{x_1&plus;x_2}{n_1&plus;n_2}" title="\hat{p} = \frac{x_1+x_2}{n_1+n_2}" /></a> 

is the sample pool proportion.






## Reference



* [S. Massa, t-Test]: http://www.stats.ox.ac.uk/~massa/Lecture%2010.pdf
[[Massa] S. Massa, t-Test](http://www.stats.ox.ac.uk/~massa/Lecture%2010.pdf)
* [NIST, 1.3.5.3. Two-Sample t-Test for Equal Means]: https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm
[[NIST Two-Sample t-Test] NIST, 1.3.5.3. Two-Sample t-Test for Equal Means](https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm)
* [From the Central Limit Theorem to the Z- and t-distributions]: https://towardsdatascience.com/introduction-tfrom-the-central-limit-theorem-to-the-z-and-t-distributions-66513defb175
[[Javier Fernandez] From the Central Limit Theorem to the Z- and t-distributions](https://towardsdatascience.com/introduction-tfrom-the-central-limit-theorem-to-the-z-and-t-distributions-66513defb175)
* [The t-test and robustness to non-normality]: https://thestatsgeek.com/2013/09/28/the-t-test-and-robustness-to-non-normality/
[[Jonathan Bartlett] The t-test and robustness to non-normality](https://thestatsgeek.com/2013/09/28/the-t-test-and-robustness-to-non-normality/)
* [Penn State, Applied Statistic: Comparing Two Population Proportions with Independent Samples]: https://newonlinecourses.science.psu.edu/stat500/node/55/
[[PSU, 1] Penn State, Applied Statistic: Comparing Two Population Proportions with Independent Samples](https://newonlinecourses.science.psu.edu/stat500/node/55/)
* [Penn State, Probability Theory and Mathematical Statistics: Comparing Two Proportions]: https://newonlinecourses.science.psu.edu/stat414/node/268/
[[PSU, 2] Penn State, Probability Theory and Mathematical Statistics: Comparing Two Proportions](https://newonlinecourses.science.psu.edu/stat414/node/268/)
* [M. Plonsky, Hypothesis Testing: Continuous Variables (2 Sample)]: https://www4.uwsp.edu/psych/stat/11/hyptest2s.htm
[[Plonsky] M. Plonsky, Hypothesis Testing: Continuous Variables (2 Sample)](https://www4.uwsp.edu/psych/stat/11/hyptest2s.htm)
* [Stattrek, Hypothesis Test for a Proportion]: https://stattrek.com/hypothesis-test/proportion.aspx
[[Stattrek: Hypothesis Test for a Proportion] Stattrek, Hypothesis Test for a Proportion](https://stattrek.com/hypothesis-test/proportion.aspx)
* [Stattrek, Hypothesis Test: Difference Between Proportions]: https://stattrek.com/hypothesis-test/difference-in-proportions.aspx
[[Stattrek: Difference Between Proportions] Stattrek, Hypothesis Test: Difference Between Proportions](https://stattrek.com/hypothesis-test/difference-in-proportions.aspx)
* [Central Limit Theorem]: https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_probability/BS704_Probability12.html
[[The Role of Probability] Central Limit Theorem](https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_probability/BS704_Probability12.html)


