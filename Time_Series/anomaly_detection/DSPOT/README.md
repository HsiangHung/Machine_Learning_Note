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

Given $\gamma$ ($\gamma \ne 0$) and $\sigma$, we need to estimate the extreme value threshold $z_q$, and then evaluate the probability $P(X > z_q) < q$, given by the desired probability $q$. ($q$ is usually a small number, like 0.001, 0.0001... etc)

Assume $n$ is the total number of observation (data points), $N_t$ the number of peaks (meaning the number of $X > t$), therefore we have

$$\bar{F}_t(x) = \frac{q}{(\frac{N_t}{n})} = \frac{qn}{N_t} \sim \left[ 1 + \frac{\gamma}{\sigma} (z_q - t) \right]^{-\frac{1}{\gamma}}$$



Univariate time-series data has only ONE column for event value and a timestamp index corresponding the event. The algorithms like AR (auto regression), MA (moving averaging) or ARIMA (Auto Regression Integrated Moving Averaging) to forecast future events. In the univariate anomaly approach, we can use one of the above models to detect the presence of strange patterns.

A typical AR(p) model can be interpreted as 

$$Y_t = \alpha + \beta_1 Y_{t-1} + \beta_2 Y_{t-2} + \cdots + \beta_{p} Y_{t-p} + \epsilon_t$$

p is the number of lagged timestamps.

## Multivariate

On the other hand, in multivariate time-series data, each timestamp index corresponds to multiple columns. For example, an AR model extends the univariate autoregressive (AR) model by capturing the linear relations between multiple variables [[Marco Cerliani]][Anomaly Detection in Multivariate Time Series with VAR]. For each input series, a regression is carried out. 

The algorithms cover that manner are VAR (vector auto-regression), VMA (vector moving-avergae), VARMA (vector auto-regression moving average), VARIMA (vector auto-regression integrated moving average) and VECM (vector error correction model) etc.

Suppose we have two time-series variables, $Y_{1,t}$ and $Y_{2,t}$ [[Selva Prabhakaran]][Vector Autoregression (VAR) – Comprehensive Guide with Examples in Python], and consider only one time step lag. Then we have

$$ \begin{matrix} 
  Y_{1,t} &=& \alpha_1 + \beta_{11,1} Y_{1, t-1} + \beta_{12,1} Y_{2,t-1} + \epsilon_{1,t}. \\ 
  Y_{2,t} &=& \alpha_2 + \beta_{21,1} Y_{1, t-1} + \beta_{22,1} Y_{2,t-1} + \epsilon_{2,t}.
  \end{matrix}
$$

We can rewrite the above equation in a matrix form:

$${\left( \matrix{ Y_{1,t} \cr Y_{2,t} } \right)} 
= {\left( \matrix{ \alpha_1 \cr \alpha_2 } \right)} + 
  \left( \matrix{\beta_{11,1} & \beta_{12,1} \cr \beta_{21,1} & \beta_{22,1}} \right)
  {\left( \matrix{ Y_{1,t-1} \cr Y_{2,t-1} } \right)} + 
  {\left( \matrix{ \epsilon_{1,t} \cr \epsilon_{2,t} } \right)}.
$$

If the auto regression involves two time steps, then we have VAR(2)

$${\left( \matrix{ Y_{1,t} \cr Y_{2,t} } \right)} 
= {\left( \matrix{ \alpha_1 \cr \alpha_2 } \right)} + 
  \left( \matrix{\beta_{11,1} & \beta_{12,1} \cr \beta_{21,1} & \beta_{22,1}} \right)
  {\left( \matrix{ Y_{1,t-1} \cr Y_{2,t-1} } \right)} + 
  \left( \matrix{\beta_{11,2} & \beta_{12,2} \cr \beta_{21,2} & \beta_{22,2}} \right)
  {\left( \matrix{ Y_{1,t-2} \cr Y_{2,t-2} } \right)} +
  {\left( \matrix{ \epsilon_{1,t} \cr \epsilon_{2,t} } \right)}.
$$

Therefore, we can generalize the VAR(p) (p lagged model) with $n$ variables:


$${\left( \matrix{ Y_{1,t} \cr Y_{2,t} \cr \vdots \cr Y_{n,t} } \right)} 
= {\left( \matrix{ \alpha_1 \cr \alpha_2 \cr \vdots \cr \alpha_n } \right)} + 
  \sum^p_{i=1}
  \left( \matrix{\beta_{11,i} & \beta_{12,i} & \dots & \beta_{1n,i} \cr 
                 \beta_{21,i} & \beta_{22,i} & \dots & \beta_{2n,i} \cr  
                 \vdots & \vdots & \ddots & \vdots \cr
                 \beta_{n1,i} & \beta_{n2,i} & \dots & \beta_{nn,i} 
                } 
  \right)
  {\left( \matrix{ Y_{1,t-i} \cr Y_{2,t-i} \cr \vdots \cr Y_{n,t-i} } \right)} +
  {\left( \matrix{ \epsilon_{1,t} \cr \epsilon_{2,t} \cr \vdots \cr \epsilon_{n,t} } \right)}.
$$



## 1. Time-Series Models

### 1.1 Exponentially Weighted Average


### 1.5 ARIMAX model




# Reference

* [Anomaly Detection in Multivariate Time Series with VAR]: https://towardsdatascience.com/anomaly-detection-in-multivariate-time-series-with-var-2130f276e5e9
[[Marco Cerliani] Anomaly Detection in Multivariate Time Series with VAR](https://towardsdatascience.com/anomaly-detection-in-multivariate-time-series-with-var-2130f276e5e9)

* [Vector Autoregression (VAR) – Comprehensive Guide with Examples in Python]: https://www.machinelearningplus.com/time-series/vector-autoregression-examples-python/
[[Selva Prabhakaran] Vector Autoregression (VAR) – Comprehensive Guide with Examples in Python](https://www.machinelearningplus.com/time-series/vector-autoregression-examples-python/)


* [Kaggle: Anomaly detection in multivariate time series]: https://www.kaggle.com/code/drscarlat/anomaly-detection-in-multivariate-time-series/notebook
[[ALEXANDER SCARLAT] Kaggle: Anomaly detection in multivariate time series](https://www.kaggle.com/code/drscarlat/anomaly-detection-in-multivariate-time-series/notebook)


* [Developing Vector AutoRegressive Model in Python!]: https://www.analyticsvidhya.com/blog/2021/08/vector-autoregressive-model-in-python/
[[Analytics Vidhya] Developing Vector AutoRegressive Model in Python!](https://www.analyticsvidhya.com/blog/2021/08/vector-autoregressive-model-in-python/)