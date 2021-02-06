# Deep Learning

## Hyperparameter

Learning rate, number of iteration, number of hidden layers, number of hidden layer units, choice of activation functions, momentum, mini-batch size, regularization.



## Bias/Variance

Check training/dev error and compare to **optimal Bayes error**: the lowest possible prediction error that can be achieved and is the same as irreducible error [[Cross Validated: What is Bayes Error in machine learning?]][What is Bayes Error in machine learning?]. Note here in DL, we may high bias & high variance models. As shown below on the right, the classifier only capture linear decision boundary but overfitting on several data instances (credit from Andrew's Ng's **Improve deep neural networks: Tuning, Regularization and Optimization** coursera class).

![bias_variance](images/bias_variance.png)

The expected value of errors is ([Wiki: Bias–variance tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff))

<a href="https://www.codecogs.com/eqnedit.php?latex=E[(y-\hat{y})^2]&space;=&space;E[\big(f(X)-\hat{f}(X)\big)^2]&space;&plus;&space;\textrm{Var}(\epsilon)&space;=&space;(\textrm{Bias}[\hat{f}])^2&space;&plus;&space;\textrm{Var}(\hat{f})&space;&plus;&space;\epsilon^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E[(y-\hat{y})^2]&space;=&space;E[\big(f(X)-\hat{f}(X)\big)^2]&space;&plus;&space;\textrm{Var}(\epsilon)&space;=&space;(\textrm{Bias}[\hat{f}])^2&space;&plus;&space;\textrm{Var}(\hat{f})&space;&plus;&space;\epsilon^2" title="E[(y-\hat{y})^2] = E[\big(f(X)-\hat{f}(X)\big)^2] + \textrm{Var}(\epsilon) = (\textrm{Bias}[\hat{f}])^2 + \textrm{Var}(\hat{f}) + \epsilon^2" /></a>

where <a href="https://www.codecogs.com/eqnedit.php?latex=\epsilon^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\epsilon^2" title="\epsilon^2" /></a> is the Bayes error [[Cross Validated: What is Bayes Error in machine learning?]][What is Bayes Error in machine learning?].


## Activation Function

![activation](images/activation.png)

### Linear activation

For classificastion, output layer uses sigmoid activation; for regression, uses linear activation.

However, if using linear activation in hidden layers, the neural network is equivalent to logisitc regression. Therefore it is critical for deep learning using non-linear activation functions.


## Dropout Regularization

Dropout is used to prevent over-fitting in deep learning.

It involves going over all the layers in a neural network and setting probability of keeping a certain nodes or not. (Of course, the input layer and the output layer are kept the same.)[[Marco Peixeiro]][How to Improve a Neural Network With Regularization] and [[Jaime Durán]][A Quick Guide on Basic Regularization Methods for Neural Networks]

The probability of keeping each node is set **at random**. You only decide of the threshold: a value that will determine if the node is kept or not. For example, if you set the threshold to 0.7, then there is a probability of 30% that a node will be removed from the network.

Therefore, this will result in a much smaller and simpler neural network, as shown below.

![dropout](images/dropout.png)

### Why randomly removing nodes from a neural network works?

Dropout is a widely used method and it was proven to greatly improve the performance of neural network.

It means that the neural network cannot rely on any input node, since each have a random probability of being removed. Therefore, the neural network will be reluctant to give high weights to certain features, because they might disappear [[Marco Peixeiro]][How to Improve a Neural Network With Regularization].
Consequently, the weights are spread across all features, making them smaller. This effectively shrinks the model and regularizes it.

#### Some observations using dropout:

From the post [[Amar Budhiraja]][Dropout in (Deep) Machine learning]:

1. Dropout forces a neural network to learn more robust features that are useful in conjunction with many different random subsets of the other neurons.
2. Dropout roughly doubles the number of iterations required to converge. However, training time for each epoch is less.
3. With H hidden units, each of which can be dropped, we have 2^H possible models. In testing phase, the entire network is considered and each activation is reduced by a factor p.

### Note from Andrew Ng's class

Dropout is used in computer vision field to prevent overfitting if there is no enough data. 

Meanwhile, the hyperparameter, the probability to keep neurons trigger, **keep_prob**, could be layer-dependent. 

As a concrete example, suppose we have a neural netwrok below. The second hidden layer has more parameters (7 times 7), and we can assign smaller **keep_prob**, and larger **keep_prob** in other layers. 

![dropout_2](images/dropout_2.png)

The drawback for dropout is difficult to define cost function. While doing prediction on test datasets, don't use dropout.


## Vanishing/Exploding Gradients

In very deep neural networks, we may meet vanishing and exploding gradient issue. Andrew Ng's deep learning class provided some intuition:

![vanishing_gradients](images/vanishing_gradient.png)

We can see if the parameter `w > 1` in very deep network, the multiplication of parameters grow exponentially and the value of y will explode. On the other hand, multiplication of parameter `w < 1` may lead to vanishing y. A partial solution to the problems of vanishing and exploding gradients (doesn't solve it entirely but helps a lot) is better or more careful choice of the **random initialization** for your neural network. 



## Batch Normalization

While using gradient descent, one can normalize/standardize input data. The advantage for doing this is to make cost function more spatially homogeneous and speed up model training. In this case we have some pictures like (credit from Andrew Ng's class)

![input_normalization](images/input_norm.png)

to explain gradient descent with data normalization benefiting faster converge. 

In DL, we can do the similar normalization processes, not only data in input layer, but also in hidden layers. This is called **batch normalization** (BN) [[Manish Chablani]][Batch Normalization]. BN can be implemented before and after activation. In the coursera DL class, Andrew suggested batch norm before applying to activation function.

Given an intermediate hidden layer, we first normalize as 

<a href="https://www.codecogs.com/eqnedit.php?latex=\mu&space;=&space;\frac{1}{n}\sum^{n}_{i=1}&space;z_i,&space;\&space;\sigma&space;=&space;\frac{1}{n}\sum^{n}_{i=1}(\mu-z_i)^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mu&space;=&space;\frac{1}{n}\sum^{n}_{i=1}&space;z_i,&space;\&space;\sigma&space;=&space;\frac{1}{n}\sum^{n}_{i=1}(\mu-z_i)^2" title="\mu = \frac{1}{n}\sum^{n}_{i=1} z_i, \ \sigma = \frac{1}{n}\sum^{n}_{i=1}(\mu-z_i)^2" /></a>

where <a href="https://www.codecogs.com/eqnedit.php?latex=n&space;\equiv&space;n^{n[l]},&space;z_i&space;\equiv&space;z^{n[l]}_i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n&space;\equiv&space;n^{n[l]},&space;z_i&space;\equiv&space;z^{n[l]}_i" title="n \equiv n^{n[l]}, z_i \equiv z^{n[l]}_i" /></a> denote the number of units in the hidden layer `l` and the value on the i-th unit in the hidden layer `l`. For notation simplicity, we drop the layer label `l`. 

Then we can normalize the values in hiddent units as

<a href="https://www.codecogs.com/eqnedit.php?latex=\tilde{z}_i&space;=&space;\gamma&space;z_{i,&space;\textrm{norm}}&space;&plus;&space;\beta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\tilde{z}_i&space;=&space;\gamma&space;z_{i,&space;\textrm{norm}}&space;&plus;&space;\beta" title="\tilde{z}_i = \gamma z_{i, \textrm{norm}} + \beta" /></a>  

where

<a href="https://www.codecogs.com/eqnedit.php?latex=z_{i,\textrm{norm}}&space;=&space;\frac{z_i&space;-&space;\mu}{\sqrt{\sigma^2&space;&plus;&space;\varepsilon}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z_{i,\textrm{norm}}&space;=&space;\frac{z_i&space;-&space;\mu}{\sqrt{\sigma^2&space;&plus;&space;\varepsilon}}" title="z_{i,\textrm{norm}} = \frac{z_i - \mu}{\sqrt{\sigma^2 + \varepsilon}}" /></a>

`β` and `γ` are now parameters and can be determined by gradient descent. The overall processes are as follows (credit from Andrew Ng's courser class)

![batch_normalization](images/batch_norm.png)

BN also has other advantages like: enabling the utilization of larger learning rates and reducing the common problem of vanishing gradients. BN also has a slight regularization effect. [[Manish Chablani]][Batch Normalization], [[Richmond Alake]][Batch Normalization In Neural Networks Explained (Algorithm Breakdown)].

The mini-batch gradient descent can also implement batch norm. If the neural networks are trained by mini-batch, to predict test data, we need to determine the `μ` and `σ` from training data. We can simply use the average `μ` by all mini-batch, or using exponentially weight average (from Andre Ng's class).











## Reference

[Dropout in (Deep) Machine learning]: https://medium.com/@amarbudhiraja/https-medium-com-amarbudhiraja-learning-less-to-learn-better-dropout-in-deep-machine-learning-74334da4bfc5
[[Amar Budhiraja] Dropout in (Deep) Machine learning](https://medium.com/@amarbudhiraja/https-medium-com-amarbudhiraja-learning-less-to-learn-better-dropout-in-deep-machine-learning-74334da4bfc5)


[What is Bayes Error in machine learning?]: https://stats.stackexchange.com/questions/302900/what-is-bayes-error-in-machine-learning
[[Cross Validated: What is Bayes Error in machine learning?] What is Bayes Error in machine learning?](https://stats.stackexchange.com/questions/302900/what-is-bayes-error-in-machine-learning)


[A Quick Guide on Basic Regularization Methods for Neural Networks]: https://medium.com/yottabytes/a-quick-guide-on-basic-regularization-methods-for-neural-networks-e10feb101328
[[Jaime Durán] A Quick Guide on Basic Regularization Methods for Neural Networks](https://medium.com/yottabytes/a-quick-guide-on-basic-regularization-methods-for-neural-networks-e10feb101328)



[How to Improve a Neural Network With Regularization]: https://towardsdatascience.com/how-to-improve-a-neural-network-with-regularization-8a18ecda9fe3
[[Marco Peixeiro] How to Improve a Neural Network With Regularization](https://towardsdatascience.com/how-to-improve-a-neural-network-with-regularization-8a18ecda9fe3)


[Batch Normalization]: https://towardsdatascience.com/batch-normalization-8a2e585775c9
[[Manish Chablani] Batch Normalization](https://towardsdatascience.com/batch-normalization-8a2e585775c9)


[Batch Normalization In Neural Networks Explained (Algorithm Breakdown)]: https://towardsdatascience.com/batch-normalization-explained-algorithm-breakdown-23d2794511c
[[Richmond Alake] Batch Normalization In Neural Networks Explained (Algorithm Breakdown)](https://towardsdatascience.com/batch-normalization-explained-algorithm-breakdown-23d2794511c)
