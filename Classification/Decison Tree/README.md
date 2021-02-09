
# Decision Tree 




## How To Interpret Probability in Tree?

In Prof. Nando de Freitas [UBC Machine Learning class](https://www.youtube.com/watch?v=pLzE2Oh9QDI&list=PLE6Wd9FR--Ecf_5nCbnSQMHqORpiChfJf&index=31), he shows a picture how probability works in a given decision tree:

![decision_tree](images/layer_probability.png)

Note even on the leaves, there exists data noise so we still see various class distribution.


## How to Select Feature for Split?

Each time when we need to split, we need to choose an optimal attribute which can perform best. There are two ways to select optimal attributes:

1. Information gain 
2. Gini index. 

Higher information gain (entropy reduction) and lower Gini index means a better attribute used for split.

Note that there is no reason to use the same feature split on each level. See [[Cross Validated: Does decision tree need to use the same feature to split in the same layer?]][Does decision tree need to use the same feature to split in the same layer?]


### 1. Information gain

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


### 2. Gini Index

The Gini index defines (assume use attribute `A` to have K branches)

<a href="https://www.codecogs.com/eqnedit.php?latex=G(A)&space;=&space;1-&space;\sum^K_{i=1}&space;(p^2_i&space;&plus;&space;n^2_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?G(A)&space;=&space;1-&space;\sum^K_{i=1}&space;(p^2_i&space;&plus;&space;n^2_i)" title="G(A) = 1- \sum^K_{i=1} (p^2_i + n^2_i)" /></a>

**Smaller Gini index** means better attribute used to split tree. (Think about if A is perfect to classify positive and negatives, then `G(A)=0`.)

Note that there is no reason to use the same feature split on each level. See [[Cross Validated: Does decision tree need to use the same feature to split in the same layer?]][Does decision tree need to use the same feature to split in the same layer?]

### 3. Numeric Attribute

For numeric attributes, how do we determine the value to split in the decision tree? As a concrete example, supposed we have a dataset like
```
  humidity | play
   60      | yes
   80      | yes 
   63      | no
   81      | yes
   92      | no
   ...     | ...
```
For numeric attributes, we sort the attribute by value. Then above data become
```
  humidity | play
   54      | yes
   58      | yes 
   59      | yes
   60      | yes
   60      | yes
   62      | yes
   63      | no 
   80      | yes
   81      | yes
   89      | yes
   90      | no
   90      | no 
   90      | no
   92      | no
```
At root, the entropy (9 positive, 5 negative) is

<a href="https://www.codecogs.com/eqnedit.php?latex=H(\frac{9}{14},\frac{5}{14})=&space;-\big(\frac{9}{14}\log&space;\frac{9}{14}&space;&plus;&space;\frac{5}{14}\log&space;\frac{5}{14}&space;\big)&space;=&space;0.94" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H(\frac{9}{14},\frac{5}{14})=&space;-\big(\frac{9}{14}\log&space;\frac{9}{14}&space;&plus;&space;\frac{5}{14}\log&space;\frac{5}{14}&space;\big)&space;=&space;0.94" title="H(\frac{9}{14},\frac{5}{14})= -\big(\frac{9}{14}\log \frac{9}{14} + \frac{5}{14}\log \frac{5}{14} \big) = 0.94" /></a>


Suppose we are going to determine the humidity threshold split, and we have two ways:

* **way A**: if humidity > 62 
* **way B**: if humidity > 89

For **way A**, if humidity <= 62, 6 positive; humidity > 62, 3 positive and 5 negative

<a href="https://www.codecogs.com/eqnedit.php?latex=H_A&space;=&space;\frac{6}{14}H(\frac{6}{6},&space;0)&space;&plus;&space;\frac{8}{14}H(\frac{3}{8},&space;\frac{5}{8})&space;=&space;\frac{6}{14}&space;\times&space;0&space;&plus;&space;\frac{8}{14}\times&space;0.95&space;=&space;0.54" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_A&space;=&space;\frac{6}{14}H(\frac{6}{6},&space;0)&space;&plus;&space;\frac{8}{14}H(\frac{3}{8},&space;\frac{5}{8})&space;=&space;\frac{6}{14}&space;\times&space;0&space;&plus;&space;\frac{8}{14}\times&space;0.95&space;=&space;0.54" title="H_A = \frac{6}{14}H(\frac{6}{6}, 0) + \frac{8}{14}H(\frac{3}{8}, \frac{5}{8}) = \frac{6}{14} \times 0 + \frac{8}{14}\times 0.95 = 0.54" /></a>


For **way B**, if humidity <= 89, 9 positive and 1 negative; humidity > 89, 4 negative

<a href="https://www.codecogs.com/eqnedit.php?latex=H_B&space;=&space;\frac{10}{14}H(\frac{9}{10},&space;\frac{1}{10})&space;&plus;&space;\frac{4}{14}H(0,&space;\frac{4}{4})&space;=&space;\frac{10}{14}\times&space;0.47&space;&plus;&space;\frac{4}{14}&space;\times&space;0&space;=&space;0.33" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_B&space;=&space;\frac{10}{14}H(\frac{9}{10},&space;\frac{1}{10})&space;&plus;&space;\frac{4}{14}H(0,&space;\frac{4}{4})&space;=&space;\frac{10}{14}\times&space;0.47&space;&plus;&space;\frac{4}{14}&space;\times&space;0&space;=&space;0.33" title="H_B = \frac{10}{14}H(\frac{9}{10}, \frac{1}{10}) + \frac{4}{14}H(0, \frac{4}{4}) = \frac{10}{14}\times 0.47 + \frac{4}{14} \times 0 = 0.33" /></a>

We can see `I(B)` > `I(A)`, so we choose humidity=0.89 to split at this step.

## Decision Tree Regression

Detail refer to [here](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Regression/Decision%20Tree) and the post [[Saed Sayad]][Decision Tree - Regression].


## Feature Importance 

To evaluate feature importance, we calculate feature importance for each split, and sum of them. For attribute A, we look for all splits which use A to split. The invidual feature importance is 

<a href="https://www.codecogs.com/eqnedit.php?latex=FI(A,c)&space;=&space;\frac{N_{c}}{N}\big(&space;\textrm{impurity}_c-\frac{N_{c,l}}{N_c}\textrm{impurity}_l&space;-&space;\frac{N_{c,r}}{N_c}\textrm{impurity}_r&space;\big)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?FI(A,c)&space;=&space;\frac{N_{c}}{N}\big(&space;\textrm{impurity}_c-\frac{N_{c,l}}{N_c}\textrm{impurity}_l&space;-&space;\frac{N_{c,r}}{N_c}\textrm{impurity}_r&space;\big)" title="FI(A,c) = \frac{N_{c}}{N}\big( \textrm{impurity}_c-\frac{N_{c,l}}{N_c}\textrm{impurity}_l - \frac{N_{c,r}}{N_c}\textrm{impurity}_r \big)" /></a>

where `Nc` means the number of instances on the "current" node. As a concrete example, suppose we have built the following tree:

![feature_importance](images/feature_importance_tree.png)


## Reference


[Does decision tree need to use the same feature to split in the same layer?]: https://stats.stackexchange.com/questions/354030/does-decision-tree-need-to-use-the-same-feature-to-split-in-the-same-layer/451780#451780
[[Cross Validated: Does decision tree need to use the same feature to split in the same layer?] Does decision tree need to use the same feature to split in the same layer?](https://stats.stackexchange.com/questions/354030/does-decision-tree-need-to-use-the-same-feature-to-split-in-the-same-layer/451780#451780)


[Decision Tree - Regression]: https://www.saedsayad.com/decision_tree_reg.htm#:~:text=Decision%20tree%20builds%20regression%20or,decision%20nodes%20and%20leaf%20nodes.
[[Saed Sayad] Decision Tree - Regression](https://www.saedsayad.com/decision_tree_reg.htm#:~:text=Decision%20tree%20builds%20regression%20or,decision%20nodes%20and%20leaf%20nodes.)

