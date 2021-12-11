
# Embedding 

One notably successful use of deep learning is embedding, a method used to represent categorical variables as continuous vectors, rather than using one-hot encoding and label encoding [[Will Koehrsen]][Neural Network Embeddings Explained], [[Matias Aravena Gamboa]][Learning embeddings for your machine learning model]. 

The main issue with one-hot encoding is that the transformation does not rely on any supervision and cause huge dimensions. The problem with LabelEncoding is that sometimes can bring a natural order on the different classes. We can greatly improve embeddings by learning them using a neural network on a **supervised** task. 


Neural network embeddings have 3 primary purposes:


[[Will Koehrsen]][Neural Network Embeddings Explained]'s article described taking all 37,000 book articles on Wikipedia and represent each one using only 50 numbers in a vector by neural network embeddings. 





Word embeddings (like Word2vec), include 

1. CBOW: Continuous bag of words (CBOW) tries to predict the current word from its surrounding words by optimizing 

<a href="https://www.codecogs.com/eqnedit.php?latex=\textrm{Loss}&space;=&space;-&space;\log&space;\big(p(w_t|w_{t-n},&space;\cdots,&space;w_{t-1},&space;w_{t&plus;1},&space;\cdots,&space;w_{t&plus;n})&space;\big)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textrm{Loss}&space;=&space;-&space;\log&space;\big(p(w_t|w_{t-n},&space;\cdots,&space;w_{t-1},&space;w_{t&plus;1},&space;\cdots,&space;w_{t&plus;n})&space;\big)" title="\textrm{Loss} = - \log \big(p(w_t|w_{t-n}, \cdots, w_{t-1}, w_{t+1}, \cdots, w_{t+n}) \big)" /></a>



![](images/two_tower_NN.png)

Or, if the user(u)-item(v) pairs has actual lable, like positive/negative lable, the two-tower NN model can be trained to minimize the difference dot product (u,v) minus the lable, like (credit from [Grokking the Machine Learning Interview: Recommendation System](https://www.educative.io/courses/grokking-the-machine-learning-interview/YQZR9pOMXJ9)):





## Reference


[Learning embeddings for your machine learning model]: https://medium.com/spikelab/learning-embeddings-for-your-machine-learning-model-a6cb4bc6542e
[[Matias Aravena Gamboa] Learning embeddings for your machine learning model](https://medium.com/spikelab/learning-embeddings-for-your-machine-learning-model-a6cb4bc6542e)



[Neural Network Embeddings Explained]: https://towardsdatascience.com/neural-network-embeddings-explained-4d028e6f0526
[[Will Koehrsen] Neural Network Embeddings Explained](https://towardsdatascience.com/neural-network-embeddings-explained-4d028e6f0526)

