
# Dimensionality reduction using Keras Auto Encoder

The autoencoder used for dimensionality reduction is an undercomplete autoencoder. The size of hidden layer is smaller than the input layer. By reducing the hidden layer size we force the network to learn the important features of the dataset. [[Varun Kruthiventi]][Dimensionality reduction using Keras Auto Encoder].


Autoencoders are is a neural network used to learn efficient data patterns in an unsupervised manner. An autoencoder ideally consists of an encoder and a decoder. The encoder is designed compress data, whereas the decoder will try to uncompress the data. The illustration of an autoencoder workflow is (credit from [Niyas Mohammed: How to autoencode your Pokémon](https://hackernoon.com/how-to-autoencode-your-pokémon-6b0f5c7b7d97))

![autoencoder](images/autoencoder.png)



An original neural network (supervised) model is trained as 

`model.fit(X, y)`

But an autocorder is trained as

`model.fit(X, X)`

In other words, we build a model to predict output with the same dimension as input and minimum loss on information [[Elior Cohen]][Reducing Dimensionality from Dimensionality Reduction Techniques]. The values of the parameters in the hidden layers is updated by back-progagation.



## Summary















## Reference

[Building Autoencoders in Keras]: https://blog.keras.io/building-autoencoders-in-keras.html
[Building Autoencoders in Keras](https://blog.keras.io/building-autoencoders-in-keras.html)

[Dimension Reduction - Autoencoders]: https://blog.paperspace.com/dimension-reduction-with-autoencoders/
[Dimension Reduction - Autoencoders](https://blog.paperspace.com/dimension-reduction-with-autoencoders/)

[Reducing Dimensionality from Dimensionality Reduction Techniques]: https://towardsdatascience.com/reducing-dimensionality-from-dimensionality-reduction-techniques-f658aec24dfe
[Elior Cohen, Reducing Dimensionality from Dimensionality Reduction Techniques](https://towardsdatascience.com/reducing-dimensionality-from-dimensionality-reduction-techniques-f658aec24dfe)

[Applied Deep Learning - Part 3: Autoencoders]: https://towardsdatascience.com/applied-deep-learning-part-3-autoencoders-1c083af4d798
[Arden Dertat, Applied Deep Learning - Part 3: Autoencoders](https://towardsdatascience.com/applied-deep-learning-part-3-autoencoders-1c083af4d798)

[Dimensionality reduction using Keras Auto Encoder]: https://www.kaggle.com/saivarunk/dimensionality-reduction-using-keras-auto-encoder
[Varun Kruthiventi, Dimensionality reduction using Keras Auto Encoder](https://www.kaggle.com/saivarunk/dimensionality-reduction-using-keras-auto-encoder)

[How to autoencode your Pokémon]: https://hackernoon.com/how-to-autoencode-your-pokémon-6b0f5c7b7d97
[Niyas Mohammed, How to autoencode your Pokémon](https://hackernoon.com/how-to-autoencode-your-pokémon-6b0f5c7b7d97)

