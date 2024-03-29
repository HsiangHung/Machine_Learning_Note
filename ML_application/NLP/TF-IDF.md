
# TF-IDF and TF-IDF Match Score


The TF-IDF match score can also be an important relevance signal for the model. It is a similarity score based on a text match between the query terms and the document. 

Assume we have 3 documents in the corpus:

```
Doc 1: Ben studies about computers in Computer Lab.
Doc 2: Steve teaches at Brown University.
Doc 3: Data Scientists work on large datasets.
```

and we are doing a search on these documents with query: **Data Scientists**.

## TF-IDF 

`tf` is the **term frequency** for a term t in document $d$:

$$tf(t,d) = \frac{\textrm{term frequency for a term t in document d}}{||D||},$$

where $||D||$ is the total number of terms in the document. In the above example, $||\textrm{Doc1}|| = 7$, $||\textrm{Doc2}||=5$, $||\textrm{Doc3}||=6$.

`idf` means inverse document frequency:

$$idf(t) = \log \Big( \frac{\textrm{Total Number Of Docs}}{\textrm{ Number Of Docs with term t in it}} \Big).$$

So the `tf-idf` score is

$$tf-idf(t, d) = tf(t, d)* idf(t).$$


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

The **TF-IDF Vector Space Representation** for the documents are:

* Doc1: {"Ben": 0.227, "study": 0.227, "computer": 0.453, "study": 0.227}
* Doc2: {"Steve": 0.317, "teach": 0.317, "Brown": 0.317, "university": 0.317}
* Doc3: {"data": 0.265, "scientist": 0.265, "work": 0.265, "large": 0.265, "dataset": 0.265}

## TF-IDF Score Match

Use similarity measures (eg, Cosine Similarity method) to find the similarity between the query and each document [[geeksforgeeks]][tf-idf Model for Page Ranking]. If query = d = {"data": 0.265, "scientist": 0.265}, the dot product of d and Doc are 0.265+0.265 = 0.53.

| term | Doc1 | Doc2 | Doc3 | 
| --- | --- | --- | --- | 
| data  |  0  | 0 | 0.265 | 
| scientist | 0 | 0 | 0.265 |



## Reference


[tf-idf Model for Page Ranking]: https://www.geeksforgeeks.org/tf-idf-model-for-page-ranking/#:~:text=tf%2Didf%20is%20a%20weighting,considered%20to%20be%20more%20important.&text=Let's%20us%20take%203%20documents%20to%20show%20how%20this%20works.
[[geeksforgeeks] tf-idf Model for Page Ranking](https://www.geeksforgeeks.org/tf-idf-model-for-page-ranking/#:~:text=tf%2Didf%20is%20a%20weighting,considered%20to%20be%20more%20important.&text=Let's%20us%20take%203%20documents%20to%20show%20how%20this%20works.)


[TF-IDF for Similarity Scores]: https://medium.datadriveninvestor.com/tf-idf-for-similarity-scores-391c3c8788e8
[[Nishant Sethi] TF-IDF for Similarity Scores](https://medium.datadriveninvestor.com/tf-idf-for-similarity-scores-391c3c8788e8)


[tf–idf]: https://en.wikipedia.org/wiki/Tf%E2%80%93idf
[[wiki: tf-idf] tf–idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)

