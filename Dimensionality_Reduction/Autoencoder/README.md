
# Dimensionality reduction using Keras Auto Encoder

Here we introdcue the autoencoder typically used for dimensionality reduction use cases where there are more number of features. This is an undercomplete autoencoder  −
  The size of hidden layer is smaller than the input layer. By reducing the hidden layer size we force the network to learn the important features of the dataset. [[1]][Dimensionality reduction using Keras Auto Encoder].


   
### Boosting

   In boosting, predictors are not made independently, but **sequentially**. The subsequent predictors learn from the mistakes of the previous predictors. Therefore, the observations have an **unequal probability of appearing in subsequent models** and ones with the **highest error appear most**, rather than bagging where the observations are chosen based on the bootstrap process. The predictors can be chosen from a range of models like decision trees, regressors, classifiers etc. Because new predictors are learning from mistakes committed by previous predictors, it takes less time/iterations to reach close to actual predictions. One can interpret boosting as trying to **minimize the bias** of the overall predictor. So when you use `boosting`, you’re incentivized to use `low-variance and high-bias estimators` (e.g. shallow decision trees). However, it could lead to **overfitting** on training data. **Gradient Boosting** (GBM) is an example of boosting algorithm.
   





## Summary

The blog [Gradient Boosting from scratch](https://medium.com/mlreview/gradient-boosting-from-scratch-1e317ae4587d) shows very nice and decent diagrams to interpret the difference between bagging and boosting. 

![autoencoder](im/autoencoder.png)














## Reference

[Dimensionality reduction using Keras Auto Encoder]: https://www.kaggle.com/saivarunk/dimensionality-reduction-using-keras-auto-encoder
[[1] Varun Kruthiventi, Dimensionality reduction using Keras Auto Encoder](https://www.kaggle.com/saivarunk/dimensionality-reduction-using-keras-auto-encoder)


[How to autoencode your Pokémon]: https://hackernoon.com/how-to-autoencode-your-pokémon-6b0f5c7b7d97
[[2] Niyas Mohammed: How to autoencode your Pokémon](https://hackernoon.com/how-to-autoencode-your-pokémon-6b0f5c7b7d97)


[Dimension Reduction - Autoencoders]: https://blog.paperspace.com/dimension-reduction-with-autoencoders/
[[3] Dimension Reduction - Autoencoders](https://blog.paperspace.com/dimension-reduction-with-autoencoders/)


[Applied Deep Learning - Part 3: Autoencoders]: https://towardsdatascience.com/applied-deep-learning-part-3-autoencoders-1c083af4d798
[[4] Arden Dertat, Applied Deep Learning - Part 3: Autoencoders](https://towardsdatascience.com/applied-deep-learning-part-3-autoencoders-1c083af4d798)

