
# Gradient Descent 

```
parameter = parameter - learning_rate * gradient
```

## Batch, Stochastic, Mini-Batch 

[[Sushant Patrikar]][Batch, Mini Batch & Stochastic Gradient Descent],[[Aditya Ananthram]][Optimizers be TensorFlow’s Appetizers], [[CrossValidated: Batch gradient descent versus stochastic gradient descent]][Batch gradient descent versus stochastic gradient descent], [[Z² Little]][Gradient Descent: Stochastic vs. Mini-batch vs. Batch vs. AdaGrad vs. RMSProp vs. Adam]

* **Batch**: Take the average of the gradients of all the training examples and then use that mean gradient to update our parameters. So that’s just one step of gradient descent in one epoch.

* **Stochastic**: If our dataset is very huge it is not an efficient way for using all examples in one epoch. Stochastic gradient descent (SGD) just uses one example at a time to take a single step. SGD can update to the parameters more frequently, like real-time updating. Notice how the cost effectively takes steps towards the minimum point of cost but does not get there directly. It can also never actually reach the very point of minimum cost, it can only be circulating in its region.

* **Min-batch**: A mixture of Batch and SGD. The drawback is that it wanders around the minimum region but never converges (like SGD).

For Batch Gradient Descent, the algorithm traces a straight line towards the minimum. If the cost function is convex, then it converges to a global minimum and if the cost function is not convex, then it converges to a local minimum. The learning rate is typically held constant over here.



The comparison between the gradient descents can be illustrated below (credit from [[Z² Little]][Gradient Descent: Stochastic vs. Mini-batch vs. Batch vs. AdaGrad vs. RMSProp vs. Adam]):
![comparison](images/gradient_comparison.png)



## The Termination Condition For Gradient Descent?


Discussion about the termination condition for gradient descent: [[CrossValidated: How to define the termination condition for gradient descent?]][How can stochastic gradient descent avoid the problem of a local minimum?], [[Mathematics: Stopping criteria for gradient method]][Stopping criteria for gradient method]

* Determine the number of iterations we need to perform to achieve a desired error .
* Terminating when changes in parameter or changes in cost functions is small enough. 
* Terminating when gradient is small enough.


## Local Minimum Trap

If the cost function is convex, it has one global minimum. If not, gradient descent may trap in a local minimum.

Stochastic gradient descent has a much noisier error surface since you are evaluating each sample iteratively. So, here are some practical tips if you are using stochastic gradient descent [[CrossValidated: How can stochastic gradient descent avoid the problem of a local minimum?]][How can stochastic gradient descent avoid the problem of a local minimum?]:

1. Shuffle the training set before each epoch (or iteration in the "standard" variant)
2. Use an adaptive learning rate to "anneal" closer to the global minimum


## Other Variants of Graident Descent

The following discussion used the same notation in [[Sebastian Ruder]][An overview of gradient descent optimization algorithms], but we can also refer to [[Sushant Patrikar]][Batch, Mini Batch & Stochastic Gradient Descent], [[Priyankur Sarkar]][What is Gradient Descent For Machine Learning].

We can denote the graident as

<a href="https://www.codecogs.com/eqnedit.php?latex=g_{t,i}&space;=&space;\frac{\partial&space;J(\theta_{t,i})}{\partial&space;\theta_{t,i}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?g_{t,i}&space;=&space;\frac{\partial&space;J(\theta_{t,i})}{\partial&space;\theta_{t,i}}" title="g_{t,i} = \frac{\partial J(\theta_{t,i})}{\partial \theta_{t,i}}" /></a>

For each step, the model parameter is updated as

<a href="https://www.codecogs.com/eqnedit.php?latex=\theta_{t&plus;1,&space;i}&space;=&space;\theta_{t,i}&space;-&space;\alpha&space;g_{t,i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\theta_{t&plus;1,&space;i}&space;=&space;\theta_{t,i}&space;-&space;\alpha&space;g_{t,i}" title="\theta_{t+1, i} = \theta_{t,i} - \alpha g_{t,i}" /></a>

### Adagrad (Adaptive Gradient Algorithm)

Adagrad modifies the general learning rate at each time step `t` for every parameter θ based on the past gradients [[Sebastian Ruder]][An overview of gradient descent optimization algorithms], [[Roan Gylberth]][An Introduction to AdaGrad]

<a href="https://www.codecogs.com/eqnedit.php?latex=\theta_{t&plus;1,&space;i}&space;=&space;\theta_{t,i}&space;-&space;\frac{\alpha}{\sqrt{\sum^t_{\tau=1}(g_{\tau,i})^2&space;&plus;&space;\epsilon}}&space;g_{t,i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\theta_{t&plus;1,&space;i}&space;=&space;\theta_{t,i}&space;-&space;\frac{\alpha}{\sqrt{\sum^t_{\tau=1}(g_{\tau,i})^2&space;&plus;&space;\epsilon}}&space;g_{t,i}" title="\theta_{t+1, i} = \theta_{t,i} - \frac{\alpha}{\sqrt{\sum^t_{\tau=1}(g_{\tau,i})^2 + \epsilon}} g_{t,i}" /></a>

### Adam (Adaptive Moment Estimation)

Adam is another method that computes adaptive learning rates for each parameter. In addition to storing an exponentially decaying average of past squared gradients `vt` like Adadelta and RMSprop, Adam also keeps an exponentially decaying average of past gradients `mt`, similar to momentum [[Sebastian Ruder]][An overview of gradient descent optimization algorithms].  In simple words you can consider it to be ADAGRAD + momentum [[Priyankur Sarkar]][What is Gradient Descent For Machine Learning].

<a href="https://www.codecogs.com/eqnedit.php?latex=\theta_{t&plus;1,&space;i}&space;=&space;\theta_{t,i}&space;-&space;\frac{\alpha}{\sqrt{\hat{v}_t}&space;&plus;&space;\epsilon}&space;\hat{m}_t" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\theta_{t&plus;1,&space;i}&space;=&space;\theta_{t,i}&space;-&space;\frac{\alpha}{\sqrt{\hat{v}_t}&space;&plus;&space;\epsilon}&space;\hat{m}_t" title="\theta_{t+1, i} = \theta_{t,i} - \frac{\alpha}{\sqrt{\hat{v}_t} + \epsilon} \hat{m}_t" /></a>

where 

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{m}_t&space;=&space;\frac{m_t}{1-\beta^t_1},&space;\&space;m_t&space;=&space;\beta_1&space;m_{t-1}&space;&plus;&space;(1-\beta_1)g_t" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{m}_t&space;=&space;\frac{m_t}{1-\beta^t_1},&space;\&space;m_t&space;=&space;\beta_1&space;m_{t-1}&space;&plus;&space;(1-\beta_1)g_t" title="\hat{m}_t = \frac{m_t}{1-\beta^t_1}, \ m_t = \beta_1 m_{t-1} + (1-\beta_1)g_t" /></a>

and 

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{v}_t&space;=&space;\frac{v_t}{1-\beta^t_2},&space;\&space;v_t&space;=&space;\beta_2&space;v_{t-1}&space;&plus;&space;(1-\beta_2)g^2_t" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{v}_t&space;=&space;\frac{v_t}{1-\beta^t_2},&space;\&space;v_t&space;=&space;\beta_2&space;v_{t-1}&space;&plus;&space;(1-\beta_2)g^2_t" title="\hat{v}_t = \frac{v_t}{1-\beta^t_2}, \ v_t = \beta_2 v_{t-1} + (1-\beta_2)g^2_t" /></a>

The proposed default values are `β1 = 0.9`, `β2 = 0.999`, and `ϵ = 10^{-8}`.




## Reference



[Optimizers be TensorFlow’s Appetizers]: https://towardsdatascience.com/optimizers-be-deeps-appetizers-511f3706aa67
[[Aditya Ananthram] Optimizers be TensorFlow’s Appetizers](https://towardsdatascience.com/optimizers-be-deeps-appetizers-511f3706aa67)


[Batch gradient descent versus stochastic gradient descent]: https://stats.stackexchange.com/questions/49528/batch-gradient-descent-versus-stochastic-gradient-descent
[[CrossValidated: Batch gradient descent versus stochastic gradient descent] Batch gradient descent versus stochastic gradient descent](https://stats.stackexchange.com/questions/49528/batch-gradient-descent-versus-stochastic-gradient-descent)


[How to define the termination condition for gradient descent?]: https://stats.stackexchange.com/questions/33136/how-to-define-the-termination-condition-for-gradient-descent
[[CrossValidated: How to define the termination condition for gradient descent?] How to define the termination condition for gradient descent?](https://stats.stackexchange.com/questions/33136/how-to-define-the-termination-condition-for-gradient-descent)


[How can stochastic gradient descent avoid the problem of a local minimum?]: https://stats.stackexchange.com/questions/90874/how-can-stochastic-gradient-descent-avoid-the-problem-of-a-local-minimum
[[CrossValidated: How can stochastic gradient descent avoid the problem of a local minimum?] How can stochastic gradient descent avoid the problem of a local minimum?](https://stats.stackexchange.com/questions/90874/how-can-stochastic-gradient-descent-avoid-the-problem-of-a-local-minimum)


[Stopping criteria for gradient method]: https://math.stackexchange.com/questions/1618330/stopping-criteria-for-gradient-method
[[Mathematics: Stopping criteria for gradient method] Stopping criteria for gradient method](https://math.stackexchange.com/questions/1618330/stopping-criteria-for-gradient-method)


[What is Gradient Descent For Machine Learning]: https://www.knowledgehut.com/blog/data-science/gradient-descent-in-machine-learning
[[Priyankur Sarkar] What is Gradient Descent For Machine Learning](https://www.knowledgehut.com/blog/data-science/gradient-descent-in-machine-learning)


[An Introduction to AdaGrad]: https://medium.com/konvergen/an-introduction-to-adagrad-f130ae871827gradient-descent-in-machine-learning
[[Roan Gylberth] An Introduction to AdaGrad](https://medium.com/konvergen/an-introduction-to-adagrad-f130ae871827)



[An overview of gradient descent optimization algorithms]: https://ruder.io/optimizing-gradient-descent/index.html#adam
[[Sebastian Ruder] An overview of gradient descent optimization algorithms](https://ruder.io/optimizing-gradient-descent/index.html#adam)


[Batch, Mini Batch & Stochastic Gradient Descent]: https://towardsdatascience.com/batch-mini-batch-stochastic-gradient-descent-7a62ecba642a
[[Sushant Patrikar] Batch, Mini Batch & Stochastic Gradient Descent](https://towardsdatascience.com/batch-mini-batch-stochastic-gradient-descent-7a62ecba642a)


[Gradient Descent: Stochastic vs. Mini-batch vs. Batch vs. AdaGrad vs. RMSProp vs. Adam]: https://xzz201920.medium.com/gradient-descent-stochastic-vs-mini-batch-vs-batch-vs-adagrad-vs-rmsprop-vs-adam-3aa652318b0d
[[Z² Little] Gradient Descent: Stochastic vs. Mini-batch vs. Batch vs. AdaGrad vs. RMSProp vs. Adam](https://xzz201920.medium.com/gradient-descent-stochastic-vs-mini-batch-vs-batch-vs-adagrad-vs-rmsprop-vs-adam-3aa652318b0d)