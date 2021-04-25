
# Decision Tree 

Table of Contents:

* [Tree algorithms: ID3, C4.5 and CART](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Classification/Decison%20Tree#tree-algorithms-id3-c45-and-cart)
* [How To Interpret Probability in Tree?](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Classification/Decison%20Tree#how-to-interpret-probability-in-tree)
* [How to Select Feature for Split?](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Classification/Decison%20Tree#how-to-select-feature-for-split)
     * [A. Information gain](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Classification/Decison%20Tree#a-information-gain)
     * [B. Gini index](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Classification/Decison%20Tree#b-gini-index)
     * [C. Numeric Attribute](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Classification/Decison%20Tree#c-numeric-attribute)
* [Decision Tree Regression](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Classification/Decison%20Tree#decision-tree-regression)
* [Feature Importance](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Classification/Decison%20Tree#feature-importance)
* [How To Deal with Missing Values](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Classification/Decison%20Tree#how-to-deal-with-missing-values)


## Tree algorithms: ID3, C4.5 and CART

Decision tree algorithms [[synergy37AI]][Tree algorithms: ID3, C4.5, C5.0 and CART]:

* **ID3 (Iterative Dichotomiser 3)** creates a multiway tree, finding for each node (i.e. in a greedy manner) the categorical feature that will yield the largest information gain for **categorical** targets.

* **C4.5** is the successor to ID3 and removed the restriction that features must be categorical by dynamically defining a discrete attribute (based on **numerical** variables) that partitions the continuous attribute value into a discrete set of intervals.

* **CART (Classification and Regression Trees)** is very similar to C4.5, but it differs in that it supports numerical target variables (regression) and does not compute rule sets. CART constructs binary trees using the feature and threshold that yields the largest information gain at each node.


Nearly every decision tree example I've come across happens to be a binary tree. There seems an exception, CHAID, is not limited to binary trees. The reason is mainly a technical issue: if you don't restrict to binary choices, there are simply too many possibilities for the next split in the tree [[Cross Validated: Are decision trees almost always binary trees?]][Are decision trees almost always binary trees?].


## How To Interpret Probability in Tree?

In Prof. Nando de Freitas [UBC Machine Learning class](https://www.youtube.com/watch?v=pLzE2Oh9QDI&list=PLE6Wd9FR--Ecf_5nCbnSQMHqORpiChfJf&index=31), he shows a picture how probability works in a given decision tree:

![decision_tree](images/layer_probability.png)

**NOTE**: 
1. The above picture explicitly describes that tree-based algorithm is available **multi-class classification**.
2. Even on the leaves, there exists data noise so we still see various class distribution.


## How to Select Feature for Split?

Each time when we need to split, we need to choose an optimal attribute which can perform best. There are two ways to select optimal attributes:

1. Information gain 
2. Gini index. 

Higher information gain (entropy reduction) and lower Gini index means a better attribute used for split.

Note that there is no reason to use the same feature split on each level. See [[Cross Validated: Does decision tree need to use the same feature to split in the same layer?]][Does decision tree need to use the same feature to split in the same layer?]


### A. Information gain

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


### B. Gini index

The Gini index defines (assume use attribute `A` to have K branches)

<a href="https://www.codecogs.com/eqnedit.php?latex=G(A)&space;=&space;1-&space;\sum^K_{i=1}&space;(p^2_i&space;&plus;&space;n^2_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?G(A)&space;=&space;1-&space;\sum^K_{i=1}&space;(p^2_i&space;&plus;&space;n^2_i)" title="G(A) = 1- \sum^K_{i=1} (p^2_i + n^2_i)" /></a>

**Smaller Gini index** means better attribute used to split tree. (Think about if A is perfect to classify positive and negatives, then `G(A)=0`.)

Note that there is no reason to use the same feature split on each level. See [[Cross Validated: Does decision tree need to use the same feature to split in the same layer?]][Does decision tree need to use the same feature to split in the same layer?]

### C. Numeric Attribute

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

<a href="https://www.codecogs.com/eqnedit.php?latex=H(\frac{9}{14},\frac{5}{14})=&space;-\big(\frac{9}{14}\log&space;\frac{9}{14}&space;&plus;&space;\frac{5}{14}\log&space;\frac{5}{14}&space;\big)&space;=&space;0.94&space;\&space;\textrm{bits}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H(\frac{9}{14},\frac{5}{14})=&space;-\big(\frac{9}{14}\log&space;\frac{9}{14}&space;&plus;&space;\frac{5}{14}\log&space;\frac{5}{14}&space;\big)&space;=&space;0.94&space;\&space;\textrm{bits}" title="H(\frac{9}{14},\frac{5}{14})= -\big(\frac{9}{14}\log \frac{9}{14} + \frac{5}{14}\log \frac{5}{14} \big) = 0.94 \ \textrm{bits}" /></a>


Suppose we are going to determine the humidity threshold split, and we have two ways:

* **way A**: if humidity > 62 
* **way B**: if humidity > 89

For **way A**, if humidity <= 62, 6 positive; humidity > 62, 3 positive and 5 negative


<a href="https://www.codecogs.com/eqnedit.php?latex=H_A&space;=&space;\frac{6}{14}H(\frac{6}{6},&space;0)&space;&plus;&space;\frac{8}{14}H(\frac{3}{8},&space;\frac{5}{8})&space;=&space;\frac{6}{14}&space;\times&space;0&space;&plus;&space;\frac{8}{14}\times&space;0.95&space;=&space;0.54&space;\&space;\textrm{bits}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_A&space;=&space;\frac{6}{14}H(\frac{6}{6},&space;0)&space;&plus;&space;\frac{8}{14}H(\frac{3}{8},&space;\frac{5}{8})&space;=&space;\frac{6}{14}&space;\times&space;0&space;&plus;&space;\frac{8}{14}\times&space;0.95&space;=&space;0.54&space;\&space;\textrm{bits}" title="H_A = \frac{6}{14}H(\frac{6}{6}, 0) + \frac{8}{14}H(\frac{3}{8}, \frac{5}{8}) = \frac{6}{14} \times 0 + \frac{8}{14}\times 0.95 = 0.54 \ \textrm{bits}" /></a>


For **way B**, if humidity <= 89, 9 positive and 1 negative; humidity > 89, 4 negative

<a href="https://www.codecogs.com/eqnedit.php?latex=H_B&space;=&space;\frac{10}{14}H(\frac{9}{10},&space;\frac{1}{10})&space;&plus;&space;\frac{4}{14}H(0,&space;\frac{4}{4})&space;=&space;\frac{10}{14}\times&space;0.47&space;&plus;&space;\frac{4}{14}&space;\times&space;0&space;=&space;0.33&space;\&space;\textrm{bits}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_B&space;=&space;\frac{10}{14}H(\frac{9}{10},&space;\frac{1}{10})&space;&plus;&space;\frac{4}{14}H(0,&space;\frac{4}{4})&space;=&space;\frac{10}{14}\times&space;0.47&space;&plus;&space;\frac{4}{14}&space;\times&space;0&space;=&space;0.33&space;\&space;\textrm{bits}" title="H_B = \frac{10}{14}H(\frac{9}{10}, \frac{1}{10}) + \frac{4}{14}H(0, \frac{4}{4}) = \frac{10}{14}\times 0.47 + \frac{4}{14} \times 0 = 0.33 \ \textrm{bits}" /></a>

We can see `I(B)` > `I(A)`, so we choose humidity=0.89 to split at this step.

## Decision Tree Regression

Detail refer to [here](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/Regression/Decision%20Tree) and the post [[Saed Sayad]][Decision Tree - Regression].


## Feature Importance 

To evaluate feature importance, we calculate feature importance for each split, and sum of them. For `attribute A`, we look for all splits which use `A` to split. The invidual feature importance is  [[Sefik Ilkin Serengil]][Feature Importance in Decision Trees], [[Stacey Ronaghan]][The Mathematics of Decision Trees, Random Forest and Feature Importance in Scikit-learn and Spark]


<a href="https://www.codecogs.com/eqnedit.php?latex=FI(A|c)&space;=&space;\frac{N_{c}}{N}\big(&space;\textrm{impurity}_c-\frac{N_{c,l}}{N_c}\textrm{impurity}_l&space;-&space;\frac{N_{c,r}}{N_c}\textrm{impurity}_r&space;\big)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?FI(A|c)&space;=&space;\frac{N_{c}}{N}\big(&space;\textrm{impurity}_c-\frac{N_{c,l}}{N_c}\textrm{impurity}_l&space;-&space;\frac{N_{c,r}}{N_c}\textrm{impurity}_r&space;\big)" title="FI(A|c) = \frac{N_{c}}{N}\big( \textrm{impurity}_c-\frac{N_{c,l}}{N_c}\textrm{impurity}_l - \frac{N_{c,r}}{N_c}\textrm{impurity}_r \big)" /></a>

where `Nc` means the number of instances on the "current" node or level, and `N` is the total number of instances. `l` and `r` denote left and right child nodes. We can simply calculate as 

<a href="https://www.codecogs.com/eqnedit.php?latex=FI(A|c)&space;=&space;N_{c}\big(&space;\textrm{impurity}_c-N_{c,l}*\textrm{impurity}_l&space;-&space;N_{c,r}*\textrm{impurity}_r&space;\big)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?FI(A|c)&space;=&space;N_{c}\big(&space;\textrm{impurity}_c-N_{c,l}*\textrm{impurity}_l&space;-&space;N_{c,r}*\textrm{impurity}_r&space;\big)" title="FI(A|c) = N_{c}\big( \textrm{impurity}_c-N_{c,l}*\textrm{impurity}_l - N_{c,r}*\textrm{impurity}_r \big)" /></a>

and eventually all are divided by `N`. The `impurity` metric is **entropy** if **C4.5** algorithm adopted. It would be **Gini** if the algorithm were **CART** [[Sefik Ilkin Serengil]][Feature Importance in Decision Trees]. 

Keep in mind for lower impurity (say, the majority is positive), both entropy and Gini index are lower. If `attribute A` works well to split, parent has higher impurity whereas child has lower impurity, then higher `FI(A|c)`.  

As a concrete example, suppose we have built the following tree (using C4.5 algorithm with entropy) (credit from [[Sefik Ilkin Serengil]][Feature Importance in Decision Trees]):

![feature_importance](images/feature_importance_tree.png)

Notice that a feature can appear several times in a decision tree as a decision point. For example, the feature outlook appears 2 times in the decision tree in 2nd and 3rd level. sum of those individual decision points will be the feature importance of Outlook.

We follow the procedures from [[Sefik Ilkin Serengil]][Feature Importance in Decision Trees]

* 1st level of the decision tree: FI(**Humidity**|1st level) = 14x0.940 – 7×0.985 – 7×0.591 = 2.121.
* 2nd level of the decision tree: FI(**Outlook**|2nd level) = 7×0.985 – 4×0.811 = 3.651; FI(**Wind**|2nd level) = 7×0.591 – 3×0.918 = 1.390
* 3rd level of the decision tree: FI(**Wind**|3rd level) = 4×0.811 = 3.244, FI(**Outlook**|3rd level) = 3×0.918 = 2.754
* Results: 

  FI(**Humidity**) = FI(**Humidity**|1st level) = 2.121

  FI(**Outlook**) = FI(**Outlook**|2nd level) + FI(**Outlook**|3rd level) = 3.651 + 2.754 = 6.405

  FI(**Wind**) = FI(**Wind**|2nd level) + FI(**Wind**|3rd level) = 1.390 + 3.244 = 4.634

Then normalize FI by diving `N=14`. We have feature importance: `"Outlook" > "Wind" > "Humidity"`.


**NOTE** [[Tim Bock]][Decision Trees Are Usually Better Than Logistic Regression]: decision trees have their own potential for misinterpretation, with many people incorrectly assuming that the order with which predictors appear in a tree tells you something about their importance. Unfortunately, this is often not the case. For example, if you have two highly correlated predictors, only one of them may appear in the tree and which one it is will be a bit of a fluke.

The consequence of all of these strengths of logistic regression is that if you are doing an academic study and wanting to make conclusions about what **causes** what, logistic regression is often much better than a decision tree. However, if instead the goal is to either make a prediction, or describe the data, then logistic regression is often a poor choice.


## How To Deal with Missing Values

There are several methods used by various decision trees. Simply ignoring the missing values (like ID3 and other old algorithms does) or treating the missing values as another category (in case of a nominal feature) are not real handling missing values [[Cross Validated: How do decision tree learning algorithms deal with missing values]][How do decision tree learning algorithms deal with missing values]. 

By Towfik Alrazihi [[Quora: In simple language, how does C4.5 deal with missing values?]][In simple language, how does C4.5 deal with missing values?], the missing values:
* goes to the node which already has the biggest number of instances.
* goes to all children with diminished weights.
* Goes randomly to only single chlid node.

## Reference


[Are decision trees almost always binary trees?]: https://stats.stackexchange.com/questions/12187/are-decision-trees-almost-always-binary-trees#:~:text=Nearly%20every%20decision%20tree%20example,to%20be%20a%20binary%20tree.&text=From%20what%20I%20gather%2C%20CHAID,a%20single%20three%2Dway%20split.
[[Cross Validated: Are decision trees almost always binary trees?] Are decision trees almost always binary trees?](https://stats.stackexchange.com/questions/12187/are-decision-trees-almost-always-binary-trees#:~:text=Nearly%20every%20decision%20tree%20example,to%20be%20a%20binary%20tree.&text=From%20what%20I%20gather%2C%20CHAID,a%20single%20three%2Dway%20split.)


[Does decision tree need to use the same feature to split in the same layer?]: https://stats.stackexchange.com/questions/354030/does-decision-tree-need-to-use-the-same-feature-to-split-in-the-same-layer/451780#451780
[[Cross Validated: Does decision tree need to use the same feature to split in the same layer?] Does decision tree need to use the same feature to split in the same layer?](https://stats.stackexchange.com/questions/354030/does-decision-tree-need-to-use-the-same-feature-to-split-in-the-same-layer/451780#451780)


[How do decision tree learning algorithms deal with missing values]: https://stats.stackexchange.com/questions/96025/how-do-decision-tree-learning-algorithms-deal-with-missing-values-under-the-hoo
[[Cross Validated: How do decision tree learning algorithms deal with missing values] How do decision tree learning algorithms deal with missing values](https://stats.stackexchange.com/questions/96025/how-do-decision-tree-learning-algorithms-deal-with-missing-values-under-the-hoo)




[In simple language, how does C4.5 deal with missing values?]: https://www.quora.com/In-simple-language-how-does-C4-5-deal-with-missing-values
[[Quora: In simple language, how does C4.5 deal with missing values?] In simple language, how does C4.5 deal with missing values?](https://www.quora.com/In-simple-language-how-does-C4-5-deal-with-missing-values)

[Decision Tree - Regression]: https://www.saedsayad.com/decision_tree_reg.htm#:~:text=Decision%20tree%20builds%20regression%20or,decision%20nodes%20and%20leaf%20nodes.
[[Saed Sayad] Decision Tree - Regression](https://www.saedsayad.com/decision_tree_reg.htm#:~:text=Decision%20tree%20builds%20regression%20or,decision%20nodes%20and%20leaf%20nodes.)


[Feature Importance in Decision Trees]: https://sefiks.com/2020/04/06/feature-importance-in-decision-trees/
[[Sefik Ilkin Serengil] Feature Importance in Decision Trees](https://sefiks.com/2020/04/06/feature-importance-in-decision-trees/)


[The Mathematics of Decision Trees, Random Forest and Feature Importance in Scikit-learn and Spark]: https://towardsdatascience.com/the-mathematics-of-decision-trees-random-forest-and-feature-importance-in-scikit-learn-and-spark-f2861df67e3
[[Stacey Ronaghan] The Mathematics of Decision Trees, Random Forest and Feature Importance in Scikit-learn and Spark](https://towardsdatascience.com/the-mathematics-of-decision-trees-random-forest-and-feature-importance-in-scikit-learn-and-spark-f2861df67e3)


[Tree algorithms: ID3, C4.5, C5.0 and CART]: https://medium.datadriveninvestor.com/tree-algorithms-id3-c4-5-c5-0-and-cart-413387342164
[[synergy37AI] Tree algorithms: ID3, C4.5, C5.0 and CART](https://medium.datadriveninvestor.com/tree-algorithms-id3-c4-5-c5-0-and-cart-413387342164)


[Decision Trees Are Usually Better Than Logistic Regression]: https://www.displayr.com/decision-trees-are-usually-better-than-logistic-regression/
[[Tim Bock] Decision Trees Are Usually Better Than Logistic Regression](https://www.displayr.com/decision-trees-are-usually-better-than-logistic-regression/)