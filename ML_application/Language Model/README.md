
# Language Model 


A statistical language model is a probability distribution over sequences of words. Given such a sequence, say of length m, it assigns a probability `P(w_1,... ,w_m)` to the whole sequence [[wiki: Language model]][Language model].

Data sparsity is a major problem in building language models. Most possible word sequences are not observed in training. One solution is to make the assumption that the probability of a word only depends on the previous `n` words; this is known as an `n`-gram model. When `n=1` it is the unigram model, known as the **bag of words model**.


Language models are used in information retrieval in the **query likelihood model**. There, a separate language model is associated with each document in a collection. Documents are ranked based on the probability of the query Q in the document's language model `M` `P(Q|M)`. Commonly, the unigram language model is used for this purpose [[wiki: Language model]][Language model].

## Unigram

A unigram model can be treated as the combination of several one-state finite automata, and splits the probabilities of different terms in a context, e.g. from

<a href="https://www.codecogs.com/eqnedit.php?latex=P(w_1,&space;w_2,&space;w_3)&space;=&space;P(w_1)P(w_2|w_1)P(w_3|w_1,w_2)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(w_1,&space;w_2,&space;w_3)&space;=&space;P(w_1)P(w_2|w_1)P(w_3|w_1,w_2)" title="P(w_1, w_2, w_3) = P(w_1)P(w_2|w_1)P(w_3|w_1,w_2)" /></a>

to

<a href="https://www.codecogs.com/eqnedit.php?latex=P(w_1,&space;w_2,&space;w_3)&space;=&space;P(w_1)P(w_2)P(w_3)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(w_1,&space;w_2,&space;w_3)&space;=&space;P(w_1)P(w_2)P(w_3)" title="P(w_1, w_2, w_3) = P(w_1)P(w_2)P(w_3)" /></a>


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

In information retrieval contexts, unigram language models are often smoothed to avoid instances where P(term) = 0. A common approach is to generate a maximum-likelihood model for the entire collection and linearly interpolate the collection model with a maximum-likelihood model for each document to smooth the model.


## n-gram

In an n-gram model, the probability `P(w_1,... ,w_m)` of observing the sentence `w_1, ..w_m` is approximated as

<a href="https://www.codecogs.com/eqnedit.php?latex=P(w_1,\cdots,&space;w_m)&space;=&space;\prod^m_{i=1}P(w_i|w_1,&space;\cdots,&space;w_{i-1})&space;\simeq&space;\prod^m_{i=1}P(w_i|w_{i-(n-1)},&space;\cdots,&space;w_{i-1})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(w_1,\cdots,&space;w_m)&space;=&space;\prod^m_{i=1}P(w_i|w_1,&space;\cdots,&space;w_{i-1})&space;\simeq&space;\prod^m_{i=1}P(w_i|w_{i-(n-1)},&space;\cdots,&space;w_{i-1})" title="P(w_1,\cdots, w_m) = \prod^m_{i=1}P(w_i|w_1, \cdots, w_{i-1}) \simeq \prod^m_{i=1}P(w_i|w_{i-(n-1)}, \cdots, w_{i-1})" /></a>



[Language model]: https://en.wikipedia.org/wiki/Language_model
[[wiki: Language model] Language model](https://en.wikipedia.org/wiki/Language_model)
