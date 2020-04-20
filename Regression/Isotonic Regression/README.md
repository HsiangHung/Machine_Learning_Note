


# Isotonic Regression

In machine learning, we train a classifier to predict, `p(y=1|X)`, the probability of an event being positive, given data `X`. In reality, however, the probability may be deviated away from true positive probability. To make the probability more meaningful, we can calibrate the probability. In general there are two approaches Platt's scaling and isotonic regression [[FastML]][Classifier calibration with Platt's scaling and isotonic regression]. Here we focus on the later. 

The idea for isotonic regression is to fit a piecewise-constant non-decreasing function instead of logistic regression. Piecewise-constant non-decreasing means stair-step shaped. Here is an example:

![ir_plot](images/isotonic_regression_plot.png)


1. Missing at Random (MAR): In MAR, the missing values are not randomly distributed across observations but are distributed within one or more sub-samples.

2. Missing Completely at Random (MCAR): This form exists when the missing values are randomly distributed across all observations.  This form can be confirmed by partitioning the data into two parts: one set containing the missing values, and the other containing the non missing values.  After partitioning the data, the most popular test, called the **t-test**, is carried out in order to check **whether there exists any difference in the sample between the two data-sets** [[2]][Missing Values in Data].


3. Missing not at Random (MNAR): Two possible reasons are that the missing value depends on the hypothetical value (e.g. People with high salaries generally do not want to reveal their incomes in surveys) or missing value is dependent on some other variable’s value (e.g. Let’s assume that females generally don’t want to reveal their ages! Here the missing value in age variable is impacted by gender variable)

In the first two cases, it is safe to remove the data with missing values depending upon their occurrences, while in the third case removing observations with missing values can **produce bias** in the model.









# Reference

[Classifier calibration with Platt's scaling and isotonic regression]: http://fastml.com/classifier-calibration-with-platts-scaling-and-isotonic-regression/
[[FastML] Classifier calibration with Platt's scaling and isotonic regression](http://fastml.com/classifier-calibration-with-platts-scaling-and-isotonic-regression/)


[Missing Values in Data]: http://www.statisticssolutions.com/missing-values-in-data/
[[2] Missing Values in Data](http://www.statisticssolutions.com/missing-values-in-data/)

    
