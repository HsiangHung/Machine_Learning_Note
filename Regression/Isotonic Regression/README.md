


# Isotonic Regression

In classification problems, a classifier is trained to predict the probability of finding a positive event, denoted as `p(y=1|X)`, given data `X`. In reality, however, the predictive probability may not align with the true positive probability, `p(X)`, defined as (number of positive events)/(number of events). To make the predictive probability more informational, we can perform probability calibration, building the map: `p(y=1|X) -> p(X)`. In general there are two approaches: Platt's scaling and isotonic regression [[FastML]][Classifier calibration with Platt's scaling and isotonic regression]. Here we only focus on the later. 

The idea for the isotonic regression model is to fit a piecewise-constant **non-decreasing** function instead of logistic regression. Piecewise-constant non-decreasing means stair-step shaped. Here is a regression example (credit from sklearn):

![ir_plot](images/isotonic_regression_plot.png)

We can see that linear regression just gives the above data in a linear fit. However, the isotonic regression shows a better fit for the monotonic relationship. 

For classification, we show another example of usage of isotonic regression (credit from [sklearn: Probability Calibration curves](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html#sphx-glr-auto-examples-calibration-plot-calibration-curve-py)):

![probability_calibration_plot](images/probability_calibration_curve.png)

This example describes predictive probability (x-axis) vs true positive probability (y-axis). The model linear support-vector classifier (SVC) gives predictive probabilities, but they overestimate at beginning and then underestimate. We can see at `p(y=1|X) = 0.4`, `p(X) ~ 0.1`, and at `p(y=1|X) = 0.8`, `p(X) ~ 1`. 


2. Missing Completely at Random (MCAR): This form exists when the missing values are randomly distributed across all observations.  This form can be confirmed by partitioning the data into two parts: one set containing the missing values, and the other containing the non missing values.  After partitioning the data, the most popular test, called the **t-test**, is carried out in order to check **whether there exists any difference in the sample between the two data-sets** [[2]][Missing Values in Data].


3. Missing not at Random (MNAR): Two possible reasons are that the missing value depends on the hypothetical value (e.g. People with high salaries generally do not want to reveal their incomes in surveys) or missing value is dependent on some other variable’s value (e.g. Let’s assume that females generally don’t want to reveal their ages! Here the missing value in age variable is impacted by gender variable)

In the first two cases, it is safe to remove the data with missing values depending upon their occurrences, while in the third case removing observations with missing values can **produce bias** in the model.









# Reference

[Classifier calibration with Platt's scaling and isotonic regression]: http://fastml.com/classifier-calibration-with-platts-scaling-and-isotonic-regression/
[[FastML] Classifier calibration with Platt's scaling and isotonic regression](http://fastml.com/classifier-calibration-with-platts-scaling-and-isotonic-regression/)


[Missing Values in Data]: http://www.statisticssolutions.com/missing-values-in-data/
[[2] Missing Values in Data](http://www.statisticssolutions.com/missing-values-in-data/)

    
