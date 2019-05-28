
# DBSCAN clustering



## Choosing Epsilon in DBSCAN

It calculates distance from each point to its nearest neighbor within the same partition, so, for a small fraction of points this distance will not be accurate [[Github]][Choosing parameters of DBSCAN algorithm]


## Validation of Brutal Searching Epsilon in DBSCAN

Validation to choose epsilon in DBSSCAN. [[Davoud Moulavi et al.]][Density-Based Clustering Validation]


In the following case, the data variance along the first principal component occurs on different classes. Therefore, after PCA, the first principal component is useful for classification.
![inter_class_variance](images/inter_class_variance.png)


   



## Summary












## Reference


[Choosing parameters of DBSCAN algorithm]: https://github.com/alitouka/spark_dbscan/wiki/Choosing-parameters-of-DBSCAN-algorithm
[Github, Choosing parameters of DBSCAN algorithm](https://github.com/alitouka/spark_dbscan/wiki/Choosing-parameters-of-DBSCAN-algorithm)



[How do I choose value of epsilon in DBSCAN?]: https://www.quora.com/How-do-I-choose-value-of-epsilon-in-DBSCAN
[Quora, How do I choose value of epsilon in DBSCAN?](https://www.quora.com/How-do-I-choose-value-of-epsilon-in-DBSCAN)

[Density-Based Clustering Validation]: http://www.dbs.ifi.lmu.de/~zimek/publications/SDM2014/DBCV.pdf
[Davoud Moulavi et al., Density-Based Clustering Validation](http://www.dbs.ifi.lmu.de/~zimek/publications/SDM2014/DBCV.pdf)



