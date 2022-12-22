# Machine Learning with Graph


## Node-Level Features

Important-based features:
* **Node degree**: the number of neighboring nodes
* **Node centrality**: 
     1. Eigenvector centrality
     2. Betweenness centrality: a node is important if it lies on many shortest paths between other nodes.
     
     $$ c_v = \sum_{s,t \ne v} \frac{\textrm{num of shortest paths between s, t containing v}}{\textrm{num of shortest paths between s, t}}.$$

     ![](images/feature_node_betweenness.png)

     3. Closeness centrality: a node is important if it has small shortest path lengths to all other nodes.

     $$ c_v = \frac{1}{ \sum_{u \ne v} \textrm{shortest path length between u and v}}$$

     ![](images/feature_node_closeness.png)

     

Structure-based features:
* **Clustering coefficient** 
* **Graphlet**

## Link-Level Features

### Distance-based feature

**Shortest path distance** between two nodes.

![](images/feature_link_distance.png)

This metric however doesn't capture the degree of neighborhood overlap. The pair (B,H) has 2 shared neighboring nodes, but (B,E) and (A,B) only have 1 such node.

### Local neighborhood overlap

Capture the number of neighboring nodes shared between nodes $u$ and $v$. Suppose a graph:

![](images/feature_link_local_neighbor.png)

* **Common neighbors**: $|N(u) \cap N(v)|$, e.g. $|N(A) \cap N(B)| = |\left{ C \right}|=1$.
* **Jaccard's coefficient**: $|N(u) \cap N(v)|/|N(u) \cup N(v)|$, e.g. $|N(A) \cap N(B)|/ |N(A) \cup N(B)|= |\left{ C \right}|/|\left{ C,D \right}|=1/2$.
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