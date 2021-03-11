
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
](https://stats.stackexchange.com/questions/269298/why-do-we-only-see-l-1-and-l-2-regularization-but-not-other-norms). L1 and L2 corresponds to Manhattan norm and Euclidean norm of complex numbers [wiki](https://en.wikipedia.org/wiki/Norm_(mathematics)). Credit from the book: [Statistical Learning with Sparsity](http://web.stanford.edu/~hastie/StatLearnSparsity/)


![Lq_regularization](images/Lq_regularization.png)