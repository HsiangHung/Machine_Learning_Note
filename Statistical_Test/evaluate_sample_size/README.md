
# Determine Sample Size for an A/B Test


Let's dive into how to actually calculate the sample size and timing you need for your next A/B test.





[[Ginny Mineo]][How to Determine Your A/B Testing Sample Size & Time Frame]



## Page View Example 

Udacity used the page view example to calculate sample size. Assume the click through rate is about 10%, and we want to run an A/B test. The minimum **effetc size** to observe is 2%, such that the confidence interval is 8%-12%. Given significance level 0.05 and statistical power 80%, we can use the [online calculator](https://www.evanmiller.org/ab-testing/sample-size.html), and the interface looks like

![](images/abtest_online_calculator.png)

It shows at least we need sample size at least 3,623 per variation to run AB test.





| Pred \ Actual | H0 is False | H0 is True | 
| :---: | :---: | :---: | 
| H0 is False | <a href="https://www.codecogs.com/eqnedit.php?latex=1&space;-&space;\beta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?1&space;-&space;\beta" title="1 - \beta" /></a> | <a href="https://www.codecogs.com/eqnedit.php?latex=\alpha&space;\textrm{&space;(Type&space;I&space;error)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\alpha&space;\textrm{&space;(Type&space;I&space;error)}" title="\alpha \textrm{ (Type I error)}" /></a> | 
| H0 is True | <a href="https://www.codecogs.com/eqnedit.php?latex=\beta&space;\textrm{&space;(Type&space;II&space;error)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\beta&space;\textrm{&space;(Type&space;II&space;error)}" title="\beta \textrm{ (Type II error)}" /></a> | <a href="https://www.codecogs.com/eqnedit.php?latex=1-\alpha" target="_blank"><img src="https://latex.codecogs.com/gif.latex?1-\alpha" title="1-\alpha" /></a> | 




| Effect size | r | 
| :---: | :---: | 
| Small | 0.1 |
| Medium | 0.3 |
| Large | 0.5 |





## Reference


[How to Determine Your A/B Testing Sample Size & Time Frame]: https://blog.hubspot.com/marketing/email-a-b-test-sample-size-testing-time
[[Ginny Mineo] How to Determine Your A/B Testing Sample Size & Time Frame](https://blog.hubspot.com/marketing/email-a-b-test-sample-size-testing-time)


