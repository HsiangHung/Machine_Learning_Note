# Gradient Boosting Extendsion - MART



Tne boosting regression trees can be extended to classification and even ranking problems. 

## Boosting regression

The procedures of building a boosting regression tree are summarize below (given (`x`, `y`))

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{fit&space;}&space;y&space;=&space;f_1(x);&space;\&space;\hat{y}_1&space;=&space;f_1(x),&space;\&space;\hat{y}^{(1)}&space;=&space;\hat{y}_1,&space;\&space;\textrm{residual&space;}&space;\epsilon_1&space;=&space;y-\hat{y}," target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{fit&space;}&space;y&space;=&space;f_1(x);&space;\&space;\hat{y}_1&space;=&space;f_1(x),&space;\&space;\hat{y}^{(1)}&space;=&space;\hat{y}_1,&space;\&space;\textrm{residual&space;}&space;\epsilon_1&space;=&space;y-\hat{y}," title="\textrm{fit } y = f_1(x); \ \hat{y}_1 = f_1(x), \ \hat{y}^{(1)} = \hat{y}_1, \ \textrm{residual } \epsilon_1 = y-\hat{y}," /></a>


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




## C. XGBoost

XGBoost (Chen) was developed to put this on a more formal footing. Both xgboost and gbm follows the principle of gradient boosting, but in XGBoost the size of the tree and the magnitude of the weights are controlled by standard **regularization** parameters. This leads to a ‘mostly’ parameter-free optimization routine. In theory that is, as in practice a plethora of parameters are used, still to control the size and shape of the trees. Regularization did however prove to be very powerful and made the algorithm much more robust [[Quora: What is the difference between eXtreme Gradient Boosting (XGBoost), AdaBoost, and Gradient Boosting?]][What is the difference between eXtreme Gradient Boosting (XGBoost), AdaBoost, and Gradient Boosting?], [[Gabriel Tseng]][Gradient Boosting and XGBoost] and [the stackexchange blog](https://datascience.stackexchange.com/questions/16904/gbm-vs-xgboost-key-differences#:~:text=Quote%20from%20the%20author%20of,which%20gives%20it%20better%20performance.).

The comprehensive tutorial on introduction to the model, [Introduction to Boosted Trees](https://xgboost.readthedocs.io/en/latest/tutorials/model.html#tree-boosting) explained more detailed [[Data Science: GBM vs XGBOOST? Key differences?]][GBM vs XGBOOST? Key differences?]. Suppose we have

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{y}^0_i&space;=&space;0&space;&plus;&space;f_0(x_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{y}^0_i&space;=&space;0&space;&plus;&space;f_0(x_i)" title="\hat{y}^0_i = 0 + f_0(x_i)" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{y}^1_i&space;=&space;\hat{y}^0_i&space;&plus;&space;f_1(x_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{y}^1_i&space;=&space;\hat{y}^0_i&space;&plus;&space;f_1(x_i)" title="\hat{y}^1_i = \hat{y}^0_i + f_1(x_i)" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{y}^2_i&space;=&space;\hat{y}^1_i&space;&plus;&space;f_2(x_i)&space;=&space;f_1(x_i)&space;&plus;&space;f_2(x_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{y}^2_i&space;=&space;\hat{y}^1_i&space;&plus;&space;f_2(x_i)&space;=&space;f_1(x_i)&space;&plus;&space;f_2(x_i)" title="\hat{y}^2_i = \hat{y}^1_i + f_2(x_i) = f_1(x_i) + f_2(x_i)" /></a>

... Eventually we have the following relation

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{y}^t_i&space;=&space;\hat{y}^{t-1}_i&space;&plus;&space;f_{t}(x_i)&space;=&space;\sum^{t-1}_{n=1}&space;f_n(x_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{y}^t_i&space;=&space;\hat{y}^{t-1}_i&space;&plus;&space;f_{t}(x_i)&space;=&space;\sum^{t-1}_{n=1}&space;f_n(x_i)" title="\hat{y}^t_i = \hat{y}^{t-1}_i + f_{t}(x_i) = \sum^{t-1}_{n=1} f_n(x_i)" /></a>

Here `f0` is like `F1` in previous discussion [Math Intuition of GBM](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Ensemble/Boosting#math-intuition-of-gbm), and `f1`, `f2`, ... are like `h1`, `h2`,....

In comparison to boosted tree, the cost function in XGBoost has regularization on the `f` functions at `t`-th iteration [Introduction to Boosted Trees](https://xgboost.readthedocs.io/en/latest/tutorials/model.html#tree-boosting), 

<a href="https://www.codecogs.com/eqnedit.php?latex=J_t&space;=&space;\sum^n_{i=1}&space;\big(&space;y_i&space;-&space;\hat{y}^t_i&space;\big)^2&space;&plus;&space;\Omega(f_t)&space;=&space;\sum^n_{i=1}&space;C(&space;y_i&space;,&space;\&space;\hat{y}^t_i&space;)&space;&plus;&space;\Omega(f_t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J_t&space;=&space;\sum^n_{i=1}&space;\big(&space;y_i&space;-&space;\hat{y}^t_i&space;\big)^2&space;&plus;&space;\Omega(f_t)&space;=&space;\sum^n_{i=1}&space;C(&space;y_i&space;,&space;\&space;\hat{y}^t_i&space;)&space;&plus;&space;\Omega(f_t)" title="J_t = \sum^n_{i=1} \big( y_i - \hat{y}^t_i \big)^2 + \Omega(f_t) = \sum^n_{i=1} C( y_i , \ \hat{y}^t_i ) + \Omega(f_t)" /></a>


Note that we can rewrite the cost function as

<a href="https://www.codecogs.com/eqnedit.php?latex=J_t&space;=&space;\sum^n_{i=1}&space;C&space;\big(&space;y_i&space;,&space;\&space;\hat{y}^{t-1}_i&space;&plus;&space;f_t(x_i)&space;\big)&space;&plus;&space;\Omega(f_t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J_t&space;=&space;\sum^n_{i=1}&space;C&space;\big(&space;y_i&space;,&space;\&space;\hat{y}^{t-1}_i&space;&plus;&space;f_t(x_i)&space;\big)&space;&plus;&space;\Omega(f_t)" title="J_t = \sum^n_{i=1} C \big( y_i , \ \hat{y}^{t-1}_i + f_t(x_i) \big) + \Omega(f_t)" /></a>

Using Taylor expansion, we can approximate the cost function up to the second order of `f`:

<a href="https://www.codecogs.com/eqnedit.php?latex=J_t&space;=&space;\sum^n_{i=1}&space;\big[&space;C(&space;y_i&space;,&space;\&space;\hat{y}^{t-1}_i)&space;&plus;&space;g_i&space;f_t(x_i)&space;&plus;&space;\frac{1}{2}h_i&space;f^2_t(x_i)&space;\big]&space;&plus;&space;\Omega(f_t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J_t&space;=&space;\sum^n_{i=1}&space;\big[&space;C(&space;y_i&space;,&space;\&space;\hat{y}^{t-1}_i)&space;&plus;&space;g_i&space;f_t(x_i)&space;&plus;&space;\frac{1}{2}h_i&space;f^2_t(x_i)&space;\big]&space;&plus;&space;\Omega(f_t)" title="J_t = \sum^n_{i=1} \big[ C( y_i , \ \hat{y}^{t-1}_i) + g_i f_t(x_i) + \frac{1}{2}h_i f^2_t(x_i) \big] + \Omega(f_t)" /></a>


where the first/second order gradients are

<a href="https://www.codecogs.com/eqnedit.php?latex=g_i&space;=&space;\partial_{y^{t-1}_i}C(y_i,&space;\&space;\hat{y}^{t-1}_i),&space;\&space;h_i&space;=&space;\partial^2_{y^{t-1}_i}C(y_i,&space;\&space;\hat{y}^{t-1}_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?g_i&space;=&space;\partial_{y^{t-1}_i}C(y_i,&space;\&space;\hat{y}^{t-1}_i),&space;\&space;h_i&space;=&space;\partial^2_{y^{t-1}_i}C(y_i,&space;\&space;\hat{y}^{t-1}_i)" title="g_i = \partial_{y^{t-1}_i}C(y_i, \ \hat{y}^{t-1}_i), \ h_i = \partial^2_{y^{t-1}_i}C(y_i, \ \hat{y}^{t-1}_i)" /></a>


Thus the specific objective at step `t` becomes

<a href="https://www.codecogs.com/eqnedit.php?latex=\sum^n_{i=1}&space;\big[&space;g_i&space;f_t(x_i)&space;&plus;&space;\frac{1}{2}h_i&space;f^2_t(x_i)&space;\big]&space;&plus;&space;\Omega(f_t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sum^n_{i=1}&space;\big[&space;g_i&space;f_t(x_i)&space;&plus;&space;\frac{1}{2}h_i&space;f^2_t(x_i)&space;\big]&space;&plus;&space;\Omega(f_t)" title="\sum^n_{i=1} \big[ g_i f_t(x_i) + \frac{1}{2}h_i f^2_t(x_i) \big] + \Omega(f_t)" /></a>

This becomes our optimization goal for the new tree. One important advantage of this definition is that the value of the objective function only depends on `g_i` and `h_i`. This is how XGBoost supports custom loss functions. We can optimize every loss function, including logistic regression and pairwise ranking, using exactly the same solver that takes `g_i` and `h_i` as input!

XGBoost define the tree `f(x)` as (cf [Introduction to Boosted Trees](https://xgboost.readthedocs.io/en/latest/tutorials/model.html#tree-boosting))

<a href="https://www.codecogs.com/eqnedit.php?latex=f_t(x)&space;=&space;\omega_{q(x)},&space;\&space;\omega&space;\in&space;R^T,&space;\&space;q:&space;R^d&space;\to&space;\lbrace&space;1,2,\cdots,&space;T&space;\rbrace" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_t(x)&space;=&space;\omega_{q(x)},&space;\&space;\omega&space;\in&space;R^T,&space;\&space;q:&space;R^d&space;\to&space;\lbrace&space;1,2,\cdots,&space;T&space;\rbrace" title="f_t(x) = \omega_{q(x)}, \ \omega \in R^T, \ q: R^d \to \lbrace 1,2,\cdots, T \rbrace" /></a>

and the complexity of the regularization term as

<a href="https://www.codecogs.com/eqnedit.php?latex=\Omega(f)&space;=&space;\gamma&space;T&space;&plus;&space;\frac{1}{2}\lambda&space;\sum^T_{j=1}&space;\omega^2_j" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Omega(f)&space;=&space;\gamma&space;T&space;&plus;&space;\frac{1}{2}\lambda&space;\sum^T_{j=1}&space;\omega^2_j" title="\Omega(f) = \gamma T + \frac{1}{2}\lambda \sum^T_{j=1} \omega^2_j" /></a>

where `ω` is the vector of scores on leaves, and `T` is the number of leaves. 

Here is the article: [Light GBM model vs XGBoost Model Parameter Tuning and Examples](https://pyligent.github.io/2019-08-20-lightGBM_XGBoost/) to show hyperparameters in XGBoost.



 




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


