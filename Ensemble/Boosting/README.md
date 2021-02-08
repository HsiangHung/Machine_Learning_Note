# Gradient Boosting and Adaboost



An ensemble is just a **collection of predictors (learners)** which come together (e.g. mean of all predictions) to give a final prediction. 

Boosting is one of ensemble techniques to **sequentially** generate predictors. The subsequent predictors learn from the mistakes of the previous predictors. Therefore, the observations (data) have an **unequal probability of appearing in subsequent models** and ones with the **highest error appear most**. The predictors can be chosen from a range of models like decision trees, regressors, classifiers etc. One can interpret boosting as trying to **minimize bias** of the overall predictor. So when you use boosting, you’re incentivized to use **low-variance and high-bias estimators** (e.g. shallow decision trees. In LGBM, tree depth > 5 may be too deep). However, it could lead to **overfitting** on training data. 

There are mainly two boosting algorithms: Gradient Boosting (GBM) and Adaptive Boosting (Adaboost). XGBoost is a brand new tool developed by Tianran Chen by optimizing GBM.


## 1. Gradient Boosting


 A GBM will start with a not very deep tree and will model the original target. Then it takes the errors from the first round of predictions, and passes the errors as a new target to a second tree. The second tree will model the error from the first tree, record the new errors and pass that as a target to the third tree. And so forth. Essentially it focuses on modelling errors from previous trees. It is high bias-low variance algorithm, and aims to decrease bias not variance. An excellent notebook [[Prince Grover-1]][Gradient Boosting from scratchs] demonstrates how a GBM minimizes bias during training (also see [[Prince Grover-2]][Gradient boosting simplified]).
   
In the following, we explain the boosting pictures using the figures depicted from [Prof. Ihler's lecture slides](http://sli.ics.uci.edu/Classes/2012F-273a?action=download&upname=10-ensembles.pdf) (also the [lecture video](https://www.youtube.com/watch?v=sRktKszFmSk)). Ben Gorman, a Kaggle master also provided a comprehensive description to interpret the math behind GBM in [[3]][A Kaggle Master Explains Gradient Boosting]. 


### Boosting steps in GBM


We usually start with a very simple estimator, say one-layer decision tree to fit the data `(x1, y1), (x2, y2),...`. In the following panels, the red points denote the data points and green dots are reisduals. We build the first regressor by fitting 

    F1(x) = y

![](images/GBM1.png)

In the above left plot, the black line indicates the `F1(x)` predictor (model). Then we compute the residuals `e1 = y - y1` (`y1` is given by the `F1(x)`) shown as green dots on the right hand plot. Next we build another model to fit the **residuals** 

    h1(x) = e1

Similarly, the black line in the above right plot indicates the `h1(x)` predictor. Now we can combine the predictors `F2(x) = F1(x) + h1(x)` and the resulting predictor is the black line shown in the left hand plot below

![](images/GBM2.png)

Now we see the `F2(x)` is a better regressor than `F1(x)` to fit the data, and leave residuals `e2 = y - y2` as shown on the right. Then we still fit the residuals `e2`

    h2(x) = e2

and so on. In this case, mathmetically we have an iterative relation

<a href="https://www.codecogs.com/eqnedit.php?latex=F_t&space;(x)&space;=&space;F_{t-1}(x)&space;&plus;&space;h_{t-1}(x)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F_t&space;(x)&space;=&space;F_{t-1}(x)&space;&plus;&space;h_{t-1}(x)" title="F_t (x) = F_{t-1}(x) + h_{t-1}(x)" /></a>

and the residual fitting model is given by   

<a href="https://www.codecogs.com/eqnedit.php?latex=h_t&space;(x)&space;=&space;y&space;-&space;F_t(x)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?h_t&space;(x)&space;=&space;y&space;-&space;F_t(x)" title="h_t (x) = y - F_t(x)" /></a>

Prof. Ihler gave a [comprehensive description](http://sli.ics.uci.edu/Classes/2012F-273a?action=download&upname=10-ensembles.pdf) about the boosting steps in his lecture and here we borrow to show below
![](images/GBM3.png)
Upper panel shows data and fitting models `F1(x)`, `F2(x)`, ....`Fm(x)` and lower shows the residuals. The first estimator is built on the leftmost, whereas the rightmost shows the last iteration. We can see by boosting, the predictors are becoming more and more complex but fit the data better and better. Meanwhile, the residuals are moving toward to smaller values (if you zoom in).



### Math Intuition of GBM

Previous description assumes all learners in the same weight. Where is the `gradient`? A GBM creates a set of predictors `F(x)`, and for a regression problem, the loss function is given by  

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{Loss}&space;=&space;J(y,&space;\hat{y})&space;=&space;\sum_i&space;\big(&space;y_i&space;-&space;\hat{y}_i&space;\big)^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{Loss}&space;=&space;J(y,&space;\hat{y})&space;=&space;\sum_i&space;\big(&space;y_i&space;-&space;\hat{y}_i&space;\big)^2" title="\textrm{Loss} = J(y, \hat{y}) = \sum_i \big( y_i - \hat{y}_i \big)^2" /></a>

The boosting process is equivalent to minimizing `Loss` by sequentially generating models `F1(x)`, `F2(x)`, .... Therefore, we can add a superscript on the `Loss` function to represent the `Loss` function in `t`-th iteration

<a href="https://www.codecogs.com/eqnedit.php?latex=J_t(y,&space;\&space;\hat{y})&space;=&space;\sum_i&space;\big(&space;y_i&space;-&space;\hat{y}^t_i&space;\big)^2&space;=&space;\sum_i&space;\big(&space;y_i&space;-&space;F_t(x_i)&space;\big)^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J_t(y,&space;\&space;\hat{y})&space;=&space;\sum_i&space;\big(&space;y_i&space;-&space;\hat{y}^t_i&space;\big)^2&space;=&space;\sum_i&space;\big(&space;y_i&space;-&space;F_t(x_i)&space;\big)^2" title="J_t(y, \ \hat{y}) = \sum_i \big( y_i - \hat{y}^t_i \big)^2 = \sum_i \big( y_i - F_t(x_i) \big)^2" /></a>


where `t = 1, 2, 3...` From the gradient descent aspect, the `Loss` is minimized as

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{y}^{m&plus;1}&space;:=\hat{y}^m&space;&plus;&space;\alpha&space;\frac{\partial&space;J_m(y,&space;\hat{y})}{\partial&space;\hat{y}^m}&space;=&space;y&space;&plus;&space;\alpha&space;\Big(&space;2&space;\sum_i&space;(y_i&space;-&space;\hat{y}^m_i)&space;\Big)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{y}^{m&plus;1}&space;:=\hat{y}^m&space;&plus;&space;\alpha&space;\frac{\partial&space;J_m(y,&space;\hat{y})}{\partial&space;\hat{y}^m}&space;=&space;y&space;&plus;&space;\alpha&space;\Big(&space;2&space;\sum_i&space;(y_i&space;-&space;\hat{y}^m_i)&space;\Big)" title="\hat{y}^{m+1} :=\hat{y}^m + \alpha \frac{\partial J_m(y, \hat{y})}{\partial \hat{y}^m} = y + \alpha \Big( 2 \sum_i (y_i - \hat{y}^m_i) \Big)" /></a>

where `\alpha` is the learning rate. From the expression, we can see the gradient is equal to the errors, and the predicted value `ym` is updated by multiplying the learning rate to the errors. This is why at each step we fit the residuals, where equivalently we are computing the gradient of `J`. The posts [[Prince Grover
-2]][Gradient boosting simplified], [[Kaggle]][A Kaggle Master Explains Gradient Boosting] and [Prof. Ilher's lecture video](https://www.youtube.com/watch?v=sRktKszFmSk) have more detailed interpretation.

Terence Parr in a Quora post [[Quora: What is an intuitive explanation of Gradient Boosting?]][What is an intuitive explanation of Gradient Boosting?] offered a very interesting picture, which explian the procedures very well.

![](images/golf.png)



## 2. AdaBoost

On the other hand, adaptive boosting **changes sample distribution** by **modifying the weights** attached to each of the instances at each iteration. It increases the weights of the wrongly predicted instances and decreases the ones of the correctly predicted instances. The weak learner thus focuses more on the difficult instances [[Quora: What is the difference between gradient boosting and adaboost?]][What is the difference between gradient boosting and adaboost?].

On the other hand, gradient boosting doesn’t modify the sample distribution. 

As a concrete example, we follow Josh Starmer's video lecture: [Adaboost, clearly explained](https://www.youtube.com/watch?v=LsK-xG1cLYA) below. Suppose we have data if patients have heart disease as follows (**chest** = if chest pain,**weight** = patient weight, **disease** = heart disease and **sample weight**):
```
 # | chest | weight | disease | sample weight|
--------------------------------------------
 1 |  Yes  |  205   |   Yes   |  1/8  |
 2 |  No   |  180   |   Yes   |  1/8  |
 3 |  Yes  |  210   |   Yes   |  1/8  |
 4 |  Yes  |  167   |   Yes   |  1/8  |
 5 |  No   |  156   |   No    |  1/8  |
 6 |  No   |  125   |   No    |  1/8  |
 7 |  Yes  |  168   |   No    |  1/8  |
 8 |  Yes  |  172   |   No    |  1/8  |
```
At the beginning each data has same sample weight = 1/8.

Suppose we select weight = 176 to split node, patients' weight > 176 as `Yes` and patients' weight < as `No`.
For `Yes` we have 3 correct, 0 incorrect and for `No` we have 4 correct and 1 incorrect (#4). Then next step we reweigh #4 data with higher sample weight than others since it is misclassified
```
 # | chest | weight | disease | new sample weight|
--------------------------------------------
 1 |  Yes  |  205   |   Yes   |  0.07  |
 2 |  No   |  180   |   Yes   |  0.07  |
 3 |  Yes  |  210   |   Yes   |  0.07  |
 4 |  Yes  |  167   |   Yes   |  0.49  |
 5 |  No   |  156   |   No    |  0.07  |
 6 |  No   |  125   |   No    |  0.07  |
 7 |  Yes  |  168   |   No    |  0.07  |
 8 |  Yes  |  172   |   No    |  0.07  |
```
Then we reconstruct data in next forest by the new sample weights. For example, given random numbers r: if r < 0.07 we pick #1, if 0.07 <= r < 0.14 we pick #2,..., if 0.21 <= r < 0.7 pick #4,.... As a result, we will have more #4 than others in the new constructed data.



## 3. XGBoost

XGBoost (Chen) was developed to put this on a more formal footing. Both xgboost and gbm follows the principle of gradient boosting, but in XGBoost the size of the tree and the magnitude of the weights are controlled by standard **regularization** parameters. This leads to a ‘mostly’ parameter-free optimization routine. In theory that is, as in practice a plethora of parameters are used, still to control the size and shape of the trees. Regularization did however prove to be very powerful and made the algorithm much more robust [[Quora: What is the difference between eXtreme Gradient Boosting (XGBoost), AdaBoost, and Gradient Boosting?]][What is the difference between eXtreme Gradient Boosting (XGBoost), AdaBoost, and Gradient Boosting?], [[Gabriel Tseng]][Gradient Boosting and XGBoost] and [the stackexchange blog](https://datascience.stackexchange.com/questions/16904/gbm-vs-xgboost-key-differences#:~:text=Quote%20from%20the%20author%20of,which%20gives%20it%20better%20performance.).

The comprehensive tutorial on introduction to the model, [Introduction to Boosted Trees](https://xgboost.readthedocs.io/en/latest/tutorials/model.html#tree-boosting) explained more detailed [[Data Science: GBM vs XGBOOST? Key differences?]][GBM vs XGBOOST? Key differences?]. Suppose we have

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{y}^0_i&space;=&space;0&space;&plus;&space;f_0(x_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{y}^0_i&space;=&space;0&space;&plus;&space;f_0(x_i)" title="\hat{y}^0_i = 0 + f_0(x_i)" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{y}^1_i&space;=&space;\hat{y}^0_i&space;&plus;&space;f_1(x_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{y}^1_i&space;=&space;\hat{y}^0_i&space;&plus;&space;f_1(x_i)" title="\hat{y}^1_i = \hat{y}^0_i + f_1(x_i)" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{y}^2_i&space;=&space;\hat{y}^1_i&space;&plus;&space;f_2(x_i)&space;=&space;f_1(x_i)&space;&plus;&space;f_2(x_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{y}^2_i&space;=&space;\hat{y}^1_i&space;&plus;&space;f_2(x_i)&space;=&space;f_1(x_i)&space;&plus;&space;f_2(x_i)" title="\hat{y}^2_i = \hat{y}^1_i + f_2(x_i) = f_1(x_i) + f_2(x_i)" /></a>

... Eventually we have the following relation

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{y}^t_i&space;=&space;\hat{y}^{t-1}_i&space;&plus;&space;f_{t}(x_i)&space;=&space;\sum^{t-1}_{n=1}&space;f_n(x_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{y}^t_i&space;=&space;\hat{y}^{t-1}_i&space;&plus;&space;f_{t}(x_i)&space;=&space;\sum^{t-1}_{n=1}&space;f_n(x_i)" title="\hat{y}^t_i = \hat{y}^{t-1}_i + f_{t}(x_i) = \sum^{t-1}_{n=1} f_n(x_i)" /></a>

Here `f0` is like `F1` in previous discussion [Math Intuition of GBM](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Ensemble/Boosting#math-intuition-of-gbm), and `f1`, `f2`, ... are like `h1`, `h2`,....

In comparison to boosted tree, the cost function in XGBoost has regularization on the `f` functions at `t`-th iteration, 

<a href="https://www.codecogs.com/eqnedit.php?latex=J_t&space;=&space;\sum^n_{i=1}&space;\big(&space;y_i&space;-&space;\hat{y}^t_i&space;\big)^2&space;&plus;&space;\Omega(f_t)&space;=&space;\sum^n_{i=1}&space;C(&space;y_i&space;,&space;\&space;\hat{y}^t_i&space;)&space;&plus;&space;\Omega(f_t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J_t&space;=&space;\sum^n_{i=1}&space;\big(&space;y_i&space;-&space;\hat{y}^t_i&space;\big)^2&space;&plus;&space;\Omega(f_t)&space;=&space;\sum^n_{i=1}&space;C(&space;y_i&space;,&space;\&space;\hat{y}^t_i&space;)&space;&plus;&space;\Omega(f_t)" title="J_t = \sum^n_{i=1} \big( y_i - \hat{y}^t_i \big)^2 + \Omega(f_t) = \sum^n_{i=1} C( y_i , \ \hat{y}^t_i ) + \Omega(f_t)" /></a>


Note that we can rewrite the cost function as

<a href="https://www.codecogs.com/eqnedit.php?latex=J_t&space;=&space;\sum^n_{i=1}&space;C(&space;y_i&space;,&space;\&space;\hat{y}^{t-1}_i&space;&plus;&space;f_t(x_i))&space;&plus;&space;\Omega(f_t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J_t&space;=&space;\sum^n_{i=1}&space;C(&space;y_i&space;,&space;\&space;\hat{y}^{t-1}_i&space;&plus;&space;f_t(x_i))&space;&plus;&space;\Omega(f_t)" title="J_t = \sum^n_{i=1} C( y_i , \ \hat{y}^{t-1}_i + f_t(x_i)) + \Omega(f_t)" /></a>


Using Taylor expansion, we can expand the cost function up to the second order:

<a href="https://www.codecogs.com/eqnedit.php?latex=J_t&space;=&space;\sum^n_{i=1}&space;\big[&space;C(&space;y_i&space;,&space;\&space;\hat{y}^{t-1}_i)&space;&plus;&space;g_i&space;f_t(x_i)&space;&plus;&space;\frac{1}{2}h_i&space;f^2_t(x_i)&space;\big]&space;&plus;&space;\Omega(f_t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J_t&space;=&space;\sum^n_{i=1}&space;\big[&space;C(&space;y_i&space;,&space;\&space;\hat{y}^{t-1}_i)&space;&plus;&space;g_i&space;f_t(x_i)&space;&plus;&space;\frac{1}{2}h_i&space;f^2_t(x_i)&space;\big]&space;&plus;&space;\Omega(f_t)" title="J_t = \sum^n_{i=1} \big[ C( y_i , \ \hat{y}^{t-1}_i) + g_i f_t(x_i) + \frac{1}{2}h_i f^2_t(x_i) \big] + \Omega(f_t)" /></a>


where the gradients are

<a href="https://www.codecogs.com/eqnedit.php?latex=g_i&space;=&space;\partial_{y^{t-1}_i}C(y_i,&space;\hat{y}^{t-1}_i),&space;\&space;h_i&space;=&space;\partial^2_{y^{t-1}_i}C(y_i,&space;\hat{y}^{t-1}_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?g_i&space;=&space;\partial_{y^{t-1}_i}C(y_i,&space;\hat{y}^{t-1}_i),&space;\&space;h_i&space;=&space;\partial^2_{y^{t-1}_i}C(y_i,&space;\hat{y}^{t-1}_i)" title="g_i = \partial_{y^{t-1}_i}C(y_i, \hat{y}^{t-1}_i), \ h_i = \partial^2_{y^{t-1}_i}C(y_i, \hat{y}^{t-1}_i)" /></a>




## 4. LightGBM

LightGBM (LGBM) model is a relatively new model. Rather than **level-wise** tree growth in regular decision tree algorithms (credit from [here](https://github.com/Microsoft/LightGBM/blob/master/docs/)), 

![level_wise](images/level-wise.png)

LGBM is **leaf-wise** tree growth, 

![leaf_wise](images/leaf-wise.png)

which shows faster performance [[Analytics Vidhya]][Which algorithm takes the crown: Light GBM vs XGBOOST?], [[Harry Moreno]][Gradient Boosting Decision trees: XGBoost vs LightGBM (and catboost)], [[Aman Cyberia]][Good summary of XGBoost vs CatBoost vs LightGBM], [[Sai Nikhilesh Kasturi]][XGBOOST vs LightGBM: Which algorithm wins the race !!!], [[Alvira Swalin]][CatBoost vs. Light GBM vs. XGBoost], [[Jason Brownlee]][Gradient Boosting with Scikit-Learn, XGBoost, LightGBM, and CatBoost], [[Github]][Github: LGBM]. Leaf-wise algorithms tend to achieve lower loss than level-wise algorithms. However, Leaf-wise may cause over-fitting when the data size is small, so LightGBM includes the max_depth parameter to limit tree depth. 

Another good introduction blogs are given by [[Andrich van Wyk]][An Overview of LightGBM] and [[Neptune.ai]][Understanding LightGBM Parameters (and How to Tune Them)]. The model API can be found [here](https://lightgbm.readthedocs.io/en/latest/Python-Intro.html) as well as [the model hyperparameter list](https://lightgbm.readthedocs.io/en/latest/Parameters.html). How to avoid overfitting in LGBM? The guide page and [[Andrich van Wyk] An Overview of LightGBM] show how to [tune hyperparameter](https://lightgbm.readthedocs.io/en/latest/Parameters-Tuning.html). The summary includes:

1. `max_bin`: the maximum numbers bins that feature values are bucketed in. A `smaller` max_bin reduces overfitting.
2. `min_child_weight`: the minimum sum hessian for a leaf. In conjuction with min_child_samples, `larger` values reduce overfitting.
3. `bagging_fraction` and `bagging_freq`: enables bagging (subsampling) of the training data. Both values need to be set for bagging to be used. The frequency controls how often (iteration) bagging is used. `Smaller` fractions and frequencies reduce overfitting.
4. `feature_fraction`: controls the subsampling of features used for training (as opposed to subsampling the actual training data in the case of bagging). `Smaller fractions` reduce overfitting.
5. `lambda_l1` (`reg_aplha`) and `lambda_L2` (`reg_lambda`): controls L1 and L2 regularization.


## 5. Comparison LighGBM vs XGboost

Here is the deeper description about LighGBM (best-first) and XGboost (depth-fist):

If you grow the full tree, best-first (leaf-wise) and depth-first (level-wise) will result in the same tree. The difference is in the order in which the tree is expanded. Since we don't normally grow trees to their full depth, order matters: application of early stopping criteria and pruning methods can result in very different trees. Because leaf-wise chooses splits based on their contribution to the global loss and not just the loss along a particular branch, it often (not always) will learn lower-error trees "faster" than level-wise. I.e. for a small number of nodes, leaf-wise will probably out-perform level-wise. As you add more nodes, without stopping or pruning they will converge to the same performance because they will literally build the same tree eventually [[Data Science: Decision trees: leaf-wise (best-first) and level-wise tree traverse]][Decision trees: leaf-wise (best-first) and level-wise tree traverse].


### Advantages of Light GBM:

 [[Sai Nikhilesh Kasturi]][XGBOOST vs LightGBM: Which algorithm wins the race !!!]

* Faster training speed and higher efficiency: Light GBM use **histogram based algorithm** i.e it buckets continuous feature values into discrete bins which fasten the training procedure.
* Lower memory usage: Replaces continuous values to discrete bins which result in lower memory usage.
* Better accuracy than any other boosting algorithm: It produces much **more complex trees** by following leaf wise split approach rather than a level-wise approach which is the main factor in achieving higher accuracy. However, it can sometimes lead to overfitting which can be avoided by setting the max_depth parameter.
* Compatibility with Large Datasets: It is capable of performing equally good with large datasets with a significant reduction in training time as compared to XGBOOST.

LightGBM uses a novel technique of Gradient-based One-Side Sampling (GOSS) to filter out the data instances for finding a split value while XGBoost uses pre-sorted algorithm & Histogram-based algorithm for computing the best split. In a nutshell, GOSS retains instances with large gradients while performing random sampling on instances with small gradients [[Sai Nikhilesh Kasturi]][XGBOOST vs LightGBM: Which algorithm wins the race !!!].

LightGBM can also handle categorical feature. XGBoost cannot handle categorical features by itself, it only accepts numerical values similar to Random Forest [[Alvira Swalin]][CatBoost vs. Light GBM vs. XGBoost]. 



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


