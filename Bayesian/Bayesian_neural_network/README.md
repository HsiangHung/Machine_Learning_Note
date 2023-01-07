# Bayesian Neural Network

**Content**

[1. Bayesian Statistics](https://github.com/HsiangHung/MachineLearningNote/tree/master/Bayesian%20and%20MCMC#1-bayesian-statistics)

[2. Maximum Likelihood/a Posteriori Estimation](https://github.com/HsiangHung/MachineLearningNote/tree/master/Bayesian%20and%20MCMC#2-maximum-likelihooda-posteriori-estimation)


[3. Markov Chain Monte Carlo for Bayesian Inference](https://github.com/HsiangHung/MachineLearningNote/tree/master/Bayesian%20and%20MCMC#3-markov-chain-monte-carlo-for-bayesian-inference)



# 1. Bayesian Statistics

## 1.1 Frequentist and Bayesian

In a traditional neural network, weights $\bf{w} = (w_1, w_2, \cdots)$ are assigned as a single value or point estimate, whereas in BNN, weights are considered a probability distribution. These probability distributions of network weights are used to estimate the uncertainty in weights and predictions. 

Figure-1 shows a schematic diagram of a BNN where weights are normally distributed.
![images](images/lasso_ridge_prior.png)

Given data $\bf{X}$, the likelihood of observing $\bf{X}$, given weights $\bf{w}$ is calculated using Bayes theorem as:

$$p(\bf{w}|\bf{X}) = \frac{p(\bf{X}|\bf{x})p(\bf{w})}{p(\bf{w})},$$

where $p(\bf{w})$ is the prior belief of the weights, equals to the integration over all possible values of the weights as:

$$p(\bf{w}) = \int p(\bf{X}|\bf{x})p(\bf{w}) d\bf{w}.$$



## 1.2 Bayes' Rule for Bayesian Inference








[Closed form Bayesian Inference for Binomial distributions]: https://suzyahyah.github.io/bayesian%20inference/2017/03/01/Closed-Form-Toy-Bayesian-Inference.html
[[Suzanna Sia] Closed form Bayesian Inference for Binomial distributions](https://suzyahyah.github.io/bayesian%20inference/2017/03/01/Closed-Form-Toy-Bayesian-Inference.html)



