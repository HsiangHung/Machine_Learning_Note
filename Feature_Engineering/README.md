# Feature Engineering


For each machine learning model, the error is determined by noise, variance, and bias. Ensemble techs can help reduce variance, and bias (noise is irreducible error) [[Ashish Bansal]][Need for Feature Engineering in Machine Learning].

An ensemble is just a **collection of predictors** which come together (e.g. mean of all predictions) to give a final prediction. The reason we use ensembles is that many different predictors trying to predict same target variable will perform a better job than any single predictor alone. Ensembling techniques are further classified into Bagging and Boosting.

### Bagging

   In bagging, we build many **independent** predictors/models/learners and combine them using some model averaging techniques. (e.g. weighted average, majority vote or normal average) We random **sub-sample/bootstrap** data for each model, so each observation is chosen with **replacement** to be used as input for each of the model. Then we take these uncorrelated learners to make a final model, by the principle of `wisdom of the crowds`. It reduces error by reducing **variance**. So when you use `bagging`, you’re incentivized to use `high-variance and low-bias estimators` (e.g. deep decision trees). Example of bagging ensemble is **Random Forest models** (RF). 
   
   
### Boosting

   In boosting, predictors are not made independently, but **sequentially**. The subsequent predictors learn from the mistakes of the previous predictors. Therefore, the observations have an **unequal probability of appearing in subsequent models** and ones with the **highest error appear most**, rather than bagging where the observations are chosen based on the bootstrap process. The predictors can be chosen from a range of models like decision trees, regressors, classifiers etc. Because new predictors are learning from mistakes committed by previous predictors, it takes less time/iterations to reach close to actual predictions. One can interpret boosting as trying to **minimize the bias** of the overall predictor. So when you use `boosting`, you’re incentivized to use `low-variance and high-bias estimators` (e.g. shallow decision trees). However, it could lead to **overfitting** on training data. **Gradient Boosting** (GBM) is an example of boosting algorithm.
   

## Models: Random Forest (RF) and Gradient Boosting (GBM)


   Both are ensemble models to produce a distribution of simple ML models on subsets of the original data, and both leverage decision trees as their base estimator, and then combine the distribution into one "aggregated" model. [[Shaked Zychlinski]][The Search for Categorical Correlation]

   Notice RF can run trees in parallel, thus making it possible to parallelize jobs on a multiprocessor machine. GBM instead uses a sequential approach.

### 1. Random forest

   A RF will build N decision trees and then average the predictions democratically. Each tree counts for one vote. Each tree uses a different sample (by **bootstrapping** the same number of data points as the original) from the original data thus introducing randomization. Decision tree is a low bias-high variance model, but RF aims to decrease variance.

   The most prominent application of RF is multi-class object detection in large-scale real-world computer vision problems [[4]][Gradient Boosting vs Random Forest].

#### Strength and Weakness

RF can handle large amount of training data efficiently and are inherently suited for multi-class problems [[5]][An Introduction to Random Forests for Multi-class Object Detection]. RF are much easier to tune than GBM. There are typically two parameters in RF: number of trees and number of features to be selected at each node. RF are harder to overfit than GBM [[4]][Gradient Boosting vs Random Forest].


Weakness: (1) A large number of trees may make the algorithm slow for real-time prediction. (2) Unlike decision trees, the classifications made by RF are **difficult for humans to interpret**. (3) For data including categorical variables with different number of levels, RF are biased in favor of those attributes with more levels. Therefore, the variable importance scores from RF are not reliable for this type of data. Methods such as partial permutations were used to solve the problem [[6]][Random Forest - Disadvantages].


### 2. Gradient boosting

   On the other hand, a GBM will start with a not very deep tree (sometimes a decision stump - a decision tree with only one split) and will model the original target. Then it takes the errors from the first round of predictions, and passes the errors as a new target to a second tree. The second tree will model the error from the first tree, record the new errors and pass that as a target to the third tree. And so forth. Essentially it focuses on modelling errors from previous trees. A shallow tree is a high bias-low variance model, but boosting aims to decrease bias. An excellent notebook demonstrate how a GBM minimizes bias during training [[3]][Gradient boosting simplified].

   A great application of GBM is anomaly detection in supervised learning settings where data is often highly imbalanced such as DNA sequences, credit card transactions or cyber security [[4]][Gradient Boosting vs Random Forest].

#### Strength and Weakness

Since boosted trees are derived by optimizing an objective function, basically GBM can be used to solve almost all objective function that we can write gradient out. This includes things like **ranking** [[7]][Efficient top rank optimization with gradient boosting for supervised anomaly detection] and **poission regression**, which RF is harder to achieve [[4]][Gradient Boosting vs Random Forest].

Weakness: (1) Sensitive to overfitting **if the data is noisy**. (2) Training generally takes **longer** because of the fact that trees are built sequentially. (3) **Harder to tune than RF** [[8]][What is better: gradient-boosted trees, or a random forest?]. There are typically three parameters: number of trees, depth of trees and learning rate, and the each tree built is generally shallow.


A classification model comparison can be found here [[9]][An Empirical Comparison of Supervised Learning Algorithms Using Different Performance Metrics (2005)].


## Summary

The blog [Gradient Boosting from scratch](https://medium.com/mlreview/gradient-boosting-from-scratch-1e317ae4587d) shows very nice and decent diagrams to interpret the difference between bagging and boosting. 

![ensembling](images/ensembling.png)

![bagging_and_boostin](images/bagging_and_boosting.png)












## Reference

[Need for Feature Engineering in Machine Learning]: https://towardsdatascience.com/need-for-feature-engineering-in-machine-learning-897df2ed00e6
[Ashish Bansal, Need for Feature Engineering in Machine Learning](https://towardsdatascience.com/need-for-feature-engineering-in-machine-learning-897df2ed00e6)



[The Search for Categorical Correlation]: https://towardsdatascience.com/the-search-for-categorical-correlation-a1cf7f1888c9
[Shaked Zychlinski, The Search for Categorical Correlation](https://towardsdatascience.com/the-search-for-categorical-correlation-a1cf7f1888c9)


[Gradient boosting simplified]: https://www.kaggle.com/grroverpr/gradient-boosting-simplified/
[[3] Gradient boosting simplified](https://www.kaggle.com/grroverpr/gradient-boosting-simplified/)


[Gradient Boosting vs Random Forest]: https://medium.com/@aravanshad/gradient-boosting-versus-random-forest-cfa3fa8f0d80
[[4] Gradient Boosting vs Random Forest](https://medium.com/@aravanshad/gradient-boosting-versus-random-forest-cfa3fa8f0d80)


[An Introduction to Random Forests for Multi-class Object Detection]: https://pdfs.semanticscholar.org/9035/e87ce49b67b751838c7346d36fe481260217.pdf
[[5] An Introduction to Random Forests for Multi-class Object Detection](https://pdfs.semanticscholar.org/9035/e87ce49b67b751838c7346d36fe481260217.pdf)


[Random Forest - Disadvantages]: http://www.liquisearch.com/random_forest/disadvantages
[[6] Random Forest - Disadvantages](http://www.liquisearch.com/random_forest/disadvantages)



[Efficient top rank optimization with gradient boosting for supervised anomaly detection]: http://ecmlpkdd2017.ijs.si/papers/paperID241.pdf
[[7] Efficient top rank optimization with gradient boosting for supervised anomaly detection](http://ecmlpkdd2017.ijs.si/papers/paperID241.pdf)


[What is better: gradient-boosted trees, or a random forest?]:http://fastml.com/what-is-better-gradient-boosted-trees-or-random-forest/
[[8] What is better: gradient-boosted trees, or a random forest?](http://fastml.com/what-is-better-gradient-boosted-trees-or-random-forest/)


[An Empirical Comparison of Supervised Learning Algorithms Using Different Performance Metrics (2005)]: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.60.3232
[[9] An Empirical Comparison of Supervised Learning Algorithms Using Different Performance Metrics (2005)](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.60.3232)