
# Tf-Idf and Match Score 


Assume we have 3 documents in the corpus:

```
Doc 1: Ben studies about computers in Computer Lab.
Doc 2: Steve teaches at Brown University.
Doc 3: Data Scientists work on large datasets.
```

and we are doing a search on these documents with query: **Data Scientists**.

## TF-IDF 

* tf(t, d): (term frequency for a term t in document d)/||D||.
* ||D||: total number of term in the document: ||Doc1|| = 7, ||Doc2||=5, ||Doc3||=6.
* idf(t) = log(Total Number Of Docs / Number Of Docs with term t in it)
* tf-idf(t, d) = tf(t, d)* idf(t)


| Doc | term | tf(t, d) | idf(t) | tf-idf(t, d) |
| --- | --- | --- | --- | --- |
|  1  | Ben        | 1/7 = 0.143| log(3/1) = 1.585 | 0.227 |
|  1  | study      | 1/7 = 0.143| log(3/1) = 1.585 | 0.227 |
|  1  | computer   | 2/7 = 0.286| log(3/1) = 1.585 | 0.453 |
|  1  | study      | 1/7 = 0.143| log(3/1) = 1.585 | 0.227 |
|  2  | Steve      | 1/5 = 0.2  | log(3/1) = 1.585 | 0.317 | 
|  2  | teach      | 1/5 = 0.2  | log(3/1) = 1.585 | 0.317 | 
|  2  | Brown      | 1/5 = 0.2  | log(3/1) = 1.585 | 0.317 | 
|  2  | university | 1/5 = 0.2  | log(3/1) = 1.585 | 0.317 | 
|  3  | data       | 1/6 = 0.167| log(3/1) = 1.585 | 0.265 | 
|  3  | scientist  | 1/6 = 0.167| log(3/1) = 1.585 | 0.265 | 
|  3  | work       | 1/6 = 0.167| log(3/1) = 1.585 | 0.265 | 
|  3  | large      | 1/6 = 0.167| log(3/1) = 1.585 | 0.265 | 
|  3  | dataset    | 1/6 = 0.167| log(3/1) = 1.585 | 0.265 | 
















## Reference

[TF-IDF for Similarity Scores]: https://medium.datadriveninvestor.com/tf-idf-for-similarity-scores-391c3c8788e8
[[Nishant Sethi] TF-IDF for Similarity Scores](https://medium.datadriveninvestor.com/tf-idf-for-similarity-scores-391c3c8788e8)


