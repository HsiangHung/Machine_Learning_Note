
# Support Vector Machine


## What are Support Vectors?


Support vectors are data points that are closer to the hyperplane and influence the position and orientation of the hyperplane. Using these support vectors, we maximize the margin of the classifier. Deleting the support vectors will change the position of the hyperplane. These are the points that help us build our SVM [[Rohith Gandhi]][Support Vector Machine — Introduction to Machine Learning Algorithms], [[Shuyu Luo]][Loss Function(Part III): Support Vector Machine], [[Priyankur Sarkar]][Support Vector Machines in Machine Learning]
.
(credit from [Wiki](https://en.wikipedia.org/wiki/Support-vector_machine) and [[Rohith Gandhi]][Support Vector Machine — Introduction to Machine Learning Algorithms])

![support_vectors](images/support_vector.png)

The support vectors are formed by the data laying along the margin.

In the upper right panel, we classify blue instances as positives 

<a href="https://www.codecogs.com/eqnedit.php?latex=\vec{w}\cdot&space;\vec{x}_{+}&space;-b&space;\geq&space;1," target="_blank"><img src="https://latex.codecogs.com/gif.latex?\vec{w}\cdot&space;\vec{x}_{+}&space;-b&space;\geq&space;1," title="\vec{w}\cdot \vec{x}_{+} -b \geq 1," /></a>

and green instances as negatives 

<a href="https://www.codecogs.com/eqnedit.php?latex=\vec{w}\cdot&space;\vec{x}_{-}&space;-b&space;\leq&space;1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\vec{w}\cdot&space;\vec{x}_{-}&space;-b&space;\leq&space;1" title="\vec{w}\cdot \vec{x}_{-} -b \leq 1" /></a>

The margin width is given

<a href="https://www.codecogs.com/eqnedit.php?latex=(\vec{x}_&plus;&space;-&space;\vec{x}_-)\cdot&space;\frac{\vec{w}&space;}{||\vec{w}&space;||}&space;=&space;\frac{(1&plus;b)-(-1&plus;b))}{||\vec{w}||}&space;=&space;\frac{2}{||\vec{w}||}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(\vec{x}_&plus;&space;-&space;\vec{x}_-)\cdot&space;\frac{\vec{w}&space;}{||\vec{w}&space;||}&space;=&space;\frac{(1&plus;b)-(-1&plus;b))}{||\vec{w}||}&space;=&space;\frac{2}{||\vec{w}||}" title="(\vec{x}_+ - \vec{x}_-)\cdot \frac{\vec{w} }{||\vec{w} ||} = \frac{(1+b)-(-1+b))}{||\vec{w}||} = \frac{2}{||\vec{w}||}" /></a>

Maximize the margin width is equalivent to minimize <a href="https://www.codecogs.com/eqnedit.php?latex=||\vec{w}||" target="_blank"><img src="https://latex.codecogs.com/gif.latex?||\vec{w}||" title="||\vec{w}||" /></a>.

## Cost Function

The cost function of SVM is very similar to that of Logistic Regression. Looking at it by y = 1 and y = 0 separately in below plot, the black line is the cost function of Logistic Regression, and the red line is for SVM. Please note that the X axis here is the raw model output, θᵀx. 

![cost_function](images/cost_function.png)

Suppose `m` is the data size, and there are `n` features, we can write the following generic form (with regularization)


<a href="https://www.codecogs.com/eqnedit.php?latex=C(\bold{\theta})&space;=&space;C&space;\sum^m_{i=1}&space;y_i&space;\textrm{Cost}_1(\theta^T&space;\bold{x}_i)&space;&plus;&space;(1-y_i)&space;\textrm{Cost}_0(\theta^T&space;\bold{x}_i)&space;&plus;&space;\frac{1}{2}\sum^n_{j=1}&space;|\theta_j|^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C(\bold{\theta})&space;=&space;C&space;\sum^m_{i=1}&space;y_i&space;\textrm{Cost}_1(\theta^T&space;\bold{x}_i)&space;&plus;&space;(1-y_i)&space;\textrm{Cost}_0(\theta^T&space;\bold{x}_i)&space;&plus;&space;\frac{1}{2}\sum^n_{j=1}&space;|\theta_j|^2" title="C(\bold{\theta}) = C \sum^m_{i=1} y_i \textrm{Cost}_1(\theta^T \bold{x}_i) + (1-y_i) \textrm{Cost}_0(\theta^T \bold{x}_i) + \frac{1}{2}\sum^n_{j=1} |\theta_j|^2" /></a>

What is the hypothesis for SVM? It’s simple and straightforward. When θᵀx ≥ 0, predict 1, otherwise, predict 0. Then we can use the hinge loss function

<a href="https://www.codecogs.com/eqnedit.php?latex=C(\bold{\theta})&space;=&space;C&space;\sum^m_{i=1}&space;\Big(&space;y_i&space;\max{\big(0,&space;1-&space;\theta^T&space;\bold{x}_i)}&space;&plus;&space;(1-y_i)&space;\max{\big(0,&space;1&space;&plus;&space;\theta^T&space;\bold{x}_i)}&space;\Big)&space;&plus;&space;\frac{1}{2}\sum^n_{j=1}&space;|\theta_j|^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C(\bold{\theta})&space;=&space;C&space;\sum^m_{i=1}&space;\Big(&space;y_i&space;\max{\big(0,&space;1-&space;\theta^T&space;\bold{x}_i)}&space;&plus;&space;(1-y_i)&space;\max{\big(0,&space;1&space;&plus;&space;\theta^T&space;\bold{x}_i)}&space;\Big)&space;&plus;&space;\frac{1}{2}\sum^n_{j=1}&space;|\theta_j|^2" title="C(\bold{\theta}) = C \sum^m_{i=1} \Big( y_i \max{\big(0, 1- \theta^T \bold{x}_i)} + (1-y_i) \max{\big(0, 1 + \theta^T \bold{x}_i)} \Big) + \frac{1}{2}\sum^n_{j=1} |\theta_j|^2" /></a>

With a very large value of C (similar to no regularization), this large margin classifier will be very sensitive to outliers. On the other hand, When C is small, we start to allow misclassified staying in the margin. We called it **Soft-margin**.


## Non-Linear SVM

The non-linear boundary problem can be solved if we introduce a kernel [[Priyankur Sarkar]][Support Vector Machines in Machine Learning]. The cost function turns to 

<a href="https://www.codecogs.com/eqnedit.php?latex=C(\bold{\theta})&space;=&space;C&space;\sum^m_{i=1}&space;\Big(&space;y_i&space;\max{\big(0,&space;1-&space;\theta^T&space;\bold{f}_i)}&space;&plus;&space;(1-y_i)&space;\max{\big(0,&space;1&space;&plus;&space;\theta^T&space;\bold{f}_i)}&space;\Big)&space;&plus;&space;\frac{1}{2}\sum^n_{j=1}&space;|\theta_j|^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C(\bold{\theta})&space;=&space;C&space;\sum^m_{i=1}&space;\Big(&space;y_i&space;\max{\big(0,&space;1-&space;\theta^T&space;\bold{f}_i)}&space;&plus;&space;(1-y_i)&space;\max{\big(0,&space;1&space;&plus;&space;\theta^T&space;\bold{f}_i)}&space;\Big)&space;&plus;&space;\frac{1}{2}\sum^n_{j=1}&space;|\theta_j|^2" title="C(\bold{\theta}) = C \sum^m_{i=1} \Big( y_i \max{\big(0, 1- \theta^T \bold{f}_i)} + (1-y_i) \max{\big(0, 1 + \theta^T \bold{f}_i)} \Big) + \frac{1}{2}\sum^n_{j=1} |\theta_j|^2" /></a>

where `f` is **Kernel Function**. In Andrew's Ng's Machine learning class, they are described as similarity function: `f1 = Similarity(x, l_1)`, `f2 = Similarity(x, l2)` and so on, where `l` are landmarks. He used **Gaussian Kernel** to describe proximity. In Scikit-learn SVM package, Gaussian Kernel is mapped to ‘rbf’ , Radial Basis Function Kernel, the only

<a href="https://www.codecogs.com/eqnedit.php?latex=f_j&space;=&space;\textrm{similarity}(x,&space;l^{(j)})&space;=&space;\exp{\Big(-\frac{||x-l^{(j)}||^2}{2\sigma^2}&space;\Big)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_j&space;=&space;\textrm{similarity}(x,&space;l^{(j)})&space;=&space;\exp{\Big(-\frac{||x-l^{(j)}||^2}{2\sigma^2}&space;\Big)}" title="f_j = \textrm{similarity}(x, l^{(j)}) = \exp{\Big(-\frac{||x-l^{(j)}||^2}{2\sigma^2} \Big)}" /></a>


We can map model as each data point represents a landmark. In this case, we turn `n` features to `m` features.
Since it turns to the data size as number of features, SVM is probably not suitable for large size data.



## SVM vs Logistic Regression

Many SVM packages have built in multi-class classification. Otherwise use one-vs-all method. For `K` classes, train `K` SVMs, each identifies if y = 1 for class {1,2,...K}. We pick class i for largest θᵀx_i.


The main differences between SVM and Logistic regression (LR) [[Georgios Drakos]][Support Vector Machine vs Logistic Regression]:

* SVM try to maximize the margin between the closest support vectors while LR optimizes the posterior class probability (log likelihood function). Thus, SVM find a solution which is as fare as possible for the two categories while LR has not this property.
* LR is more sensitive to outliers than SVM because the cost function of LR diverges faster than those of SVM.
* Logistic Regression produces probabilistic values while SVM produces 1 or 0.


Try logistic regression first and see how you do with that simpler model. If logistic regression fails and you have reason to believe your data won’t be linearly separable, try an SVM with a non-linear kernel like a Radial Basis Function (RBF). See the comparison provided by Andrew's Ng's Machine learning coursera class

![LR_vs_SVM](images/LR_vs_SVM.png)





## Quiz

[25 Questions to test a Data Scientist on Support Vector Machines](https://www.analyticsvidhya.com/blog/2017/10/svm-skilltest/)







## Reference



[Support Vector Machine vs Logistic Regression]: https://www.knowledgehut.com/blog/data-science/support-vector-machines-in-machine-learning
[[Georgios Drakos] Support Vector Machine vs Logistic Regression](https://www.knowledgehut.com/blog/data-science/support-vector-machines-in-machine-learning)




[Support Vector Machines in Machine Learning]: https://www.knowledgehut.com/blog/data-science/support-vector-machines-in-machine-learning
[[Priyankur Sarkar] Support Vector Machines in Machine Learning](https://www.knowledgehut.com/blog/data-science/support-vector-machines-in-machine-learning)


[Support Vector Machine — Introduction to Machine Learning Algorithms]: https://towardsdatascience.com/support-vector-machine-introduction-to-machine-learning-algorithms-934a444fca47
[[Rohith Gandhi] Support Vector Machine — Introduction to Machine Learning Algorithms](https://towardsdatascience.com/support-vector-machine-introduction-to-machine-learning-algorithms-934a444fca47)


[Loss Function(Part III): Support Vector Machine]: https://towardsdatascience.com/optimization-loss-function-under-the-hood-part-iii-5dff33fa015d
[[Shuyu Luo] Loss Function(Part III): Support Vector Machine](https://towardsdatascience.com/optimization-loss-function-under-the-hood-part-iii-5dff33fa015d)

