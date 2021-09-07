
# Determine Sample Size for an A/B Test

## What is a “Sample Size”?

[[Statistics How To]][Sample Size in Statistics (How to Find it): Excel, Cochran’s Formula, General Tips]

A sample size is a **part of the population** chosen for a survey or experiment. For example, you might take a survey of dog owner’s brand preferences. You won’t want to survey all the millions of dog owners in the country (either because it’s too expensive or time consuming), so you take a sample size. That may be several thousand owners. The sample size is a representation of all dog owner’s brand preferences. If you choose your sample wisely, it will be a good representation.

## When Error can Creep in

When you only survey a **small** sample of the population, uncertainty creeps in to your statistics. If you can only survey a certain percentage of the true population, you can never be 100% sure that your statistics are a complete and accurate representation of the population. This uncertainty is called sampling error and is usually measured by a confidence interval. For example, you might state that your results are at a **90% confidence level**. That means if you were to **repeat** your survey over and over, **90% of the time your would get the results within the interval**.

## How to Find a Sample Size in Statistics

A sample is a percentage of the total population in statistics. You can use the data from a sample to make inferences about a population as a whole. For example, the standard deviation of a sample can be used to approximate the standard deviation of a population. Finding a sample size can be one of the most challenging tasks in statistics and depends upon many factors including the size of your original population.

### Large population

Assume we have large enough populations. The margin of error is given by

<a href="https://www.codecogs.com/eqnedit.php?latex=e&space;=&space;Z&space;\sqrt{\frac{p(1-p)}{n_0}}&space;=&space;Z&space;\sqrt{\frac{pq}{n_0}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e&space;=&space;Z&space;\sqrt{\frac{p(1-p)}{n_0}}&space;=&space;Z&space;\sqrt{\frac{pq}{n_0}}" title="e = Z \sqrt{\frac{p(1-p)}{n_0}} = Z \sqrt{\frac{pq}{n_0}}" /></a>

Then given **confidence level** and **margin of error**, reversely the sample size needed per variation can be estimated by cochran formula [[Statistics How To]][Sample Size in Statistics (How to Find it): Excel, Cochran’s Formula, General Tips]:

<a href="https://www.codecogs.com/eqnedit.php?latex=n_0&space;=&space;\frac{Z^2&space;pq}{e^2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n_0&space;=&space;\frac{Z^2&space;pq}{e^2}" title="n_0 = \frac{Z^2 pq}{e^2}" /></a>

Suppose we are doing a study on the inhabitants of a **large** town, and want to find out how many households serve breakfast in the mornings. We don’t have much information on the subject to begin with, so we’re going to assume that half of the families serve breakfast: this gives us **maximum variability. So p = 0.5**. Now let’s say we want 95% confidence, and at least 5%—plus or minus—precision [[Statistics How To]][Sample Size in Statistics (How to Find it): Excel, Cochran’s Formula, General Tips]. 

A 95 % confidence level gives us Z values of 1.96, per the normal tables, so we get

 
     round((1.96/0.05) * (1.96/0.05) * 0.5 * 0.5 ) + 1 = 385


So a random sample of 385 households in our target population should be enough to give us the confidence levels we need.


### Samll population - modification for the Cochran Formula

If the population we’re studying is **small**, we can modify the sample size we calculated in the above formula by using this equation [[Statistics How To]][Sample Size in Statistics (How to Find it): Excel, Cochran’s Formula, General Tips], [[Survey Monkey]][Sample size calculator]:

<a href="https://www.codecogs.com/eqnedit.php?latex=n&space;=\frac{n_0}{1&plus;\frac{n_0-1}{N}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n&space;=\frac{n_0}{1&plus;\frac{n_0-1}{N}}" title="n =\frac{n_0}{1+\frac{n_0-1}{N}}" /></a>


Here `n0` is Cochran’s sample size recommendation, **N is the population size**, and `n` is the new, adjusted sample size. In our earlier example, `n0=385` and if there were just 1000 households in the target population, we would calculate

    385 / (1 + ( 384 / 1000 )) = 278

So for this smaller population, all we need are 278 households in our sample; a substantially smaller sample size.

This is the size **one your variations** needs to be. So for your email send, if you have one control and one variation, you'll need to double this number. If you had a control and two variations, you'd triple it. (And so on.) [[Ginny Mineo]][How to Determine Your A/B Testing Sample Size & Time Frame]

Here are the calculators from [survey system](https://www.surveysystem.com/sscalc.htm) and [survey monkey](https://www.surveymonkey.com/mp/sample-size-calculator/).

### Given a confidence level and width, unknown population standard deviation

Example question: 41% of Jacksonville residents said that they had been in a hurricane. How many adults should be surveyed to estimate the true proportion of adults who have been in a hurricane, with a 95% confidence interval 6% wide?

z-score for 95% confidence interval is 1.96. The margin of error is given by the half width: 6% / 2 = 0.03. Gven percentage. p = 41% = 0.41, so q = 1-p = 0.59. If you aren’t given phat, use p = q = 50%. So the 

     (1.96/0.03) * (1.96/0.03) * 0.40 * 0.59 = 1033

1,033 people to survey.


### Given a confidence level and width, known population standard deviation

<a href="https://www.codecogs.com/eqnedit.php?latex=n&space;=&space;\Big(&space;\frac{Z_{\alpha&space;/2}&space;\sigma}{e}&space;\Big)^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n&space;=&space;\Big(&space;\frac{Z_{\alpha&space;/2}&space;\sigma}{e}&space;\Big)^2" title="n = \Big( \frac{Z_{\alpha /2} \sigma}{e} \Big)^2" /></a>

Example question: Suppose we want to know the average age of an Florida State College student, plus or minus 0.5 years. We’d like to be 99% confident about our result. From a previous study, we know that the standard deviation for the population is 2.9.

      (2.58 * 2.9 / 0.5) * (2.58 * 2.9 / 0.5) = 223



## Page View Example, Required Statistical Power

[Udacity](https://www.youtube.com/watch?v=WnQoZzxas-g&t=15s) shows the page view example to calculate sample size. Here we assume population is large enough (for internet, it is true), but we demand statistical power. 

Assume the conversion rate is about 10%, and we want to run an A/B test. The minimum **effetc size** (practical significance level) to observe is 2%, such that the confidence interval is 8%-12%. Given significance level 5% and statistical power 80%, we can use another [online calculator](https://www.evanmiller.org/ab-testing/sample-size.html), and the interface looks like

![](images/abtest_online_calculator.png)

Note the `absolute` is selected to make 8%-12% confidence interval. The online calculator shows at least we need sample size of 3,623 page views per variation (in each group) to see significant results in the AB test.



Predicting how many users we need depends on a few factors, such as how big we think the difference will be between variants, how many variants there are, and what the conversion rates are. **The larger the difference between variants, the more confident you can be that the results are statistically significant with fewer samples.**

Here is a table of roughly how many users per variant (including baseline) we recommend using at the start of your test:

| | Low conversion rates (5%) | Medium conversion rates (15%) | High conversion rates (70%) |
| --- | --- | --- | --- | --- |
| Small difference between variants (10% lift) | 40,000 | 10,000 | 700 | 
| meidum difference between variants (20% lift) | 8,000 | 2,500 | 150 | 




## Reference


* [How to Determine Your A/B Testing Sample Size & Time Frame]: https://blog.hubspot.com/marketing/email-a-b-test-sample-size-testing-time
[[Ginny Mineo] How to Determine Your A/B Testing Sample Size & Time Frame](https://blog.hubspot.com/marketing/email-a-b-test-sample-size-testing-time)
* [Sample size calculator]: https://www.surveymonkey.com/mp/sample-size-calculator/
[[Survey Monkey] Sample size calculator](https://www.surveymonkey.com/mp/sample-size-calculator/)
* [Sample Size in Statistics (How to Find it): Excel, Cochran’s Formula, General Tips]: https://www.statisticshowto.com/probability-and-statistics/find-sample-size/
[[Statistics How To] Sample Size in Statistics (How to Find it): Excel, Cochran’s Formula, General Tips](https://www.statisticshowto.com/probability-and-statistics/find-sample-size/)