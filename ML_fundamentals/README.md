
# Machine Learning Fundamentals 



This space is dedicated to some fundamental theory on Machine Learning.

Some recommended summary:

* Jin Yan, [Machine Learning Questions](https://yanjin.space/blog/2020/2020305.html)
* Knowledge hut, Machine learning series. e.g. [Support Vector Machines in Machine Learning](https://www.knowledgehut.com/blog/data-science/support-vector-machines-in-machine-learning)


## Data Sparsity

**Rakshith Gowda Kodihalli** [[Quora: What is data sparsity?]][What is data sparsity?]: Any data which as very large zero value and very little no zero value then it is called sparse data. And the way in which data is saved is sparse matrix. The example is like:

| c1 | c2 | c3 | c4 | c5 |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 5 | 0 |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 |
| 3 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 |

In this we can only save key ,value, location only for non zero elements:
`(c1, R5): 5`, `(c3, R3): 1`, `(c4, R1): 5`.

### How do you deal with training data with high sparsity?

**Tony Petrov**: Dimensionality reduction: PCA and SVD. It could also be the case that you’ve one-hot encoded variables which are better represented by embeddings.  **Information value scores** of each variable is important as high dimensionality data is bound to have a lot of collinear variables which will break most matrix based algorithms, also look at the p-values of each variable and remove the least important ones.

[What is data sparsity?]: https://www.quora.com/What-is-data-sparsity
[[Quora: What is data sparsity?] What is data sparsity?](https://www.quora.com/What-is-data-sparsity)

[How do you deal with training data with high sparsity and large number of features (~1k) in machine learning?]: https://www.quora.com/How-do-you-deal-with-training-data-with-high-sparsity-and-large-number-of-features-1k-in-machine-learning
[[Quora: How do you deal with training data with high sparsity and large number of features (~1k) in machine learning?] How do you deal with training data with high sparsity and large number of features (~1k) in machine learning?](https://www.quora.com/How-do-you-deal-with-training-data-with-high-sparsity-and-large-number-of-features-1k-in-machine-learning)

## Why only L1 and L2 regularization but not other norms?

The `Lq` norms with q < 1 is not convex, so difficult to optimize [Cross Validated: Why do we only see L1 and L2 regularization but not other norms?
](https://stats.stackexchange.com/questions/269298/why-do-we-only-see-l-1-and-l-2-regularization-but-not-other-norms). L1 and L2 corresponds to Manhattan norm and Euclidean norm of complex numbers [wiki](https://en.wikipedia.org/wiki/Norm_(mathematics)). Other norm (credit from the book: [Statistical Learning with Sparsity](http://web.stanford.edu/~hastie/StatLearnSparsity/)):


![Lq_regularization](images/Lq_regularization.png)


## Entropy, Cross-Entropy, and KL-Divergence 

### a. Entropy

Given probability distribution p, it tells us how unpredictable the probability distribution is.

<a href="https://www.codecogs.com/eqnedit.php?latex=H(p)&space;=&space;-&space;\sum_i&space;p_i&space;\log&space;p_i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H(p)&space;=&space;-&space;\sum_i&space;p_i&space;\log&space;p_i" title="H(p) = - \sum_i p_i \log p_i" /></a>

Say, a fair coin, `p(H) = p(T) = 1/2`, then `H = log2`. But if `p(H) = 0.99`, then `H ~ 0`, i.e. less uncertainty.

### b. Cross-Entropy

Cross-Entropy is a function of both true probability distribution `p` and predicted probability distribution `q`:

<a href="https://www.codecogs.com/eqnedit.php?latex=H(p,&space;q)&space;=&space;-&space;\sum_i&space;p_i&space;\log&space;q_i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H(p,&space;q)&space;=&space;-&space;\sum_i&space;p_i&space;\log&space;q_i" title="H(p, q) = - \sum_i p_i \log q_i" /></a>

If our predictions are perfect, that is the predicted distribution is equal to the true distribution, then the cross-entropy is simply equal to entropy. But, if the distributions differ, then the cross-entropy will be greater than the entropy by some number of bits. This amount by which the cross-entropy exceeds the entropy is called the **Relative Entropy** or more commonly known as the **Kullback-Leibler Divergence (KL Divergence)**. (see [Aakarsh Yelisetty: Entropy, Cross-Entropy, and KL-Divergence Explained!](https://towardsdatascience.com/entropy-cross-entropy-and-kl-divergence-explained-b09cdae917a))



### c. KL-Divergence

Kullback-Leibler Divergence measures information lost.

```
Cross_entropy = Entropy + KL-divergence
```

<a href="https://www.codecogs.com/eqnedit.php?latex=D_{KL}(p||q)&space;=&space;\big(-\sum_i&space;p_i&space;\log&space;q_i&space;\big)&space;-&space;\big(&space;-\sum_i&space;p_i&space;\log&space;p_i&space;\big)&space;=&space;\sum_i&space;p_i&space;\log&space;\Big(&space;\frac{p_i}{q_i}\Big)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D_{KL}(p||q)&space;=&space;\big(-\sum_i&space;p_i&space;\log&space;q_i&space;\big)&space;-&space;\big(&space;-\sum_i&space;p_i&space;\log&space;p_i&space;\big)&space;=&space;\sum_i&space;p_i&space;\log&space;\Big(&space;\frac{p_i}{q_i}\Big)" title="D_{KL}(p||q) = \big(-\sum_i p_i \log q_i \big) - \big( -\sum_i p_i \log p_i \big) = \sum_i p_i \log \Big( \frac{p_i}{q_i}\Big)" /></a>


The [blog: Kullback-Leibler Divergence Explained](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) shows using KL divergence to minimize how much information loss we have when approximating a distribution. We can combine KL divergence with neural networks allows us to learn very complex approximating distribution for our data. A common approach to this is called a "Variational Autoencoder" which learns the best way to approximate the information in a data set.

The [blog: Intuitive Guide to Understanding KL Divergence](https://towardsdatascience.com/light-on-math-machine-learning-intuitive-guide-to-understanding-kl-divergence-2b382ca2b2a8) shows an example using KL-divergence to interpret approximation to a true distribution with the bionomial and uniform distribition.


## Convex Function

The strict definition of a convert function is

<a href="https://www.codecogs.com/eqnedit.php?latex=f(tx_1&space;&plus;&space;(1-t)x_2)&space;\le&space;tf(x_1)&space;&plus;&space;(1-t)f(x_2),&space;\&space;0&space;<&space;t&space;<&space;1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(tx_1&space;&plus;&space;(1-t)x_2)&space;\le&space;tf(x_1)&space;&plus;&space;(1-t)f(x_2),&space;\&space;0&space;<&space;t&space;<&space;1" title="f(tx_1 + (1-t)x_2) \le tf(x_1) + (1-t)f(x_2), \ 0 < t < 1" /></a>

Note, in a convex function, the local minimum global minimum. See the [proof](https://planetmath.org/localminimumofconvexfunctionisnecessarilyglobal).

## Newton Method


It is a method for finding the root of a function, rather than its maxima or minima. This means that, if the problem satisfies the constraints of Newton’s method, we can find `x` for which `f(x)=0`. **NOT** `f'(x)=0`, as was the case for gradient descent. Therefore, we, apply Newton’s method on the **derivative** `f'(x)` of the cost function (`f''(x)`, second-order derivatives), not on the cost function itself [[Gabriele De Luca]][Gradient Descent vs. Newton’s Gradient Descent], [[Stack overflow: What is the difference between Gradient Descent and Newton's Gradient Descent?]][What is the difference between Gradient Descent and Newton's Gradient Descent?].

<a href="https://www.codecogs.com/eqnedit.php?latex=x_{n&plus;1}&space;=&space;x_n&space;&plus;&space;\frac{f^{\prime}(x_n)}{f^{\prime&space;\prime}(x_n)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{n&plus;1}&space;=&space;x_n&space;&plus;&space;\frac{f^{\prime}(x_n)}{f^{\prime&space;\prime}(x_n)}" title="x_{n+1} = x_n + \frac{f^{\prime}(x_n)}{f^{\prime \prime}(x_n)}" /></a>

For multivariate, `f''(x)` turns to the Hessian matrix. For example, in [[Cross Validated: Why is Newton's method not widely used in machine learning?]][Why is Newton's method not widely used in machine learning?], assume <a href="https://www.codecogs.com/eqnedit.php?latex=f&space;=&space;f(x,y)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f&space;=&space;f(x,y)" title="f = f(x,y)" /></a>, then

<a href="https://www.codecogs.com/eqnedit.php?latex=x_{n&plus;1}&space;=&space;x_n&space;-&space;[\bold&space;H&space;f]^{-1}f^{\prime}(x_n)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{n&plus;1}&space;=&space;x_n&space;-&space;[\bold&space;H&space;f]^{-1}f^{\prime}(x_n)" title="x_{n+1} = x_n - [\bold H f]^{-1}f^{\prime}(x_n)" /></a>

### a. Primary difference

1. The first difference lies in the fact that gradient descent is parametric according to the learning rate `\alpha`. Newton’s method isn’t parametric, which means that we can apply it without worrying for hyperparameter optimization. (A parametric version of Newton’s method also exists, in truth, but it only applies in cases for which we operate with a polynomial function with multiple roots.)

2. The second difference has to do with the cost function on which we apply the algorithm. Newton’s method has **stronger constraints in terms of the differentiability of the function than gradient descent**. If the second derivative of the function is undefined in the function’s root, then we can apply gradient descent on it but not Newton’s method.

3. The third difference consists of the behavior around stationary points. If gradient descent encounters a stationary point during iteration, the program continues to run, albeit the parameters don’t update. Newton’s method, however, we have `f'(x) = f''(x) = 0`. The program that runs it would therefore terminate.


### b. Why is Newton's method not widely used in machine learning?

The analytic expression for the second derivative is often complicated or intractable, requiring a lot of computation. Numerical methods for computing the second derivative also require a lot of computation, `O(N^2)`, where `N` is the number of features. On the other hand, computing the gradient is only `O(N)`. But the next step to invert Hessian, which is `O(N^3)`. So while computing the Hessian is expensive, inverting it or solving least squares is often even worse.

Newton method attracts to saddle points and saddle points are common in machine learning. As an example in [[Cross Validated: Why is Newton's method not widely used in machine learning?]][Why is Newton's method not widely used in machine learning?], if 

<a href="https://www.codecogs.com/eqnedit.php?latex=f&space;=&space;f(x,y)&space;=&space;x^2-y^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f&space;=&space;f(x,y)&space;=&space;x^2-y^2" title="f = f(x,y) = x^2-y^2" /></a>

you see how the Newton method led you to the saddle point at `x = y = 0`. In contrast, the gradient descent method will not lead to the saddle point. The gradient is zero at the saddle point, but a tiny step out would pull the optimization away as you can see from the gradient above - its gradient on y-variable is negative.



[Why is Newton's method not widely used in machine learning?]: https://stats.stackexchange.com/questions/253632/why-is-newtons-method-not-widely-used-in-machine-learning
[[Cross Validated: Why is Newton's method not widely used in machine learning?] Why is Newton's method not widely used in machine learning?](https://stats.stackexchange.com/questions/253632/why-is-newtons-method-not-widely-used-in-machine-learning)

[Gradient Descent vs. Newton’s Gradient Descent]: https://www.baeldung.com/cs/gradient-descent-vs-newtons-gradient-descent
[[Gabriele De Luca] Gradient Descent vs. Newton’s Gradient Descent](https://www.baeldung.com/cs/gradient-descent-vs-newtons-gradient-descent)

[What is the difference between Gradient Descent and Newton's Gradient Descent?]: https://stackoverflow.com/questions/12066761/what-is-the-difference-between-gradient-descent-and-newtons-gradient-descent
[[Stack overflow: What is the difference between Gradient Descent and Newton's Gradient Descent?] What is the difference between Gradient Descent and Newton's Gradient Descent?](https://stackoverflow.com/questions/12066761/what-is-the-difference-between-gradient-descent-and-newtons-gradient-descent)
