
# Gradient Boosting Extension - MART


 Boosting is a method of converting weak learners into strong learners. 

Tne idea of boosting regression trees can be mapping to classification and ranking problems. It is called MART(Multiple Additive Regression Trees), where the output of the model is a linear combination of the outputs of a set of regression trees.

The following content follows Chris Burge's review paper: [From RankNet to LambdaRank to LambdaMART: An Overview](https://www.microsoft.com/en-us/research/uploads/prod/2016/02/MSR-TR-2010-82.pdf). The LambdaMART is particularly designed as MART + LambdaRank.

Here is Prof. Tom´aˇs Tunys' lecture slide: [LambdaMART Demystified](https://staff.fnwi.uva.nl/e.kanoulas/wp-content/uploads/Lecture-8-1-LambdaMart-Demystified.pdf).

## Boosting regression

The procedures of building a boosting regression tree are summarize below (given (`x`, `y`))

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{fit&space;}&space;f_0(x)&space;=&space;y;&space;\&space;\hat{y}_0&space;=&space;f_0(x),&space;\&space;\hat{y}^{(0)}&space;=&space;\hat{y}_0&space;=&space;f_0(x),&space;\&space;\textrm{residual&space;}&space;\epsilon_1&space;=&space;y-\hat{y}^{(0)}," target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{fit&space;}&space;f_0(x)&space;=&space;y;&space;\&space;\hat{y}_0&space;=&space;f_0(x),&space;\&space;\hat{y}^{(0)}&space;=&space;\hat{y}_0&space;=&space;f_0(x),&space;\&space;\textrm{residual&space;}&space;\epsilon_1&space;=&space;y-\hat{y}^{(0)}," title="\textrm{fit } f_0(x) = y; \ \hat{y}_0 = f_0(x), \ \hat{y}^{(0)} = \hat{y}_0 = f_0(x), \ \textrm{residual } \epsilon_1 = y-\hat{y}^{(0)}," /></a>


<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{fit&space;}&space;f_1(x)&space;=&space;\epsilon_1;&space;\&space;\hat{\epsilon}_1&space;=&space;f_1(x),&space;\&space;\hat{y}^{(1)}&space;=&space;\hat{y}_0&space;&plus;&space;\hat{\epsilon}_1&space;=&space;f_0&space;&plus;f_1,&space;\&space;\textrm{res&space;}&space;\epsilon_2&space;=&space;y-\hat{y}^{(1)}," target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{fit&space;}&space;f_1(x)&space;=&space;\epsilon_1;&space;\&space;\hat{\epsilon}_1&space;=&space;f_1(x),&space;\&space;\hat{y}^{(1)}&space;=&space;\hat{y}_0&space;&plus;&space;\hat{\epsilon}_1&space;=&space;f_0&space;&plus;f_1,&space;\&space;\textrm{res&space;}&space;\epsilon_2&space;=&space;y-\hat{y}^{(1)}," title="\textrm{fit } f_1(x) = \epsilon_1; \ \hat{\epsilon}_1 = f_1(x), \ \hat{y}^{(1)} = \hat{y}_0 + \hat{\epsilon}_1 = f_0 +f_1, \ \textrm{res } \epsilon_2 = y-\hat{y}^{(1)}," /></a>


<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{fit&space;}&space;f_2(x)&space;=&space;\epsilon_2;&space;\&space;\hat{y}^{(2)}&space;=&space;\hat{y}_0&space;&plus;&space;\hat{\epsilon}_1&space;&plus;&space;\hat{\epsilon}_2&space;=&space;f_0&space;&plus;&space;f_1&space;&plus;&space;f_2,&space;\&space;\textrm{res&space;}&space;\epsilon_3&space;=&space;y-\hat{y}^{(2)}," target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{fit&space;}&space;f_2(x)&space;=&space;\epsilon_2;&space;\&space;\hat{y}^{(2)}&space;=&space;\hat{y}_0&space;&plus;&space;\hat{\epsilon}_1&space;&plus;&space;\hat{\epsilon}_2&space;=&space;f_0&space;&plus;&space;f_1&space;&plus;&space;f_2,&space;\&space;\textrm{res&space;}&space;\epsilon_3&space;=&space;y-\hat{y}^{(2)}," title="\textrm{fit } f_2(x) = \epsilon_2; \ \hat{y}^{(2)} = \hat{y}_0 + \hat{\epsilon}_1 + \hat{\epsilon}_2 = f_0 + f_1 + f_2, \ \textrm{res } \epsilon_3 = y-\hat{y}^{(2)}," /></a>

....


<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{y}^{(n)}&space;=&space;\hat{y}^0&space;&plus;&space;\hat{\epsilon}_1&space;&plus;&space;\hat{\epsilon}_2&space;\cdots&space;&plus;&space;\hat{\epsilon}_{n-1}&space;=&space;\hat{y}^{(n-1)}&space;&plus;&space;f_n(x)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{y}^{(n)}&space;=&space;\hat{y}^0&space;&plus;&space;\hat{\epsilon}_1&space;&plus;&space;\hat{\epsilon}_2&space;\cdots&space;&plus;&space;\hat{\epsilon}_{n-1}&space;=&space;\hat{y}^{(n-1)}&space;&plus;&space;f_n(x)" title="\hat{y}^{(n)} = \hat{y}^0 + \hat{\epsilon}_1 + \hat{\epsilon}_2 \cdots + \hat{\epsilon}_{n-1} = \hat{y}^{(n-1)} + f_n(x)" /></a>


As explained by Pulkit Bansal in the [Quora post](https://www.quora.com/What-is-an-intuitive-explanation-of-Gradient-Boosting), we are modeling `F = f0 + f1 + f2  + .. + fn`,  where each of these is a decision tree, and each new tree is a fit on a modified version of the original data set. The following picture also provides a good interpretation about the gradient boosting process:

![](images/golf.png)

or 

![](images/boosting_tree.png)

and each tree `f1`, `f2`, .... provides approaching results toward to the true target. The collection of the trees forms an ensemble.

Note the cost function for regression is 

<a href="https://www.codecogs.com/eqnedit.php?latex=C&space;=&space;\frac{1}{2}(y&space;-&space;\hat{y})^2," target="_blank"><img src="https://latex.codecogs.com/gif.latex?C&space;=&space;\frac{1}{2}(y&space;-&space;\hat{y})^2," title="C = \frac{1}{2}(y - \hat{y})^2," /></a>

therefore residuals is equivalent to finding the gradient of the cost function [[Cross Validated: Gradient in Gradient Boosting]][Gradient in Gradient Boosting]

<a href="https://www.codecogs.com/eqnedit.php?latex=y&space;-&space;\hat{y}&space;=&space;-&space;\frac{\partial&space;C}{\partial&space;\hat{y}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y&space;-&space;\hat{y}&space;=&space;-&space;\frac{\partial&space;C}{\partial&space;\hat{y}}" title="y - \hat{y} = - \frac{\partial C}{\partial \hat{y}}" /></a>

and responses in the boosting machine are updated as 

<a href="https://www.codecogs.com/eqnedit.php?latex=y&space;\to&space;y&space;-&space;\alpha&space;\frac{\partial&space;C}{\partial&space;\hat{y}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y&space;\to&space;y&space;-&space;\alpha&space;\frac{\partial&space;C}{\partial&space;\hat{y}}" title="y \to y - \alpha \frac{\partial C}{\partial \hat{y}}" /></a>


### Binary classification using MART











 




## Reference






[Gradient in Gradient Boosting]: https://stats.stackexchange.com/questions/338658/gradient-in-gradient-boosting/340376#340376
[[Cross Validated: Gradient in Gradient Boosting] Gradient in Gradient Boosting](https://stats.stackexchange.com/questions/338658/gradient-in-gradient-boosting/340376#340376)








