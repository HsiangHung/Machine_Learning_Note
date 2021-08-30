
# Permutation Test

This is a very awesome virtual explanation for the permutation test by Jared Wilber [[Jared Wilber]][The Permutation Test]. The main idea is that, we want to see how likely the initial test statistic from our A/B test (between control and treatment groups) happens from population variance.

The algorithm comprises the following steps:

1. Determine and calculate the initial test-statistic by control and treatment groups.
2. Permute the treatment assignment and construct test-statistic distribution.
3. Calculate the p-value by the initial test-statistic of the permutation distribution.


## Prcoess

![](images/example_p1.png)

Split smaple two groups: in the treatment group alpaca used new shampoo where in the control group only old shampoo. Note randomization of treatment assignment is very important.
![](images/example_p2.png)

![](images/example_p3.png)

Calculate initial test statistic from mean difference between control and treatment groups:
![](images/example_p4.png)

Reshuffle the treament group. Now in both the treament and control groups, there are alpaca using new and old shampoo. Then for each treatment assignment permutation, we calculate a test statistic:
![](images/example_p5.png)

More permutations generate more test statistics:
![](images/example_p6.png)

The test statistics generate a test statistic distribution. This distribution describes the test statistics variance if null hypothesis is true (no difference between control and treatment groups).
![](images/example_p7.png)

Then we want to see where the initial test statistic is, and we can compute p-value to know how likely it happens by chance:
![](images/example_p8.png)

![](images/example_p9.png)





Usually we want α < 0.05. On the other hand, β is the probability of making type-II error, that given the null hypothesis is false you fail to reject the hypothesis

<a href="https://www.codecogs.com/eqnedit.php?latex=\beta&space;=&space;\textrm{Pr}(\textrm{fail&space;to&space;reject&space;H}_0|&space;\textrm{H}_0&space;\textrm{&space;is&space;False})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\beta&space;=&space;\textrm{Pr}(\textrm{fail&space;to&space;reject&space;H}_0|&space;\textrm{H}_0&space;\textrm{&space;is&space;False})" title="\beta = \textrm{Pr}(\textrm{fail to reject H}_0| \textrm{H}_0 \textrm{ is False})" /></a> 






#### Reference

[The Permutation Test]: https://www.jwilber.me/permutationtest/
[[Jared Wilber] The Permutation Test](https://www.jwilber.me/permutationtest/)
