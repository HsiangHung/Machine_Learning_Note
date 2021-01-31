# Support Vector Machine


## What Does "Small Dataset" Mean?


[[Shuyu Luo]][Loss Function(Part III): Support Vector Machine]

When the data has `n << p` (number of samples << number of features) --  common in industries like medical data -- the richer feature space implies a much higher risk to **overfit** the data. Thus, when n << p, **high variance models should be avoided** entirely [[Cheng-Tao Chu]][Machine Learning Done Wrong], [[Quora: What are some machine learning algorithms that can learn well even with a small data set?]][What are some machine learning algorithms that can learn well even with a small data set?]. Or by Xavier Amatriain in the Quora post, from a Bayesian point of view, if you don’t have much data, you should mostly trust your prior.




## Summary


For small datasets we should avoid overfitting. Try [[Ahmed El Deeb]][What to do with “small” data?], [[Rafael Alencar]][Dealing with very small datasets]
* Use simple models
* Beware the outliers
* Select the features
* Balance the dataset with synthetic samples (SMOTE)
* Model averaging






## Reference

[Loss Function(Part III): Support Vector Machine]: https://towardsdatascience.com/optimization-loss-function-under-the-hood-part-iii-5dff33fa015d
[[Shuyu Luo] Loss Function(Part III): Support Vector Machine](https://towardsdatascience.com/optimization-loss-function-under-the-hood-part-iii-5dff33fa015d)

