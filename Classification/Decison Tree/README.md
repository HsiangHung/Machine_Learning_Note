
# Decision Tree 




## How To Interpret Probability in Tree?

In Prof. Nando de Freitas [UBC Machine Learning class](https://www.youtube.com/watch?v=pLzE2Oh9QDI&list=PLE6Wd9FR--Ecf_5nCbnSQMHqORpiChfJf&index=31), he shows a picture how probability works in a given decision tree:

![decision_tree](images/layer_probability.png)

Note even on the leaves, there exists data noise so we still see various class distribution.


## How to Select Feature for Split?

### a. Information gain

Given a split way of features, calculate entropy for root and its childs. The tree split is to **maximize reduction of the entropy**, which is defined as **information gain**. Given a class, the entropy defines

<a href="https://www.codecogs.com/eqnedit.php?latex=H(p,n)&space;=&space;-p\log&space;p&space;-n\log&space;n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H(p,n)&space;=&space;-p\log&space;p&space;-n\log&space;n" title="H(p,n) = -p\log p -n\log n" /></a>

where `p` and `n` are probability of positive and negative events

<a href="https://www.codecogs.com/eqnedit.php?latex=p&space;=&space;\frac{N_p}{N_p&plus;N_n},&space;\&space;n&space;=&space;\frac{N_n}{N_p&plus;N_n}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p&space;=&space;\frac{N_p}{N_p&plus;N_n},&space;\&space;n&space;=&space;\frac{N_n}{N_p&plus;N_n}" title="p = \frac{N_p}{N_p+N_n}, \ n = \frac{N_n}{N_p+N_n}" /></a>

Then we can calculate **Expected Entropy** (EH) remaining after trying attribute `A` (with branches i=1,2,...,K types) in childs as

<a href="https://www.codecogs.com/eqnedit.php?latex=EH(A)&space;=&space;\sum^K_{i=1}&space;H(p_i,&space;n_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?EH(A)&space;=&space;\sum^K_{i=1}&space;H(p_i,&space;n_i)" title="EH(A) = \sum^K_{i=1} H(p_i, n_i)" /></a>

The information gain is `H(p,n) - EH(A)` for attribute `A`, where `H(p,n)` is on root. Below is an example (from Prof. Nando de Freitas UBC Machine Learning class). From the root to next level, which attribute should we use? `patrons` or food `type`?

![example_information_gain](images/example_information_gain.png)

We can see `I(patrons) > I(type)`, so we choose `patrons` to split data for enxt step (using `type` is not helpful to classification).

Later information gain leads to less homogeneity on class distributions. See examples below: 

![split_example](images/split_example.png)

We can see the larger information gain split makes better classification.


### b. Gini Index

The Gini index defines (assume use attribute `A` to have K branches)

<a href="https://www.codecogs.com/eqnedit.php?latex=G(A)&space;=&space;1-&space;\sum^K_{i=1}&space;(p^2_i&space;&plus;&space;n^2_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?G(A)&space;=&space;1-&space;\sum^K_{i=1}&space;(p^2_i&space;&plus;&space;n^2_i)" title="G(A) = 1- \sum^K_{i=1} (p^2_i + n^2_i)" /></a>

**Smaller Gini index** means better attribute used to split tree. (Think about if A is perfect to classify positive and negatives, then Gini = 0)

Note that there is no reason to use the same feature split on each level. See [[Cross Validated: Does decision tree need to use the same feature to split in the same layer?]][Does decision tree need to use the same feature to split in the same layer?]


## Reference


[Does decision tree need to use the same feature to split in the same layer?]: https://stats.stackexchange.com/questions/354030/does-decision-tree-need-to-use-the-same-feature-to-split-in-the-same-layer/451780#451780
[[Cross Validated: Does decision tree need to use the same feature to split in the same layer?] Does decision tree need to use the same feature to split in the same layer?](https://stats.stackexchange.com/questions/354030/does-decision-tree-need-to-use-the-same-feature-to-split-in-the-same-layer/451780#451780)


