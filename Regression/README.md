
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


Table of Contents:

* [1. Metric](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Regression#1-metric)
     * [1.A R-squared](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Regression#1a-r-squared)
     * [1.B Adjusted R-squared](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Regression#1b-adjusted-r-squared)
* [2. Linear Regression](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Regression#2-linear-regression)
     * [2.A Assumption for linear regression](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Regression#2a-assumption-for-linear-regression)
     * [2.B Maximum likelihood estimate](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Regression#2b-maximum-likelihood-estimate)
* [3. Multicollinearity](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Regression#3-multicollinearity)
     * [3.A How to test Multicollinearity?](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Regression#3a-how-to-test-multicollinearity)
     * [3.B How to deal with Multicollinearity](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Regression#3b-how-to-deal-with-multicollinearity)
* [4. Deep learning for regression](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Regression#4-deep-learning-for-regression)



## 1. Metric

A simple evaludation for regression models is MSE, mean saured errors. There are others:

### 1.A R-squared

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


### 1.B Adjusted R-squared

A major problem is that R-sqaured is related to the number of variables we add to our regression model. That is, even if we are adding redundant variables to the data, the value of R-squared does not decrease. This clearly does not make sense because some of the independent variables might not be useful in determining the target variable. 

The adjusted R-squared compares the descriptive power of regression models that include diverse numbers of predictors. [[Aniruddha Bhandari]][Analytics Vidhya: Key Difference between R-squared and Adjusted R-squared for Regression Analysis]:

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{Adjusted&space;R}^2&space;=&space;1-&space;\frac{(1-R^2)(n-1)}{(m-p-1)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{Adjusted&space;R}^2&space;=&space;1-&space;\frac{(1-R^2)(n-1)}{(m-p-1)}" title="\textrm{Adjusted R}^2 = 1- \frac{(1-R^2)(n-1)}{(m-p-1)}" /></a>

Thus, if R-squared does not increase significantly on the addition of a new independent variable (higher `p`), then `1/(m-p-1)` increases and Adjusted R-squared will actually decrease.

On the other hand, if on adding the new independent variable we see a significant increase in R-squared value, then the Adjusted R-squared value will also increase.


## 2. Linear Regression

The linear regression has a generic form

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{y}&space;=&space;\theta_0&space;&plus;&space;\theta_1&space;x_1&space;&plus;&space;\theta_2&space;x_2&space;&plus;\cdots&space;&plus;&space;\epsilon&space;=&space;\bold{x}&space;\theta&space;&plus;&space;\epsilon" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{y}&space;=&space;\theta_0&space;&plus;&space;\theta_1&space;x_1&space;&plus;&space;\theta_2&space;x_2&space;&plus;\cdots&space;&plus;&space;\epsilon&space;=&space;\bold{x}&space;\theta&space;&plus;&space;\epsilon" title="\hat{y} = \theta_0 + \theta_1 x_1 + \theta_2 x_2 +\cdots + \epsilon = \bold{x} \theta + \epsilon" /></a>


### 2.A Assumption for linear regression

There are four assumptions associated with a linear regression model [[BUMC]][Simple Linear Regression]:

* **Independence**: Observations are independent of each other.

* **Linearity**: The relationship between X and the mean of Y is linear. Look for **residual vs fitted value** plots. To fix this, you can include polynomial terms (`X`, `X^2`, `X^3`) or interaction terms in your model to capture the non-linear effect.

![](images/non_linear_effect.png)


* **Homoscedasticity**: The variance of residual is the same for any value of X, i.e. error terms must have constant variance.

* **Normality**: For any fixed value of X, Y is normally distributed.


### 2.B Maximum likelihood estimate

Given a model `θ`, the likelihood of having a data point `(xi, yi)` is a normal distribution as

<a href="https://www.codecogs.com/eqnedit.php?latex=P(\bold{x}_i,&space;y_i|\theta)&space;\propto&space;e^{-(y_i-\hat{y}_i)^2/2\sigma^2}&space;=&space;e^{-(y_i-\bold{\theta}^T&space;\bold{x}_i)^2/2\sigma^2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(\bold{x}_i,&space;y_i|\theta)&space;\propto&space;e^{-(y_i-\hat{y}_i)^2/2\sigma^2}&space;=&space;e^{-(y_i-\bold{\theta}^T&space;\bold{x}_i)^2/2\sigma^2}" title="P(\bold{x}_i, y_i|\theta) \propto e^{-(y_i-\hat{y}_i)^2/2\sigma^2} = e^{-(y_i-\bold{\theta}^T \bold{x}_i)^2/2\sigma^2}" /></a>

Thus the total likelihood of having the entire dataset `D={(x1, y1), (x2, y2),..}` is

<a href="https://www.codecogs.com/eqnedit.php?latex=L(\bold{\theta})&space;=&space;P(\bold{D}|\theta)&space;=&space;\prod^n_{i=1}&space;\frac{1}{\sqrt{2&space;\pi&space;\sigma^2}}e^{-\frac{(y_i&space;-\bold{\theta}^T&space;\bold{x}_i)^2}{2\sigma^2}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?L(\bold{\theta})&space;=&space;P(\bold{D}|\theta)&space;=&space;\prod^n_{i=1}&space;\frac{1}{\sqrt{2&space;\pi&space;\sigma^2}}e^{-\frac{(y_i&space;-\bold{\theta}^T&space;\bold{x}_i)^2}{2\sigma^2}}" title="L(\bold{\theta}) = P(\bold{D}|\theta) = \prod^n_{i=1} \frac{1}{\sqrt{2 \pi \sigma^2}}e^{-\frac{(y_i -\bold{\theta}^T \bold{x}_i)^2}{2\sigma^2}}" /></a>

The following is the picture, credit from Prof. Nando de Freitas's UBC Machine learning class. For each x, the likelihood of having y is described normal distribution, and the mean value is the linear fit:

![](images/gaussian_likelihood.png)


## 3. Multicollinearity


Multicollinearity causes the following two basic types of problems:

1. The coefficient estimates can swing wildly based on which other independent variables are in the model. The coefficients become very sensitive to small changes in the model.
2. Multicollinearity reduces the precision of the estimate coefficients, which weakens the statistical power of your regression model. You might not be able to trust the p-values to identify independent variables that are statistically significant.


Severe multicollinearity is a major problem, because it increases the variance of the regression coefficients, making them unstable. The more variance they have, the **more difficult it is to interpret the coefficients**.

### 3.A How to test Multicollinearity?

1. Correlation matrix / Correlation plot
2. Variation Inflation Factor (VIF): identifies correlation between independent variables and the strength of that correlation. 

The VIF for the `j`-th predictor is [[Penn stat: STAT 462 - Applied Regression Analysis]][10.7 - Detecting Multicollinearity Using Variance Inflation Factors]:

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{VIF}_j&space;=&space;\frac{1}{1-R^2_j}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{VIF}_j&space;=&space;\frac{1}{1-R^2_j}" title="\textrm{VIF}_j = \frac{1}{1-R^2_j}" /></a>

where <a href="https://www.codecogs.com/eqnedit.php?latex=R^2_j" target="_blank"><img src="https://latex.codecogs.com/gif.latex?R^2_j" title="R^2_j" /></a> is the R-sqaured value obtained by regressing the `j`-th predictor on the remaining predictors.

* VIF = 1 → No correlation
* VIF = 1 to 5 Moderate correlation
* VIF >10 → High correlation

### 3.B How to deal with Multicollinearity

* **Remove highly correlated predictors from the model**: If you have two or more factors with a high VIF, remove one from the model. Consider using stepwise regression, best subsets regression, or specialized knowledge of the data set to remove these variables. Select the model that has the highest R-squared value [[Minitab Blog]][Enough Is Enough! Handling Multicollinearity in Regression Analysis]. 

* **combine variables**: Use Partial Least Squares Regression (PLS) or **Principal Components Analysis**, regression methods that cut the number of predictors to a smaller set of uncorrelated components [[Minitab Blog]][Enough Is Enough! Handling Multicollinearity in Regression Analysis], [[Sushmitha Pulagam]][How to detect and deal with Multicollinearity].

Some notes by [[Jim Frost]][Multicollinearity in Regression Analysis: Problems, Detection, and Solutions]:

1. The severity of the problems increases with the degree of the multicollinearity. Therefore, if you have only moderate multicollinearity, you may not need to resolve it.
2. Multicollinearity affects only the specific independent variables that are correlated. Therefore, if multicollinearity is not present for the independent variables that you are particularly interested in, you may not need to resolve it. Suppose your model contains the experimental variables of interest and some control variables. If high multicollinearity exists for the control variables but not the experimental variables, then you can interpret the experimental variables without problems.
3. Multicollinearity affects the coefficients and p-values, but it does not influence the predictions, precision of the predictions, and the goodness-of-fit statistics. **If your primary goal is to make predictions, and you don’t need to understand the role of each independent variable, you don’t need to reduce severe multicollinearity**.



## 4. Deep learning for regression

California house price prediction from Kaggle:

1. [House-Price-Prediction-Regression-with-Tensorflow-Keras-](https://github.com/Harshita9511/House-Price-Prediction-Regression-with-Tensorflow-Keras-/blob/master/Housing_Price_Prediction_(Regression)_with_Tensorflow_Keras.ipynb)
2. [Kaggle-California-Housing-Prices](https://github.com/mohitgupta-omg/Kaggle-California-Housing-Prices/blob/master/k%20California%20Housing%20Prices.ipynb)





## Reference




[Analytics Vidhya: Key Difference between R-squared and Adjusted R-squared for Regression Analysis]: https://www.analyticsvidhya.com/blog/2020/07/difference-between-r-squared-and-adjusted-r-squared/
[[Aniruddha Bhandari] Analytics Vidhya: Key Difference between R-squared and Adjusted R-squared for Regression Analysis](https://www.analyticsvidhya.com/blog/2020/07/difference-between-r-squared-and-adjusted-r-squared/)


[QSimple Linear Regression]: https://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/R/R5_Correlation-Regression/R5_Correlation-Regression4.html
[[BUMC] Simple Linear Regression](https://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/R/R5_Correlation-Regression/R5_Correlation-Regression4.html)


[Multicollinearity in Regression Analysis: Problems, Detection, and Solutions]: https://statisticsbyjim.com/regression/multicollinearity-in-regression-analysis/
[[Jim Frost] Multicollinearity in Regression Analysis: Problems, Detection, and Solutions](https://statisticsbyjim.com/regression/multicollinearity-in-regression-analysis/)


[Enough Is Enough! Handling Multicollinearity in Regression Analysis]: https://blog.minitab.com/en/understanding-statistics/handling-multicollinearity-in-regression-analysis
[[Minitab Blog] Enough Is Enough! Handling Multicollinearity in Regression Analysis](https://blog.minitab.com/en/understanding-statistics/handling-multicollinearity-in-regression-analysis)


[10.7 - Detecting Multicollinearity Using Variance Inflation Factors]: https://online.stat.psu.edu/stat462/node/180/
[[Penn stat: STAT 462 - Applied Regression Analysis] 10.7 - Detecting Multicollinearity Using Variance Inflation Factors](https://online.stat.psu.edu/stat462/node/180/)


[Quroa: What is the difference between R-squared and Adjusted R-squared?]: https://www.quora.com/What-is-the-difference-between-R-squared-and-Adjusted-R-squared
[[Quora: What is the difference between R-squared and Adjusted R-squared?] Quora: What is the difference between R-squared and Adjusted R-squared?](https://www.quora.com/What-is-the-difference-between-R-squared-and-Adjusted-R-squared)


[How to detect and deal with Multicollinearity]: https://towardsdatascience.com/how-to-detect-and-deal-with-multicollinearity-9e02b18695f1
[[Sushmitha Pulagam] How to detect and deal with Multicollinearity](https://towardsdatascience.com/how-to-detect-and-deal-with-multicollinearity-9e02b18695f1)




