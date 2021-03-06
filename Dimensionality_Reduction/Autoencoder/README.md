
# Dimensionality reduction using Keras AutoEncoder

The autoencoder used for dimensionality reduction is an undercomplete autoencoder. The size of hidden layer is smaller than the input layer. By reducing the hidden layer size we force the network to learn the important features of the dataset. [[Varun Kruthiventi]][Dimensionality reduction using Keras Auto Encoder].


Autoencoders are neural network models used to learn efficient data patterns in an unsupervised manner. An autoencoder ideally consists of an **encoder** and a **decoder**. The encoder is designed **compress** data, whereas the decoder will try to **uncompress** the data. The illustration of an autoencoder workflow is (credit from [Niyas Mohammed: How to autoencode your Pokémon](https://hackernoon.com/how-to-autoencode-your-pokémon-6b0f5c7b7d97))

![autoencoder](images/autoencoder.png)


An original neural network (supervised) model is trained as 

`model.fit(X, y)`

But an autocorder is trained as

`model.fit(X, X)`

In other words, we build a model to predict output with the same dimension as input and minimum loss on information [[Elior Cohen]][Reducing Dimensionality from Dimensionality Reduction Techniques]. The values of the parameters in the hidden layers is updated by back-progagation.

## Interpretation of AutoEncoders

The autoencoder learns an approximation for the identity function, and by placing constraints on the network, such as by limiting the number of hidden units, we can discover interesting structure about the data [[UFLDL Tutorial]][Autoencoders].

As a concrete example, suppose the inputs x are the pixel intensity values from a 10×10 image (100 pixels) so n=100, and there are 50 hidden units in layer L2, and we still have output layer n=100. Since there are only 50 hidden units, the network is forced to learn a ”compressed” representation of the input, i.e. **reconstruct** the 100-pixel input x. If the input were completely random—say, each `x_i` comes from an iid Gaussian independent of the other features—then this compression task would be very difficult. But if there is structure in the data, for example, if some of the input features are correlated, then this algorithm will be able to discover some of those correlations [[UFLDL Tutorial]][Autoencoders].

## Cost (Loss) Function

Our overall cost function for the autoencoder is [[UFLDL Tutorial]][Autoencoders][[Jermey Jordan]][Introduction to autoencoders]

<a href="https://www.codecogs.com/eqnedit.php?latex=C&space;=&space;C(x,&space;\hat{x})&space;&plus;&space;\textrm{regularization}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C&space;=&space;C(x,&space;\hat{x})&space;&plus;&space;\textrm{regularization}" title="C = C(x, \hat{x}) + \textrm{regularization}" /></a>

The first term comes the reconstruction cost `C(x,x̂)`, which is the same as the cost function in [supervised neural networks](http://ufldl.stanford.edu/tutorial/supervised/MultiLayerNeuralNetworks/). If followed Andrew Ng's Machine Learning class's notation, it reads

<a href="https://www.codecogs.com/eqnedit.php?latex=C(x,\hat{x})&space;=&space;J(\Theta)=&space;\frac{1}{m}\sum^m_{i=1}&space;\frac{1}{2}||&space;h_{\Theta}(x_i)&space;-y_i&space;||^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C(x,\hat{x})&space;=&space;J(\Theta)=&space;\frac{1}{m}\sum^m_{i=1}&space;\frac{1}{2}||&space;h_{\Theta}(x_i)&space;-y_i&space;||^2" title="C(x,\hat{x}) = J(\Theta)= \frac{1}{m}\sum^m_{i=1} \frac{1}{2}|| h_{\Theta}(x_i) -y_i ||^2" /></a>

The second is the regularization term to **penalize the activations** of hidden units. There are two main ways to penalize the activation:

L1 Regularization:

   <a href="https://www.codecogs.com/eqnedit.php?latex=C(x,\hat{x})&space;&plus;&space;\sum_{h}\sum_i&space;|a^{(h)}_i|" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C(x,\hat{x})&space;&plus;&space;\sum_{h}\sum_i&space;|a^{(h)}_i|" title="C(x,\hat{x}) + \sum_{h}\sum_i |a^{(h)}_i|" /></a>

or KL-Divergence: In essence, KL-divergence is a measure of the difference between two probability distributions. Suppose we will write <a href="https://www.codecogs.com/eqnedit.php?latex=a^{(h)}_j" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a^{(h)}_j" title="a^{(h)}_j" /></a>  to denote the activation of the `j`-th hidden unit of hidden layer `h`, when the network is given a specific input x, then 

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{\rho}_j&space;=&space;\frac{1}{m}&space;\sum^m_{i=1}&space;\big[&space;a^{(h)}_j(x^{(i)})&space;\big]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{\rho}_j&space;=&space;\frac{1}{m}&space;\sum^m_{i=1}&space;\big[&space;a^{(h)}_j(x^{(i)})&space;\big]" title="\hat{\rho}_j = \frac{1}{m} \sum^m_{i=1} \big[ a^{(h)}_j(x^{(i)}) \big]" /></a>

be the average activation of hidden unit j (averaged over the training set). We would like to (approximately) enforce the constraint 

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{\rho}_j&space;=&space;\rho" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{\rho}_j&space;=&space;\rho" title="\hat{\rho}_j = \rho" /></a>

where `ρ` is a ”‘sparsity parameter”’, typically a small value close to zero (say ρ=0.05). In other words, we would like the average activation of each hidden neuron j to be close to 0.05 (say). 

Therefore the regularization term to our optimization objective that penalizes <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{\rho}_j" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{\rho}_j" title="\hat{\rho}_j" /></a> deviating significantly from ρ  is

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{regularization}&space;=&space;\sum^{n_l-1}_{l=1}&space;\sum^{s_l}_{j=1}&space;\textrm{KL}(\rho&space;||&space;\hat{\rho}_j)&space;=&space;\sum^{n_l-1}_{l=1}&space;\sum^{s_l}_{j=1}&space;\Big(&space;\rho&space;\log\frac{\rho}{\hat{\rho_j}}&space;&plus;&space;(1-\rho)\log\frac{1-\rho}{1-\hat{\rho_j}}&space;\Big)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{regularization}&space;=&space;\sum^{n_l-1}_{l=1}&space;\sum^{s_l}_{j=1}&space;\textrm{KL}(\rho&space;||&space;\hat{\rho}_j)&space;=&space;\sum^{n_l-1}_{l=1}&space;\sum^{s_l}_{j=1}&space;\Big(&space;\rho&space;\log\frac{\rho}{\hat{\rho_j}}&space;&plus;&space;(1-\rho)\log\frac{1-\rho}{1-\hat{\rho_j}}&space;\Big)" title="\textrm{regularization} = \sum^{n_l-1}_{l=1} \sum^{s_l}_{j=1} \textrm{KL}(\rho || \hat{\rho}_j) = \sum^{n_l-1}_{l=1} \sum^{s_l}_{j=1} \Big( \rho \log\frac{\rho}{\hat{\rho_j}} + (1-\rho)\log\frac{1-\rho}{1-\hat{\rho_j}} \Big)" /></a>















## Reference


[Building Autoencoders in Keras]: https://blog.keras.io/building-autoencoders-in-keras.html
[Building Autoencoders in Keras](https://blog.keras.io/building-autoencoders-in-keras.html)

[Applied Deep Learning - Part 3: Autoencoders]: https://towardsdatascience.com/applied-deep-learning-part-3-autoencoders-1c083af4d798
[[Arden Dertat] Applied Deep Learning - Part 3: Autoencoders](https://towardsdatascience.com/applied-deep-learning-part-3-autoencoders-1c083af4d798)


[Dimension Reduction - Autoencoders]: https://blog.paperspace.com/dimension-reduction-with-autoencoders/
[[ASHWINI KUMAR PAL] Dimension Reduction - Autoencoders](https://blog.paperspace.com/dimension-reduction-with-autoencoders/)

[Reducing Dimensionality from Dimensionality Reduction Techniques]: https://towardsdatascience.com/reducing-dimensionality-from-dimensionality-reduction-techniques-f658aec24dfe
[[Elior Cohen] Reducing Dimensionality from Dimensionality Reduction Techniques](https://towardsdatascience.com/reducing-dimensionality-from-dimensionality-reduction-techniques-f658aec24dfe)


[Introduction to autoencoders]: https://www.jeremyjordan.me/autoencoders/
[[Jermey Jordan] Introduction to autoencoders](https://www.jeremyjordan.me/autoencoders/)


[How to autoencode your Pokémon]: https://hackernoon.com/how-to-autoencode-your-pokémon-6b0f5c7b7d97
[[Niyas Mohammed] How to autoencode your Pokémon](https://hackernoon.com/how-to-autoencode-your-pokémon-6b0f5c7b7d97)


[Autoencoders]: http://ufldl.stanford.edu/tutorial/unsupervised/Autoencoders/
[[UFLDL Tutorial] Autoencoders](http://ufldl.stanford.edu/tutorial/unsupervised/Autoencoders/)


[Dimensionality reduction using Keras Auto Encoder]: https://www.kaggle.com/saivarunk/dimensionality-reduction-using-keras-auto-encoder
[[Varun Kruthiventi] Dimensionality reduction using Keras Auto Encoder](https://www.kaggle.com/saivarunk/dimensionality-reduction-using-keras-auto-encoder)
