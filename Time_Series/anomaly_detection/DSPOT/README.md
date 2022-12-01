# DSPOT

## Introduction 

DSPOT is a drift stream POT method, fitting generalized Pareto distribution (GPD) to detect extreme values. In the code, the DSPOT algorithm only focuses on upper extremem values. To detect both upper and lower extreme extreme values, we use the specific variant of DSPOT, called biDSPOT.

Assume we have an extreme value distribution. The Pickands-Balkema-de Haan theorem states, that there exists a cumulative distribution function $F(x)$, which reads as

$$\bar{F}_t(x) = P( X - t > x | X > t) \sim \big[ 1 + \frac{\gamma}{\sigma}(x - \mu) \big]^{-1/\gamma}$$

The distribution has $iid$ vairables $X > t$ has asymptotic power-law tail behavior. Note in the above $\gamma \ne 0$ is required. The actual cumulative distribution function then reads as 

$$ F = 1 - \bar{F}.$$

The above function $F(t)$ is called GPD. In the paper, $\mu =0$ is used. Then we have

$$\bar{F}_t(x) \sim \big( 1 + \frac{\gamma}{\sigma} x \big)^{-\frac{1}{\gamma}}$$

Rather than fitting an EVD to the extreme values of $X$, the paper used the peak-over-threshold (POT) approach fit the GPD to the excesses of $X-t$.


## Extreme Value Threshold $z_q$ Determination

### A. $z_q$ for $\gamma \ne 0$

Given $\gamma$ ($\gamma \ne 0$) and $\sigma$, we need to estimate the extreme value threshold $z_q$, and then evaluate the probability $P(X > z_q) < q$, given by the desired probability $q$. ($q$ is usually a small number, like 0.001, 0.0001... etc)

Assume $n$ is the total number of observation (data points), $N_t$ the number of peaks (meaning the number of $X > t$), therefore we have

$$\bar{F}_t(x) = \frac{q}{(\frac{N_t}{n})} = \frac{qn}{N_t} \sim \left[ 1 + \frac{\gamma}{\sigma} (z_q - t) \right]^{-\frac{1}{\gamma}}$$

By simple algebra, the lower extremem value threshold $z_q$ is given by

$$z_q \simeq t - \frac{\sigma}{\gamma}\left[ \Big( \frac{qn}{N_t}\Big)^{-\gamma} -1 \right],$$

where in the GPD $z_q < t$.


### B. $z_q$ for $\gamma = 0$

For the $\gamma = 0$ case, the cumulative distribution $\bar{F}_t(x)$ turns out to be

$$ \bar{F}_t(x) \sim e^{-(x-\mu)/sigma}, $$

which has exponential tail asymptotic behavior. The upper extremem value GPD ($z_q > t$) can be derived as 

$$\frac{qn}{N_t} \sim e^{-(z_q -t)/\sigma} \to z_q \simeq t - \sigma \ln \Big \frac{qn}{N_t} \Big).$$

On the other hand, the lower extremem value GPD ($ t < z_q$) is given as

$$\frac{qn}{N_t} \sim e^{-(t - z_q)/\sigma} \to z_q \simeq t + \sigma \ln \Big \frac{qn}{N_t} \Big).$$


## Log-Likelihood Function

The cumulative distribution $\bar{F}_t(x)$ is defined as the integral over the probability probability $P(x^{\prime})$, such that

$$F(x) = \int^{x}_0 P(x^{\pime}) dx^{\prime} = 1 - \bar{F}_t(x) = 1 - \left( 1 + \frac{\gamma}{\sigma}x \right)^{-\frac{1}{\gamma}}.$$

Therefore, taking the derivative of the cumulative function, the probability density function $P(x)$ turns out to be either

$$P(x) = \frac{1}{\sigma}\left( 1 + \frac{\gamma}{\sigma}x \right)^{(1+\frac{1}{\gamma})}, $$

if $\gamma \ne 0$, or 

$$P(x) = \frac{1}{\sigma} e^{-x/ \sigma}, $$

if $\gamma = 0$.

$$ \begin{matrix} 
  Y_{1,t} &=& \alpha_1 + \beta_{11,1} Y_{1, t-1} + \beta_{12,1} Y_{2,t-1} + \epsilon_{1,t}. \\ 
  Y_{2,t} &=& \alpha_2 + \beta_{21,1} Y_{1, t-1} + \beta_{22,1} Y_{2,t-1} + \epsilon_{2,t}.
  \end{matrix}
$$

By the result, the log-likelihood function is defined as 

$$\log L(\gamma, \sigma, X) = \log \Prod^{N_t}_i P(x_i) = -N_t \log \sigma - (1+\frac{1}{\gamma}) \sum^{N_t}_i \log \Big( 1 + \frac{\gamma}{\sigma} x_i \Big)$$

if $\gamma \ne 0$, or 

$$ \log L(\gamma, \sigma, X) =  - N_t \log \sigma - \frac{1}{\sigma} \sum^{N_t}_i x_i, $$

if $\gamma = 0$.


# Reference

* [Anomaly Detection in Multivariate Time Series with VAR]: https://towardsdatascience.com/anomaly-detection-in-multivariate-time-series-with-var-2130f276e5e9
[[Marco Cerliani] Anomaly Detection in Multivariate Time Series with VAR](https://towardsdatascience.com/anomaly-detection-in-multivariate-time-series-with-var-2130f276e5e9)

* [Vector Autoregression (VAR) – Comprehensive Guide with Examples in Python]: https://www.machinelearningplus.com/time-series/vector-autoregression-examples-python/
[[Selva Prabhakaran] Vector Autoregression (VAR) – Comprehensive Guide with Examples in Python](https://www.machinelearningplus.com/time-series/vector-autoregression-examples-python/)


* [Kaggle: Anomaly detection in multivariate time series]: https://www.kaggle.com/code/drscarlat/anomaly-detection-in-multivariate-time-series/notebook
[[ALEXANDER SCARLAT] Kaggle: Anomaly detection in multivariate time series](https://www.kaggle.com/code/drscarlat/anomaly-detection-in-multivariate-time-series/notebook)


* [Developing Vector AutoRegressive Model in Python!]: https://www.analyticsvidhya.com/blog/2021/08/vector-autoregressive-model-in-python/
[[Analytics Vidhya] Developing Vector AutoRegressive Model in Python!](https://www.analyticsvidhya.com/blog/2021/08/vector-autoregressive-model-in-python/)