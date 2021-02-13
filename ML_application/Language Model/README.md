
# Language Model 


A statistical language model is a probability distribution over sequences of words. Given such a sequence, say of length m, it assigns a probability {\displaystyle `P(w_1,... ,w_m)` to the whole sequence.

Data sparsity is a major problem in building language models. Most possible word sequences are not observed in training. One solution is to make the assumption that the probability of a word only depends on the previous `n` words; this is known as an `n`-gram model. When `n=1` it is the unigram model, known as the bag of words model.


