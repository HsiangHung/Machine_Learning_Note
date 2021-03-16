
# Anti-Abuse

In social media, fake profiles can be used to carry out many different types of abuse: scraping, spamming, fraud, and phishing, among others. By preventing or promptly removing fake accounts on the site, we ensure that legitimate users are protected.

## Feature Design:

### 1. Attributes present at or around registration time — **Profile** Features

A set of human-curated words and phrases that violated Terms of Service and Community Guidelines — to identify and remove potentially fraudulent accounts. 

However, the list tended to handle context works rather poorly. For instance, while the word “escort” was sometimes associated with prostitution, it was also used in contexts like a “security escort” or “medical escort.”. Linkedin identified problematic words responsible for high levels of **false positives** and sampled appropriate accounts from the member base containing these words. The accounts were then manually labeled and added to the training set, after which the model was trained and deployed in production.






### 2. Attributes that develop over time — Connections with other users in the network, activity or **behaviour** patterns (graph)

### LinkedIn

Over 660 million users, 303 million of whom are active monthly [source](https://venturebeat.com/2020/01/16/linkedin-is-using-ai-to-spot-and-remove-inappropriate-user-accounts/).

[Automated Fake Account Detection at LinkedIn]: https://engineering.linkedin.com/blog/2018/09/automated-fake-account-detection-at-linkedin
[[Jenelle Bray] Automated Fake Account Detection at LinkedIn](https://engineering.linkedin.com/blog/2018/09/automated-fake-account-detection-at-linkedin)

![](images/fake_account_funnel.png)

1. **Registration scoring**: For many types of abuse, attackers require a **large** number of fake accounts for the attack to be financially feasible. Every new user registration attempt is evaluated by a machine-learned model that gives an abuse risk score. Signup attempts with a low abuse risk score are allowed to register right away, while attempts with a high abuse risk score are prevented from creating an account. Attempts with **medium** risk scores are **challenged by our security measures to verify** that they are real people.

2. **Clustering**: Create clusters of accounts by grouping them based on shared attributes, and then find account clusters that show a statistically abnormal distribution of data, which is indicative of being created or controlled by a single bad actor. These are supervised machine learning models that **use features per cluster** instead of per member. The models score the clusters, then propagate the cluster label to individual accounts. This cluster approach allows us to catch more fake accounts quickly, faster than we could if we wait for them to start taking abusive actions on the site (see [here](https://github.com/HsiangHung/Machine_Learning_Note/tree/master/ML_application/Anti-Abuse#clustering) for more details).

3. **Activity-based models**: Our models require more information on these accounts’ **behavior** (types of bad behavior, like send spam inMail, illeagal post) to decide whether they are indeed fake.

4. **Human element**: Members' reports and manual review investigation.










## Clustering 

The blog [[Preeti Hemant]][Detecting Suspicious Accounts in Online Social Networks] implements clustering method to create features, and use the clustering results to labeled individual account. The cluster detection pipeline is as follows (credit from [[Preeti Hemant]][Detecting Suspicious Accounts in Online Social Networks]):

![](images/cluster_detection_pipeline.png)

1. **Cluster Builder**: this component takes the raw list of accounts and builds clusters of accounts along with their raw features. Then each individual account can be identified clusters.

2. **Profile Featurizer**: this module converts raw data for each cluster into a single numerical vector representing the cluster, extracting information from the raw features. The features could be

* Basic distribution features — Statistical measures for each column. Mean or quartiles for numerical features, number of unique values for categorial features
* Pattern features — Mapping of user-generated text to a categorical space (e.g. patterns in email addresses)
* Frequency features — Frequency of each feature value over all the individual accounts and their distribution over these frequencies. Clusters of legitimate accounts have some high-frequency and some low-frequency data, clusters of **malicious accounts** however, show **less variance** in their data frequencies.

3. **Account Scorer**: this component assigns the clustering aggregated features to individual account. We then used the generated features plus raw features to train the models and evaluate their performance on previously unseen data.



## Reference

[Detecting Suspicious Accounts in Online Social Networks]: https://towardsdatascience.com/detecting-suspicious-accounts-in-online-social-networks-48eabf4c75b6
[[Preeti Hemant] Detecting Suspicious Accounts in Online Social Networks](https://towardsdatascience.com/detecting-suspicious-accounts-in-online-social-networks-48eabf4c75b6)



