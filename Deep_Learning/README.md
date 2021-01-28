
## Dropout Regularization

Dropout involves going over all the layers in a neural network and setting probability of keeping a certain nodes or not. (Of course, the input layer and the output layer are kept the same.)[[Marco Peixeiro]][How to Improve a Neural Network With Regularization]

The probability of keeping each node is set at random. You only decide of the threshold: a value that will determine if the node is kept or not. For example, if you set the threshold to 0.7, then there is a probability of 30% that a node will be removed from the network.

Therefore, this will result in a much smaller and simpler neural network, as shown below.

![dropout](images/dropout.png)

### Why randomly removing nodes from a neural network works?

Dropout is a widely used method and it was proven to greatly improve the performance of neural network.

It means that the neural network cannot rely on any input node, since each have a random probability of being removed. Therefore, the neural network will be reluctant to give high weights to certain features, because they might disappear.
Consequently, the weights are spread across all features, making them smaller. This effectively shrinks the model and regularizes it.









Here is the post [[Jason Brownlee]][A Gentle Introduction to Mini-Batch Gradient Descent and How to Configure Batch Size] to discuss what value of batch size in Mini-Batch Gradient Descent. A good default for batch size might be 32, and 64,.... 

The comparison between the gradient descents can be illustrated below (credit from [[Z² Little]][Gradient Descent: Stochastic vs. Mini-batch vs. Batch vs. AdaGrad vs. RMSProp vs. Adam]):
![comparison_gradient](images/gradient_comparison.png)






## Other Variants of Gradient Descent

There are many variants of SGD (stochastic gradient descent). We will briefly introduce them in the following discussion and explain with the same notation in [[Sebastian Ruder]][An overview of gradient descent optimization algorithms] and [[Jaime Durán]][Everything You Need to Know about Gradient Descent Applied to Neural Networks]. [[Sushant Patrikar]][Batch, Mini Batch & Stochastic Gradient Descent], [[Priyankur Sarkar]][What is Gradient Descent For Machine Learning] also provide good introduction.

In the following, we designate the graident as

<a href="https://www.codecogs.com/eqnedit.php?latex=g_{t}&space;=&space;\frac{\partial&space;J(\theta_{t})}{\partial&space;\theta_{t}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?g_{t}&space;=&space;\frac{\partial&space;J(\theta_{t})}{\partial&space;\theta_{t}}" title="g_{t} = \frac{\partial J(\theta_{t})}{\partial \theta_{t}}" /></a>

For each step `t`, the model parameter is updated as








Dropout means that the neural network cannot rely on any input node, since each have a random probability of being removed. Therefore, the neural network will be reluctant to give high weights to certain features, because they might disappear.
Consequently, the weights are spread across all features, making them smaller. This effectively shrinks the model and regularizes it.

## Reference



[How to Improve a Neural Network With Regularization]: https://towardsdatascience.com/how-to-improve-a-neural-network-with-regularization-8a18ecda9fe3
[[Marco Peixeiro] How to Improve a Neural Network With Regularization](https://towardsdatascience.com/how-to-improve-a-neural-network-with-regularization-8a18ecda9fe3)



