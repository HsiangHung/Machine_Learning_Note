
# Measure Similarity Using Time-series data

##  Dynamic time warping
To measure the similarity between two time-series data, we can use [**Dynamic time warping**](https://en.wikipedia.org/wiki/Dynamic_time_warping).

The idea to compare arrays with different length is to build one-to-many and many-to-one matches so that the total distance can be minimised between the two. [[Ricardo Portilla and Brenner Heintz]][Understanding Dynamic Time Warping], [[Jeremy Zhang]][Dynamic Time Warping - Explanation and Code Implementation]

Suppose we have two different arrays red and blue with different length, [[Ricardo Portilla and Brenner Heintz]][Understanding Dynamic Time Warping] provided a good interpreation plot:

![](images/Euclidean_vs_DTW.jpg)

In Python, scipy supports a libray to compute dynamic time wrapping, see [Dynamic Time Warping (DTW)](https://dtaidistance.readthedocs.io/en/latest/usage/dtw.html):
```
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean

x = np.array([1, 2, 3, 3, 7])
y = np.array([1, 2, 2, 2, 2, 2, 2, 4])

distance, path = fastdtw(x, y, dist=euclidean)

print(distance)
``` 
It returns distance = 5.



#### Reference

* [How can we quantify similarity between time series?]: https://tech.gorilla.co/how-can-we-quantify-similarity-between-time-series-ed1d0b633ca0
[[Alexander Bader] How can we quantify similarity between time series?](https://tech.gorilla.co/how-can-we-quantify-similarity-between-time-series-ed1d0b633ca0)

* [Understanding Dynamic Time Warping]: https://www.databricks.com/blog/2019/04/30/understanding-dynamic-time-warping.html
[[Ricardo Portilla and Brenner Heintz] Understanding Dynamic Time Warping](https://www.databricks.com/blog/2019/04/30/understanding-dynamic-time-warping.html)

* [Dynamic Time Warping - Explanation and Code Implementation]: https://towardsdatascience.com/dynamic-time-warping-3933f25fcdd
[[Jeremy Zhang] Dynamic Time Warping - Explanation and Code Implementation](https://towardsdatascience.com/dynamic-time-warping-3933f25fcdd)

