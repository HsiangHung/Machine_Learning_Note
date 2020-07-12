# Bayesian Optimization

Bayesian Optimization is useful to help us search optiaml hyperparameters. It is particularly important in machine learnin; sometimes we need to fine tune hyperparameter to find optimal solution. Bayesian Optimization use historical information to efficiently find solution rather than grid search and random search.[[Mike Kraus]][Using Bayesian Optimization to reduce the time spent on hyperparameter tuning].


code examples are [here](https://www.programcreek.com/python/example/98788/hyperopt.Trials)
   


### 1. Random forest

   A RF will build N decision trees and then average the predictions democratically. Each tree counts for one vote. Each tree uses a different sample (by **bootstrapping** the same number of data points as the original) from the original data thus introducing randomization. Decision tree is a low bias-high variance model, but RF aims to decrease variance.

   The most prominent application of RF is multi-class object detection in large-scale real-world computer vision problems [[4]][Gradient Boosting vs Random Forest].







A classification model comparison can be found here [[9]][An Empirical Comparison of Supervised Learning Algorithms Using Different Performance Metrics (2005)].


## Summary

The blog [Gradient Boosting from scratch](https://medium.com/mlreview/gradient-boosting-from-scratch-1e317ae4587d) shows very nice and decent diagrams to interpret the difference between bagging and boosting. 

![ensembling](images/ensembling.png)













## Reference

[Using Bayesian Optimization to reduce the time spent on hyperparameter tuning]: https://medium.com/vantageai/bringing-back-the-time-spent-on-hyperparameter-tuning-with-bayesian-optimisation-2e21a3198afb
[[Mike Kraus] Using Bayesian Optimization to reduce the time spent on hyperparameter tuning](https://medium.com/vantageai/bringing-back-the-time-spent-on-hyperparameter-tuning-with-bayesian-optimisation-2e21a3198afb)


[A Conceptual Explanation of Bayesian Hyperparameter Optimization for Machine Learning]: https://towardsdatascience.com/a-conceptual-explanation-of-bayesian-model-based-hyperparameter-optimization-for-machine-learning-b8172278050f
[[Will Koehrsen] A Conceptual Explanation of Bayesian Hyperparameter Optimization for Machine Learning](https://towardsdatascience.com/a-conceptual-explanation-of-bayesian-model-based-hyperparameter-optimization-for-machine-learning-b8172278050f)



