# Heterogeneous & Knowledge Graph

What if the graph has multiple relation types? 

![](images/relation_GCN.png)

Use different neural network weights for different relation types.


## Relational GCN (RGCN):

$$ \bf{h}^{(k+1)}_v = \sigma \left( \sum_{r \in R} \sum_{u \in N(v)^r} \frac{1}{c_{v,r}} \bf{W}^{(k)}_r  \frac{h^{(k)}_u}{|N(v)|} + \bf{W}^{(k)}_0 h^{(k)}_v  \right),$$

