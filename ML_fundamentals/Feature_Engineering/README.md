# Feature Engineering


Feature Selection/Extraction is one of the most important concepts in Machine learning which is a process of selecting a subset of relevant features/ attributes (such as a column in tabular data) that are most relevant for the modelling. Irrelevant or partially relevant features can negatively impact model performance. Benefits of Feature Engineering include [[Ashish Bansal]][Need for Feature Engineering in Machine Learning]:

1. Reduce Overfitting
2. Improves Accuracy
3. Reduce Training Time

In the following, we follow several blogs to list of feature engineering procedures [[Ashish Bansal]][Need for Feature Engineering in Machine Learning], [[Reinhard Sellmair]][How to handle correlated Features?]. The feature selection processes include:

### 1. Remove zero standard deviation features.

Of course, if a feature has only one value or all are missing values, it is not useful as a predictor in models.

### 2. Remove low variance features.

On the other hand, if a low variance feature is not likely to be a predictor in models.

```Python
from sklearn.feature_selection import VarianceThreshold
sel= VarianceThreshold(threshold=0.18)
sel.fit(df)
mask = sel.get_support()
reduced_df = df.loc[:, mask]
```

### 3. Remove highly-correlated features 

   Correlation is a way to understand the relationship between multiple variables and attributes in your dataset [[Will Badr]][Why Feature Correlation Matters.. A Lot!].
   
   If feature **A** and **B** have high correlation, it means that one of the features are redundant which may lead to overfitting or mutlicollinearity. Though boosted trees algorithms are immune to multicollinearity by nature, the multicollinearity issue can mislead interpretation on feature importance when using linear model.
   
   Note that correlation should not be interpreted as causation.

   We can simply set `threshold value > 0.8` to determine if features are highly-correlated, but in reality it should depend on dataset. For example, if feature **A** and **B** are highly correlated and **B** has higher correlation with respect to target (dependent) variable than **A**, we will retain feature **B**.
   
   Depending on variable types (numeric and categorical), there are several ways to calculate correlation:

   #### 3A. Numeric attributes

   `Pearson Correlation Coefficient` can be used with **continuous** variables that have a **linear** relationship, defined as

   <a href="https://www.codecogs.com/eqnedit.php?latex=\rho_{x,y}&space;=&space;\frac{\sum_i&space;(x_i&space;-&space;\bar{x})(y_i-\bar{y})}{\sigma_x&space;\sigma_y}," target="_blank"><img src="https://latex.codecogs.com/gif.latex?\rho_{x,y}&space;=&space;\frac{\sum_i&space;(x_i&space;-&space;\bar{x})(y_i-\bar{y})}{\sigma_x&space;\sigma_y}," title="\rho_{x,y} = \frac{\sum_i (x_i - \bar{x})(y_i-\bar{y})}{\sigma_x \sigma_y}," /></a>
   
   where <a href="https://www.codecogs.com/eqnedit.php?latex=\sigma_x" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sigma_x" title="\sigma_x" /></a> the standard deviation of `x`. The Pearson coefficient score used `pearsonr(X,Y)` from [scipy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html) and the first value is the Pearson Correlation Coefficients and the second value is the P-value.

   `Spearman Correlation Coefficient` or called `Spearman's Rank-Order Correlation` is used if variables have a **non-linear** relationship. It can also be used with **ordinal** categorical variables, and determines the strength and direction of the **monotonic relationship** between your two variables [[Laerd]][Spearman's Rank-Order Correlation]. You can get the Spearman coefficient score by running: `scipy.stats.spearmanr(X,Y)`.

   There is also another popular method called — `Kendall’s Tau Coefficient` which is also based on variable ranks but unlike Spearman’s coefficient, it does not take into account the difference between ranks.
   
   #### 3B. Categorical attributes


   The simplest way to convert a categorical attribute is using dummy variable, called **One-Hot Encoding**. This approach however may expand feature dimenionality. Theoretically it could be exponential growth.


   [`Cramér’s V`](https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_V) is based on a nominal variation of [**Pearson’s Chi-Square Test**](https://machinelearningmastery.com/chi-squared-test-for-machine-learning/), defined as

   <a href="https://www.codecogs.com/eqnedit.php?latex=V&space;=&space;\Big(\frac{\chi^2/n}{\text{min}(k-1,&space;r-1)}&space;\Big)^{0.5}," target="_blank"><img src="https://latex.codecogs.com/gif.latex?V&space;=&space;\Big(\frac{\chi^2/n}{\text{min}(k-1,&space;r-1)}&space;\Big)^{0.5}," title="V = \Big(\frac{\chi^2/n}{\text{min}(k-1, r-1)} \Big)^{0.5}," /></a>

   where <a href="https://www.codecogs.com/eqnedit.php?latex=\chi^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\chi^2" title="\chi^2" /></a> is derived from Pearson's chi-squared test, `n` is the grand total of observations, `k` being the number of columns and `r` being the number of rows. 

   The output is in the range of [0,1], where 0 means no association and 1 is full association. Unlike correlation, there are no negative values [[Shaked Zychlinski]][The Search for Categorical Correlation]. Like correlation, Cramer’s V is symmetrical — it is insensitive to swapping x and y. The blog author Shaked Zychlinski indicated the code to compute the correlation:

   ```Python
   def cramers_v(x, y):
      confusion_matrix = pd.crosstab(x,y)
      stat = ss.chi2_contingency(confusion_matrix)[0]
      n = confusion_matrix.sum().sum()
      phi2 = stat/n
      r,k = confusion_matrix.shape
      return np.sqrt(phi2/min(r-1, k-1))
   ```

   #### 3C. Between Categorical and Numeric Variables 

   refer [[Outside Two Standard Deviations]][An overview of correlation measures between categorical and continuous variables].

### 4. Information Value (IV) and Weight of Evidence (WOE)

The weight of evidence tells the predictive power of an **independent** variable (predictor) in relation to the **dependent** variable. Since it evolved from credit scoring world, it is generally described as a measure of the separation of good and bad customers. "Bad Customers" refers to the customers who defaulted on a loan and won't pay back, and "Good Customers" refers to the customers who paid back loan. [[Deepanshu Bhalla]][Weight of evidence (WOE) and information value (IV) explained], [[Roopam Upadhyay]][Information Value (IV) and Weight of Evidence (WOE) – A Case Study from Banking (Part 4)] In a particular group, say bin-i, WOE reads

<a href="https://www.codecogs.com/eqnedit.php?latex=\text{WOE}_i&space;=&space;\ln&space;\Big(&space;\frac{&space;\text{%&space;of&space;Good&space;(nonfraud)&space;in&space;bin-i}&space;}&space;{\text{%&space;of&space;Bad&space;(fraud)&space;in&space;bin-i}}&space;\Big)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\text{WOE}_i&space;=&space;\ln&space;\Big(&space;\frac{&space;\text{%&space;of&space;Good&space;(nonfraud)&space;in&space;bin-i}&space;}&space;{\text{%&space;of&space;Bad&space;(fraud)&space;in&space;bin-i}}&space;\Big)" title="\text{WOE}_i = \ln \Big() \frac{ \text{% of Good (nonfraud) in bin-i} } {\text{% of Bad (fraud) in bin-i}} \Big)," /></a>

where `% of Goods` and `% of Bads` mean that % of Good Customers in the bin-`i` over all Good customers,  and % of Bad Customers in the bin-`i` over bad customers, respectively and `ln` is natural log. Note that for each bin, there is one WOE.

To calulate WOE, we need to create bins (like every 10% population, or a equal value range like age 20-30, 30-40...) for a continuous independent variable (if catgeorical, no need). Fewer bins, more smoothing and leave out noise. For each bin, we have a WOE. [[Deepanshu Bhalla]][Weight of evidence (WOE) and information value (IV) explained] has more detailed discussion on binning continuous variable.

Information value (IV) is the the sum over all bins:

<a href="https://www.codecogs.com/eqnedit.php?latex=IV&space;=&space;\sum_i&space;\Big[&space;\big(\text{%&space;of&space;Good&space;in&space;bin-i}\big)&space;-&space;\big(&space;\text{%&space;of&space;Bad&space;in&space;bin-i}&space;\big)&space;\Big]*\text{WOE}_i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?IV&space;=&space;\sum_i&space;\Big[&space;\big(\text{%&space;of&space;Good&space;in&space;bin-i}\big)&space;-&space;\big(&space;\text{%&space;of&space;Bad&space;in&space;bin-i}&space;\big)&space;\Big]*\text{WOE}_i" title="IV = \sum_i \Big[ \big(\text{% of Good in bin-i}\big) - \big( \text{% of Bad in bin-i} \big) \Big]*\text{WOE}_i" /></a>


A feature with IV < 0.02 suggests it is a useless preditor. [[Roopam Upadhyay]][Information Value (IV) and Weight of Evidence (WOE) – A Case Study from Banking (Part 4)], [[Sundar Krishnan]][Weight of evidence and Information Value using Python], [[Deepanshu Bhalla]][Weight of evidence (WOE) and information value (IV) explained] and in feature engineering we can remove it. `0.3 < IV < 0.5` indicates a strong predictor. If `IV > 0.5`, instead we should be suspicious to check it is useful. 


### 5. Feature Selection By Machine Learning

Finding out the coefficients with respect to features using logistic regression or with `L1 regularization` (Lasso). Remove those features which have low coefficients. 



   
   




## Summary













## Reference

[Need for Feature Engineering in Machine Learning]: https://towardsdatascience.com/need-for-feature-engineering-in-machine-learning-897df2ed00e6
[[Ashish Bansal] Need for Feature Engineering in Machine Learning](https://towardsdatascience.com/need-for-feature-engineering-in-machine-learning-897df2ed00e6)


[Weight of evidence (WOE) and information value (IV) explained]: https://www.listendata.com/2015/03/weight-of-evidence-woe-and-information.html
[[Deepanshu Bhalla] Weight of evidence (WOE) and information value (IV) explained](https://www.listendata.com/2015/03/weight-of-evidence-woe-and-information.html)


[Spearman's Rank-Order Correlation]: https://statistics.laerd.com/statistical-guides/spearmans-rank-order-correlation-statistical-guide.php#:~:text=The%20Spearman's%20rank%2Dorder%20correlation%20is%20the%20nonparametric%20version%20of,association%20between%20two%20ranked%20variables.
[[Laerd] Spearman's Rank-Order Correlation](https://statistics.laerd.com/statistical-guides/spearmans-rank-order-correlation-statistical-guide.php#:~:text=The%20Spearman's%20rank%2Dorder%20correlation%20is%20the%20nonparametric%20version%20of,association%20between%20two%20ranked%20variables.)


[An overview of correlation measures between categorical and continuous variables]: https://medium.com/@outside2SDs/an-overview-of-correlation-measures-between-categorical-and-continuous-variables-4c7f85610365
[[Outside Two Standard Deviations] An overview of correlation measures between categorical and continuous variables](https://medium.com/@outside2SDs/an-overview-of-correlation-measures-between-categorical-and-continuous-variables-4c7f85610365)


[How to handle correlated Features?]: https://www.kaggle.com/reisel/how-to-handle-correlated-features
[[Reinhard Sellmair] Kaggle: How to handle correlated Features?](https://www.kaggle.com/reisel/how-to-handle-correlated-features)


[Information Value (IV) and Weight of Evidence (WOE) – A Case Study from Banking (Part 4)]: http://ucanalytics.com/blogs/information-value-and-weight-of-evidencebanking-case/
[[Roopam Upadhyay] Information Value (IV) and Weight of Evidence (WOE) – A Case Study from Banking (Part 4)](http://ucanalytics.com/blogs/information-value-and-weight-of-evidencebanking-case/)



[The Search for Categorical Correlation]: https://towardsdatascience.com/the-search-for-categorical-correlation-a1cf7f1888c9
[[Shaked Zychlinski] The Search for Categorical Correlation](https://towardsdatascience.com/the-search-for-categorical-correlation-a1cf7f1888c9)


[Weight of evidence and Information Value using Python]: https://medium.com/@sundarstyles89/weight-of-evidence-and-information-value-using-python-6f05072e83eb
[[Sundar Krishnan] Weight of evidence and Information Value using Python](https://medium.com/@sundarstyles89/weight-of-evidence-and-information-value-using-python-6f05072e83eb)


[Why Feature Correlation Matters.. A Lot!]: https://towardsdatascience.com/why-feature-correlation-matters-a-lot-847e8ba439c4
[[Will Badr] Why Feature Correlation Matters.. A Lot!](https://towardsdatascience.com/why-feature-correlation-matters-a-lot-847e8ba439c4)

