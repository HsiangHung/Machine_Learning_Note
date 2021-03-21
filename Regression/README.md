
# Regression 

Regression is to models when the target variable `y` is numeric, continuous

```
y = f(x)
```


Assume `m` is the number of data points, the cost function reads

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{C}&space;=&space;\sum^m_{i=1}&space;(y_i&space;-&space;\hat{y}_i)^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{C}&space;=&space;\sum^m_{i=1}&space;(y_i&space;-&space;\hat{y}_i)^2" title="\textrm{C} = \sum^m_{i=1} (y_i - \hat{y}_i)^2" /></a>

where <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{y}_i&space;=&space;\bold{x}_i&space;\theta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{y}_i&space;=&space;\bold{x}_i&space;\theta" title="\hat{y}_i = \bold{x}_i \theta" /></a> is the predicted value, and residuals are defined as the difference between the actual value and the value predicted by our linear regression model:

<a href="https://www.codecogs.com/eqnedit.php?latex=e_i&space;=&space;\hat{y}_i&space;-&space;y_i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e_i&space;=&space;\hat{y}_i&space;-&space;y_i" title="e_i = \hat{y}_i - y_i" /></a>

**Residual sum of squares** or **RSS** is equal to the cost function.

The lower the value of RSS, the better is the model predictions. The optimization objective is to minimize the cost function (RSS). 

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{RSS}&space;=&space;\sum_i&space;(y_i&space;-&space;\hat{y}_i)^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{RSS}&space;=&space;\sum_i&space;(y_i&space;-&space;\hat{y}_i)^2" title="\textrm{RSS} = \sum_i (y_i - \hat{y}_i)^2" /></a>

## Metric

A simple evaludation for regression models is MSE, mean saured errors.

#### R-squared

R-squared statistic or coefficient of determination is a scale invariant statistic that gives the proportion of variation in target variable explained by the linear regression model. [[Aniruddha Bhandari]][Analytics Vidhya: Key Difference between R-squared and Adjusted R-squared for Regression Analysis]

Total Sum of Squares is 

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{TSS}&space;=&space;\sum_i&space;(y_i&space;-&space;\bar{y})^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{TSS}&space;=&space;\sum_i&space;(y_i&space;-&space;\bar{y})^2" title="\textrm{TSS} = \sum_i (y_i - \bar{y})^2" /></a>

TSS or Total sum of squares gives the total variation in target variable `y`.

TSS-RSS gives us how much variation in `y` is explained by our model. R-squared is the ratio with repect to total variance explained by model:

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{R-sqaured}&space;=&space;\frac{\textrm{TSS-RSS}}{\textrm{TSS}}&space;=&space;1-&space;\frac{\textrm{RSS}}{\textrm{TSS}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{R-sqaured}&space;=&space;\frac{\textrm{TSS-RSS}}{\textrm{TSS}}&space;=&space;1-&space;\frac{\textrm{RSS}}{\textrm{TSS}}" title="\textrm{R-sqaured} = \frac{\textrm{TSS-RSS}}{\textrm{TSS}} = 1- \frac{\textrm{RSS}}{\textrm{TSS}}" /></a>

`RSS/TSS` is the variance in `y` **NOT** explained by the model.

R-squared value always lies between 0 and 1. If this value is 0.7, then it means that the independent variables explain 70% of the variation in the target variable. A higher R-squared value indicates a higher amount of variability being explained by our model and vice-versa: a better model, lower RSS value, higher R-sqaured values.


#### Adjusted R-squared

A major problem is that R-sqaured is related to the number of variables we add to our regression model. That is, even if we are adding redundant variables to the data, the value of R-squared does not decrease. This clearly does not make sense because some of the independent variables might not be useful in determining the target variable. 

Adjusted R-squared deals with this issue [[Aniruddha Bhandari]][Analytics Vidhya: Key Difference between R-squared and Adjusted R-squared for Regression Analysis]:

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{Adjusted&space;R}^2&space;=&space;1-&space;\frac{(1-R^2)(n-1)}{(m-p-1)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{Adjusted&space;R}^2&space;=&space;1-&space;\frac{(1-R^2)(n-1)}{(m-p-1)}" title="\textrm{Adjusted R}^2 = 1- \frac{(1-R^2)(n-1)}{(m-p-1)}" /></a>



## Linear Regression

The linear regression has a generic form

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{y}&space;=&space;\theta_0&space;&plus;&space;\theta_1&space;x_1&space;&plus;&space;\theta_2&space;x_2&space;&plus;\cdots&space;&plus;&space;\epsilon&space;=&space;\bold{x}&space;\theta&space;&plus;&space;\epsilon" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{y}&space;=&space;\theta_0&space;&plus;&space;\theta_1&space;x_1&space;&plus;&space;\theta_2&space;x_2&space;&plus;\cdots&space;&plus;&space;\epsilon&space;=&space;\bold{x}&space;\theta&space;&plus;&space;\epsilon" title="\hat{y} = \theta_0 + \theta_1 x_1 + \theta_2 x_2 +\cdots + \epsilon = \bold{x} \theta + \epsilon" /></a>


## Assumption 


## Maximum Likelihood Estimate








#### b. If no business concern

If there is no external business concern about low TPR or high FPR, one option is to weight them equally by choosing the threshold: (a) is a `median value` of probability distribution, (2) maximizes `TPR-FPR`, (3) has optimal `F1 score` [[Cross Validated: How to determine the optimal threshold for a classifier and generate ROC curve?]][How to determine the optimal threshold for a classifier and generate ROC curve?]: 

 <a href="https://www.codecogs.com/eqnedit.php?latex=F_1&space;=&space;\frac{2\textrm{P}\textrm{R}}{\textrm{P}&plus;\textrm{R}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F_1&space;=&space;\frac{2\textrm{P}\textrm{R}}{\textrm{P}&plus;\textrm{R}}" title="F_1 = \frac{2\textrm{P}\textrm{R}}{\textrm{P}+\textrm{R}}" /></a>

where P = Precision and R = Recall.



![](images/ROC_PR_model_comparison.png)





## Loss Function: Cross-Entropy


The cross-entropy of the generic form given a data record is 

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{Cross-Entropy}&space;=&space;-\sum_c&space;p_c&space;\log&space;q_c" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{Cross-Entropy}&space;=&space;-\sum_c&space;p_c&space;\log&space;q_c" title="\textrm{Cross-Entropy} = -\sum_c p_c \log q_c" /></a>

where `c` denotes class labels. `p` is the probability of target having class = c, and `q` is the probability of prediction as class = c. In classification, cross-entropy is used to be loss to optimize.

The cross-entropy can be used as loss to optimize using gradient descent in classification.






## Reference







[Analytics Vidhya: Key Difference between R-squared and Adjusted R-squared for Regression Analysis]: https://www.analyticsvidhya.com/blog/2020/07/difference-between-r-squared-and-adjusted-r-squared/
[[Aniruddha Bhandari] Analytics Vidhya: Key Difference between R-squared and Adjusted R-squared for Regression Analysis](https://www.analyticsvidhya.com/blog/2020/07/difference-between-r-squared-and-adjusted-r-squared/)


