


# Isotonic Regression

In classification problems, a classifier is trained to predict the probability of finding a positive event, denoted as `p(y=1|X)`, given data `X`. In reality, however, the predictive probability may not align with the true positive probability, `p(X)`, defined as (number of positive events)/(number of events). To make the predictive probability more informational, we can perform probability calibration, building the map: `p(y=1|X) -> p(X)`. In general there are two approaches: Platt's scaling and isotonic regression [[FastML]][Classifier calibration with Platt's scaling and isotonic regression]. Here we only focus on the later. 

The idea for the isotonic regression model is to fit a piecewise-constant **non-decreasing** function instead of logistic regression. Piecewise-constant non-decreasing means stair-step shaped. Here is a regression example (credit from sklearn):

![ir_plot](images/isotonic_regression_plot.png)

We can see that linear regression just gives the above data in a linear fit. However, the isotonic regression shows a better fit for the monotonic relationship. 

For classification, we show another example of usage of isotonic regression (credit from [sklearn: Probability Calibration curves](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html#sphx-glr-auto-examples-calibration-plot-calibration-curve-py)):

![probability_calibration_plot](images/probability_calibration_curve.png)

This example describes predictive probability (x-axis) vs true positive probability (y-axis). The model linear support-vector classifier (SVC) gives predictive probabilities, but they overestimate at beginning and then underestimate. We can see at `p(y=1|X) = 0.4`, `p(X) ~ 0.1`, and at `p(y=1|X) = 0.8`, `p(X) ~ 1`. 










# Reference


[Isotonic Regression is THE Coolest Machine-Learning Model You Might Not Have Heard Of]: https://towardsdatascience.com/isotonic-regression-is-the-coolest-machine-learning-model-you-might-not-have-heard-of-3ce14afc6d1e
[[Emmett Boudreau] Isotonic Regression is THE Coolest Machine-Learning Model You Might Not Have Heard Of](https://towardsdatascience.com/isotonic-regression-is-the-coolest-machine-learning-model-you-might-not-have-heard-of-3ce14afc6d1e)

[Classifier calibration with Platt's scaling and isotonic regression]: http://fastml.com/classifier-calibration-with-platts-scaling-and-isotonic-regression/
[[FastML] Classifier calibration with Platt's scaling and isotonic regression](http://fastml.com/classifier-calibration-with-platts-scaling-and-isotonic-regression/)

