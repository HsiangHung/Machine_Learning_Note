# Feature Engineering


Feature Selection/Extraction is one of the most important concepts in Machine learning which is a process of selecting a subset of relevant features/ attributes (such as a column in tabular data) that are most relevant for the modelling. Irrelevant or partially relevant features can negatively impact model performance. Benefits of Feature Engineering include [[Ashish Bansal]][Need for Feature Engineering in Machine Learning]:
1. Reduce Overfitting
2. Improves Accuracy
3. Reduce Training Time

In the following, we follow several blogs to list of feature engineering procedures [[Ashish Bansal]][Need for Feature Engineering in Machine Learning], [[Reinhard Sellmair]][How to handle correlated Features?]. The steps include:

### A. Remove zero standard deviation features.

### B. Remove low variance features.

```Python
from sklearn.feature_selection import VarianceThreshold
sel= VarianceThreshold(threshold=0.18)
sel.fit(df)
mask = sel.get_support()
reduced_df = df.loc[:, mask]
```

### C. Remove highly-correlated features 

   Correlation is a way to understand the relationship between multiple variables and attributes in your dataset [[Will Badr]][Why Feature Correlation Matters.. A Lot!].
   
   The features A and B have high correlation coefficient meaning that the features are redundant which may lead to overfitting or mutlicollinearity. Though boosted trees algorithms are immune to multicollinearity by nature, the multicollinearity issue can mislead interpretation on feature importance when using linear model.
   
   Note that correlation should not be interpreted as causation.

   We can simply set `threshold value > 0.8` as threshold value but in reality it should depend on dataset. Depending on variable types (numeric and categorical), there are several ways to calculate correlation:

   #### C1. Numeric attributes

   `Pearson Correlation Coefficient` can be used with continuous variables that have a **linear** relationship. The Pearson coefficient score used `pearsonr(X,Y)` and the first value is the Pearson Correlation Coefficients and the second value is the P-value.

   `Spearman Correlation Coefficient` is used if variables have a **non-linear** relationship. It can also be used with ordinal categorical variables. You can get the Spearman coefficient score by running: `scipy.stats.spearmanr(X,Y)`.

   There is also another popular method called — `Kendall’s Tau Coefficient` which is also based on variable ranks but unlike Spearman’s coefficient, it does not take into account the difference between ranks.
   
   #### C2. Categorical attributes

   `Cramér’s V` is based on a nominal variation of [**Pearson’s Chi-Square Test**](https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_V). The output is in the range of [0,1], where 0 means no association and 1 is full association. Unlike correlation, there are no negative values [[Shaked Zychlinski]][The Search for Categorical Correlation]. Like correlation, Cramer’s V is symmetrical — it is insensitive to swapping x and y. The blog author Shaked Zychlinski indicated the code to compute the correlation:

   ```Python
   def cramers_v(x, y):
      confusion_matrix = pd.crosstab(x,y)
      stat = ss.chi2_contingency(confusion_matrix)[0]
      n = confusion_matrix.sum().sum()
      phi2 = stat/n
      r,k = confusion_matrix.shape
      return np.sqrt(phi2/min(r-1, k-1))
   ```


### D. Feature Reduction 



   
   




## Summary

The blog [Gradient Boosting from scratch](https://medium.com/mlreview/gradient-boosting-from-scratch-1e317ae4587d) shows very nice and decent diagrams to interpret the difference between bagging and boosting. 

![ensembling](images/ensembling.png)

![bagging_and_boostin](images/bagging_and_boosting.png)












## Reference

[Need for Feature Engineering in Machine Learning]: https://towardsdatascience.com/need-for-feature-engineering-in-machine-learning-897df2ed00e6
[[Ashish Bansal] Need for Feature Engineering in Machine Learning](https://towardsdatascience.com/need-for-feature-engineering-in-machine-learning-897df2ed00e6)



[How to handle correlated Features?]: https://www.kaggle.com/reisel/how-to-handle-correlated-features
[[Reinhard Sellmair] How to handle correlated Features?](https://www.kaggle.com/reisel/how-to-handle-correlated-features)



[The Search for Categorical Correlation]: https://towardsdatascience.com/the-search-for-categorical-correlation-a1cf7f1888c9
[[Shaked Zychlinski] The Search for Categorical Correlation](https://towardsdatascience.com/the-search-for-categorical-correlation-a1cf7f1888c9)


[Why Feature Correlation Matters.. A Lot!]: https://towardsdatascience.com/why-feature-correlation-matters-a-lot-847e8ba439c4
[[Will Badr] Why Feature Correlation Matters.. A Lot!](https://towardsdatascience.com/why-feature-correlation-matters-a-lot-847e8ba439c4)

