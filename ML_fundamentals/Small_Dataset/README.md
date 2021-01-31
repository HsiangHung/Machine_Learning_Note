# Machine Learning with Small Dataset


## What Does "Small Dataset" Mean?

When the data has `n << p` (number of samples << number of features) --  common in industries like medical data -- the richer feature space implies a much higher risk to **overfit** the data. Thus, when n << p, **high variance models should be avoided** entirely [[Cheng-Tao Chu]][Machine Learning Done Wrong], [[Quora: What are some machine learning algorithms that can learn well even with a small data set?]][What are some machine learning algorithms that can learn well even with a small data set?]. Or by Xavier Amatriain [[Quora: What are some machine learning algorithms that can learn well even with a small data set?]][What are some machine learning algorithms that can learn well even with a small data set?], from a Bayesian point of view, if you don’t have much data, you should mostly trust your prior.

So, if you have a small dataset, you need models that have few parameters (low complexity) and/or a strong prior, or doing perform feature selection and regularization [[Ahmed El Deeb]][What to do with “small” data?]. **Bayesian inference** may be well suited for dealing with smaller datasets, especially if you can use domain expertise to construct sensible priors. Meanwhile, it is also a good idea to try model averaging and estimate confidence intervals rather than point estimates [[Ahmed El Deeb]][What to do with “small” data?].

## What are good examples of such models?

Linear models such as linear/logistic regression. Not only you can adapt the number of parameters easily, but the models also assume linear interactions only. Simple Bayesian models such as **Naive Bayes** where you also have few parameters and a direct way to adjust your prior. Also, **KNN** also works well sometimes. The paper [[5]][Learning from Little: Comparison of Classifiers Given Little Training] talked about the comparison of a variety of classifiers using small amount of data, showing that different models excel in different regions of the learning surface, leading to meta-knowledge about which to apply in different situations.

**Cleaning up your data** is also important. A StackExchange post [[4]][Small data set in machine learning] mentioned that if you have millions of data, a couple of outliers will not be a problem. But with only a few, they will definitely skew your results [[Ahmed El Deeb]][What to do with “small” data?].


There is so-call one-shot limitation learning tech to propose, using small amount of data to train models [[6]][Machine Learning with Small Data], [[7]][One-Shot Imitation Learnin].


## Summary














## Reference


[Machine Learning Done Wrong]: http://ml.posthaven.com/machine-learning-done-wrong
[[Cheng-Tao Chu] Machine Learning Done Wrong](http://ml.posthaven.com/machine-learning-done-wrong)

[What are some machine learning algorithms that can learn well even with a small data set?]: https://www.quora.com/What-are-some-machine-learning-algorithms-that-can-learn-well-even-with-a-small-data-set
[[Quora: What are some machine learning algorithms that can learn well even with a small data set?] What are some machine learning algorithms that can learn well even with a small data set?](https://www.quora.com/What-are-some-machine-learning-algorithms-that-can-learn-well-even-with-a-small-data-set)

[What to do with “small” data?]: https://medium.com/rants-on-machine-learning/what-to-do-with-small-data-d253254d1a89
[[Ahmed El Deeb] What to do with “small” data?](https://medium.com/rants-on-machine-learning/what-to-do-with-small-data-d253254d1a89)

[Small data set in machine learning]: https://datascience.stackexchange.com/questions/26140/small-data-set-in-machine-learning/26146#26146
[[4] Small data set in machine learning](https://datascience.stackexchange.com/questions/26140/small-data-set-in-machine-learning/26146#26146)

[Learning from Little: Comparison of Classifiers Given Little Training]: https://link.springer.com/chapter/10.1007/978-3-540-30116-5_17
[[5] Learning from Little: Comparison of Classifiers Given Little Training](https://link.springer.com/chapter/10.1007/978-3-540-30116-5_17)

[Machine Learning with Small Data]: http://rbharath.github.io/machine-learning-with-small-data/
[[6] Machine Learning with Small Data](http://rbharath.github.io/machine-learning-with-small-data/)

[One-Shot Imitation Learning]: https://arxiv.org/abs/1703.07326
[[7] One-Shot Imitation Learning](https://arxiv.org/abs/1703.07326)