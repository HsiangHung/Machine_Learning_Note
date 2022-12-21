# Machine Learning with Graph


## Link-Level Features

### Distance-based feature

Shortest path distance between two nodes. Doesn't capture the degree of neighborhood overlap

### Local neighborhood overlap

Capture the number of neighboring nodes shared between nodes $u$ and $v$.
* Common neighbors $|N(u) \cap N(v)|$
* Jaccard's coefficient  $|N(u) \cap N(v)|/|N(u) \cup N(v)|$
* Adamic-Adar index


### Global neighborhood overlap

* Katz index: the number of paths of **all lengths** between a pair of nodes.
* Use adjaceny matrix powers. If A is adjaceny matrix, $A^k_{uv}$ specifies the number of paths of length $k$ between node $u$ and $v$.
* Katz index:

$$S_{uv} = \sum^{\infty}_{k=0} \beta^{k} A^k_{uv},$$ where $\beta = [0, 1]$
* Katz index matrix can be computed in close-form:

$$\bf{S} = \sum^{\infty}_{k=0} \left( \bf{I} - \beta \bf{A}\right)^{-1} - \bf{I}. $$
