
# Confidence Intervals


## Confidence Interval for Two Independent Samples, Continuous Outcome

[[Terence Shin]][40 Statistics Interview Problems and Answers for Data Scientists] In a study of emergency room waiting times, investigators consider a new and the standard triage systems. To test the systems, administrators selected 20 nights and randomly assigned the new triage system to be used on 10 nights and the standard system on the remaining 10 nights. They calculated the nightly median waiting time (MWT) to see a physician. The average MWT for the new system was 3 hours with a variance of 0.60 while the average MWT for the old system was 5 hours with a variance of 0.68. Consider the 95% confidence interval estimate for the differences of the mean MWT associated with the new system. **Assume a constant variance.** What is the interval? Subtract in this order (New System — Old System).


### Equal variance

#### If n1 > 30 or n2 > 30, use the Z-table

<a href="https://www.codecogs.com/eqnedit.php?latex=\big(\bar{x}_1&space;-\bar{x}_2\big)&space;\pm&space;z&space;S_p&space;\sqrt{\frac{1}{n_1}&plus;\frac{1}{n_2}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\big(\bar{x}_1&space;-\bar{x}_2\big)&space;\pm&space;z&space;S_p&space;\sqrt{\frac{1}{n_1}&plus;\frac{1}{n_2}}" title="\big(\bar{x}_1 -\bar{x}_2\big) \pm z S_p \sqrt{\frac{1}{n_1}+\frac{1}{n_2}}" /></a>


#### If n1 < 30 or n2 < 30, use the t-table

<a href="https://www.codecogs.com/eqnedit.php?latex=\big(\bar{x}_1&space;-\bar{x}_2\big)&space;\pm&space;t_{n_1&plus;n_2-2}&space;S_p&space;\sqrt{\frac{1}{n_1}&plus;\frac{1}{n_2}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\big(\bar{x}_1&space;-\bar{x}_2\big)&space;\pm&space;t_{n_1&plus;n_2-2}&space;S_p&space;\sqrt{\frac{1}{n_1}&plus;\frac{1}{n_2}}" title="\big(\bar{x}_1 -\bar{x}_2\big) \pm t_{n_1+n_2-2} S_p \sqrt{\frac{1}{n_1}+\frac{1}{n_2}}" /></a>


<a href="https://www.codecogs.com/eqnedit.php?latex=S_p&space;=\sqrt{\frac{(n_1-1)s_1^2&plus;(n_2-1)s_2^2}{n_1&plus;n_2-2}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?S_p&space;=\sqrt{\frac{(n_1-1)s_1^2&plus;(n_2-1)s_2^2}{n_1&plus;n_2-2}}" title="S_p =\sqrt{\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}}" /></a>


### Equal variances are not assume

When the two independent samples are assumed to be drawn from populations with unequal variances,

<a href="https://www.codecogs.com/eqnedit.php?latex=\big(&space;\bar{x}_1&space;-&space;\bar{x}_2&space;\big)&space;\pm&space;t&space;\sqrt{\frac{s_1^2}{n_1}&plus;\frac{s_2^2}{n_2}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\big(&space;\bar{x}_1&space;-&space;\bar{x}_2&space;\big)&space;\pm&space;t&space;\sqrt{\frac{s_1^2}{n_1}&plus;\frac{s_2^2}{n_2}}" title="\big( \bar{x}_1 - \bar{x}_2 \big) \pm t \sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}" /></a>



#### Reference

* [SPSS TUTORIALS: INDEPENDENT SAMPLES T TEST]: https://libguides.library.kent.edu/spss/independentttest
[[Kent State University] SPSS TUTORIALS: INDEPENDENT SAMPLES T TEST](https://libguides.library.kent.edu/spss/independentttest)



* [40 Statistics Interview Problems and Answers for Data Scientists]:https://towardsdatascience.com/40-statistics-interview-problems-and-answers-for-data-scientists-6971a02b7eee
[[Terence Shin] 40 Statistics Interview Problems and Answers for Data Scientists](https://towardsdatascience.com/40-statistics-interview-problems-and-answers-for-data-scientists-6971a02b7eee)
