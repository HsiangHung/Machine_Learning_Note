
# What is stationarity?

`X` is strictly stationary meaning if the distribution of (`x[t+1]`,…,`x[t+k]`) is identical to that of (`x[1]`,…,`x[k]`) for each t and k. From Wiki: a stationary process is a stochastic process whose joint **probability distribution does not change when shifted in time or space** (by IrishStat, [[StackExchange, 1]][Why does a time series have to be stationary?]). Consequently, a stationary time-series is one whose statistical properties such as **mean**, **variance**, **autocorrelation**, etc. are all **constant over time**. [[Robert Nau, Stationarity and differencing]][Stationarity and differencing]

Most statistical forecasting methods are based on the assumption that the time series can be rendered approximately stationary (i.e., "stationarized") through the use of mathematical transformations. Thus, finding the sequence of transformations to stationarize a time-series often provides important clues in the search for an appropriate forecasting model. 

It turns out that a lot of data becomes stationary after certain transformation. [ARIMA](https://people.duke.edu/~rnau/411arim.htm) model is a model for non-stationarity, by stationarizing a time-series through **differencing** (assumes that the data becomes stationary after differencing). If a series is stationary, we can just implement ARMA model (by mpiktas [[StackExchange, 1]][Why does a time series have to be stationary?] and Rob Hyndman [[Rob Hyndman]][The ARIMAX model muddle]). 


# Why time-series data needs to be stationary?

If the series is consistently increasing over time, the sample mean and variance will grow with the size of the sample, and they will always underestimate the mean and variance in future periods. 

In addition to this, stationary processes avoid the problem of **spurious regression**. 


# How to transform nonstationary time-series to be stationary?

Most business and economic time series are far from stationary when expressed in their original units of measurement, and even after deflation or seasonal adjustment they will typically still exhibit trends, cycles, random-walking, and other non-stationary behavior.


### Trend-stationary

If the series has a stable long-run trend and tends to revert to the trend line following a disturbance, it may be possible to stationarize it by de-trending (e.g., by fitting a trend line and subtracting it out prior to fitting a model, or else by including the time index as an independent variable in a regression or ARIMA model), perhaps in conjunction with logging or deflating. Such a series is said to be **trend-stationary**.


### Difference-stationary

Sometimes even de-trending is not sufficient to make the series stationary, however.
After detrending, if the mean, variance, and autocorrelations of the original series are still not constant in time, we may need to transform the de-trended series into a series of period-to-period and/or season-to-season differences. Such a series is said to be **difference-stationary**.


### ARIMA(p,d,q)

By Sunny Mewati [[Quora, 1]][What's the difference between ARMA, ARIMA, and ARIMAX, in layman's terms?], Box and Jenkins claimed (successfully) [[Box, Jenkins, Reinsel]][Time Series Analysis] that nonstationary data can be made stationary by differencing the series. This series, <a href="http://www.codecogs.com/eqnedit.php?latex=Y^*" target="_blank"><img src="http://latex.codecogs.com/gif.latex?Y^*" title="Y^*" /></a> is the input in Box-Jenkins analysis. The general model for <a href="http://www.codecogs.com/eqnedit.php?latex=Y^*" target="_blank"><img src="http://latex.codecogs.com/gif.latex?Y^*" title="Y^*" /></a> is written as

<a href="http://www.codecogs.com/eqnedit.php?latex=Y^*_t&space;=&space;\phi_1&space;Y^*_{t-1}&space;&plus;&space;\phi_2&space;Y^*_{t-2}&space;&plus;&space;\cdots&space;&plus;&space;\phi_p&space;Y^*_{t-p}&space;&plus;&space;\epsilon_t&space;&plus;&space;\theta_1&space;\epsilon_{t-1}&space;&plus;&space;\theta_2&space;\epsilon_{t-2}&space;&plus;&space;\cdots&space;\theta_q&space;\epsilon_{t-q}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?Y^*_t&space;=&space;\phi_1&space;Y^*_{t-1}&space;&plus;&space;\phi_2&space;Y^*_{t-2}&space;&plus;&space;\cdots&space;&plus;&space;\phi_p&space;Y^*_{t-p}&space;&plus;&space;\epsilon_t&space;&plus;&space;\theta_1&space;\epsilon_{t-1}&space;&plus;&space;\theta_2&space;\epsilon_{t-2}&space;&plus;&space;\cdots&space;\theta_q&space;\epsilon_{t-q}" title="Y^*_t = \phi_1 Y^*_{t-1} + \phi_2 Y^*_{t-2} + \cdots + \phi_p Y^*_{t-p} + \epsilon_t + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2} + \cdots \theta_q \epsilon_{t-q}" /></a>

where ϕ and θ are unknown parameters and ϵ are independent identically distributed error terms with zero mean. Here, <a href="http://www.codecogs.com/eqnedit.php?latex=Y^*" target="_blank"><img src="http://latex.codecogs.com/gif.latex?Y^*" title="Y^*" /></a>
is only expressed in terms of its past values and the current and past values of error terms. This model is called Autoregressive Integrated Moving Average or `ARIMA(p,d,q)` model of Y. `p` is the number of lagged values of <a href="http://www.codecogs.com/eqnedit.php?latex=Y^*" target="_blank"><img src="http://latex.codecogs.com/gif.latex?Y^*" title="Y^*" /></a> which represents the autoregressive (AR) nature of model, `q` is the number of lagged values of the error term which represents the moving average (MA) nature of model and `d` is the number of times Y has to be differences to produce the stationary <a href="http://www.codecogs.com/eqnedit.php?latex=Y^*" target="_blank"><img src="http://latex.codecogs.com/gif.latex?Y^*" title="Y^*" /></a>.

The AR component is the linear combination of observable values of Y while the MA component is the linear combination of the unobservable white noise disturbance terms. This is just one of those trivialities that you would get used to with time.

The term **integrated** implies that in order to obtain a forecast of Y, we have to sum up (or **integrate over**) the values of <a href="http://www.codecogs.com/eqnedit.php?latex=Y^*" target="_blank"><img src="http://latex.codecogs.com/gif.latex?Y^*" title="Y^*" /></a> because <a href="http://www.codecogs.com/eqnedit.php?latex=Y^*" target="_blank"><img src="http://latex.codecogs.com/gif.latex?Y^*" title="Y^*" /></a> are the differenced values of the original series Y. If no differencing is involved, this model is called an Autoregressive Moving Average, i.e. `ARMA(p,q)`.


### ARIMAX model

Econometricians developed another class of models that incorporated auroregressive and moving average components of Box-Jenkins approach with the ‘explanatory variables’ approach of standard econometrics [[Rob Hyndman]][The ARIMAX model muddle]. The simplest of such models is the ARIMAX which is just an ARIMA with additional explanatory variables, written as

<a href="http://www.codecogs.com/eqnedit.php?latex=Y^*_t&space;=&space;\beta&space;x_t&space;&plus;&space;\phi_1&space;Y^*_{t-1}&space;&plus;&space;\phi_2&space;Y^*_{t-2}&space;&plus;&space;\cdots&space;&plus;&space;\phi_p&space;Y^*_{t-p}&space;&plus;&space;\epsilon_t&space;&plus;&space;\theta_1&space;\epsilon_{t-1}&space;&plus;&space;\theta_2&space;\epsilon_{t-2}&space;&plus;&space;\cdots&space;\theta_q&space;\epsilon_{t-q}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?Y^*_t&space;=&space;\beta&space;x_t&space;&plus;&space;\phi_1&space;Y^*_{t-1}&space;&plus;&space;\phi_2&space;Y^*_{t-2}&space;&plus;&space;\cdots&space;&plus;&space;\phi_p&space;Y^*_{t-p}&space;&plus;&space;\epsilon_t&space;&plus;&space;\theta_1&space;\epsilon_{t-1}&space;&plus;&space;\theta_2&space;\epsilon_{t-2}&space;&plus;&space;\cdots&space;\theta_q&space;\epsilon_{t-q}" title="Y^*_t = \beta x_t + \phi_1 Y^*_{t-1} + \phi_2 Y^*_{t-2} + \cdots + \phi_p Y^*_{t-p} + \epsilon_t + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2} + \cdots \theta_q \epsilon_{t-q}" /></a>

here

### Unit root test 


# Reference


[Time Series Analysis]: https://onlinelibrary.wiley.com/doi/book/10.1002/9781118619193
[[Box, Jenkins, Reinsel] Time Series Analysis](https://onlinelibrary.wiley.com/doi/book/10.1002/9781118619193)

[What's the difference between ARMA, ARIMA, and ARIMAX, in layman's terms?]: https://www.quora.com/Whats-the-difference-between-ARMA-ARIMA-and-ARIMAX-in-laymans-terms-What-exactly-do-P-D-Q-mean-and-how-do-you-know-what-to-put-in-for-them-in-say-R-1-0-2-or-2-1-1
[[Quora, 1] What's the difference between ARMA, ARIMA, and ARIMAX, in layman's terms?](https://www.quora.com/Whats-the-difference-between-ARMA-ARIMA-and-ARIMAX-in-laymans-terms-What-exactly-do-P-D-Q-mean-and-how-do-you-know-what-to-put-in-for-them-in-say-R-1-0-2-or-2-1-1)

[The ARIMAX model muddle]: https://robjhyndman.com/hyndsight/arimax/
[[Rob Hyndman] The ARIMAX model muddle](https://robjhyndman.com/hyndsight/arimax/)

[Stationarity and differencing]: https://people.duke.edu/~rnau/411diff.htm
[[Robert Nau, Stationarity and differencing] Stationarity and differencing](https://people.duke.edu/~rnau/411diff.htm)

[ARIMA models for time series forecasting]: https://people.duke.edu/~rnau/411arim.htm
[[Robert Nau, ARIMA] ARIMA models for time series forecasting](https://people.duke.edu/~rnau/411arim.htm)

[Why does a time series have to be stationary?]: https://stats.stackexchange.com/questions/19715/why-does-a-time-series-have-to-be-stationary
[[StackExchange, 1] Why does a time series have to be stationary?](https://stats.stackexchange.com/questions/19715/why-does-a-time-series-have-to-be-stationary)

