
# Confidence Intervals (CI)


## Confidence Interval for Two Independent Samples, Continuous Outcome

[Confidence Interval for Two Independent Samples, Continuous Outcome](https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_confidence_intervals/bs704_confidence_intervals5.html), 
[[Kent State University]][SPSS TUTORIALS: INDEPENDENT SAMPLES T TEST], [[JMP]][The Two-Sample t-Test], [[UF Biostatistics]][Two Independent Samples]

### Equal variance is assumed

When the two independent samples are assumed to be drawn from populations with identical population variances:

If n1 > 30 or n2 > 30, use the Z-table, the CI is

<a href="https://www.codecogs.com/eqnedit.php?latex=\big(\bar{x}_1&space;-\bar{x}_2\big)&space;\pm&space;z&space;S_p&space;\sqrt{\frac{1}{n_1}&plus;\frac{1}{n_2}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\big(\bar{x}_1&space;-\bar{x}_2\big)&space;\pm&space;z&space;S_p&space;\sqrt{\frac{1}{n_1}&plus;\frac{1}{n_2}}" title="\big(\bar{x}_1 -\bar{x}_2\big) \pm z S_p \sqrt{\frac{1}{n_1}+\frac{1}{n_2}}" /></a>


If n1 < 30 or n2 < 30, use the t-table, the CI is

<a href="https://www.codecogs.com/eqnedit.php?latex=\big(\bar{x}_1&space;-\bar{x}_2\big)&space;\pm&space;t_{n_1&plus;n_2-2}&space;S_p&space;\sqrt{\frac{1}{n_1}&plus;\frac{1}{n_2}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\big(\bar{x}_1&space;-\bar{x}_2\big)&space;\pm&space;t_{n_1&plus;n_2-2}&space;S_p&space;\sqrt{\frac{1}{n_1}&plus;\frac{1}{n_2}}" title="\big(\bar{x}_1 -\bar{x}_2\big) \pm t_{n_1+n_2-2} S_p \sqrt{\frac{1}{n_1}+\frac{1}{n_2}}" /></a>

where the pooled standard deviation is

<a href="https://www.codecogs.com/eqnedit.php?latex=S_p&space;=\sqrt{\frac{(n_1-1)s_1^2&plus;(n_2-1)s_2^2}{n_1&plus;n_2-2}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?S_p&space;=\sqrt{\frac{(n_1-1)s_1^2&plus;(n_2-1)s_2^2}{n_1&plus;n_2-2}}" title="S_p =\sqrt{\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}}" /></a>


### Equal variances are not assume

When the two independent samples are assumed to be drawn from populations with unequal variances, the CI is  

<a href="https://www.codecogs.com/eqnedit.php?latex=\big(&space;\bar{x}_1&space;-&space;\bar{x}_2&space;\big)&space;\pm&space;t&space;\sqrt{\frac{s_1^2}{n_1}&plus;\frac{s_2^2}{n_2}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\big(&space;\bar{x}_1&space;-&space;\bar{x}_2&space;\big)&space;\pm&space;t&space;\sqrt{\frac{s_1^2}{n_1}&plus;\frac{s_2^2}{n_2}}" title="\big( \bar{x}_1 - \bar{x}_2 \big) \pm t \sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}" /></a> 


### Example 1

[[Terence Shin]][40 Statistics Interview Problems and Answers for Data Scientists] In a study of emergency room waiting times, investigators consider a new and the standard triage systems. To test the systems, administrators selected 20 nights and randomly assigned the new triage system to be used on 10 nights and the standard system on the remaining 10 nights. They calculated the nightly median waiting time (MWT) to see a physician. The average MWT for the new system was 3 hours with a variance of 0.60 while the average MWT for the old system was 5 hours with a variance of 0.68. Consider the 95% confidence interval estimate for the differences of the mean MWT associated with the new system. **Assume a constant variance.** What is the interval? Subtract in this order (New System — Old System).

<a href="https://www.codecogs.com/eqnedit.php?latex=\big(&space;3&space;-&space;5&space;\big)&space;\pm&space;t_{18}&space;\sqrt{\frac{(9*0.6^2&plus;9*0.68^2)}{18}}&space;\sqrt{\frac{2}{10}}&space;=&space;-2\pm&space;2.101*0.352" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\big(&space;3&space;-&space;5&space;\big)&space;\pm&space;t_{18}&space;\sqrt{\frac{(9*0.6^2&plus;9*0.68^2)}{18}}&space;\sqrt{\frac{2}{10}}&space;=&space;-2\pm&space;2.101*0.352" title="\big( 3 - 5 \big) \pm t_{18} \sqrt{\frac{(9*0.6^2+9*0.68^2)}{18}} \sqrt{\frac{2}{10}} = -2\pm 2.101*0.352" /></a>


### Example 2

[[Terence Shin]][40 Statistics Interview Problems and Answers for Data Scientists] To further test the hospital triage system, administrators selected 200 nights and randomly assigned a new triage system to be used on 100 nights and a standard system on the remaining 100 nights. They calculated the nightly median waiting time (MWT) to see a physician. The average MWT for the new system was 4 hours with a standard deviation of 0.5 hours while the average MWT for the old system was 6 hours with a standard deviation of 2 hours. Consider the hypothesis of a decrease in the mean MWT associated with the new treatment. What does the 95% independent group confidence interval with unequal variances suggest vis a vis this hypothesis? 

Because there’s so many observations per group, just use the Z quantile instead of the T.

<a href="https://www.codecogs.com/eqnedit.php?latex=\big(&space;4&space;-&space;6&space;\big)&space;\pm&space;z^*&space;\sqrt{\frac{(99*0.5^2&plus;99*2^2)}{200-2}}&space;\sqrt{\frac{2}{100}}&space;=&space;-2\pm&space;1.96*0.20506" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\big(&space;4&space;-&space;6&space;\big)&space;\pm&space;z^*&space;\sqrt{\frac{(99*0.5^2&plus;99*2^2)}{200-2}}&space;\sqrt{\frac{2}{100}}&space;=&space;-2\pm&space;1.96*0.20506" title="\big( 4 - 6 \big) \pm z^* \sqrt{\frac{(99*0.5^2+99*2^2)}{200-2}} \sqrt{\frac{2}{100}} = -2\pm 1.96*0.20506" /></a>



## Confidence Interval for Two Independent Samples, Dichotomous Outcome

The formula for the [confidence interval for the difference in proportions](https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_confidence_intervals/bs704_confidence_intervals7.html) is:

<a href="https://www.codecogs.com/eqnedit.php?latex=\big(&space;\hat{p}_1&space;-&space;\hat{p}_2)&space;\pm&space;z&space;\sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1}&space;&plus;&space;\frac{\hat{p}_2(1-\hat{p}_2)}{n_2}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\big(&space;\hat{p}_1&space;-&space;\hat{p}_2)&space;\pm&space;z&space;\sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1}&space;&plus;&space;\frac{\hat{p}_2(1-\hat{p}_2)}{n_2}}" title="\big( \hat{p}_1 - \hat{p}_2) \pm z \sqrt{\frac{\hat{p}_1(1-\hat{p}_1)}{n_1} + \frac{\hat{p}_2(1-\hat{p}_2)}{n_2}}" /></a>



#### Reference

* [The Two-Sample t-Test]: https://www.jmp.com/en_us/statistics-knowledge-portal/t-test/two-sample-t-test.html
[[JMP] The Two-Sample t-Test](https://www.jmp.com/en_us/statistics-knowledge-portal/t-test/two-sample-t-test.html)
* [SPSS TUTORIALS: INDEPENDENT SAMPLES T TEST]: https://libguides.library.kent.edu/spss/independentttest
[[Kent State University] SPSS TUTORIALS: INDEPENDENT SAMPLES T TEST](https://libguides.library.kent.edu/spss/independentttest)
* [40 Statistics Interview Problems and Answers for Data Scientists]:https://towardsdatascience.com/40-statistics-interview-problems-and-answers-for-data-scientists-6971a02b7eee
[[Terence Shin] 40 Statistics Interview Problems and Answers for Data Scientists](https://towardsdatascience.com/40-statistics-interview-problems-and-answers-for-data-scientists-6971a02b7eee)
* [Two Independent Samples]:https://bolt.mph.ufl.edu/6050-6052/unit-4b/module-13/two-independent-samples/
[[UF Biostatistics] Two Independent Samples](https://bolt.mph.ufl.edu/6050-6052/unit-4b/module-13/two-independent-samples/)

