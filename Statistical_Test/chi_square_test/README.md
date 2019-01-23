
#  Chi-Square test 

t-test is used **when sample size is too small or population standard deviation is unknown**. Note we have assumption the sample is approximate normal distribution.

## When to use t-test rather than z-test

Suppose we have sample X = {X1, X2, ....Xn}, the sample mean is <a href="https://www.codecogs.com/eqnedit.php?latex=\bar{X}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{X}" title="\bar{X}" /></a> and the population standard deviation is σ. Our null and alternative hypotheses are

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{H}_0:&space;\bar{X}&space;=&space;\mu,&space;\&space;\&space;\textrm{H}_a:&space;\bar{X}&space;\ne&space;\mu" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{H}_0:&space;\bar{X}&space;=&space;\mu,&space;\&space;\&space;\textrm{H}_a:&space;\bar{X}&space;\ne&space;\mu" title="\textrm{H}_0: \bar{X} = \mu, \ \ \textrm{H}_a: \bar{X} \ne \mu" /></a>


The distribution of T will be **more dispersed** than that of Z. This implies that you underestimate probabilities of extreme observations, such that what you compute have too narrow confidence intervals.


## Student’s t-Distribution

William Gossett computed the distribution of the t-statistic while working for the Guiness brewery, published it under the pseudonym Student, so called Student's t-distribution. He was concerned with **small sample sizes**.

The t-distribution has a single parameter called the number of degrees of freedom; his is equal to the sample size minus 1. For large samples, typically more than 50, the sample standard deviation is very accurate, and the t-distribution is close to a normal distribution. See below [[Massa]][S. Massa, t-Test].

![](images/t-distribution.png)



The workflow to determine using z-test or t-test is as follows [[Massa]][S. Massa, t-Test]

![](images/t-test_flowchart.png)













## Reference



[S. Massa, t-Test]: http://www.stats.ox.ac.uk/~massa/Lecture%2010.pdf
[[Massa] S. Massa, t-Test](http://www.stats.ox.ac.uk/~massa/Lecture%2010.pdf)


[NIST, 1.3.5.3. Two-Sample t-Test for Equal Means]: https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm
[[NIST Two-Sample t-Test] NIST, 1.3.5.3. Two-Sample t-Test for Equal Means](https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm)


[Penn State, Applied Statistic: Comparing Two Population Proportions with Independent Samples]: https://newonlinecourses.science.psu.edu/stat500/node/55/
[[PSU, 1] Penn State, Applied Statistic: Comparing Two Population Proportions with Independent Samples](https://newonlinecourses.science.psu.edu/stat500/node/55/)


[Penn State, Probability Theory and Mathematical Statistics: Comparing Two Proportions]: https://newonlinecourses.science.psu.edu/stat414/node/268/
[[PSU, 2] Penn State, Probability Theory and Mathematical Statistics: Comparing Two Proportions](https://newonlinecourses.science.psu.edu/stat414/node/268/)


[M. Plonsky, Hypothesis Testing: Continuous Variables (2 Sample)]: https://www4.uwsp.edu/psych/stat/11/hyptest2s.htm
[[Plonsky] M. Plonsky, Hypothesis Testing: Continuous Variables (2 Sample)](https://www4.uwsp.edu/psych/stat/11/hyptest2s.htm)


[Stattrek, Hypothesis Test for a Proportion]: https://stattrek.com/hypothesis-test/proportion.aspx
[[Stattrek: Hypothesis Test for a Proportion] Stattrek, Hypothesis Test for a Proportion](https://stattrek.com/hypothesis-test/proportion.aspx)



[Stattrek, Hypothesis Test: Difference Between Proportions]: https://stattrek.com/hypothesis-test/difference-in-proportions.aspx
[[Stattrek: Difference Between Proportions] Stattrek, Hypothesis Test: Difference Between Proportions](https://stattrek.com/hypothesis-test/difference-in-proportions.aspx)



