
# Regression 

Generally form

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{y}&space;=&space;\theta_0&space;&plus;&space;\theta_1&space;x_1&space;&plus;&space;\theta_2&space;x_2&space;&plus;\cdots&space;=&space;\bold{x}&space;\theta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{y}&space;=&space;\theta_0&space;&plus;&space;\theta_1&space;x_1&space;&plus;&space;\theta_2&space;x_2&space;&plus;\cdots&space;=&space;\bold{x}&space;\theta" title="\hat{y} = \theta_0 + \theta_1 x_1 + \theta_2 x_2 +\cdots = \bold{x} \theta" /></a>

The cost function reads

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{C}&space;=&space;\sum^m_{i=1}&space;(y_i&space;-&space;\hat{y}_i)^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{C}&space;=&space;\sum^m_{i=1}&space;(y_i&space;-&space;\hat{y}_i)^2" title="\textrm{C} = \sum^m_{i=1} (y_i - \hat{y}_i)^2" /></a>

where <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{y}_i&space;=&space;\bold{x}_i&space;\theta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{y}_i&space;=&space;\bold{x}_i&space;\theta" title="\hat{y}_i = \bold{x}_i \theta" /></a> is the predicted value, and residuals are defined as the difference between the actual value and the value predicted by our linear regression model:

<a href="https://www.codecogs.com/eqnedit.php?latex=e_i&space;=&space;\hat{y}_i&space;-&space;y_i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e_i&space;=&space;\hat{y}_i&space;-&space;y_i" title="e_i = \hat{y}_i - y_i" /></a>

## Metric


#### MSE

#### R-squared

#### Adjusted R-squared

| model |  bias |  variance | 
| --- | --- | --- | 
| [Naive bayes](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Classification/Naive%20Bayes)  | high | low | 
| Logistic regression| high | low|
| [Tree](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Classification/Decison%20Tree) | low | high |
| [SVM](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Classification/Support%20Vector%20Machine) | low | high |

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







[Softmax Regression]: http://deeplearning.stanford.edu/tutorial/supervised/SoftmaxRegression/support-vector-machines-in-machine-learning
[[UFLDL Tutorial] Softmax Regression](http://deeplearning.stanford.edu/tutorial/supervised/SoftmaxRegression/)


