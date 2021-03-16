
# Anti-Abuse


**Feature Design**:
1. Attributes present at or around registration time — **Profile** Features
2. Attributes that develop over time — Connections with other users in the network, activity or **behaviour** patterns (graph)




## Clustering 

The blog [[Preeti Hemant]][Detecting Suspicious Accounts in Online Social Networks] implements clustering method to create features, and use the clustering results to labeled individual account. The cluster detection pipeline is as follows:

![](images/cluster_detection_pipeline.png)

1. **Cluster Builder**: this component takes the raw list of accounts and builds clusters of accounts along with their raw features. Then each individual account can be identified clusters.

2. **Profile Featurizer**: this module converts raw data for each cluster into a single numerical vector representing the cluster, extracting information from the raw features. The features could be

* Basic distribution features — Statistical measures for each column. Mean or quartiles for numerical features, number of unique values for categorial features
* Pattern features — Mapping of user-generated text to a categorical space (e.g. patterns in email addresses)
* Frequency features — Frequency of each feature value over all the individual accounts and their distribution over these frequencies. Clusters of legitimate accounts have some high-frequency and some low-frequency data, clusters of **malicious accounts** however, show **less variance** in their data frequencies.





[Detecting Suspicious Accounts in Online Social Networks]: https://towardsdatascience.com/detecting-suspicious-accounts-in-online-social-networks-48eabf4c75b6
[[Preeti Hemant] Detecting Suspicious Accounts in Online Social Networks](https://towardsdatascience.com/detecting-suspicious-accounts-in-online-social-networks-48eabf4c75b6)



