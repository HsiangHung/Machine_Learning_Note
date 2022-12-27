# Machine Learning with Graph

$\textcolor{red}{NOTE: \ The \ majority \ of \ the \ note \ page \ follows \ Prof. \ Jure \ Leskovec's \ CS224W \ 'Machine \ Learning \ With \ Graph' \ lectures.}$


# 1. Feature Engineering


## 1.1 Node-Level Features

Important-based features:
* **Node degree**: the number of neighboring nodes
* **Node centrality**: 
     1. **Eigenvector centrality**
     2. **Betweenness centrality**: a node is important if it lies on many shortest paths between other nodes.
     
      $$ c_v = \sum_{s,t \ne v} \frac{\textrm{num of shortest paths between s, t containing v}}{\textrm{num of shortest paths between s, t}}.$$

     ![](images/feature_node_betweenness.png)

     3. **Closeness centrality**: a node is important if it has small shortest path lengths to all other nodes.

     $$ c_v = \frac{1}{ \sum_{u \ne v} \textrm{shortest path length between u and v}}$$

     ![](images/feature_node_closeness.png)

     

Structure-based features:
* **Clustering coefficient** 
* **Graphlet**

## 1.2 Link-Level Features

### 1.2.1 Distance-based feature

**Shortest path distance** between two nodes.

![](images/feature_link_distance.png)

This metric however doesn't capture the degree of neighborhood overlap. The pair (B,H) has 2 shared neighboring nodes, but (B,E) and (A,B) only have 1 such node.

### 1.2.2 Local neighborhood overlap

Capture the number of neighboring nodes shared between nodes $u$ and $v$. Suppose we have a graph below and denote $N(v)$ as the neighbors of node $v$:

![](images/feature_link_local_neighbor.png)

* **Common neighbors**: $|N(u) \cap N(v)|$, e.g. $|N(A) \cap N(B)| = |\lbrace C \rbrace|=1$.
* **Jaccard's coefficient**: $|N(u) \cap N(v)|/|N(u) \cup N(v)|$, e.g. $|N(A) \cap N(B)|/ |N(A) \cup N(B)|= | \lbrace C \rbrace |/| \lbrace C,D \rbrace |=1/2$.
* **Adamic-Adar index**: $\sum_{u \in \lbrace N(u) \cap N(v) \rbrace} \frac{1}{\log(k_u)}$, e.g. $\frac{1}{\log(k_C)}=\frac{1}{\log 4}$.


However, the local neighborhood overlap metric will be zero if two nodes have no nodes shared in common. Potentially these nodes may be connected in future.

### 1.2.3 Global neighborhood overlap

**Katz index**: the number of paths of **all lengths** between a pair of nodes.
* Use adjaceny matrix powers. If A is adjaceny matrix, $A^k_{uv}$ specifies the number of paths of length $k$ between node $u$ and $v$.
* Katz index:

$$S_{uv} = \sum^{\infty}_{k=0} \beta^{k} A^k_{uv}, \ \ \textrm{where } \beta = [0, 1].$$ 

* Katz index matrix can be computed in close-form:

$$\bf{S} = \sum^{\infty}_{k=0} \left( \bf{I} - \beta \bf{A}\right)^{-1} - \bf{I}. $$

Here we implemented the geometric series formula 

$$\sum^{\infty}_{k=0} \beta^k \bf{A}^k = \left( \bf{I} - \beta \bf{A}\right)^{-1} $$

## 1.3 Graph-Level Features

Kernel method: graph kernel is to measure similarity between two graphs.

Goal: Design graph feature vector $\phi(G)$:
* **Graphlet kernel**: graph is represented as **Bag-of-graphlets**. Computationally expansive.
* **Weisfeiler-Lehman kernel**: represented as **Bag-of-color** (apply k-step color refinement) and computationally efficient. The time complexity $O(n)$, $n$ is the number of edges.



# 2. Graph Representation Learning

**Goal**: Efficient task-independent feature learning for machine learning with graphs!

![](images/node_embedding_0.png)

## 2.1 Node embedding

* Map nodes into an embedding space.
* Encode nodes so that similarity (e.g. dot product) among nodes in embedding space approximate similarity in graph.

![](images/node_embedding_1.png)


### 2.1.1 Shallow encoder

* Simplest encoding approach: encoder **ENC** is just a embedding-**lookup**, $\textrm{ENC}(u) = z_u$ where $u \in V$. Directly optimize the embedding for **each node**.
* $\bf{Z}$ matrix, where each column vector $z_u$ denotes a node embedding vector, and the number of row denotes embedding dimensionality.
![](images/node_embedding_lookup.png)
* Method: Deepwalk, Node2vec, but both don't capture structural similarity.
* Decoder: **DEC** maps from embeddings (based on node similarity) to the similarity score $\textrm{DEC}(z^T_u z_v)$.
* Objective: maximize $z^T_u z_v$ for node pairs (u, v) which are similar
$$\textrm{similarity}(u, v) \approx z^T_u z_v.$$

## 2.2 Node Classification

Messgae passing labels, similar nodes are connected (correlation).  

Two explanations for nodes in networks are correlated:
* social Homophily: The tendency of individuals to associate and bond with similar others
* Influence: Social connections can influence the individual characteristics of a person

Collective classification: assign labels to all nodes in the network. Three techniques:
* Relational classification
* Iterative classification
* Correct & Smooth

### 2.2.1 Relational classification

Prbabilistic relational classification: Propagate node labels across the network. Class probability $Y_v$ of node $v$ is a weighted average of class probabilities of its neighbors.

$$P(Y_v=c) = \frac{1}{\sum_{(u,v) \in E} A_{uv}}\sum_{(u,v) \in E} A_{uv}P(Y_u=c),$$
where $P(Y_v=c)$ is the probability of node $v$ having label $c$.

* For labeled nodes $v$, initialize label $Y_v$ with ground-truth label $Y^*_v$.
* For unlabeled nodes, initialize $Y_v= 0.5$.

![](images/label_relational_classification_0.png)

* Iteratively update all nodes in a random order until convergence or until maximum number of iterations is reached.
     * For example, for the first iteration,
     ![](images/label_relational_classification_1.png)
     * We continue the following iterations to update each node until the convergence:
     ![](images/label_relational_classification_2.png)

* Challenges:
     * Convergence is not guaranteed
     * Model cannot use node feature information

### 2.2.2 Iterative classification

* Relational classifier does not use node attributes.
* Iterative classification: Classify node $v$ based on its attributes $f_v$ as well as labels $z_v$ of neighbor set $N_v$.

### 2.2.3 Loopy belief propagation 
