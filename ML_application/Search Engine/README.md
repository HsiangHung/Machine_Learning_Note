
# Search Engine Optimization (SEO)

## Learning to Rank

Learning to Rank (LTR) is a class of techniques that apply supervised machine learning (ML) to solve ranking problems. The main difference between LTR and traditional supervised ML is this [[Nikhil Dandekar]][Intuitive explanation of Learning to Rank (and RankNet, LambdaRank and LambdaMART)]:

* Traditional ML solves a prediction problem (classification or regression) on a single instance at a time. E.g. if you are doing spam detection on email, you will look at all the features associated with that email and classify it as spam or not. The aim of traditional ML is to come up with a class (spam or no-spam) or a single numerical score for that instance.
* LTR solves a ranking problem on a list of items. The aim of LTR is to come up with optimal ordering of those items. As such, LTR doesn't care much about the exact score that each item gets, but cares more about the relative ordering among all the items.

The most common application of LTR is search engine ranking.

Not all pairwise errors are created equal. Because we use DCG as our scoring function, it is critical that the algorithm gets the top results right.


## Metric

A decent metric that captures this notion of correct order is the count of inversions in your ranking, the number of times a lower-rated result appears above a higher-rated one. 

### A. Mean reciprocal rank (MRR)

The mean reciprocal rank is the average of the reciprocal ranks of results for a sample of queries Q [wiki: Mean reciprocal rank](https://en.wikipedia.org/wiki/Mean_reciprocal_rank):

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{MRR}&space;=&space;\frac{1}{|Q|}\sum^{|Q|}_{i=1}\frac{1}{\textrm{rank}_i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{MRR}&space;=&space;\frac{1}{|Q|}\sum^{|Q|}_{i=1}\frac{1}{\textrm{rank}_i}" title="\textrm{MRR} = \frac{1}{|Q|}\sum^{|Q|}_{i=1}\frac{1}{\textrm{rank}_i}" /></a>

where `rank_i` refers to the rank position of the **first** relevant document for the i-th query.

#### Example
For example, suppose we have the following three sample queries for a system that tries to translate English words to their plurals. In each case, the system makes three guesses, with the first one being the one it thinks is most likely correct:

```
| Query |   Proposed Results   | Correct | Rank | Reciprocal rank
|  cat  |  catten, cati, cats  |   cats  |   3  |     1/3
| tori  | torii, tori, toruses |   tori  |   2  |     1/2
| virus | viruses, virii, viri | viruses |   1  |      1
```
Given those three samples, we could calculate the mean reciprocal rank as (1/3 + 1/2 + 1)/3 = 11/18 or about 0.61.

If none of the proposed results are correct, reciprocal rank is 0.[1] Note that only the rank of the first relevant answer is considered, possible further relevant answers are ignored. If users are interested also in further relevant items, **mean average precision** is a potential alternative metric.


### B. Mean average precision (MAP)

Given a precision-recall curve, plotting precision `P(r)` as a function of recall `r`, average precision computes the average value of `p(r)` over the interval from `r=0` to `r=1` [[wiki: Mean average precision]][ Mean average precision]:

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{AveP(q)}&space;=&space;\int^1_0&space;p(r)&space;dr" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{AveP(q)}&space;=&space;\int^1_0&space;p(r)&space;dr" title="\textrm{AveP(q)} = \int^1_0 p(r) dr" /></a>

In the information retrieval, precision has different definitions. As defined by Wiki, precision is defined as the ratio of the retrived documents that are relevant to user’s query over the retrieved documents.

Mean average precision for a set of queries is the mean of the average precision scores for each query.

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{MAP}&space;=&space;\frac{\sum^Q_{q=1}\textrm{AveP(q)}}{Q}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{MAP}&space;=&space;\frac{\sum^Q_{q=1}\textrm{AveP(q)}}{Q}" title="\textrm{MAP} = \frac{\sum^Q_{q=1}\textrm{AveP(q)}}{Q}" /></a>

where Q is the number of queries.

#### Example

supposed given a query, we have the following rank result:

![rank_example](images/rank_example.png)

The document labeled with green is relevant to query; we can regard as positives. Red ones regard as negatives. Then we have precision and recall are
```
Precision @1 = 1/(1+0) = 1; Recall @1 = 1/(1+3) = 0.25.
Precision @4 = 3/(3+1) = 0.75; Recall @4 = 3/(3+1) = 0.75.
Precision @8 = 4/(4+4) = 0.5; Recall @8 = 4/(4+0) = 1.
```
Average Precision can be computed using

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{AveP(q)}&space;=&space;\sum_K&space;\big(&space;\textrm{Recall}@k&space;-&space;\textrm{Recall}@(k-1)&space;\big)*&space;\textrm{Precision}@k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{AveP(q)}&space;=&space;\sum_K&space;\big(&space;\textrm{Recall}@k&space;-&space;\textrm{Recall}@(k-1)&space;\big)*&space;\textrm{Precision}@k" title="\textrm{AveP(q)} = \sum_K \big( \textrm{Recall}@k - \textrm{Recall}@(k-1) \big)* \textrm{Precision}@k" /></a>

The article [[Felipe Almeida]][Evaluation Metrics for Ranking problems: Introduction and Examples] used the algrithm to calculate averge precision:
```Python
if document@rank k is relevant:
    correctPrediction += 1
    runningSum += correctPrediction/k
```
using the above, we have
```
At rank 1: RunningSum = 0 + 1/1 = 1; correctPrediciton = 1
At rank 2: No change. wrong prediction.
At rank 3: RunningSum = 1 + 2/3 = 1.8; correctPrediciton = 2
At rank 4: RunningSum = 1.8 + 3/4 = 2.55; correctPrediciton = 3
At rank 5: No change, wrong prediction.
At rank 6: RunningSum = 2.55 + 4/6 = 3.22; correctPrediciton = 4
At rank 7: No change, wrong prediction.
At rank 8: No change, wrong prediction.
```


### C. Discounted cumulative gain (DCG)






## Amazon 



## Reference

Felipe Almeida

[Evaluation Metrics for Ranking problems: Introduction and Examples]: https://queirozf.com/entries/evaluation-metrics-for-ranking-problems-introduction-and-examples
[[Felipe Almeida] Evaluation Metrics for Ranking problems: Introduction and Examples](https://queirozf.com/entries/evaluation-metrics-for-ranking-problems-introduction-and-examples)


[How Does Amazon's Search Algorithm Work?]: https://www.omniaretail.com/blog/how-does-amazons-search-algorithm-work
[[Grace Baldwin] How Does Amazon's Search Algorithm Work?](https://www.omniaretail.com/blog/how-does-amazons-search-algorithm-work)

[Intuitive explanation of Learning to Rank (and RankNet, LambdaRank and LambdaMART)]: https://medium.com/@nikhilbd/intuitive-explanation-of-learning-to-rank-and-ranknet-lambdarank-and-lambdamart-fe1e17fac418
[[Nikhil Dandekar] Intuitive explanation of Learning to Rank (and RankNet, LambdaRank and LambdaMART)](https://medium.com/@nikhilbd/intuitive-explanation-of-learning-to-rank-and-ranknet-lambdarank-and-lambdamart-fe1e17fac418)



[Mean average precision]: https://en.wikipedia.org/wiki/Evaluation_measures_(information_retrieval)#Mean_average_precision
[[wiki: Mean average precision] Mean average precision](https://en.wikipedia.org/wiki/Evaluation_measures_(information_retrieval)#Mean_average_precision)


[Mean reciprocal rank]: https://en.wikipedia.org/wiki/Mean_reciprocal_rank
[[wiki: Mean reciprocal rank] Mean reciprocal rank](https://en.wikipedia.org/wiki/Mean_reciprocal_rank)



