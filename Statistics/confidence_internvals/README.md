
# Confidence Intervals


### Confidence Interval for Two Independent Samples, Continuous Outcome

[[Terence Shin]][40 Statistics Interview Problems and Answers for Data Scientists] In a study of emergency room waiting times, investigators consider a new and the standard triage systems. To test the systems, administrators selected 20 nights and randomly assigned the new triage system to be used on 10 nights and the standard system on the remaining 10 nights. They calculated the nightly median waiting time (MWT) to see a physician. The average MWT for the new system was 3 hours with a variance of 0.60 while the average MWT for the old system was 5 hours with a variance of 0.68. Consider the 95% confidence interval estimate for the differences of the mean MWT associated with the new system. **Assume a constant variance.** What is the interval? Subtract in this order (New System — Old System).


* If n1 > 30 or n2 > 30, use the Z-table:

<a href="https://www.codecogs.com/eqnedit.php?latex=\big(\bar{x}_1&space;-\bar{x}_2\big)&space;\pm&space;z&space;S_p&space;\sqrt{\frac{1}{n_1}&plus;\frac{1}{n_2}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\big(\bar{x}_1&space;-\bar{x}_2\big)&space;\pm&space;z&space;S_p&space;\sqrt{\frac{1}{n_1}&plus;\frac{1}{n_2}}" title="\big(\bar{x}_1 -\bar{x}_2\big) \pm z S_p \sqrt{\frac{1}{n_1}+\frac{1}{n_2}}" /></a>


* If n1 < 30 or n2 < 30, use the t-table:

<a href="https://www.codecogs.com/eqnedit.php?latex=\big(\bar{x}_1&space;-\bar{x}_2\big)&space;\pm&space;t_{n_1&plus;n_2-2}&space;S_p&space;\sqrt{\frac{1}{n_1}&plus;\frac{1}{n_2}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\big(\bar{x}_1&space;-\bar{x}_2\big)&space;\pm&space;t_{n_1&plus;n_2-2}&space;S_p&space;\sqrt{\frac{1}{n_1}&plus;\frac{1}{n_2}}" title="\big(\bar{x}_1 -\bar{x}_2\big) \pm t_{n_1+n_2-2} S_p \sqrt{\frac{1}{n_1}+\frac{1}{n_2}}" /></a>


<a href="https://www.codecogs.com/eqnedit.php?latex=\beta&space;=&space;\textrm{Pr}(\textrm{fail&space;to&space;reject&space;H}_0|&space;\textrm{H}_0&space;\textrm{&space;is&space;False})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\beta&space;=&space;\textrm{Pr}(\textrm{fail&space;to&space;reject&space;H}_0|&space;\textrm{H}_0&space;\textrm{&space;is&space;False})" title="\beta = \textrm{Pr}(\textrm{fail to reject H}_0| \textrm{H}_0 \textrm{ is False})" /></a> 

Ideally, we want both lower <a href="https://www.codecogs.com/eqnedit.php?latex=\alpha" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\alpha" title="\alpha" /></a>, but also lower <a href="https://www.codecogs.com/eqnedit.php?latex=\beta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\beta" title="\beta" /></a>. 


<a href="https://www.codecogs.com/eqnedit.php?latex=1-\beta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?1-\beta" title="1-\beta" /></a> is the power. Higher power has more reliable statistical testing. Usually we want power > 0.8.


#### Reference

* [S. Massa, Kolmogorov Smirnov Test & Power of Tests]: http://www.stats.ox.ac.uk/~massa/Lecture%2013.pdf
[[Massa] S. Massa, Kolmogorov Smirnov Test & Power of Tests](http://www.stats.ox.ac.uk/~massa/Lecture%2013.pdf)



### B. Correlation family: Effect sizes based on "variance explained"

These effect sizes estimate the amount of the variance within an experiment that is "explained" or "accounted for" by the experiment's model. Pearson's correlation, often denoted r and introduced by Karl Pearson, is widely used as an effect size when paired quantitative data are available[[wiki]][Wiki-Effect size, Effect size], [[statisticssolution]][statisticssolution, Effect Size].

| Effect size | r | 
| :---: | :---: | 
| Small | 0.1 |
| Medium | 0.3 |
| Large | 0.5 |






#### Reference

* [40 Statistics Interview Problems and Answers for Data Scientists]:https://towardsdatascience.com/40-statistics-interview-problems-and-answers-for-data-scientists-6971a02b7eee
[[Terence Shin] 40 Statistics Interview Problems and Answers for Data Scientists](https://towardsdatascience.com/40-statistics-interview-problems-and-answers-for-data-scientists-6971a02b7eee)
