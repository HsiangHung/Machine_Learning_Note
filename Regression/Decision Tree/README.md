
# Decision Tree - Regression


This article is dedicated to describe how a DT works in regreesion problems, followed by [[Saed Sayad]][Decision Tree - Regression]. 

Suppose we have a dataset like

![dataset](images/dataset.png)

where attributes (predictors) are `X = (outlook, temp, humidity, windy)`, and the target variable is `y = hours played`, which is continuous. Therefore it is a regression problem. We will explain how to create a regression model as shown above (on the right).

## Split Features Using Continuous Targets

For each split, we compute standard deviation (SD) for each attribute, and choose the attribute with maximal **Standard Deviation Reduction (SDR)** to split. The SD is computed for each attribute as 

$$S(X, y) = \sum_{c}P(c)S(c).$$

The processes are as folllows:

1. First, at root, we compute SD for target variables `hours played`. The average `hours play` (target) is 39.8 and the SD is 9.32.

2. Next we choose an attribute. Suppose we choose `overlook` to split, there are three categories: "overcast", "rainy", "sunny". After that, the data will be split as follows: ![split](images/DTR_split.png)  

Then the SDR is computed `S("overlook", "hours played") = 9.32 - 7.66 = 1.66` (shown as below (a)) ![steps](images/SDR.png) 

3. Similarly, we compute SDR for other attributes: `temp`, `humidity`, `windy`, as shown in (b). Among these predictors, `outlook` attribute has maximal SDR, so we select `overlook` to split first.

4. Next we look at nodes described by "overcast", "rainy", "sunny". In practice, we need some termination criteria. For example, when coefficient of deviation (CV) for a branch becomes smaller than a certain threshold (e.g., 10%) and/or when too few instances (n) remain in the branch (e.g. n=3). For node "overcast" the subset does not need any further splitting because its CV (8%) is less than the threshold (10%). Thus "Overcast" is a leaf node. 

5. However, the "Sunny" branch has an CV (28%) more than the threshold (10%) which needs further splitting. We select "Temp" as the best best node after "Outlook" because it has the largest SDR. 


## Coefficient of Variation

In [[Saed Sayad]][Decision Tree - Regression], the author mentioned using Coefficient of Variance (CV), to decide when to stop splitting in the DTR. CV is defined as SD/mean. 

Followed the above exmaple, after first split, in the `overlook = overcast` branch, CV is 8%, below threshold 10%. Therefore we can stop to split this branch.



## Reference


[Decision Tree - Regression]: https://www.saedsayad.com/decision_tree_reg.htm#:~:text=Decision%20tree%20builds%20regression%20or,decision%20nodes%20and%20leaf%20nodes.
[[Saed Sayad] Decision Tree - Regression](https://www.saedsayad.com/decision_tree_reg.htm#:~:text=Decision%20tree%20builds%20regression%20or,decision%20nodes%20and%20leaf%20nodes.)


