# Bayesian Neural Network

**Content**

[1. Bayesian Statistics](https://github.com/HsiangHung/MachineLearningNote/tree/master/Bayesian%20and%20MCMC#1-bayesian-statistics)

[2. Maximum Likelihood/a Posteriori Estimation](https://github.com/HsiangHung/MachineLearningNote/tree/master/Bayesian%20and%20MCMC#2-maximum-likelihooda-posteriori-estimation)


[3. Markov Chain Monte Carlo for Bayesian Inference](https://github.com/HsiangHung/MachineLearningNote/tree/master/Bayesian%20and%20MCMC#3-markov-chain-monte-carlo-for-bayesian-inference)



# 1. Bayesian Statistics

## 1.1 Frequentist and Bayesian

In a traditional neural network, weights $\bf{w} = (w_1, w_2, \cdots, b_1, \cdots)$ are assigned as a single value or point estimate, whereas in BNN, weights are considered a probability distribution. These probability distributions of network weights are used to estimate the uncertainty in weights and predictions. 

Figure-1 shows a schematic diagram of a BNN where weights are normally distributed [[Sabber Ahamed]][Bayesian Neural network].
![](images/weight_distribution.png)

Given data $\bf{X}$, the likelihood of observing $\bf{X}$, given weights $\bf{w}$ is calculated using Bayes theorem as:

$$p(\bf{w}|\bf{X}) = \frac{p(\bf{X}|\bf{x})p(\bf{w})}{p(\bf{w})},$$

where $p(\bf{w})$ is the prior belief of the weights, equals to the integration over all possible values of the weights as:

$$p(\bf{w}) = \int p(\bf{X}|\bf{x})p(\bf{w}) d\bf{w}.$$



## 1.2 Bayes' Rule for Bayesian Inference








[Bayesian Neural network]: https://towardsdatascience.com/bayesian-neural-network-7041dd09f2cc
[[Sabber Ahamed] Bayesian Neural network](https://towardsdatascience.com/bayesian-neural-network-7041dd09f2cc)



