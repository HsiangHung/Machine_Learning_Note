# Deal With Missing Data

Data imputation depends on the kind of problem  —  Time series Analysis, ML, Regression etc. and it is difficult to provide a general solution [[Alvira Swalin]][How to Handle Missing Data].

Note that imputation does not necessarily give better results, so we have to be really careful before removing observations. Without handling properly by the researcher, then he/she may end up drawing an inaccurate inference [[statisticssolutions.com]][Missing Values in Data].

Table of Contents:

* [1. Reasons For Missing Data](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/ML_fundamentals/Missing_Data#1-reasons-for-missing-data)
* [2. Handling Missing Values](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/ML_fundamentals/Missing_Data#2-handling-missing-values)



## 1. Reasons For Missing Data

Before jumping to the methods of data imputation, we have to understand the reason why data goes missing [[Alvira Swalin]][How to Handle Missing Data]:


1. **Missing at Random (MAR)**: In MAR, the missing values are not randomly distributed across observations but are distributed within one or more sub-samples.

2. **Missing Completely at Random (MCAR)**: This form exists when the missing values are randomly distributed across all observations.  This form can be confirmed by partitioning the data into two parts: one set containing the missing values, and the other containing the non missing values.  After partitioning the data, the most popular test, called the **t-test**, is carried out in order to check **whether there exists any difference in the sample between the two data-sets** [[statisticssolutions.com]][Missing Values in Data].


3. **Missing not at Random (MNAR)**: Two possible reasons are that the missing value depends on the hypothetical value (e.g. People with high salaries generally do not want to reveal their incomes in surveys) or missing value is dependent on some other variable’s value (e.g. Let’s assume that females generally don’t want to reveal their ages! Here the missing value in age variable is impacted by gender variable)

In the first two cases, it is safe to remove the data with missing values depending upon their occurrences, while in the third case removing observations with missing values can **produce bias** in the model.


## 2. Handling Missing Values

It is always better to keep data than to discard it. Sometimes you can drop variables if the data is missing for more than 60% observations but only if that variable is insignificant. Having said that, imputation is always a preferred choice over dropping variables.

### 2.A Deletion

The researcher may leave the data or do data imputation to replace the them.  Suppose the number of cases of missing values is extremely small; then, an expert researcher may drop or omit those values from the analysis.  In statistical language, if the number of the cases is less than 5% of the sample, then the researcher can drop them [[statisticssolutions.com]][Missing Values in Data].


In the case of multivariate analysis, if there is a larger number of missing values, then it can be better to drop those cases (rather than do imputation) and replace them.  On the other hand, in univariate analysis, imputation can decrease the amount of bias in the data, if the values are missing at random.

keep in mind that if the data are MCAR, then he may choose a pair-wise or a list-wise deletion of missing value cases.  If, however, the data are not MCAR, then imputation to replace them is conducted.

The researcher should keep in mind that if the data are MCAR, then he may choose a pair-wise or a list-wise deletion of missing value cases.  If, however, the data are not MCAR, then imputation to replace them is conducted.

#### Listwise


### 2.B Imputation

#### Mean, Median and Mode

Computing the overall mean, median or mode is a very basic imputation method, it is the only tested function that takes no advantage of the time series characteristics or relationship between the variables. It is very fast, but has clear disadvantages. One disadvantage is that mean imputation **reduces variance** in the dataset [[Alvira Swalin]][How to Handle Missing Data].


#### Linear Regression

To begin, several predictors of the variable with missing values are identified using a correlation matrix. The best predictors are selected and used as independent variables in a regression equation. The variable with missing data is used as the dependent variable. Cases with complete data for the predictor variables are used to generate the regression equation; the equation is then used to predict missing values for incomplete cases. 

In an **iterative process**, values for the missing variable are inserted and then all cases are used to predict the dependent variable. These steps are repeated **until** there is little difference between the predicted values from one step to the next, that is they **converge** [[Alvira Swalin]][How to Handle Missing Data].

It “theoretically” provides good estimates for missing values. However, there are several disadvantages of this model which tend to outweigh the advantages. First, because the replaced values were predicted from other variables they tend to fit together “too well” and so standard error is deflated. One must also assume that there is a linear relationship between the variables used in the regression equation when there may not be one.

### KNN (K Nearest Neighbors)

There are other machine learning techniques like XGBoost and Random Forest for data imputation but we will be discussing KNN as it is widely used. In this method, k neighbors are chosen based on some distance measure and their average is used as an imputation estimate. The method requires the selection of the number of nearest neighbors, and a distance metric. KNN can predict both discrete attributes (the most frequent value among the k nearest neighbors) and continuous attributes (the mean among the k nearest neighbors)
The distance metric varies according to the type of data:

1. Continuous Data: The commonly used distance metrics for continuous data are Euclidean, Manhattan and Cosine

2. Categorical Data: Hamming distance is generally used in this case. It takes all the categorical attributes and for each, count one if the value is not the same between two points. The Hamming distance is then equal to the number of attributes for which the value was different.
One of the most attractive features of the KNN algorithm is that it is simple to understand and easy to implement. The non-parametric nature of KNN gives it an edge in certain settings where the data may be highly “unusual”.
One of the obvious drawbacks of the KNN algorithm is that it becomes time-consuming when analyzing large datasets because it searches for similar instances through the entire dataset. Furthermore, the accuracy of KNN can be severely degraded with high-dimensional data because there is little difference between the nearest and farthest neighbor.



# Reference

* [How to Handle Missing Data]: https://towardsdatascience.com/how-to-handle-missing-data-8646b18db0d4
[[Alvira Swalin] How to Handle Missing Data](https://towardsdatascience.com/how-to-handle-missing-data-8646b18db0d4)
* [Missing Values in Data]: http://www.statisticssolutions.com/missing-values-in-data/
[[statisticssolutions.com] Missing Values in Data](http://www.statisticssolutions.com/missing-values-in-data/)

    
