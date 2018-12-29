# Deal With Missing Data

Data imputation depends on the kind of problem  —  Time series Analysis, ML, Regression etc. and it is difficult to provide a general solution [[1]][How to Handle Missing Data].

Note that imputation does not necessarily give better results, so we have to be really careful before removing observations. Without handling properly by the researcher, then he/she may end up drawing an inaccurate inference [[2]][Missing Values in Data].


# Reasons why data goes missing

Before jumping to the methods of data imputation, we have to understand the reason why data goes missing [[1]][How to Handle Missing Data]:


1. Missing at Random (MAR): In MAR, the missing values are not randomly distributed across observations but are distributed within one or more sub-samples.

2. Missing Completely at Random (MCAR): This form exists when the missing values are randomly distributed across all observations.  This form can be confirmed by partitioning the data into two parts: one set containing the missing values, and the other containing the non missing values.  After partitioning the data, the most popular test, called the **t-test**, is carried out in order to check **whether there exists any difference in the sample between the two data-sets** [[2]][Missing Values in Data].


3. Missing not at Random (MNAR): Two possible reasons are that the missing value depends on the hypothetical value (e.g. People with high salaries generally do not want to reveal their incomes in surveys) or missing value is dependent on some other variable’s value (e.g. Let’s assume that females generally don’t want to reveal their ages! Here the missing value in age variable is impacted by gender variable)

In the first two cases, it is safe to remove the data with missing values depending upon their occurrences, while in the third case removing observations with missing values can **produce bias** in the model.


# Handling Missing Values

## Deletion

The researcher may leave the data or do data imputation to replace the them.  Suppose the number of cases of missing values is extremely small; then, an expert researcher may drop or omit those values from the analysis.  In statistical language, if the number of the cases is less than 5% of the sample, then the researcher can drop them [[2]][Missing Values in Data].


In the case of multivariate analysis, if there is a larger number of missing values, then it can be better to drop those cases (rather than do imputation) and replace them.  On the other hand, in univariate analysis, imputation can decrease the amount of bias in the data, if the values are missing at random.

keep in mind that if the data are MCAR, then he may choose a pair-wise or a list-wise deletion of missing value cases.  If, however, the data are not MCAR, then imputation to replace them is conducted.

The researcher should keep in mind that if the data are MCAR, then he may choose a pair-wise or a list-wise deletion of missing value cases.  If, however, the data are not MCAR, then imputation to replace them is conducted.

### Listwise






# Reference

[How to Handle Missing Data]: https://towardsdatascience.com/how-to-handle-missing-data-8646b18db0d4
[[1] How to Handle Missing Data](https://towardsdatascience.com/how-to-handle-missing-data-8646b18db0d4)


[Missing Values in Data]: http://www.statisticssolutions.com/missing-values-in-data/
[[2] Missing Values in Data](http://www.statisticssolutions.com/missing-values-in-data/)

    
