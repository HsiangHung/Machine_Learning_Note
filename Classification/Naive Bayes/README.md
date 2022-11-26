
# Naive Bayes Classifier


The Naive Bayes classifier is based on the Bayes theorem

$$P(B|A) = \frac{P(A|B)P(B)}{P(A)}$$

Given dataset $X=(x_1, x_2, .... x_f), y$, there are $f$ features for each event. We predict $y$ as

$$P(y|X) = \frac{P(X|y)P(y)}{P(X)} \propto P(X|y)P(y)$$

The assumption in the Naive Bayes classifier is, the features $x_1, x_2...$ are independent each other [[Rohith Gandhi]][Naive Bayes Classifier]. Therfore, we can rewrite the above posterior as

$$P(y|X) = P(y|x_1,x_2,\cdots, x_f) = \frac{P(y) P(x_1|y)P(x_2|y)\cdots P(x_f|y)}{P(x_1)P(x_2)\cdots P(x_f)} \propto P(y)\prod^f_{i=1} P(x_i|y)$$

The class $y$ is determined by maximum probability

$$y = \textrm{argmax}_y \big[ P(y) \prod^f_i P(x_i|y) \big].$$

Given $x$, if $y=1$ has higher probability than $y=0$, we assign $y=1$ for the event.

## Learning Naive Bayes

### Categorical feature

If $x$ is categorical, $P(x|y)$ is simply a count ratio. As a concrete example, we use the weather data (from [University of Edinburgh lecture](http://www.inf.ed.ac.uk/teaching/courses/inf2b/learnSlides/inf2b12-learnlec06.pdf)) as follows

![](images/example_data1.png)

The data has predictors: `x1=Outlook`, `x2=Temperature`, `x3=Humidity`, `x4=Windy`, and target `y=Play`. We will have prior `P(y)` like [[Zixuan Zhang]][Naive Bayes Explained]

$$P(\textrm{play}) = \frac{\textrm{count(play)}}{\textrm{count(all)}} = \frac{9}{14},$$

and the likelihood $P(x|y)$ as 

$$P(\textrm{sunny}|\textrm{play}) = \frac{\textrm{count(sunny, play)}}{\textrm{count(play)}}=\frac{2}{9}$$

Note if some feature values never show (maybe lack of data), their likelihood will be zero, which makes the whole posterior probability zero. One simple way to fix this problem is called **Laplace smoothing**. We can rewrite the likelihood as

$$P(x_i=A|y=1) = \frac{\textrm{count(}x_i\textrm{=A, y=1)}+1}{\textrm{count(y=1)} + V}$$

where $V$ is the number of distinct categories for $x_i$.

For example, although `count(Outlook=overcast, y=No) = 0`, with the Lapalce smoothing, $\textrm{P(overcast|No)}$ is not vanishing ($ V = 3 $).


### Continuous feature

If feature is continuous, and we visualize the data and see a bell-curve-like distribution, it is fair to make an assumption that the feature is a normal distribution. For example, suppose $x_i$ is continuous variable, we look for the mean value and standard deviation under $y=1$

$$P(x| y = 1) = \frac{1}{\sqrt{2 \pi \sigma_i}}e^{-\frac{(x-\mu_i)^2}{2\sigma^2_i}}$$


## Text Mining

### Multinomial Naive Bayes

This is mostly used for document multi-class problem, i.e whether a document belongs to the category of sports, politics, technology etc. The features/predictors used by the classifier are the **frequency** of the words present in the document. For example, in a sentence or a paragraph $x$, if there are $k$ distinct words and word-1 appears $x_1$ times, word-2 $x_2$ times,... etc, we will have

$$P(x|y) = \theta^{x_1}_1\theta^{x_2}_2 \cdots \theta^{x_k}_k,$$

where $θ_i$ is the ratio of `count(word-i, y)` and `count(y)` from corpus.


### Bernoulli Naive Bayes

If predictors are boolean variables and targets to predict are only yes or no, we can use Bernoulli distribution. For example, if a predictor is whether word-i occurs in the text or not and we want to predict positive/negative comments.

$$P(x|y) = \theta^{x_1}_1 (1-\theta_1)^{1-x_1} \cdots \theta^{x_k}_k (1-\theta_k)^{1-x_k}$$


## Pro and Con

The pro and con are listed below [[Zixuan Zhang]][Naive Bayes Explained]

### Pro
1. Even though the naive assumption is rarely true, the algorithm performs surprisingly good in many cases
2. Handles high dimensional data well. Easy to parallelize and handles big data well
3. Performs better than more complicated models when the data set is small

### Con
1. The estimated probability is often inaccurate because of the naive assumption. Not ideal for regression use or probability estimation
2. When data is abundant, other more complicated models tend to outperform Naive Bayes






## Reference



* [Naive Bayes Classifier]: https://towardsdatascience.com/naive-bayes-classifier-81d512f50a7c
[[Rohith Gandhi] Naive Bayes Classifier](https://towardsdatascience.com/naive-bayes-classifier-81d512f50a7c)
* [Naive Bayes Explained]: https://towardsdatascience.com/naive-bayes-explained-9d2b96f4a9c0
[[Zixuan Zhang] Naive Bayes Explained](https://towardsdatascience.com/naive-bayes-explained-9d2b96f4a9c0)




