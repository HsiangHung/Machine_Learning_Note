# Gradient Boosting Extension - MART


Tne idea of boosting regression trees can be mapping to classification and ranking problems. It is called MART(Multiple Additive Regression Trees), where the output of the model is a linear combination of the outputs of a set of regression trees.


## Boosting regression

The procedures of building a boosting regression tree are summarize below (given (`x`, `y`))

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{fit&space;}&space;y&space;=&space;f_1(x);&space;\&space;\hat{y}_1&space;=&space;f_1(x),&space;\&space;\hat{y}^{(1)}&space;=&space;\hat{y}_1,&space;\&space;\textrm{residual&space;}&space;\epsilon_1&space;=&space;y-\hat{y}^{(1)}," target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{fit&space;}&space;y&space;=&space;f_1(x);&space;\&space;\hat{y}_1&space;=&space;f_1(x),&space;\&space;\hat{y}^{(1)}&space;=&space;\hat{y}_1,&space;\&space;\textrm{residual&space;}&space;\epsilon_1&space;=&space;y-\hat{y}^{(1)}," title="\textrm{fit } y = f_1(x); \ \hat{y}_1 = f_1(x), \ \hat{y}^{(1)} = \hat{y}_1, \ \textrm{residual } \epsilon_1 = y-\hat{y}^{(1)}," /></a>


<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{fit&space;}&space;\epsilon_1&space;=&space;f_2(x);&space;\&space;\hat{\epsilon}_1&space;=&space;f_2(x),&space;\&space;\hat{y}^{(2)}&space;=&space;\hat{y}_1&space;&plus;&space;\hat{\epsilon}_1,&space;\&space;\textrm{residual&space;}&space;\epsilon_2&space;=&space;y-\hat{y}^{(2)}," target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{fit&space;}&space;\epsilon_1&space;=&space;f_2(x);&space;\&space;\hat{\epsilon}_1&space;=&space;f_2(x),&space;\&space;\hat{y}^{(2)}&space;=&space;\hat{y}_1&space;&plus;&space;\hat{\epsilon}_1,&space;\&space;\textrm{residual&space;}&space;\epsilon_2&space;=&space;y-\hat{y}^{(2)}," title="\textrm{fit } \epsilon_1 = f_2(x); \ \hat{\epsilon}_1 = f_2(x), \ \hat{y}^{(2)} = \hat{y}_1 + \hat{\epsilon}_1, \ \textrm{residual } \epsilon_2 = y-\hat{y}^{(2)}," /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{fit&space;}&space;\epsilon_2&space;=&space;f_3(x);&space;\&space;\hat{\epsilon}_2&space;=&space;f_3(x),&space;\&space;\hat{y}^{(3)}&space;=&space;\hat{y}_1&space;&plus;&space;\hat{\epsilon}_1&space;&plus;&space;\hat{\epsilon}_2,&space;\&space;\textrm{residual&space;}&space;\epsilon_3&space;=&space;y-\hat{y}^{(3)}," target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{fit&space;}&space;\epsilon_2&space;=&space;f_3(x);&space;\&space;\hat{\epsilon}_2&space;=&space;f_3(x),&space;\&space;\hat{y}^{(3)}&space;=&space;\hat{y}_1&space;&plus;&space;\hat{\epsilon}_1&space;&plus;&space;\hat{\epsilon}_2,&space;\&space;\textrm{residual&space;}&space;\epsilon_3&space;=&space;y-\hat{y}^{(3)}," title="\textrm{fit } \epsilon_2 = f_3(x); \ \hat{\epsilon}_2 = f_3(x), \ \hat{y}^{(3)} = \hat{y}_1 + \hat{\epsilon}_1 + \hat{\epsilon}_2, \ \textrm{residual } \epsilon_3 = y-\hat{y}^{(3)}," /></a>

....


<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{y}^{(n)}&space;=&space;\hat{y}_1&space;&plus;&space;\hat{\epsilon}_1&space;&plus;&space;\hat{\epsilon}_2&space;\cdots&space;&plus;&space;\hat{\epsilon}_{n-1}&space;=&space;\hat{y}^{(n-1)}&space;&plus;&space;f_n(x)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{y}^{(n)}&space;=&space;\hat{y}_1&space;&plus;&space;\hat{\epsilon}_1&space;&plus;&space;\hat{\epsilon}_2&space;\cdots&space;&plus;&space;\hat{\epsilon}_{n-1}&space;=&space;\hat{y}^{(n-1)}&space;&plus;&space;f_n(x)" title="\hat{y}^{(n)} = \hat{y}_1 + \hat{\epsilon}_1 + \hat{\epsilon}_2 \cdots + \hat{\epsilon}_{n-1} = \hat{y}^{(n-1)} + f_n(x)" /></a>

The following picture provides a good intuition about the gradient boosting process:

![](images/golf.png)


Note the cost function for regression is 

<a href="https://www.codecogs.com/eqnedit.php?latex=C&space;=&space;\frac{1}{2}(y&space;-&space;\hat{y})^2," target="_blank"><img src="https://latex.codecogs.com/gif.latex?C&space;=&space;\frac{1}{2}(y&space;-&space;\hat{y})^2," title="C = \frac{1}{2}(y - \hat{y})^2," /></a>

therefore residuals is equivalent to finding the gradient of the cost function

<a href="https://www.codecogs.com/eqnedit.php?latex=y&space;-&space;\hat{y}&space;=&space;-&space;\frac{\partial&space;C}{\partial&space;\hat{y}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y&space;-&space;\hat{y}&space;=&space;-&space;\frac{\partial&space;C}{\partial&space;\hat{y}}" title="y - \hat{y} = - \frac{\partial C}{\partial \hat{y}}" /></a>

and responses in the boosting machine are updated as 

<a href="https://www.codecogs.com/eqnedit.php?latex=y&space;\to&space;y&space;-&space;\alpha&space;\frac{\partial&space;C}{\partial&space;\hat{y}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y&space;\to&space;y&space;-&space;\alpha&space;\frac{\partial&space;C}{\partial&space;\hat{y}}" title="y \to y - \alpha \frac{\partial C}{\partial \hat{y}}" /></a>


### Binary classification using MART











 




## Reference


[CatBoost vs. Light GBM vs. XGBoost]: https://towardsdatascience.com/catboost-vs-light-gbm-vs-xgboost-5f93620723db
[[Alvira Swalin] CatBoost vs. Light GBM vs. XGBoost](https://towardsdatascience.com/catboost-vs-light-gbm-vs-xgboost-5f93620723db)


[An Overview of LightGBM]: https://www.avanwyk.com/an-overview-of-lightgbm/#:~:text=%2Dlightgbm%2Doverview.-,LightGBM,%2DSide%20Sampling%20(Goss).
[[Andrich van Wyk] An Overview of LightGBM](https://www.avanwyk.com/an-overview-of-lightgbm/#:~:text=%2Dlightgbm%2Doverview.-,LightGBM,%2DSide%20Sampling%20(Goss).)


[Good summary of XGBoost vs CatBoost vs LightGBM]: https://www.kaggle.com/c/LANL-Earthquake-Prediction/discussion/89909
[[Aman Cyberia] Good summary of XGBoost vs CatBoost vs LightGBM](https://www.kaggle.com/c/LANL-Earthquake-Prediction/discussion/89909)


[Which algorithm takes the crown: Light GBM vs XGBOOST?]: https://www.analyticsvidhya.com/blog/2017/06/which-algorithm-takes-the-crown-light-gbm-vs-xgboost/
[[Analytics Vidhya] Which algorithm takes the crown: Light GBM vs XGBOOST?](https://www.analyticsvidhya.com/blog/2017/06/which-algorithm-takes-the-crown-light-gbm-vs-xgboost/)


[Decision trees: leaf-wise (best-first) and level-wise tree traverse]:https://datascience.stackexchange.com/questions/26699/decision-trees-leaf-wise-best-first-and-level-wise-tree-traverse
[[Data Science: Decision trees: leaf-wise (best-first) and level-wise tree traverse] Decision trees: leaf-wise (best-first) and level-wise tree traverse](https://datascience.stackexchange.com/questions/26699/decision-trees-leaf-wise-best-first-and-level-wise-tree-traverse)


[GBM vs XGBOOST? Key differences?]: https://datascience.stackexchange.com/questions/16904/gbm-vs-xgboost-key-differences
[[Data Science: GBM vs XGBOOST? Key differences?] GBM vs XGBOOST? Key differences?](https://datascience.stackexchange.com/questions/16904/gbm-vs-xgboost-key-differences)

[Which models can handle null values?]: https://datascience.stackexchange.com/questions/67167/which-models-can-handle-null-values
[[Data Science: Which models can handle null values?] Which models can handle null values?](https://datascience.stackexchange.com/questions/67167/which-models-can-handle-null-values)



[Gradient Boosting and XGBoost]: https://medium.com/@gabrieltseng/gradient-boosting-and-xgboost-c306c1bcfaf5
[[Gabriel Tseng] Gradient Boosting and XGBoost](https://medium.com/@gabrieltseng/gradient-boosting-and-xgboost-c306c1bcfaf5)


[Github: LGBM]: https://github.com/Microsoft/LightGBM/blob/master/docs/Features.rst#leaf-wise-best-first-tree-growth
[[Github] Github: LGBM](https://github.com/Microsoft/LightGBM/blob/master/docs/Features.rst#leaf-wise-best-first-tree-growth)


[Gradient Boosting Decision trees: XGBoost vs LightGBM (and catboost)]: https://medium.com/kaggle-nyc/gradient-boosting-decision-trees-xgboost-vs-lightgbm-and-catboost-72df6979e0bb#:~:text=In%20summary%2C%20LightGBM%20improves%20on,fraction%20of%20the%20whole%20dataset.
[[Harry Moreno] Gradient Boosting Decision trees: XGBoost vs LightGBM (and catboost)](https://medium.com/kaggle-nyc/gradient-boosting-decision-trees-xgboost-vs-lightgbm-and-catboost-72df6979e0bb#:~:text=In%20summary%2C%20LightGBM%20improves%20on,fraction%20of%20the%20whole%20dataset.)


[Gradient Boosting with Scikit-Learn, XGBoost, LightGBM, and CatBoost]: https://machinelearningmastery.com/gradient-boosting-with-scikit-learn-xgboost-lightgbm-and-catboost/
[[Jason Brownlee] Gradient Boosting with Scikit-Learn, XGBoost, LightGBM, and CatBoost](https://machinelearningmastery.com/gradient-boosting-with-scikit-learn-xgboost-lightgbm-and-catboost/)


[A Kaggle Master Explains Gradient Boosting]: http://blog.kaggle.com/2017/01/23/a-kaggle-master-explains-gradient-boosting/
[[Kaggle] A Kaggle Master Explains Gradient Boosting](http://blog.kaggle.com/2017/01/23/a-kaggle-master-explains-gradient-boosting/)


[Light GBM model vs XGBoost Model Parameter Tuning and Examples]: https://pyligent.github.io/2019-08-20-lightGBM_XGBoost/
[[Tao Lin] Light GBM model vs XGBoost Model Parameter Tuning and Examples](https://pyligent.github.io/2019-08-20-lightGBM_XGBoost/)


[Understanding LightGBM Parameters (and How to Tune Them)]: https://neptune.ai/blog/lightgbm-parameters-guide
[[Neptune.ai] Understanding LightGBM Parameters (and How to Tune Them)](https://neptune.ai/blog/lightgbm-parameters-guide)


[What is an intuitive explanation of Gradient Boosting?]: https://www.quora.com/What-is-an-intuitive-explanation-of-Gradient-Boosting
[[Quora: What is an intuitive explanation of Gradient Boosting?] What is an intuitive explanation of Gradient Boosting?](https://www.quora.com/What-is-an-intuitive-explanation-of-Gradient-Boosting)


[What is the difference between gradient boosting and adaboost?]: https://www.quora.com/What-is-the-difference-between-gradient-boosting-and-adaboost#
[[Quora: What is the difference between gradient boosting and adaboost?] What is the difference between gradient boosting and adaboost?](https://www.quora.com/What-is-the-difference-between-gradient-boosting-and-adaboost#)


[What is the difference between eXtreme Gradient Boosting (XGBoost), AdaBoost, and Gradient Boosting?]: https://www.quora.com/What-is-the-difference-between-eXtreme-Gradient-Boosting-XGBoost-AdaBoost-and-Gradient-Boosting
[[Quora: What is the difference between eXtreme Gradient Boosting (XGBoost), AdaBoost, and Gradient Boosting?] What is the difference between eXtreme Gradient Boosting (XGBoost), AdaBoost, and Gradient Boosting?](https://www.quora.com/What-is-the-difference-between-eXtreme-Gradient-Boosting-XGBoost-AdaBoost-and-Gradient-Boosting)


[Gradient Boosting from scratchs]: https://medium.com/mlreview/gradient-boosting-from-scratch-1e317ae4587d
[[Prince Grover-1] Gradient Boosting from scratchs](https://medium.com/mlreview/gradient-boosting-from-scratch-1e317ae4587d)


[Gradient boosting simplified]: https://www.kaggle.com/grroverpr/gradient-boosting-simplified/
[[Prince Grover-2] Gradient boosting simplified](https://www.kaggle.com/grroverpr/gradient-boosting-simplified/)


[XGBOOST vs LightGBM: Which algorithm wins the race !!!]: https://towardsdatascience.com/lightgbm-vs-xgboost-which-algorithm-win-the-race-1ff7dd4917d#:~:text=The%20development%20of%20Boosting%20Machines,because%20it%20is%20extremely%20powerful.
[[Sai Nikhilesh Kasturi] XGBOOST vs LightGBM: Which algorithm wins the race !!!](https://towardsdatascience.com/lightgbm-vs-xgboost-which-algorithm-win-the-race-1ff7dd4917d#:~:text=The%20development%20of%20Boosting%20Machines,because%20it%20is%20extremely%20powerful.)


