
# Softmax Regression


Softmax regression (or **Multinomial Logistic Regression**, **Maximum Entropy Classifier**, or just **Multi-class Logistic Regression** [[KDNuggets]][What is Softmax Regression and How is it Related to Logistic Regression?]) is a generalization of logistic regression to the case where we want to handle multiple classes. In logistic regression we assumed that the labels were binary: y(i)∈{0,1}. We used such a classifier to distinguish between two kinds of hand-written digits. Softmax regression allows us to handle y(i)∈{1,…,K} where K is the number of classes, i.e. multi-class classification.

The following content are from [[UFLDL Tutorial]][Softmax Regression].

## Binary Classification

For binary case, the hypothesis in logistic regression is


<a href="https://www.codecogs.com/eqnedit.php?latex=h_{\theta}(x_i)&space;=&space;P(y_i|\theta,&space;\bold{x}_i)&space;=\frac{1}{1&plus;e^{-\theta^T&space;\bold{x}_i}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?h_{\theta}(x_i)&space;=&space;P(y_i|\theta,&space;\bold{x}_i)&space;=\frac{1}{1&plus;e^{-\theta^T&space;\bold{x}_i}}" title="h_{\theta}(x_i) = P(y_i|\theta, \bold{x}_i) =\frac{1}{1+e^{-\theta^T \bold{x}_i}}" /></a>

The cost fucntion is cross entropy

<a href="https://www.codecogs.com/eqnedit.php?latex=C(\theta)&space;=&space;-&space;\sum^m_{i=1}&space;\Big[&space;y_i&space;\log&space;h_{\theta}(x_i)&space;&plus;&space;(1-y_i)&space;\log&space;(1-h_{\theta}(x_i))&space;\Big]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C(\theta)&space;=&space;-&space;\sum^m_{i=1}&space;\Big[&space;y_i&space;\log&space;h_{\theta}(x_i)&space;&plus;&space;(1-y_i)&space;\log&space;(1-h_{\theta}(x_i))&space;\Big]" title="C(\theta) = - \sum^m_{i=1} \Big[ y_i \log h_{\theta}(x_i) + (1-y_i) \log (1-h_{\theta}(x_i)) \Big]" /></a>


## Multiclass Classification

In the softmax regression setting, the hypothesis hθ(x) takes the following form:

<a href="https://www.codecogs.com/eqnedit.php?latex=h_{\theta}(x_i)&space;=&space;\begin{bmatrix}&space;P(y_i=1|\theta,&space;\bold{x}_i)&space;\\&space;P(y_i=2|\theta,&space;\bold{x}_i)&space;\\&space;\vdots&space;\\&space;P(y_i=K|\theta,&space;\bold{x}_i)&space;\end{bmatrix}&space;=&space;\frac{1}{\sum^K_{j=1}&space;\exp{&space;\big(&space;\theta^{(j)T}&space;\bold{x}_i&space;\big)}&space;}\begin{bmatrix}&space;\exp{\big(&space;\theta^{(1)T}&space;\bold{x}_i&space;\big)}&space;\\&space;\exp{&space;\big(&space;\theta^{(2)T}&space;\bold{x}_i&space;\big)&space;}&space;\\&space;\vdots&space;\\&space;\exp{&space;\big(&space;\theta^{(K)T}&space;\bold{x}_i&space;\big)&space;}&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?h_{\theta}(x_i)&space;=&space;\begin{bmatrix}&space;P(y_i=1|\theta,&space;\bold{x}_i)&space;\\&space;P(y_i=2|\theta,&space;\bold{x}_i)&space;\\&space;\vdots&space;\\&space;P(y_i=K|\theta,&space;\bold{x}_i)&space;\end{bmatrix}&space;=&space;\frac{1}{\sum^K_{j=1}&space;\exp{&space;\big(&space;\theta^{(j)T}&space;\bold{x}_i&space;\big)}&space;}\begin{bmatrix}&space;\exp{\big(&space;\theta^{(1)T}&space;\bold{x}_i&space;\big)}&space;\\&space;\exp{&space;\big(&space;\theta^{(2)T}&space;\bold{x}_i&space;\big)&space;}&space;\\&space;\vdots&space;\\&space;\exp{&space;\big(&space;\theta^{(K)T}&space;\bold{x}_i&space;\big)&space;}&space;\end{bmatrix}" title="h_{\theta}(x_i) = \begin{bmatrix} P(y_i=1|\theta, \bold{x}_i) \\ P(y_i=2|\theta, \bold{x}_i) \\ \vdots \\ P(y_i=K|\theta, \bold{x}_i) \end{bmatrix} = \frac{1}{\sum^K_{j=1} \exp{ \big( \theta^{(j)T} \bold{x}_i \big)} }\begin{bmatrix} \exp{\big( \theta^{(1)T} \bold{x}_i \big)} \\ \exp{ \big( \theta^{(2)T} \bold{x}_i \big) } \\ \vdots \\ \exp{ \big( \theta^{(K)T} \bold{x}_i \big) } \end{bmatrix}" /></a>


Now `θ` is a n-by-K matrix (`n` features and `K` classes) obtained by

<a href="https://www.codecogs.com/eqnedit.php?latex=\theta&space;=&space;\begin{pmatrix}&space;\begin{pmatrix}&space;|&space;\\&space;\theta^{(1)}&space;\\&space;|&space;\end{pmatrix}&space;&&space;\begin{pmatrix}&space;|&space;\\&space;\theta^{(2)}&space;\\&space;|&space;\end{pmatrix}&space;&&space;\cdots&space;&&space;\begin{pmatrix}&space;|&space;\\&space;\theta^{(K)}&space;\\&space;|&space;\end{pmatrix}&space;\end{pmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\theta&space;=&space;\begin{pmatrix}&space;\begin{pmatrix}&space;|&space;\\&space;\theta^{(1)}&space;\\&space;|&space;\end{pmatrix}&space;&&space;\begin{pmatrix}&space;|&space;\\&space;\theta^{(2)}&space;\\&space;|&space;\end{pmatrix}&space;&&space;\cdots&space;&&space;\begin{pmatrix}&space;|&space;\\&space;\theta^{(K)}&space;\\&space;|&space;\end{pmatrix}&space;\end{pmatrix}" title="\theta = \begin{pmatrix} \begin{pmatrix} | \\ \theta^{(1)} \\ | \end{pmatrix} & \begin{pmatrix} | \\ \theta^{(2)} \\ | \end{pmatrix} & \cdots & \begin{pmatrix} | \\ \theta^{(K)} \\ | \end{pmatrix} \end{pmatrix}" /></a>


The cost function is

<a href="https://www.codecogs.com/eqnedit.php?latex=C(\theta)&space;=&space;-&space;\sum^m_{i=1}&space;\sum^K_{j=1}\bold{I}(y_i=j)\log\big(&space;h_{\theta}(x_i)&space;\big)&space;=&space;-&space;\sum^m_{i=1}&space;\sum^K_{j=1}&space;\bold{I}(y_i=j)\log\big(&space;\frac{e^{\theta^{(j)T}\bold{x}_i}}{\sum^K_{j=1}e^{\theta^{(j)T}\bold{x}_i}}&space;\big)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C(\theta)&space;=&space;-&space;\sum^m_{i=1}&space;\sum^K_{j=1}\bold{I}(y_i=j)\log\big(&space;h_{\theta}(x_i)&space;\big)&space;=&space;-&space;\sum^m_{i=1}&space;\sum^K_{j=1}&space;\bold{I}(y_i=j)\log\big(&space;\frac{e^{\theta^{(j)T}\bold{x}_i}}{\sum^K_{j=1}e^{\theta^{(j)T}\bold{x}_i}}&space;\big)" title="C(\theta) = - \sum^m_{i=1} \sum^K_{j=1}\bold{I}(y_i=j)\log\big( h_{\theta}(x_i) \big) = - \sum^m_{i=1} \sum^K_{j=1} \bold{I}(y_i=j)\log\big( \frac{e^{\theta^{(j)T}\bold{x}_i}}{\sum^K_{j=1}e^{\theta^{(j)T}\bold{x}_i}} \big)" /></a>

where `I = 1` for y = j; otherwise `I=0`. 

The high-level workflow of logisitc and softmax regressions are summarized below (credit from [[KDNuggets]][What is Softmax Regression and How is it Related to Logistic Regression?])

![](workflow.png)


## Reference


[What is Softmax Regression and How is it Related to Logistic Regression?]: https://www.kdnuggets.com/2016/07/softmax-regression-related-logistic-regression.html#:~:text=Softmax%20Regression%20(synonyms%3A%20Multinomial%20Logistic,the%20classes%20are%20mutually%20exclusive).
[[KDNuggets] What is Softmax Regression and How is it Related to Logistic Regression?](https://www.kdnuggets.com/2016/07/softmax-regression-related-logistic-regression.html#:~:text=Softmax%20Regression%20(synonyms%3A%20Multinomial%20Logistic,the%20classes%20are%20mutually%20exclusive).)




[Softmax Regression]: http://deeplearning.stanford.edu/tutorial/supervised/SoftmaxRegression/support-vector-machines-in-machine-learning
[[UFLDL Tutorial] Softmax Regression](http://deeplearning.stanford.edu/tutorial/supervised/SoftmaxRegression/)


