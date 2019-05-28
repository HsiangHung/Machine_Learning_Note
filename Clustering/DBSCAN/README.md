
# DBSCAN clustering

DBSCAN is a popular clustering algorithm which is fundamentally very different from k-means.

* In k-means clustering, each cluster is represented by a centroid, and points are assigned to whichever centroid they are closest to. In DBSCAN, there are no centroids, and clusters are formed by linking nearby points to one another.




## Choosing Epsilon in DBSCAN

It calculates distance from each point to its nearest neighbor within the same partition, so, for a small fraction of points this distance will not be accurate [[Github]][Choosing parameters of DBSCAN algorithm]


[[Nadia Rahmah and Imas Sukaesih Sitanggang]][Determination of Optimal Epsilon (Eps) Value on DBSCAN Algorithm to Clustering Data on Peatland Hotspots in Sumatra]


[[Mohammed T. H. Elbatta and Wesam M. Ashour]][A dynamic Method for Discovering Density Varied Clusters]


## Validation of Brutal Searching Epsilon in DBSCAN

Validation to choose epsilon in DBSSCAN. [[Davoud Moulavi et al.]][Density-Based Clustering Validation]


In the following case, the data variance along the first principal component occurs on different classes. Therefore, after PCA, the first principal component is useful for classification.
![inter_class_variance](images/inter_class_variance.png)


   



## Summary












## Reference


[Determination of Optimal Epsilon (Eps) Value on DBSCAN Algorithm to Clustering Data on Peatland Hotspots in Sumatra]:https://iopscience.iop.org/article/10.1088/1755-1315/31/1/012012/pdf
[Nadia Rahmah and Imas Sukaesih Sitanggang, Determination of Optimal Epsilon (Eps) Value on DBSCAN Algorithm to Clustering Data on Peatland Hotspots in Sumatra](https://iopscience.iop.org/article/10.1088/1755-1315/31/1/012012/pdf)


[A dynamic Method for Discovering Density Varied Clusters]:https://www.researchgate.net/publication/256706346_A_dynamic_Method_for_Discovering_Density_Varied_Clusters
[Mohammed T. H. Elbatta and Wesam M. Ashour, A dynamic Method for Discovering Density Varied Clusters](https://www.researchgate.net/publication/256706346_A_dynamic_Method_for_Discovering_Density_Varied_Clusters)



[Choosing parameters of DBSCAN algorithm]: https://github.com/alitouka/spark_dbscan/wiki/Choosing-parameters-of-DBSCAN-algorithm
[Github, Choosing parameters of DBSCAN algorithm](https://github.com/alitouka/spark_dbscan/wiki/Choosing-parameters-of-DBSCAN-algorithm)

[How do I choose value of epsilon in DBSCAN?]: https://www.quora.com/How-do-I-choose-value-of-epsilon-in-DBSCAN
[Quora, How do I choose value of epsilon in DBSCAN?](https://www.quora.com/How-do-I-choose-value-of-epsilon-in-DBSCAN)

[Density-Based Clustering Validation]: http://www.dbs.ifi.lmu.de/~zimek/publications/SDM2014/DBCV.pdf
[Davoud Moulavi et al., Density-Based Clustering Validation](http://www.dbs.ifi.lmu.de/~zimek/publications/SDM2014/DBCV.pdf)



