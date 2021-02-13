
# Language Model 


A statistical language model is a probability distribution over sequences of words. Given such a sequence, say of length m, it assigns a probability `P(w_1,... ,w_m)` to the whole sequence [[wiki: Language model]][Language model].

Data sparsity is a major problem in building language models. Most possible word sequences are not observed in training. One solution is to make the assumption that the probability of a word only depends on the previous `n` words; this is known as an `n`-gram model. When `n=1` it is the unigram model, known as the bag of words model.


Language models are used in information retrieval in the **query likelihood model**. There, a separate language model is associated with each document in a collection. Documents are ranked based on the probability of the query Q in the document's language model `M` `P(Q|M)`. Commonly, the unigram language model is used for this purpose [[wiki: Language model]][Language model].

## Unigram

A unigram model splits the probabilities of different terms in a context, e.g. from

<a href="https://www.codecogs.com/eqnedit.php?latex=P(w_1,&space;w_2,&space;w_3)&space;=&space;P(w_1)P(w_2|w_1)P(w_3|w_1,w_2)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(w_1,&space;w_2,&space;w_3)&space;=&space;P(w_1)P(w_2|w_1)P(w_3|w_1,w_2)" title="P(w_1, w_2, w_3) = P(w_1)P(w_2|w_1)P(w_3|w_1,w_2)" /></a>

to

<a href="https://www.codecogs.com/eqnedit.php?latex=P(w_1,&space;w_2,&space;w_3)&space;=&space;P(w_1)P(w_2)P(w_3)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(w_1,&space;w_2,&space;w_3)&space;=&space;P(w_1)P(w_2)P(w_3)" title="P(w_1, w_2, w_3) = P(w_1)P(w_2)P(w_3)" /></a>

[Language model]: https://en.wikipedia.org/wiki/Language_model
[[wiki: Language model] Language model](https://en.wikipedia.org/wiki/Language_model)
