
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

### Some observations using dropout:

From the post [[Amar Budhiraja]][Dropout in (Deep) Machine learning]:

1. Dropout forces a neural network to learn more robust features that are useful in conjunction with many different random subsets of the other neurons.
2. Dropout roughly doubles the number of iterations required to converge. However, training time for each epoch is less.
3. With H hidden units, each of which can be dropped, we have 2^H possible models. In testing phase, the entire network is considered and each activation is reduced by a factor p.
















## Reference

[Dropout in (Deep) Machine learning]: https://medium.com/@amarbudhiraja/https-medium-com-amarbudhiraja-learning-less-to-learn-better-dropout-in-deep-machine-learning-74334da4bfc5
[[Amar Budhiraja] Dropout in (Deep) Machine learning](https://medium.com/@amarbudhiraja/https-medium-com-amarbudhiraja-learning-less-to-learn-better-dropout-in-deep-machine-learning-74334da4bfc5)




[A Quick Guide on Basic Regularization Methods for Neural Networks]: https://medium.com/yottabytes/a-quick-guide-on-basic-regularization-methods-for-neural-networks-e10feb101328
[[Jaime Durán] A Quick Guide on Basic Regularization Methods for Neural Networks](https://medium.com/yottabytes/a-quick-guide-on-basic-regularization-methods-for-neural-networks-e10feb101328)



[How to Improve a Neural Network With Regularization]: https://towardsdatascience.com/how-to-improve-a-neural-network-with-regularization-8a18ecda9fe3
[[Marco Peixeiro] How to Improve a Neural Network With Regularization](https://towardsdatascience.com/how-to-improve-a-neural-network-with-regularization-8a18ecda9fe3)


