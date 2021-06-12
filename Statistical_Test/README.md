
# Statistical Testing

The conversion matrix of testing is [[Massa]][S. Massa, Kolmogorov Smirnov Test & Power of Tests]

| Pred \ Actual | H0 is False | H0 is True | 
| :---: | :---: | :---: | 
| H0 is False | <a href="https://www.codecogs.com/eqnedit.php?latex=1&space;-&space;\beta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?1&space;-&space;\beta" title="1 - \beta" /></a> | <a href="https://www.codecogs.com/eqnedit.php?latex=\alpha&space;\textrm{&space;(Type&space;I&space;error)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\alpha&space;\textrm{&space;(Type&space;I&space;error)}" title="\alpha \textrm{ (Type I error)}" /></a> | 
| H0 is True | <a href="https://www.codecogs.com/eqnedit.php?latex=\beta&space;\textrm{&space;(Type&space;II&space;error)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\beta&space;\textrm{&space;(Type&space;II&space;error)}" title="\beta \textrm{ (Type II error)}" /></a> | <a href="https://www.codecogs.com/eqnedit.php?latex=1-\alpha" target="_blank"><img src="https://latex.codecogs.com/gif.latex?1-\alpha" title="1-\alpha" /></a> | 


where `Pred` means the statistical testing results. 

<a href="https://www.codecogs.com/eqnedit.php?latex=\alpha&space;=&space;\textrm{Pr}(\textrm{reject&space;H}_0|&space;\textrm{H}_0&space;\textrm{&space;is&space;True})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\alpha&space;=&space;\textrm{Pr}(\textrm{reject&space;H}_0|&space;\textrm{H}_0&space;\textrm{&space;is&space;True})" title="\alpha = \textrm{Pr}(\textrm{reject H}_0| \textrm{H}_0 \textrm{ is True})" /></a> 

is the probability, that given the null hypothesis is true, you reject. 

<a href="https://www.codecogs.com/eqnedit.php?latex=\beta&space;=&space;\textrm{Pr}(\textrm{fail&space;to&space;reject&space;H}_0|&space;\textrm{H}_0&space;\textrm{&space;is&space;False})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\beta&space;=&space;\textrm{Pr}(\textrm{fail&space;to&space;reject&space;H}_0|&space;\textrm{H}_0&space;\textrm{&space;is&space;False})" title="\beta = \textrm{Pr}(\textrm{fail to reject H}_0| \textrm{H}_0 \textrm{ is False})" /></a> 

is the probability, that given the null hypothesis is false, you fail to reject. 

Ideally, we wish not only lower <a href="https://www.codecogs.com/eqnedit.php?latex=\alpha" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\alpha" title="\alpha" /></a>, but also lower <a href="https://www.codecogs.com/eqnedit.php?latex=\beta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\beta" title="\beta" /></a>.


<a href="https://www.codecogs.com/eqnedit.php?latex=1-\beta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?1-\beta" title="1-\beta" /></a> is the power. Higher power has more reliable statistical testing.



## Effect size

### A. Effect sizes based on differences between means

The effect size θ based on means usually considers the standardized mean difference between **two** populations [[wiki][Wiki-Effect size, Effect size], [[Merra]][Merra, Power Analysis, Statistical Significance, & Effect Size]:

<a href="https://www.codecogs.com/eqnedit.php?latex=\theta&space;=&space;\frac{\mu_1&space;-\mu_2}{\sigma}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\theta&space;=&space;\frac{\mu_1&space;-\mu_2}{\sigma}" title="\theta = \frac{\mu_1 -\mu_2}{\sigma}" /></a>

where μ1 is the mean for one population, μ2 is the mean for the other population, and σ is a standard deviation based on either or both populations.

### B. Effect sizes based on "variance explained"

These effect sizes estimate the amount of the variance within an experiment that is "explained" or "accounted for" by the experiment's model. Pearson's correlation, often denoted r and introduced by Karl Pearson, is widely used as an effect size when paired quantitative data are available[[wiki]][Wiki-Effect size, Effect size], [[statisticssolution]][statisticssolution, Effect Size].

| Effect size | r | 
| :---: | :---: | 
| Small | 0.1 |
| Medium | 0.3 |
| Large | 0.5 |


## Reference



[S. Massa, Kolmogorov Smirnov Test & Power of Tests]: http://www.stats.ox.ac.uk/~massa/Lecture%2013.pdf
[[Massa] S. Massa, Kolmogorov Smirnov Test & Power of Tests](http://www.stats.ox.ac.uk/~massa/Lecture%2013.pdf)


[Merra, Power Analysis, Statistical Significance, & Effect Size]: https://meera.snre.umich.edu/power-analysis-statistical-significance-effect-size#:~:text=Generally%2C%20effect%20size%20is%20calculated,of%20one%20of%20the%20groups.
[[Merra] Merra, Power Analysis, Statistical Significance, & Effect Size](https://meera.snre.umich.edu/power-analysis-statistical-significance-effect-size#:~:text=Generally%2C%20effect%20size%20is%20calculated,of%20one%20of%20the%20groups.)


[Wiki-Effect size, Effect size]: https://en.wikipedia.org/wiki/Effect_size
[[wiki] Wiki-Effect size, Effect size](https://en.wikipedia.org/wiki/Effect_size)


[statisticssolution, Effect Size]: https://www.statisticssolutions.com/free-resources/directory-of-statistical-analyses/effect-size/
[[statisticssolution] statisticssolution, Effect Size](https://www.statisticssolutions.com/free-resources/directory-of-statistical-analyses/effect-size/)


