
# Language Model 


A statistical language model is a probability distribution over sequences of words $\lbrace w_1, w_2, \cdots \rbrace$. Given such a sequence, say of length $m$, it assigns a probability $P(w_1, \cdots , w_m)$ to the whole sequence [[wiki: Language model]][Language model].

**Data sparsity** is a major problem in building language models. Most possible word sequences are not observed in training. One solution is to make the assumption that the probability of a word only depends on the previous $n$ words; this is known as an $n$-gram model. When $n=1$ it is the **unigram** model, known as the **bag of words model**.


Language models are used in information retrieval in the **query likelihood model**. There, a separate language model is associated with each document in a collection. Documents are ranked based on the probability of the query $Q$ in the document's language model $M$, i.e. $P(Q|M)$. Commonly, the unigram language model is used for this purpose [[wiki: Language model]][Language model].

## Unigram

A unigram model can be treated as the combination of several one-state finite automata, and splits the probabilities of different terms in a context, e.g. from

$$P(w_1, w_2, w_3) = P(w_1)P(w_2|w_1)P(w_3|w_1,w_2)$$

to

$$P(w_1, w_2, w_3) = P(w_1)P(w_2)P(w_3).$$

In this model, the probability of each word only depends on that word's own probability in the document, so we only have one-state finite automata as units.  The following is an illustration of a unigram model of a document [[wiki: Language model]][Language model]


| term | a | world | likes | we | share | ....|
| --- | --- | --- | --- | --- | --- | ---- |
| Probability in doc | 0.1 |  0.2  | 0.05  | 0.05 | 0.3 | ...|

<!-- ```
term               | a	| world | likes |  we  | share | ... 
--------------------------------------------------------------
Probability in doc | 0.1|  0.2  | 0.05  | 0.05 |  0.3  | ...
``` -->

The automaton itself has a probability distribution over the entire vocabulary of the model, summing to 1

$$\sum_{w} P(w) = 1$$

The probability generated for a specific query is calculated as

$$P(Q) = \prod_{\textrm{word in query Q}} P(w).$$

Different documents have unigram models, with different hit probabilities of words in it. The probability distributions from different documents are used to generate hit probabilities for each query. Documents can be ranked for a query according to the probabilities. Example of unigram models of two documents:


| term (w) | a | world | likes | we | share | ....|
| --- | --- | --- | --- | --- | --- | ---- |
| p(w) in doc1 | 0.1 |  0.2  | 0.05  | 0.05 | 0.3 | ...|
| p(w) in doc2 | 0.3 |  0.1  | 0.03  | 0.02 | 0.4 | ...|


<!-- ```
   term   |  a | world | likes |  we  | share | ... 
------------------------------------------------------
P in doc1 | 0.1|  0.2  | 0.05  | 0.05 |  0.3  | ...
------------------------------------------------------
P in doc2 | 0.3|  0.1  | 0.03  | 0.02 |  0.4  | ...
``` -->
If P in doc2 > P in doc1, then rank doc2 in front of doc1. 

In information retrieval contexts, unigram language models are often smoothed to avoid instances where $P(w) = 0$. A common approach is to generate a maximum-likelihood model for the entire collection and linearly interpolate the collection model with a maximum-likelihood model for each document to smooth the model.


## n-gram

In an n-gram model, the probability $P(w_1,... ,w_m)$ of observing the sentence $w_1, \cdots, w_m$ is approximated as

$$P(w_1,\cdots, w_m) = \prod^m_{i=1}P(w_i|w_1, \cdots, w_{i-1}) \simeq \prod^m_{i=1}P(w_i|w_{i-(n-1)}, \cdots, w_{i-1})$$

The conditional probability can be calculated from n-gram model frequency counts:


$$P(w_i|w_{i-(n-1)}, \cdots, w_{i-1}) = \frac{P(w_{i-(n-1)}, \cdots, w_{i-1}, w_i)}{P(w_{i-(n-1)}, \cdots, w_{i-1})}.$$

The terms bigram and trigram language models denote n-gram models with n = 2 and n = 3, respectively.

Typically, the n-gram model probabilities are not derived directly from frequency counts, because models derived this way have severe problems when confronted with any n-grams that have not been explicitly seen before. Instead, some form of smoothing is necessary, assigning some of the total probability mass to unseen words or n-grams.



If the sentence is "I saw the red house", in a bigram (n = 2) language model, the probability of the sentence is approximated as

$${\displaystyle P({\text{I, saw, the, red, house}})\approx P({\text{I}}\mid \langle s\rangle )P({\text{saw}}\mid {\text{I}})P({\text{the}}\mid {\text{saw}})P({\text{red}}\mid {\text{the}})P({\text{house}}\mid {\text{red}})P(\langle /s\rangle \mid {\text{house}})}$$

whereas in a trigram (n = 3) language model, the approximation is

$${\displaystyle P({\text{I, saw, the, red, house}})\approx P({\text{I}}\mid \langle s\rangle ,\langle s\rangle )P({\text{saw}}\mid \langle s\rangle ,I)P({\text{the}}\mid {\text{I, saw}})P({\text{red}}\mid {\text{saw, the}})P({\text{house}}\mid {\text{the, red}})P(\langle /s\rangle \mid {\text{red, house}})}$$

Note that the context of the first $n–1$ n-grams is filled with start-of-sentence markers, typically denoted `<s>`.


## Neural Networks

Neural language models (or continuous space language models) use continuous representations or **embeddings of words** to make their predictions. 

Continuous space embeddings help to alleviate the **curse of dimensionality** in language modeling: as language models are trained on larger and larger texts, the number of unique words (the vocabulary) increases. The number of possible sequences of words **increases exponentially** with the size of the vocabulary, causing a data sparsity problem because of the exponentially many sequences. Neural networks avoid this problem by **representing words in a distributed way, as non-linear combinations of weights in a neural net**.

Typically, neural net language models are constructed and trained as **probabilistic classifiers** that learn to predict a probability distribution

$${\displaystyle P(w_{t}|\mathrm {context} )\,\forall t\in V}, $$

i.e., the network is trained to predict a probability distribution over the vocabulary, given some linguistic context. The network predicts usually predicts a probability from a feature vector representing the **previous** k words:

$${\displaystyle P(w_{t}|w_{t-k},\dots ,w_{t-1})}.$$

Another option is to use **future** words as well as **past** words as features, so that the estimated probability is

$$P(w_{t}|w_{{t-k}},\dots ,w_{{t-1}},w_{{t+1}},\dots ,w_{{t+k}}).$$

This is called a bag-of-words model. 

When the feature vectors for the words in the context are combined by a continuous operation, this model is referred to as the **continuous bag-of-words architecture (CBOW)**.

Given a sequence of training words $w_1, w_2, \cdots ,w_T$, one maximizes the average log-probability

$$ \frac{1}{T} \sum_{t=1}^{T} \sum_{-k \le j\le k,j \ne 0} \log P(w_{t+j}|w_t), $$

where $k$, the size of the training context, can be a function of the center word $w_t$. This is called a **skip-gram** language model.

Bag-of-words and skip-gram models are the basis of the **word2vec** program [[wiki: Word2vec]][Word2vec]. As the name implies, word2vec represents each distinct word with a particular list of numbers called a vector. The vectors are chosen carefully such that a simple mathematical function (the **cosine similarity** between the vectors) indicates the level of **semantic similarity** between the words represented by those vectors.


Instead of using neural net language models to produce actual probabilities, word2vec instead uses the distributed representation encoded in the networks' **hidden** layers as representations of words; each word is then mapped onto an $n$-dimensional real vector called the word embedding, where $n$ is the size of the hidden layer just before the output layer. 

For example, in some such models, if v is the function that maps a word $w$ to its $n$-dimensional vector representation, then

$$v(\textrm{king})-v(\textrm{queen}) \simeq v(\textrm{male}) - v(\textrm{female}).$$

```
v(king)-v(queen) ~ v(male) - v(female)
```


## Reference

[Language model]: https://en.wikipedia.org/wiki/Language_model
[[wiki: Language model] Language model](https://en.wikipedia.org/wiki/Language_model)

[Word2vec]: https://en.wikipedia.org/wiki/Word2vec
[[wiki: Word2vec] Word2vec](https://en.wikipedia.org/wiki/Word2vec)

