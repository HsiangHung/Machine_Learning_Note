
# Support Vector Machine


## What Does "Small Dataset" Mean?


[[Shuyu Luo]][Loss Function(Part III): Support Vector Machine]

Support vectors are data points that are closer to the hyperplane and influence the position and orientation of the hyperplane. Using these support vectors, we maximize the margin of the classifier. Deleting the support vectors will change the position of the hyperplane. These are the points that help us build our SVM.

![support_vectors](images/support_vector.png)



## Summary


For small datasets we should avoid overfitting. Try [[Ahmed El Deeb]][What to do with “small” data?], [[Rafael Alencar]][Dealing with very small datasets]
* Use simple models
* Beware the outliers
* Select the features
* Balance the dataset with synthetic samples (SMOTE)
* Model averaging






## Reference

[Loss Function(Part III): Support Vector Machine]: https://towardsdatascience.com/optimization-loss-function-under-the-hood-part-iii-5dff33fa015d
[[Shuyu Luo] Loss Function(Part III): Support Vector Machine](https://towardsdatascience.com/optimization-loss-function-under-the-hood-part-iii-5dff33fa015d)

