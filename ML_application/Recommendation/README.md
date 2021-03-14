
# Recommendation Engine 

We divides recommendation problem into 2 subproblems: 1) choosing top-N candidates and 2) ranking them.

### Collaborative filtering

We considered a recommendation problem as a **supervised** machine learning task:

* User-based collaborative filtering
* Item-based collaborative filtering
* Matrix decompositions

We can also apply **unsupervised** methods to solve the recommendation problem.

At the start of a business, there is a lack of previous users’ grades, and clustering would be the best approach. We identify user groups and recommend each user in this group the same items. When we have enough data, using clustering as the first step is helpful for shrinking the selection of relevant neighbors in collaborative filtering algorithms.





One notably successful use of deep learning is embedding, a method used to represent categorical variables as continuous vectors, rather than using one-hot encoding and label encoding [[Will Koehrsen]][Neural Network Embeddings Explained], [[Matias Aravena Gamboa]][Learning embeddings for your machine learning model]. 

The main issue with one-hot encoding is that the transformation does not rely on any supervision and cause huge dimensions. The problem with LabelEncoding is that sometimes can bring a natural order on the different classes. We can greatly improve embeddings by learning them using a neural network on a **supervised** task. 





![word_embedding](images/word_embedding.png)



**Auto-encoders** use neural networks consisting of both an encoder and a decoder; encoder learns to compress the raw image pixel data to a small dimension, whereas decoders decompresses it via a decoder to re-generate the same input image. Once we have trained the model, we only use the encoder (first N network layers) to generate embeddings for images.



[Recommendation System Algorithms]: https://blog.statsbot.co/recommendation-system-algorithms-ba67f39ac9a3
[[Daniil Korbut] Recommendation System Algorithms](https://blog.statsbot.co/recommendation-system-algorithms-ba67f39ac9a3)



