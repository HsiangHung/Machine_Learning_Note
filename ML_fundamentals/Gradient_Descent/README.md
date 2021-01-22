
# Gradient Descent 




## The Termination Condition For Gradient Descent?


Discussion about the termination condition for gradient descent: [[CrossValidated-1]][How can stochastic gradient descent avoid the problem of a local minimum?], [[Mathematics]][Stopping criteria for gradient method]

* Determine the number of iterations we need to perform to achieve a desired error .
* Terminating when changes in parameter or changes in cost functions is small enough. 
* Terminating when gradient is small enough.


## Local Minimum Trap

Stochastic gradient descent has a much noisier error surface since you are evaluating each sample iteratively. So, here are some practical tips if you are using stochastic gradient descent:

1. shuffle the training set before each epoch (or iteration in the "standard" variant)
2. use an adaptive learning rate to "anneal" closer to the global minimum








## Reference


[How to define the termination condition for gradient descent?]: https://stats.stackexchange.com/questions/33136/how-to-define-the-termination-condition-for-gradient-descent
[[CrossValidated-1] How to define the termination condition for gradient descent?](https://stats.stackexchange.com/questions/33136/how-to-define-the-termination-condition-for-gradient-descent)


[How can stochastic gradient descent avoid the problem of a local minimum?]: https://stats.stackexchange.com/questions/90874/how-can-stochastic-gradient-descent-avoid-the-problem-of-a-local-minimum
[[CrossValidated-2] How can stochastic gradient descent avoid the problem of a local minimum?](https://stats.stackexchange.com/questions/90874/how-can-stochastic-gradient-descent-avoid-the-problem-of-a-local-minimum)


[Stopping criteria for gradient method]: https://math.stackexchange.com/questions/1618330/stopping-criteria-for-gradient-method
[[Mathematics] Stopping criteria for gradient method](https://math.stackexchange.com/questions/1618330/stopping-criteria-for-gradient-method)

