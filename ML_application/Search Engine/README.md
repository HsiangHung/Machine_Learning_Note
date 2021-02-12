
# Search Engine Optimization (SEO)

## Learning to Rank

Learning to Rank (LTR) is a class of techniques that apply supervised machine learning (ML) to solve ranking problems. The main difference between LTR and traditional supervised ML is this [[Nikhil Dandekar]][Intuitive explanation of Learning to Rank (and RankNet, LambdaRank and LambdaMART)]:

* Traditional ML solves a prediction problem (classification or regression) on a single instance at a time. E.g. if you are doing spam detection on email, you will look at all the features associated with that email and classify it as spam or not. The aim of traditional ML is to come up with a class (spam or no-spam) or a single numerical score for that instance.
* LTR solves a ranking problem on a list of items. The aim of LTR is to come up with optimal ordering of those items. As such, LTR doesn't care much about the exact score that each item gets, but cares more about the relative ordering among all the items.

The most common application of LTR is search engine ranking.

[Intuitive explanation of Learning to Rank (and RankNet, LambdaRank and LambdaMART)]: https://medium.com/@nikhilbd/intuitive-explanation-of-learning-to-rank-and-ranknet-lambdarank-and-lambdamart-fe1e17fac418
[[Nikhil Dandekar] Intuitive explanation of Learning to Rank (and RankNet, LambdaRank and LambdaMART)](https://medium.com/@nikhilbd/intuitive-explanation-of-learning-to-rank-and-ranknet-lambdarank-and-lambdamart-fe1e17fac418)


## Metric

A decent metric that captures this notion of correct order is the count of inversions in your ranking, the number of times a lower-rated result appears above a higher-rated one. 

### Mean reciprocal rank

The mean reciprocal rank is the average of the reciprocal ranks of results for a sample of queries Q:

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{MRR}&space;=&space;\frac{1}{|Q|}\sum^{|Q|}_{i=1}\frac{1}{\textrm{rank}_i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{MRR}&space;=&space;\frac{1}{|Q|}\sum^{|Q|}_{i=1}\frac{1}{\textrm{rank}_i}" title="\textrm{MRR} = \frac{1}{|Q|}\sum^{|Q|}_{i=1}\frac{1}{\textrm{rank}_i}" /></a>

where `rank_i` refers to the rank position of the **first** relevant document for the i-th query.






Not all pairwise errors are created equal. Because we use DCG as our scoring function, it is critical that the algorithm gets the top results right.



## Amazon 


[How Does Amazon's Search Algorithm Work?]: https://www.omniaretail.com/blog/how-does-amazons-search-algorithm-work
[[Grace Baldwin] How Does Amazon's Search Algorithm Work?](https://www.omniaretail.com/blog/how-does-amazons-search-algorithm-work)



