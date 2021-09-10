
# Hypothesis Test

[[Statistics How to]][Hypothesis Testing]

* **Step 1**: State the Null hypothesis. 
* **Step 2**: State the Alternate Hypothesis.
* **Step 3**: Draw a picture to help you visualize the problem.
* **Step 4**: State the alpha level. If you aren’t given an alpha level, use 5% (0.05). 
* **Step 5**: Find the test statistic using this formula.
* **Step 6**: Determine if rejection the null hypothesis.






## One Sample Z Test

A principal at a certain school claims that the students in his school are above average intelligence. A random sample of thirty students IQ scores have a mean score of 112.5. Is there sufficient evidence to support the principal’s claim? The mean population IQ is 100 with a standard deviation of 15.

<a href="https://www.codecogs.com/eqnedit.php?latex=Z&space;=&space;\frac{\bar{x}-\mu_0}{\sigma\sqrt{n}}&space;=&space;\frac{112.5-100}{15/\sqrt{30}}=4.56" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Z&space;=&space;\frac{\bar{x}-\mu_0}{\sigma\sqrt{n}}&space;=&space;\frac{112.5-100}{15/\sqrt{30}}=4.56" title="Z = \frac{\bar{x}-\mu_0}{\sigma\sqrt{n}} = \frac{112.5-100}{15/\sqrt{30}}=4.56" /></a>


The p-value < α=0.05. Therefore we reject the null hypothesis; i.e. the students' IQ are higher than mean population IQ.


## Z Test or T Test?

The workflows to determine if using Z-test or T-test? Credits from [slide # 18 from S. Massa](http://www.stats.ox.ac.uk/~massa/Lecture%2010.pdf) and [From the Central Limit Theorem to the Z- and t-distributions](https://towardsdatascience.com/introduction-tfrom-the-central-limit-theorem-to-the-z-and-t-distributions-66513defb175).

![](images/Z_T_test.png)

Even though population is not skewed but if sample size is large (`n > 30`), we can still use t-test due to central limit theorem [[Javier Fernandez]][From the Central Limit Theorem to the Z- and t-distributions], [[Jonathan Bartlett]][The t-test and robustness to non-normality]. However, if small sample size, we can use boostrapping to generate boostrapping distribution and evaluate the confidence interval [Coursera-Bootstrapping](https://www.coursera.org/learn/inferential-statistics-intro/lecture/u3k1n/bootstrapping).


## Chi-Square or T test?

Select various inference, depending on data type, categorical or numeric and purpose. See the youtube explanation [Choosing a Statistical Test for Your IB Biology IA](https://www.youtube.com/watch?v=ulk_JWckJ78)

![](images/category_test_1.png)

If more than 2 groups to compare, we use ANOVA.

![](images/category_test_2.png)


#### Reference


* [From the Central Limit Theorem to the Z- and t-distributions]: https://towardsdatascience.com/introduction-tfrom-the-central-limit-theorem-to-the-z-and-t-distributions-66513defb175
[[Javier Fernandez] From the Central Limit Theorem to the Z- and t-distributions](https://towardsdatascience.com/introduction-tfrom-the-central-limit-theorem-to-the-z-and-t-distributions-66513defb175)
* [The t-test and robustness to non-normality]: https://thestatsgeek.com/2013/09/28/the-t-test-and-robustness-to-non-normality/
[[Jonathan Bartlett] The t-test and robustness to non-normality](https://thestatsgeek.com/2013/09/28/the-t-test-and-robustness-to-non-normality/)
* [Hypothesis Testing]: https://www.statisticshowto.com/probability-and-statistics/hypothesis-testing/
[[Statistics How to] Hypothesis Testing](https://www.statisticshowto.com/probability-and-statistics/hypothesis-testing/)
