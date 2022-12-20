# Graph


## Vertex Degree

### Complement Graph

The complement of a graph $G=(V, E)$ is a graph of $G=(V, \bar{E})$ where two graphs have same set of vertices $V$ and:
* Two vertices are connected in $\bar{G}$ if and only if they are NOT connected in $G$.
* $(u, v) \in E$ if and only if $(u, v) \not\in \bar{E}$.

![](images/complement_graph.png)

### Walk and Path

#### Definition 

*  A walk in a graph is a sequence of edges, such that each edge starts in a vertex where the previous edge ended. Note that a walk contains the same edge several times
* The length of a walk is a number of edges in it. 
* A path is a walk where all edges are the distinct.
* A simple path is a path where all vertices are distinct

#### Example

![](images/walk_path.png)

* Walk: start from the $v_6$, $(e_1, e_2, e_4, e_5, e_3, e_1)$.
* Path: $(e_7, e_6, e_4, and e_5.)$. It's not a simple path, because we've visited $v_2$ twice.
* Simple path: $(e_7, e_6, e_2, e_3)$.


