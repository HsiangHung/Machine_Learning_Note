
# Search Engine Optimization (SEO)

## Learning to Rank

Learning to Rank (LTR) is a class of techniques that apply supervised machine learning (ML) to solve ranking problems. The main difference between LTR and traditional supervised ML is this [[Nikhil Dandekar]][Intuitive explanation of Learning to Rank (and RankNet, LambdaRank and LambdaMART)]:

* Traditional ML solves a prediction problem (classification or regression) on a single instance at a time. E.g. if you are doing spam detection on email, you will look at all the features associated with that email and classify it as spam or not. The aim of traditional ML is to come up with a class (spam or no-spam) or a single numerical score for that instance.
* LTR solves a ranking problem on a list of items. The aim of LTR is to come up with optimal ordering of those items. As such, LTR doesn't care much about the exact score that each item gets, but cares more about the relative ordering among all the items.

The most common application of LTR is search engine ranking.

[Intuitive explanation of Learning to Rank (and RankNet, LambdaRank and LambdaMART)]: https://medium.com/@nikhilbd/intuitive-explanation-of-learning-to-rank-and-ranknet-lambdarank-and-lambdamart-fe1e17fac418
[[Nikhil Dandekar] Intuitive explanation of Learning to Rank (and RankNet, LambdaRank and LambdaMART)](https://medium.com/@nikhilbd/intuitive-explanation-of-learning-to-rank-and-ranknet-lambdarank-and-lambdamart-fe1e17fac418)



## Data to Prepare

Most major search engines have a human-powered relevance measurement system which acts as an oracle for completeness and correctness. It also lets you measure how good you are relative to your competitors [[Quroa: How does Google measure the quality of their search results?]][How does Google measure the quality of their search results?]

1. Generate a sample of a few thousand search queries
2. Issue those search queries on your search engine 
3. Train a set of human raters to rate the quality of these results. 
4. Repeat the "extract results - rate results" step 

[How does Google measure the quality of their search results?]: https://www.quora.com/How-does-Google-measure-the-quality-of-their-search-results
[[Quroa: How does Google measure the quality of their search results?] How does Google measure the quality of their search results?](https://www.quora.com/How-does-Google-measure-the-quality-of-their-search-results)


## Metric to Evaluate 

A decent metric that captures this notion of correct order is the count of inversions in your ranking, the number of times a lower-rated result appears above a higher-rated one. 

### A. Mean reciprocal rank (MRR)

The mean reciprocal rank is the average of the reciprocal ranks of results for a sample of queries Q [[wiki: Mean reciprocal rank]](https://en.wikipedia.org/wiki/Mean_reciprocal_rank):

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

Therefore, a pairwise error at positions 1 and 2 is much more severe than an error at positions 9 and 10, all other things being equal. Our algorithm needs to factor this potential gain (or loss) in DCG for each of the result pairs.

One advantage of DCG over other metrics is that it also works if document relevances are a real number. In other words, when each document is not simply relevant/non-relevant (as in the example), but has a relevance score instead [[Felipe Almeida]][Evaluation Metrics for Ranking problems: Introduction and Examples], [[Pranay Chandekar]][Evaluate your Recommendation Engine using NDCG].

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{DCG@k}&space;=&space;\sum^k_{i=1}&space;\frac{2^{rel_i}-1}{\log(i&plus;1)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{DCG@k}&space;=&space;\sum^k_{i=1}&space;\frac{2^{rel_i}-1}{\log(i&plus;1)}" title="\textrm{DCG@k} = \sum^k_{i=1} \frac{2^{rel_i}-1}{\log(i+1)}" /></a>


Not all pairwise errors are created equal. Because we use DCG as our scoring function, it is critical that the algorithm gets the top results right. Therefore, a pairwise error at positions 1 and 2 is much more severe than an error at positions 9 and 10, all other things being equal. Our algorithm needs to factor this potential gain (or loss) in DCG for each of the result pairs.


DCG **higher** is better [[Pranay Chandekar]][Evaluate your Recommendation Engine using NDCG].

```
At rank 1: rel_1 = 1; DCG@1= 1
At rank 2: No change. wrong prediction.
At rank 3: rel_3 = 1; DCG@3 = DCG@2 + 1/log(1+3) = 1 + 1/2 = 1.5.
At rank 4: rel_4 = 1; DCG@4 = DCG@3 + 1/log(1+4) = 1.93.
At rank 5: No change, wrong prediction.
At rank 6: rel_6 = 1; DCG@6 = DCG@5 + 1/log(1+6) = 2.29.
At rank 7: No change, wrong prediction.
At rank 8: No change, wrong prediction.
```

### D. Normalized Discounted Cumulative Gain (NDCG)

A way to make comparison across queries fairer is to normalize the DCG score by the maximum possible DCG at each threshold [[Felipe Almeida]][Evaluation Metrics for Ranking problems: Introduction and Examples], [[Pranay Chandekar]][Evaluate your Recommendation Engine using NDCG]

```
NDCG@k = DCG@k/IDCG@k
```

Where IDCG@k is the best possible value for DCG@k, i.e. the value of DCG for the best possible ranking of relevant documents at threshold k. See below table:

![rank_example_NDCG](images/rank_example_NDCG.png)



### Reference

[Evaluation Metrics for Ranking problems: Introduction and Examples]: https://queirozf.com/entries/evaluation-metrics-for-ranking-problems-introduction-and-examples
[[Felipe Almeida] Evaluation Metrics for Ranking problems: Introduction and Examples](https://queirozf.com/entries/evaluation-metrics-for-ranking-problems-introduction-and-examples)


[Evaluate your Recommendation Engine using NDCG]: https://towardsdatascience.com/evaluate-your-recommendation-engine-using-ndcg-759a851452d1
[[Pranay Chandekar] Evaluate your Recommendation Engine using NDCG](https://towardsdatascience.com/evaluate-your-recommendation-engine-using-ndcg-759a851452d1)


[Mean average precision]: https://en.wikipedia.org/wiki/Evaluation_measures_(information_retrieval)#Mean_average_precision
[[wiki: Mean average precision] Mean average precision](https://en.wikipedia.org/wiki/Evaluation_measures_(information_retrieval)#Mean_average_precision)


[Mean reciprocal rank]: https://en.wikipedia.org/wiki/Mean_reciprocal_rank
[[wiki: Mean reciprocal rank] Mean reciprocal rank](https://en.wikipedia.org/wiki/Mean_reciprocal_rank)





## A/B Testing for Search

There’s no single way to perform A/B testing for search. You have to decide whether the test will compare **click-through rate** (CTR), **mean reciprocal rank** (MRR) of clicks, **conversion rate**, **revenue**, or some other search success metric. You also have to determine how long to run each test, considering not only the need to establish statistical significance but also the possibility of a novelty effect. A/B testing search isn’t just a switch that you flip on — it’s a science [[Daniel Tunkelang]][A/B Testing for Search is Different].

A/B tests randomly assign users to treatment groups and compare the performance of the groups. But A/B tests for search have an important nuance: not all search queries are affected by the test. As we just discussed, some of the highest-ROI work on improving search succeeds by targeting only a small fraction of search queries.

To make this nuance concrete, let’s consider an A/B test that targets 10% of search queries with the goal of achieving a 5% conversion lift for those queries. That would translate into an overall 0.5% conversion lift for the site. A 0.5% conversion lift may not sound like a lot, but for a major retailer that translates into millions of dollars a year.

As we discussed earlier, the size of the improvement target determines how long the test has to run before you can evaluate its success with statistical significance. In our example, **establishing whether a test achieves a 5% conversion lift on 10% of queries takes far less time than establishing whether the test achieves a a 0.5% conversion lift on 100% of queries** — days as opposed to months. You can explore these numbers yourself using a nifty [online A/B testing calculator](https://vwo.com/tools/ab-test-duration-calculator/).




### Reference

[A/B Testing for Search is Different]: https://dtunkelang.medium.com/a-b-testing-for-search-is-different-f6b0f6f4d0f5
[[Daniel Tunkelang] A/B Testing for Search is Different](https://dtunkelang.medium.com/a-b-testing-for-search-is-different-f6b0f6f4d0f5)



## Amazon 

A talk from A9 search team by [Daria Sorokina - Amazon Search: The Joy of Ranking Products](https://www.youtube.com/watch?v=NLrhmn-EZ88&list=PLCsjIud8mFqzb_FAWTL9ewiNWHvNoDigM) in MLconf SF 2016 conference.

Set up your products for visibility and sales in Amazon wesbite search :
* Product detail page copy - keyword research is harvesting your advertising.
* Product images & video -  Show your product from different angles and have a high enough resolution that shoppers can zoom in to thoroughly examine it.
* EBC/A+ EMC content - content formats may increase your sales by as much as 10%
* Price
* Availability
* Ratings and reviews - take care customer's bad reviews if needed. Amazon also rewards sellers that prioritize customer service
* Advertisements - Buying ads will not inherently boost your organic rankings. However, paid placements take up prime slots on the search results page, which can increase traffic to a product listing and drive sales
* Fulfillment method - If you have late or missed shipments, cancellations, etc., each thing dings your seller score


### Reference


[Amazon’s A9 product ranking algorithm: Your guide to Amazon SEO for maximum visibility]: https://searchengineland.com/amazons-a9-product-ranking-algorithm-beginners-guide-329801
[[George Nguyen] Amazon’s A9 product ranking algorithm: Your guide to Amazon SEO for maximum visibility](https://searchengineland.com/amazons-a9-product-ranking-algorithm-beginners-guide-329801)


[How Does Amazon's Search Algorithm Work?]: https://www.omniaretail.com/blog/how-does-amazons-search-algorithm-work
[[Grace Baldwin] How Does Amazon's Search Algorithm Work?](https://www.omniaretail.com/blog/how-does-amazons-search-algorithm-work)




