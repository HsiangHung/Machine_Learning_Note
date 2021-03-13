
# Embedding 

One notably successful use of deep learning is embedding, a method used to represent discrete variables as continuous vectors.



A statistical language model is a probability distribution over sequences of words. Given such a sequence, say of length m, it assigns a probability `P(w_1,... ,w_m)` to the whole sequence [[wiki: Language model]][Language model].




In this model, the probability of each word only depends on that word's own probability in the document, so we only have one-state finite automata as units.  The following is an illustration of a unigram model of a document [[wiki: Language model]][Language model]

```
term               | a	| world | likes |  we  | share | ... 
--------------------------------------------------------------
Probability in doc | 0.1|  0.2  | 0.05  | 0.05 |  0.3  | ...
```

The automaton itself has a probability distribution over the entire vocabulary of the model, summing to 1

<a href="https://www.codecogs.com/eqnedit.php?latex=\sum_{w}&space;P(w)&space;=&space;1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sum_{w}&space;P(w)&space;=&space;1" title="\sum_{w} P(w) = 1" /></a>

The probability generated for a specific query is calculated as

<a href="https://www.codecogs.com/eqnedit.php?latex=P(Q)&space;=&space;\prod_{\textrm{word&space;in&space;query&space;Q}}&space;P(w)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(Q)&space;=&space;\prod_{\textrm{word&space;in&space;query&space;Q}}&space;P(w)" title="P(Q) = \prod_{\textrm{word in query Q}} P(w)" /></a>

Different documents have unigram models, with different hit probabilities of words in it. The probability distributions from different documents are used to generate hit probabilities for each query. Documents can be ranked for a query according to the probabilities. Example of unigram models of two documents:

```
   term   |  a | world | likes |  we  | share | ... 
------------------------------------------------------
P in doc1 | 0.1|  0.2  | 0.05  | 0.05 |  0.3  | ...
------------------------------------------------------
P in doc2 | 0.3|  0.1  | 0.03  | 0.02 |  0.4  | ...
```
If P in doc2 > P in doc1, then rank doc2 in front of doc1. 

In information retrieval contexts, unigram language models are often smoothed to avoid instances where P(term) = 0. A common approach is to generate a maximum-likelihood model for the entire collection and linearly interpolate the collection model with a maximum-likelihood model for each document to smooth the model.





## Reference

[Language model]: https://en.wikipedia.org/wiki/Language_model
[[wiki: Language model] Language model](https://en.wikipedia.org/wiki/Language_model)

[Word2vec]: https://en.wikipedia.org/wiki/Word2vec
[[wiki: Word2vec] Word2vec](https://en.wikipedia.org/wiki/Word2vec)

