# Heterogeneous & Knowledge Graph


[talk: Homin Lee - The Observability Graph: Knowledge Graphs for Automated Infrastructure Observability](https://vimeo.com/369632039)


What if the graph has multiple relation types? 

![](images/relation_GCN.png)

Use different neural network weights for different relation types.


## Relational GCN (RGCN):

$$ \bf{h}^{(k+1)}_v = \sigma \left( \sum_{r \in R} \sum_{u \in N^r_v} \frac{1}{c_{v,r}} \bf{W}^{(k)}_r  h^{(k)}_u + \bf{W}^{(k)}_0 h^{(k)}_v  \right),$$

