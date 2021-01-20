
# Classification 




## Metric

### Precision and Recall

In most cases, there are no perfect classifiers. A good common question is which metric should we use for model selection, precision or recall? Classifier to have high True Positive Rate (TPR) or False Positive Rate (FPR)? It depends on domain and our business goal.

Call the definition:

```
             * Truth *
   ------- | Pos | Neg |
  Pred Pos | TP  | FP  |
  Pred Neg | FN  | TN  |
```
The relevant metrics are 
```
precision = TP/(TP+FP), recall = TP/(TP+FN)
```
and
```
TPR = recall, FPR = FP/(FP+TN)
```
Each probability threshold in classifier determiones a set of the above metrics. Also we can define review rate 
```
review rate = N(prob > threshold)/N
```
where `N` is the number of data points.

Here is the post to list some examples whrn precision is important and when recall is important ? [[StackExchange-1]][When is precision more important over recall?] [[StackExchange-2]][How to determine the optimal threshold for a classifier and generate ROC curve?]. Depends on whhcih we want to minimize, FP or FN costs more? Note it has been mentioned in the post that you could have 100% recall yet have a useless model: if your model always outputs a positive prediction, it would have 100% recall but be completely uninformative.

Here I just summarize the answers in the post and list in the following:

1. For rare cancer data modeling, a false negative is usually more disastrous than a false positive for preliminary diagnoses. We want to minimize FN to have higher recall. So **Recall** is a better measure than precision.

2. For YouTube recommendations, false-negatives is less of a concern. **Precision** is better here.

3. Image a lot of free customers register in our websites every daily. The customer call center team doesn't care to call a guy that is not going to buy (so FP is not important) but for us is very important that all of them with high temperature are always in my selection. That means that a model needs to have a high **Recall**.

4. For spam filtering, a false positive occurs when spam filtering or spam blocking techniques wrongly classify a legitimate email message as spam and, as a result, interferes with its delivery and we may lose important messgaes. Therefore we prefer more FP over more FP, and **Precision** is more important.

5. Let us say that a machine learning model is created to predict whether a certain day is a good day to launch satellites or not based on the weather. If the model accidentally predicts that a good day to launch satellites is bad (FN), we miss the chance to launch. This is not such a big deal. However, if the model predicts that it is a good day, but it is actually a bad day to launch the satellites (FP) then the satellites may be destroyed and the cost of damages will be in the billions. This is a case **Precision** is more important.

6. In the case of airport security, where a safety risk is the positive class, we want to make sure that every potential safety risk is investigated. In this case, we will have high **Recall** at the expense of precision (a lot of bags where there are no safety hazards will be investigated).


If there is no external concern about low TPR or high FPR, one option is to weight them equally by choosing the threshold that maximizes TPR-FPT, or use `F1 score`

```
F1 = Precision * Recall/(Precision + Recall)
```


`a(i)` can be interpreted as **similarity**; the smaller value, the better the clustering.

Next we can define **dissimilarity** by considering the mean distance from `i` to all points in other clusters where `i` is not in:

<a href="https://www.codecogs.com/eqnedit.php?latex={\displaystyle&space;b(i)=\min&space;_{k\neq&space;i}{\frac&space;{1}{|C_{k}|}}\sum&space;_{j\in&space;C_{k}}d(i,j)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\displaystyle&space;b(i)=\min&space;_{k\neq&space;i}{\frac&space;{1}{|C_{k}|}}\sum&space;_{j\in&space;C_{k}}d(i,j)}" title="{\displaystyle b(i)=\min _{k\neq i}{\frac {1}{|C_{k}|}}\sum _{j\in C_{k}}d(i,j)}" /></a>



The silhouette score can be computed using Scikit-learn. [The sklearn page](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html) shows an excellent example. From our bare eyes, the best outcome is given by 4 clusters. We can visualize silhouette score `s(i)` for each data point in different clusters:

![silhouette_n_2](images/silhouette_n2.png)
![silhouette_n_3](images/silhouette_n3.png)
![silhouette_n_4](images/silhouette_n4.png)
![silhouette_n_5](images/silhouette_n5.png)
![silhouette_n_6](images/silhouette_n6.png)

and we see the 4 clusters (execpet for 2 clusters) certainly gives the highest silhouette score from the page.
```
For n_clusters = 2 The average silhouette_score is : 0.7049787496083262 
For n_clusters = 3 The average silhouette_score is : 0.5882004012129721
For n_clusters = 4 The average silhouette_score is : 0.6505186632729437
For n_clusters = 5 The average silhouette_score is : 0.56376469026194
For n_clusters = 6 The average silhouette_score is : 0.4504666294372765
```



## Reference


[When is precision more important over recall?]: https://datascience.stackexchange.com/questions/30881/when-is-precision-more-important-over-recall
[[StackExchange-1] When is precision more important over recall?](https://datascience.stackexchange.com/questions/30881/when-is-precision-more-important-over-recall)


[How to determine the optimal threshold for a classifier and generate ROC curve?]: https://stats.stackexchange.com/questions/123124/how-to-determine-the-optimal-threshold-for-a-classifier-and-generate-roc-curve#:~:text=A%20really%20easy%20way%20to,positive%20rate(fpr)%20overlap.
[[StackExchange-2] How to determine the optimal threshold for a classifier and generate ROC curve?](https://stats.stackexchange.com/questions/123124/how-to-determine-the-optimal-threshold-for-a-classifier-and-generate-roc-curve#:~:text=A%20really%20easy%20way%20to,positive%20rate(fpr)%20overlap.)

