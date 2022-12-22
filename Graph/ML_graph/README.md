# Machine Learning with Graph


## Node-Level Features

Important-based features:
* **Node degree**: the number of neighboring nodes
* **Node centrality**: 
     1. Eigenvector centrality
     2. Betweenness centrality: a node is important if it lies on many shortes paths between other nodes.
     
     $$ c_v = \sum_{s,t \ne v} \frac{\textrm{num of shortest paths between s, t containing v}}{\textrm{num of shortest paths between s, t}} $$

     3. Closeness centrality

Structure-based features:
* **Clustering coefficient** 
* **Graphlet**

## Link-Level Features

### Distance-based feature

Shortest path distance between two nodes. Doesn't capture the degree of neighborhood overlap

### Local neighborhood overlap

Capture the number of neighboring nodes shared between nodes $u$ and $v$.
* **Common neighbors**: $|N(u) \cap N(v)|$
* **Jaccard's coefficient**: $|N(u) \cap N(v)|/|N(u) \cup N(v)|$
* **Adamic-Adar index**

However, the metric will be zero if two nodes have no nodes shared in common. Potentially these nodes may be connected in future.

### Global neighborhood overlap

**Katz index**: the number of paths of **all lengths** between a pair of nodes.
* Use adjaceny matrix powers. If A is adjaceny matrix, $A^k_{uv}$ specifies the number of paths of length $k$ between node $u$ and $v$.
* Katz index:

$$S_{uv} = \sum^{\infty}_{k=0} \beta^{k} A^k_{uv}, \ \ \textrm{where } \beta = [0, 1].$$ 

* Katz index matrix can be computed in close-form:

$$\bf{S} = \sum^{\infty}_{k=0} \left( \bf{I} - \beta \bf{A}\right)^{-1} - \bf{I}. $$


## Graph-Level Features

Kernel method: graph kernel is to measure similarity between two graphs.
Design graph feature vector $\Phi(G)$.