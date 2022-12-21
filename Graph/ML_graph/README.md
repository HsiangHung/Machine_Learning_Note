# Machine Learning with Graph


## Link Feature

### Global Neighborhood Overlap

* Katz index: the number of paths of **all lengths** between a pair of nodes.
* Use adjaceny matrix powers. If A is adjaceny matrix, $A^k_{uv}$ specifies the number of paths of length $k$ between node $u$ and $v$.
* Katz index:

$$S_{uv} = \sum_^{\infty}_{k=0} \beta^{k} A^k_{uv}$$
