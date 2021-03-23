
# Regression 

Regression is to models when the target variable `y` is numeric, continuous

```
y = f(x)
```


Assume `m` is the number of data points, the cost function reads

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{C}&space;=&space;\sum^m_{i=1}&space;(y_i&space;-&space;\hat{y}_i)^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{C}&space;=&space;\sum^m_{i=1}&space;(y_i&space;-&space;\hat{y}_i)^2" title="\textrm{C} = \sum^m_{i=1} (y_i - \hat{y}_i)^2" /></a>

where <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{y}_i&space;=&space;\bold{x}_i&space;\theta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{y}_i&space;=&space;\bold{x}_i&space;\theta" title="\hat{y}_i = \bold{x}_i \theta" /></a> is the predicted value, and residuals are defined as the difference between the actual value `y` and the predicted value:

<a href="https://www.codecogs.com/eqnedit.php?latex=e_i&space;=&space;\hat{y}_i&space;-&space;y_i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e_i&space;=&space;\hat{y}_i&space;-&space;y_i" title="e_i = \hat{y}_i - y_i" /></a>

The optimization objective is to minimize the cost function. 


## Metric

A simple evaludation for regression models is MSE, mean saured errors. There are others:

#### R-squared

R-squared statistic or coefficient of determination is a scale invariant statistic that gives the proportion of variation in target variable explained by the linear regression model. [[Aniruddha Bhandari]][Analytics Vidhya: Key Difference between R-squared and Adjusted R-squared for Regression Analysis]

For R-sqaured, we need RSS and TSS. **Residual sum of squares (RSS)** is equal to the cost function:

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{RSS}&space;=&space;\sum_i&space;(y_i&space;-&space;\hat{y}_i)^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{RSS}&space;=&space;\sum_i&space;(y_i&space;-&space;\hat{y}_i)^2" title="\textrm{RSS} = \sum_i (y_i - \hat{y}_i)^2" /></a>

The lower the value of RSS, the better is the model predictions. **Total Sum of Squares (TSS)** is 

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{TSS}&space;=&space;\sum_i&space;(y_i&space;-&space;\bar{y})^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{TSS}&space;=&space;\sum_i&space;(y_i&space;-&space;\bar{y})^2" title="\textrm{TSS} = \sum_i (y_i - \bar{y})^2" /></a>

TSS or Total sum of squares gives the total variation in target variable `y`.

TSS-RSS gives us how much variation in `y` is explained by our model. R-squared is the ratio with repect to total variance explained by model:

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{R-sqaured}&space;=&space;\frac{\textrm{TSS-RSS}}{\textrm{TSS}}&space;=&space;1-&space;\frac{\textrm{RSS}}{\textrm{TSS}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{R-sqaured}&space;=&space;\frac{\textrm{TSS-RSS}}{\textrm{TSS}}&space;=&space;1-&space;\frac{\textrm{RSS}}{\textrm{TSS}}" title="\textrm{R-sqaured} = \frac{\textrm{TSS-RSS}}{\textrm{TSS}} = 1- \frac{\textrm{RSS}}{\textrm{TSS}}" /></a>

`RSS/TSS` is the variance in `y` **NOT** explained by the model.

0 <= R-squared <= 1. If this value is 0.7, it means that the independent variables explain 70% of the variation in the target variable. A higher R-squared value indicates a higher amount of variability being explained by our model and vice-versa: a better model, lower RSS value, higher R-sqaured values.


#### Adjusted R-squared

A major problem is that R-sqaured is related to the number of variables we add to our regression model. That is, even if we are adding redundant variables to the data, the value of R-squared does not decrease. This clearly does not make sense because some of the independent variables might not be useful in determining the target variable. 

The adjusted R-squared compares the descriptive power of regression models that include diverse numbers of predictors. [[Aniruddha Bhandari]][Analytics Vidhya: Key Difference between R-squared and Adjusted R-squared for Regression Analysis]:

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{Adjusted&space;R}^2&space;=&space;1-&space;\frac{(1-R^2)(n-1)}{(m-p-1)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{Adjusted&space;R}^2&space;=&space;1-&space;\frac{(1-R^2)(n-1)}{(m-p-1)}" title="\textrm{Adjusted R}^2 = 1- \frac{(1-R^2)(n-1)}{(m-p-1)}" /></a>

Thus, if R-squared does not increase significantly on the addition of a new independent variable (higher `p`), then `1/(m-p-1)` increases and Adjusted R-squared will actually decrease.

On the other hand, if on adding the new independent variable we see a significant increase in R-squared value, then the Adjusted R-squared value will also increase.


## Linear Regression

The linear regression has a generic form

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{y}&space;=&space;\theta_0&space;&plus;&space;\theta_1&space;x_1&space;&plus;&space;\theta_2&space;x_2&space;&plus;\cdots&space;&plus;&space;\epsilon&space;=&space;\bold{x}&space;\theta&space;&plus;&space;\epsilon" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{y}&space;=&space;\theta_0&space;&plus;&space;\theta_1&space;x_1&space;&plus;&space;\theta_2&space;x_2&space;&plus;\cdots&space;&plus;&space;\epsilon&space;=&space;\bold{x}&space;\theta&space;&plus;&space;\epsilon" title="\hat{y} = \theta_0 + \theta_1 x_1 + \theta_2 x_2 +\cdots + \epsilon = \bold{x} \theta + \epsilon" /></a>


### Assumption 

There are four assumptions associated with a linear regression model [[BUMC]][Simple Linear Regression]:

* **Independence**: Observations are independent of each other.

* **Linearity**: The relationship between X and the mean of Y is linear. Look for **residual vs fitted value** plots. To fix this, you can include polynomial terms (`X`, `X^2`, `X^3`) or interaction terms in your model to capture the non-linear effect.

![](images/non_linear_effect.png)


* **Homoscedasticity**: The variance of residual is the same for any value of X, i.e. error terms must have constant variance.

* **Normality**: For any fixed value of X, Y is normally distributed.


### Maximum Likelihood Estimate

Given a model and a data point `(xi, yi)`, the likelihood is

<a href="https://www.codecogs.com/eqnedit.php?latex=P(\bold{x}_i,&space;y_i|\theta)&space;\sim&space;\exp{\frac{(y_i-\bold{\theta}^T&space;\bold{x}_i)^2}{2\sigma^2}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(\bold{x}_i,&space;y_i|\theta)&space;\sim&space;\exp{\frac{(y_i-\bold{\theta}^T&space;\bold{x}_i)^2}{2\sigma^2}}" title="P(\bold{x}_i, y_i|\theta) \sim \exp{\frac{(y_i-\bold{\theta}^T \bold{x}_i)^2}{2\sigma^2}}" /></a>

Thus the total likelidhood for entire data set `D` is

<a href="https://www.codecogs.com/eqnedit.php?latex=L(\bold{\theta})&space;=&space;P(\bold{X}|\theta)&space;=&space;\prod^n_{i=1}&space;\frac{1}{\sqrt{2&space;\pi&space;\sigma^2}}e^{-\frac{(y_i&space;-\bold{\theta}^T&space;\bold{x}_i)^2}{2\sigma^2}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?L(\bold{\theta})&space;=&space;P(\bold{X}|\theta)&space;=&space;\prod^n_{i=1}&space;\frac{1}{\sqrt{2&space;\pi&space;\sigma^2}}e^{-\frac{(y_i&space;-\bold{\theta}^T&space;\bold{x}_i)^2}{2\sigma^2}}" title="L(\bold{\theta}) = P(\bold{X}|\theta) = \prod^n_{i=1} \frac{1}{\sqrt{2 \pi \sigma^2}}e^{-\frac{(y_i -\bold{\theta}^T \bold{x}_i)^2}{2\sigma^2}}" /></a>


![](images/gaussian_likelihood.png)

















## Reference







[Analytics Vidhya: Key Difference between R-squared and Adjusted R-squared for Regression Analysis]: https://www.analyticsvidhya.com/blog/2020/07/difference-between-r-squared-and-adjusted-r-squared/
[[Aniruddha Bhandari] Analytics Vidhya: Key Difference between R-squared and Adjusted R-squared for Regression Analysis](https://www.analyticsvidhya.com/blog/2020/07/difference-between-r-squared-and-adjusted-r-squared/)


[QSimple Linear Regression]: https://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/R/R5_Correlation-Regression/R5_Correlation-Regression4.html
[[BUMC] Simple Linear Regression](https://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/R/R5_Correlation-Regression/R5_Correlation-Regression4.html)


[Quroa: What is the difference between R-squared and Adjusted R-squared?]: https://www.quora.com/What-is-the-difference-between-R-squared-and-Adjusted-R-squared
[[Quora: What is the difference between R-squared and Adjusted R-squared?] Quora: What is the difference between R-squared and Adjusted R-squared?](https://www.quora.com/What-is-the-difference-between-R-squared-and-Adjusted-R-squared)


