
# Dimensionality reduction using Keras Auto Encoder

Here we introdcue the autoencoder typically used for dimensionality reduction use cases where there are more number of features. This is an undercomplete autoencoder  −
  The size of hidden layer is smaller than the input layer. By reducing the hidden layer size we force the network to learn the important features of the dataset.

For each machine learning model, the error is determined by noise, variance, and bias. Ensemble techs can help reduce variance, and bias (noise is irreducible error) [[1]][Dimensionality reduction using Keras Auto Encoder].

An ensemble is just a **collection of predictors** which come together (e.g. mean of all predictions) to give a final prediction. The reason we use ensembles is that many different predictors trying to predict same target variable will perform a better job than any single predictor alone. Ensembling techniques are further classified into Bagging and Boosting.


   
### Boosting

   In boosting, predictors are not made independently, but **sequentially**. The subsequent predictors learn from the mistakes of the previous predictors. Therefore, the observations have an **unequal probability of appearing in subsequent models** and ones with the **highest error appear most**, rather than bagging where the observations are chosen based on the bootstrap process. The predictors can be chosen from a range of models like decision trees, regressors, classifiers etc. Because new predictors are learning from mistakes committed by previous predictors, it takes less time/iterations to reach close to actual predictions. One can interpret boosting as trying to **minimize the bias** of the overall predictor. So when you use `boosting`, you’re incentivized to use `low-variance and high-bias estimators` (e.g. shallow decision trees). However, it could lead to **overfitting** on training data. **Gradient Boosting** (GBM) is an example of boosting algorithm.
   

## Models: Random Forest (RF) and Gradient Boosting (GBM)


   Both are ensemble models to produce a distribution of simple ML models on subsets of the original data, and both leverage decision trees as their base estimator, and then combine the distribution into one "aggregated" model. [[2]][What are the differences between Random Forest and Gradient Tree Boosting algorithms?]

   Notice RF can run trees in parallel, thus making it possible to parallelize jobs on a multiprocessor machine. GBM instead uses a sequential approach.






## Summary

The blog [Gradient Boosting from scratch](https://medium.com/mlreview/gradient-boosting-from-scratch-1e317ae4587d) shows very nice and decent diagrams to interpret the difference between bagging and boosting. 

![ensembling](images/ensembling.png)

![bagging_and_boostin](images/bagging_and_boosting.png)












## Reference

[Dimensionality reduction using Keras Auto Encoder]: https://www.kaggle.com/saivarunk/dimensionality-reduction-using-keras-auto-encoder
[[1] Varun Kruthiventi, Dimensionality reduction using Keras Auto Encoder](https://www.kaggle.com/saivarunk/dimensionality-reduction-using-keras-auto-encoder)


[How to autoencode your Pokémon]: https://hackernoon.com/how-to-autoencode-your-pokémon-6b0f5c7b7d97
[[2] Niyas Mohammed: How to autoencode your Pokémon](https://hackernoon.com/how-to-autoencode-your-pokémon-6b0f5c7b7d97)


[Dimension Reduction - Autoencoders]: https://blog.paperspace.com/dimension-reduction-with-autoencoders/
[[3] Dimension Reduction - Autoencoders](https://blog.paperspace.com/dimension-reduction-with-autoencoders/)


