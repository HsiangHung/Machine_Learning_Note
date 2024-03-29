
# Gradient Boosting Extension - MART


 Boosting is a method of converting weak learners into strong learners. 

The idea of boosting regression trees can be mapping to classification and ranking problems. It is called MART(Multiple Additive Regression Trees), where the output of the model is a linear combination of the outputs of a set of regression trees.

The following content follows Chris Burge's review paper: [From RankNet to LambdaRank to LambdaMART: An Overview](https://www.microsoft.com/en-us/research/uploads/prod/2016/02/MSR-TR-2010-82.pdf). The LambdaMART is particularly designed as MART + LambdaRank.

Here is Prof. Tomas Tunys' lecture slide: [LambdaMART Demystified](https://staff.fnwi.uva.nl/e.kanoulas/wp-content/uploads/Lecture-8-1-LambdaMart-Demystified.pdf).

## 1. Boosting regression

The procedures of building a boosting regression tree are summarize below (given (`x`, `y`))


* $\textrm{fit } f_0(x) = y; \ \hat{y}_0 = f_0(x), \ \hat{y}^{(0)} = \hat{y}_0 = f_0(x), \ \textrm{res} \epsilon_1 = y-\hat{y}^{(0)},$

* $\textrm{fit } f_1(x) = \epsilon_1; \ \hat{\epsilon}_1 = f_1(x), \ \hat{y}^{(1)} = \hat{y}_0 + \hat{\epsilon}_1 = f_0 +f_1, \ \textrm{res } \epsilon_2 = y-\hat{y}^{(1)},$

* $\textrm{fit } f_2(x) = \epsilon_2; \ \hat{y}^{(2)} = \hat{y}_0 + \hat{\epsilon}_1 + \hat{\epsilon}_2 = f_0 + f_1 + f_2, \ \textrm{res } \epsilon_3 = y-\hat{y}^{(2)},$

* $\cdots$

* $\hat{y}^{(n)} = \hat{y}^0 + \hat{\epsilon}_1 + \hat{\epsilon}_2 \cdots + \hat{\epsilon}_n = \hat{y}^{(n-1)} + f_n(x).$

As explained by Pulkit Bansal in the [Quora post](https://www.quora.com/What-is-an-intuitive-explanation-of-Gradient-Boosting), we are modeling $F_n = f_0 + f_1 + f_2  + .. + f_n$,  where each of these is a decision tree, and each new tree is a fit on a modified version of the original data set. 

The following picture also provide a good interpretation about the gradient boosting process:

![](images/golf.png)

where each tree $f_1$, $f_2$, .... provides approaching results toward to the true target. Below shows the idea: the collection of the trees forms an ensemble. Each boosting procedure generated a tree to correct prediction approaching toward to true target, such that the error is reducing: (credit from [[Aratrika Pal]][Gradient Boosting Trees for Classification: A Beginner’s Guide])

![](images/boosting_tree.png)



Note the cost function for regression is 

$$C = \frac{1}{2}(y - \hat{y})^2.$$

Therefore residuals is equivalent to finding the gradient of the cost function [[Cross Validated: Gradient in Gradient Boosting]][Gradient in Gradient Boosting]

$$y - \hat{y} = - \frac{\partial C}{\partial \hat{y}},$$

and responses in the boosting machine are updated as 

$$y \to y - \alpha \frac{\partial C}{\partial \hat{y}}.$$


## 2. MART for Binary Classification

For classification, this will be equal to **log(odds)** of the **dependent variable** (Similar to logisitic regreesion, which fits linear functions on log(odds)). In the following, we follow the discussion from [[Aratrika Pal]][Gradient Boosting Trees for Classification: A Beginner’s Guide].

Suppose we have the following dataset

| # | chest pain | good blood circulation | blocked arteries | heart disease|
| --- | --- | --- | --- | --- | 
| 1 |  No  |  No   |   No   |  No  |
| 2 |  Yes   |  Yes   |   Yes   |  Yes  |
| 3 |  Yes  |  Yes   |   No  |  Yes  |
| 4 |  Yes  |  No   |   No   |  Yes  |
| 5 |  Yes   |  No   |   Yes    |  Yes  |
| 6 |  No   |  Yes   |   No    |  No  |

### 2.1 Initial tree

The first tree is simply a classifier (tree) giving prediction by `log(odds)`. In the above dataset, there are 4 people with and 2 without heart disease, so `log(odds)` is equal to 

    log(odds) = log(p/1-p) = log(4/2) = 0.6931 ~ 0.7

Next, we convert this to a probability using the Logistic Function,

$$p = \frac{e^{\textrm{log(odds)}}}{1+e^{\textrm{log(odds)}}} = \frac{1}{1+e^{-\textrm{log(odds)}}} = 0.6667 \sim 0.7.$$

If we consider the probability threshold as 0.5, this means that our initial prediction is that all the individuals have Heart Disease.

Next we calculate the residuals for each observation by using the following formula,

     Residual = Actual value — Predicted value

where Actual value= 1 if the person has Heart Disease and 0 if not and Predicted value = 0.7,


| # | chest pain | good blood circulation | blocked arteries | heart disease| actual | 1st | residual |
| --- | --- | --- | --- | --- | --- | --- | --- | 
| 1 |  No  |  No   |   No   |  No  | 0 |  0.7 | -0.7 |
| 2 |  Yes   |  Yes   |   Yes   |  Yes  | 1 | 0.7 | 0.3 |
| 3 |  Yes  |  Yes   |   No  |  Yes  | 1 | 0.7 | 0.3 |
| 4 |  Yes  |  No   |   No   |  Yes  | 1 | 0.7 | 0.3 |
| 5 |  Yes   |  No   |   Yes    |  Yes  | 1 | 0.7 | 0.3 |
| 6 |  No   |  Yes   |   No    |  No  | 0 | 0.7 | -0.7 |


### 2.2 Second boosting tree

Next step is to build a Decision Tree to predict the residuals using Chest Pain, Good Blood Circulation and Blocked Arteries. Assumed we built the following sample tree (from [[Aratrika Pal]][Gradient Boosting Trees for Classification: A Beginner’s Guide]):

![](images/tree-1.png)


How do we calculate the predicted residuals in each leaf? The initial prediction was in terms of log(odds) and the leaves are derived from a probability. Hence, we need to do some transformation to get the predicted residuals in terms of log(odds). The most common transformation is done using the following formula 

$$\frac{\sum \textrm{Resisual}_i}{\sum (\textrm{PrevProb}_i) (1-\textrm{PrevProb}_i)}.$$


## Reference




* [Gradient Boosting Trees for Classification: A Beginner’s Guide]: https://medium.com/swlh/gradient-boosting-trees-for-classification-a-beginners-guide-596b594a14ea
[[Aratrika Pal] Gradient Boosting Trees for Classification: A Beginner’s Guide](https://medium.com/swlh/gradient-boosting-trees-for-classification-a-beginners-guide-596b594a14ea)


* [Gradient in Gradient Boosting]: https://stats.stackexchange.com/questions/338658/gradient-in-gradient-boosting/340376#340376
[[Cross Validated: Gradient in Gradient Boosting] Gradient in Gradient Boosting](https://stats.stackexchange.com/questions/338658/gradient-in-gradient-boosting/340376#340376)


* [Gradient Boosting In Classification: Not a Black Box Anymore!]: https://blog.paperspace.com/gradient-boosting-for-classification/
[[Vihar Kurama] Gradient Boosting In Classification: Not a Black Box Anymore!](https://blog.paperspace.com/gradient-boosting-for-classification/)









