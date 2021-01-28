
## Dropout Regularization

Dropout involves going over all the layers in a neural network and setting probability of keeping a certain nodes or not. (Of course, the input layer and the output layer are kept the same.)[[Marco Peixeiro]][How to Improve a Neural Network With Regularization] and [[Jaime Durán]][A Quick Guide on Basic Regularization Methods for Neural Networks]

The probability of keeping each node is set at random. You only decide of the threshold: a value that will determine if the node is kept or not. For example, if you set the threshold to 0.7, then there is a probability of 30% that a node will be removed from the network.

Therefore, this will result in a much smaller and simpler neural network, as shown below.

![dropout](images/dropout.png)

### Why randomly removing nodes from a neural network works?

Dropout is a widely used method and it was proven to greatly improve the performance of neural network.

It means that the neural network cannot rely on any input node, since each have a random probability of being removed. Therefore, the neural network will be reluctant to give high weights to certain features, because they might disappear.
Consequently, the weights are spread across all features, making them smaller. This effectively shrinks the model and regularizes it.

















## Reference


[A Quick Guide on Basic Regularization Methods for Neural Networks]: https://medium.com/yottabytes/a-quick-guide-on-basic-regularization-methods-for-neural-networks-e10feb101328
[[Jaime Durán] A Quick Guide on Basic Regularization Methods for Neural Networks](https://medium.com/yottabytes/a-quick-guide-on-basic-regularization-methods-for-neural-networks-e10feb101328)



[How to Improve a Neural Network With Regularization]: https://towardsdatascience.com/how-to-improve-a-neural-network-with-regularization-8a18ecda9fe3
[[Marco Peixeiro] How to Improve a Neural Network With Regularization](https://towardsdatascience.com/how-to-improve-a-neural-network-with-regularization-8a18ecda9fe3)



