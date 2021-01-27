
# Naive Bayes Classifier


The Naive Bayes classifier is based on the Bayes theorem

<a href="https://www.codecogs.com/eqnedit.php?latex=P(B|A)&space;=&space;\frac{P(A|B)P(B)}{P(A)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(B|A)&space;=&space;\frac{P(A|B)P(B)}{P(A)}" title="P(B|A) = \frac{P(A|B)P(B)}{P(A)}" /></a>


Given dataset `X=(x1, x2, .... xf), y`, there are `f` features for each event. We predict `y` as

<a href="https://www.codecogs.com/eqnedit.php?latex=P(y|X)&space;=&space;\frac{P(X|y)P(y)}{P(X)}&space;\propto&space;P(X|y)P(y)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(y|X)&space;=&space;\frac{P(X|y)P(y)}{P(X)}&space;\propto&space;P(X|y)P(y)" title="P(y|X) = \frac{P(X|y)P(y)}{P(X)} \propto P(X|y)P(y)" /></a>

The assumption in the Naive Bayes classifier is, the features `x1, x2...` are independent each other [[Rohith Gandhi]][Naive Bayes Classifier]. Therfore, we can rewrite the above posterior as

<a href="https://www.codecogs.com/eqnedit.php?latex=P(y|X)&space;=&space;P(y|x_1,x_2,\cdots,&space;x_f)&space;=&space;\frac{P(y)&space;P(x_1|y)P(x_2|y)\cdots&space;P(x_f|y)}{P(x_1)P(x_2)\cdots&space;P(x_f)}&space;\propto&space;P(y)\prod^f_{i=1}&space;P(x_i|y)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(y|X)&space;=&space;P(y|x_1,x_2,\cdots,&space;x_f)&space;=&space;\frac{P(y)&space;P(x_1|y)P(x_2|y)\cdots&space;P(x_f|y)}{P(x_1)P(x_2)\cdots&space;P(x_f)}&space;\propto&space;P(y)\prod^f_{i=1}&space;P(x_i|y)" title="P(y|X) = P(y|x_1,x_2,\cdots, x_f) = \frac{P(y) P(x_1|y)P(x_2|y)\cdots P(x_f|y)}{P(x_1)P(x_2)\cdots P(x_f)} \propto P(y)\prod^f_{i=1} P(x_i|y)" /></a>

The class `y` is determined by maximum probability

<a href="https://www.codecogs.com/eqnedit.php?latex=y&space;=&space;\textrm{argmax}_y&space;P(y)&space;\prod^f_{i=1}&space;P(x_i|y)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y&space;=&space;\textrm{argmax}_y&space;P(y)&space;\prod^f_{i=1}&space;P(x_i|y)" title="y = \textrm{argmax}_y P(y) \prod^f_{i=1} P(x_i|y)" /></a>

Given `x`, if `y=1` has higher probability than `y=0`, we assign y=1 for the event.

## Example

As a concrete example, we use the weather data (from [University of Edinburgh lecture](http://www.inf.ed.ac.uk/teaching/courses/inf2b/learnSlides/inf2b12-learnlec06.pdf)) as follows

![weather_data](images/example_data1.png)

The features are `x1=Outlook`, `x2=Temperature`, `x3=Humidity`, `x4=Windy`, and `y=Play`. We will have prior [[Zixuan Zhang]][Naive Bayes Explained]

<a href="https://www.codecogs.com/eqnedit.php?latex=P(\textrm{play})&space;=&space;\frac{\textrm{count&space;of&space;play}}{\textrm{total&space;count}}&space;=&space;\frac{9}{14}," target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(\textrm{play})&space;=&space;\frac{\textrm{count&space;of&space;play}}{\textrm{total&space;count}}&space;=&space;\frac{9}{14}," title="P(\textrm{play}) = \frac{\textrm{count of play}}{\textrm{total count}} = \frac{9}{14}," /></a>

and the likelihood as 

<a href="https://www.codecogs.com/eqnedit.php?latex=P(\textrm{sunny}|\textrm{play})&space;=&space;\frac{\textrm{count&space;of&space;sunny&space;and&space;play}}{\textrm{count&space;of&space;play}}=\frac{2}{9}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(\textrm{sunny}|\textrm{play})&space;=&space;\frac{\textrm{count&space;of&space;sunny&space;and&space;play}}{\textrm{count&space;of&space;play}}=\frac{2}{9}" title="P(\textrm{sunny}|\textrm{play}) = \frac{\textrm{count of sunny and play}}{\textrm{count of play}}=\frac{2}{9}" /></a>



## Metric

### Silhouette Score






## Reference


[Naive Bayes Explained]: https://towardsdatascience.com/naive-bayes-explained-9d2b96f4a9c0
[[Zixuan Zhang] Naive Bayes Explained](https://towardsdatascience.com/naive-bayes-explained-9d2b96f4a9c0)


[Naive Bayes Classifier]: https://towardsdatascience.com/naive-bayes-classifier-81d512f50a7c
[[Rohith Gandhi] Naive Bayes Classifier](https://towardsdatascience.com/naive-bayes-classifier-81d512f50a7c)




