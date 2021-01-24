
# Decision Tree 




## How To Interpret Probability in Tree?

In Prof. Nando de Freitas UBC Machine Learning class, he shows a picture how probability works in a given decision tree:

![decision_tree](images/layer_probability.png)

Note even on the leaves, there exists data noise so we still see various class distribution.


## How to Select Feature for Split?

### Information gain

Given a split way of features, calculate entropy for root and its childs. The tree split is to maximize reduction of the entropy, which is defined as **information gain**. Given a class, the entropy defines

<a href="https://www.codecogs.com/eqnedit.php?latex=H(p,n)&space;=&space;-p\log&space;p&space;-n\log&space;n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H(p,n)&space;=&space;-p\log&space;p&space;-n\log&space;n" title="H(p,n) = -p\log p -n\log n" /></a>

where `p` and `n` are probability of positive and negative events

<a href="https://www.codecogs.com/eqnedit.php?latex=p&space;=&space;\frac{N_p}{N_p&plus;N_n},&space;\&space;n&space;=&space;\frac{N_n}{N_p&plus;N_n}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p&space;=&space;\frac{N_p}{N_p&plus;N_n},&space;\&space;n&space;=&space;\frac{N_n}{N_p&plus;N_n}" title="p = \frac{N_p}{N_p+N_n}, \ n = \frac{N_n}{N_p+N_n}" /></a>

Then we can calculate **Expected Entropy** (EH) remaining after trying attribute `A` (with branches i=1,2,...,K) in childs as

<a href="https://www.codecogs.com/eqnedit.php?latex=EH(A)&space;=&space;\sum^K_{i=1}&space;H(p_i,&space;n_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?EH(A)&space;=&space;\sum^K_{i=1}&space;H(p_i,&space;n_i)" title="EH(A) = \sum^K_{i=1} H(p_i, n_i)" /></a>

The information gain is `H(p,n) - EH(A)` for attribute `A`, where `H(p,n)` is on root. Below is an example

![example_information_gain](images/example_information_gain.png)

Later information gain leads to less homogeneity on class distributions. See examples below: 

![split_example](images/split_example.png)

We can see the larger information gain split makes better classification.


## Reference


[When is precision more important over recall?]: https://datascience.stackexchange.com/questions/30881/when-is-precision-more-important-over-recall
[[StackExchange-1] When is precision more important over recall?](https://datascience.stackexchange.com/questions/30881/when-is-precision-more-important-over-recall)


[How to determine the optimal threshold for a classifier and generate ROC curve?]: https://stats.stackexchange.com/questions/123124/how-to-determine-the-optimal-threshold-for-a-classifier-and-generate-roc-curve#:~:text=A%20really%20easy%20way%20to,positive%20rate(fpr)%20overlap.
[[StackExchange-2] How to determine the optimal threshold for a classifier and generate ROC curve?](https://stats.stackexchange.com/questions/123124/how-to-determine-the-optimal-threshold-for-a-classifier-and-generate-roc-curve#:~:text=A%20really%20easy%20way%20to,positive%20rate(fpr)%20overlap.)

