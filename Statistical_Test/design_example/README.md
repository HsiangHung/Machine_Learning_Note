
# A Guide to A/B Testing

An A/B test is designed to test the hypothesis in such a way that observed difference between the two groups should be either due to random chance or due to a true difference between the groups.

Before getting deeper into A/B testing, let’s answer the following questions [[Idil Ismiguzel]][A Guide to A/B Testing — How to Formulate, Design and Interpret]:

### 1. What can be tested?
Visible and invisible changes can be tested with A/B testing. Examples to visible changes can be new additions to the UI, changes in the design and layout or headline messages. A very popular example is Google’s 41 (yes, not 2) different shades of blue experiment where they randomly showed a shade of blue to each 2.5% of users to understand which color shade earns more clicks. Examples to invisible changes can be page load time or testing different recommendation algorithms. A popular example is Amazon’s A/B test that showed every 100ms increase in page load time decreased the sales by 1%.

### 2. What can’t be tested?
New experiences are not suitable for implementing A/B tests. Because a new experience can show change aversion behavior where users don’t like changes and prefer to stick to the old version, or it can show novelty effect where users feel very excited and want to test out everything

### 3. How can we choose the metrics?
Metric selection needs to consider both sensitivity and robustness. Sensitivity means that metrics should be able to catch the changes and robustness means that metrics shouldn’t change too much from irrelevant effects. As an example, most of the time if the metric is a “mean”, it is sensitive to outliers but not robust. If the metric is a “median”, it is robust but not sensitive for small group changes.

In order to consider both sensitivity and robustness in the metric selection, we can apply filtering and segmentation while creating the control and experiment samples. Filtering and segmentation can be based on user demographics (i.e. age, gender), the language of the platform, internet browser, device type (i.e. iOS or Android), cohort and etc.








#### Reference

[A Guide to A/B Testing — How to Formulate, Design and Interpret]: https://towardsdatascience.com/a-guide-to-a-b-testing-how-to-formulate-design-and-interpret-f820cc62e21a
[[Idil Ismiguzel] A Guide to A/B Testing — How to Formulate, Design and Interpret](https://towardsdatascience.com/a-guide-to-a-b-testing-how-to-formulate-design-and-interpret-f820cc62e21a)

