
# Recommendation Engine 

We divides recommendation problem into 2 subproblems: 1) choosing top-N candidates and 2) ranking them.

## Collaborative filtering

We considered a recommendation problem as a **supervised** machine learning task:

* User-based collaborative filtering
* Item-based collaborative filtering
* Matrix factorization

We can also apply **unsupervised** methods to solve the recommendation problem.

At the start of a business, there is a lack of previous users’ grades, and clustering would be the best approach. We identify user groups and recommend each user in this group the same items. When we have enough data, using clustering as the first step is helpful for shrinking the selection of relevant neighbors in collaborative filtering algorithms.





<!-- ![word_embedding](images/word_embedding.png) -->


## Cold Start 

If an item was already popular with a certain group of people, then others that fit the group’s profile are likely to respond well to the ad. However, if each time a new item is placed on your site, it goes through the cold start phase due to the lack of valuable user interactions. 

Recommendation engines that run on collaborative filtering recommend each item (products advertised on your site) based on user actions. The more user actions an item has, the easier it is to tell which user would be interested in it and what other items are similar to it. As time progresses, the system will be able to give more and more accurate recommendations.

We can list products based on the date of the post: the newest first. Even though the newest ads are actually the most relevant ones, a recommendation system has far less confidence in recommending them to your users than it has with older items.

### The solution

**Content-based filtering** is the method that answers this question. Our system first uses the metadata of new products when creating recommendations, while visitor action is secondary for a certain period of time.

Every recommendation solution has a different method to cope with the cold start problem, and after getting over the rough cold start, the real work of the engine begins.

* The very first step is to apply a popularity based strategy. 

* Trending products can be determined by global trends and what’s been popular recently, regionally, or at that certain time of the day.

* Next step, you can narrow the selection of ads you display for visitors by making use of contextual information: Geolocating users with either their geoIP or their mobile device’s GPS co- ordinates.

* Knowing the referrer (which site the visitor came from), the device (mobile, desktop), the operating system (iOS, Windows, Android) and the browser type (Chrome, IE, Safari, etc) will help with personalizing the ads you display.


[Recommendation System Algorithms]: https://blog.statsbot.co/recommendation-system-algorithms-ba67f39ac9a3
[[Daniil Korbut] Recommendation System Algorithms](https://blog.statsbot.co/recommendation-system-algorithms-ba67f39ac9a3)


[The Cold Start Problem for Recommender Systems]: https://medium.com/yusp/the-cold-start-problem-for-recommender-systems-89a76505a7
[[Mark Milankovich] The Cold Start Problem for Recommender Systems](https://medium.com/yusp/the-cold-start-problem-for-recommender-systems-89a76505a7)



