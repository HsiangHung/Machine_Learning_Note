# Anomaly Detection in Time Series 

# Introduction 

## Univariate 
Univariate time-series data has only ONE column for event value and a timestamp index corresponding the event. The algorithms like AR (auto regression), MA (moving averaging) or ARIMA (Auto Regression Integrated Moving Averaging) to forecast future events. In the univariate anomaly approach, we can use one of the above models to detect the presence of strange patterns.

A typical AR(p) model can be interpreted as 

$$Y_t = \alpha + \beta_1 Y_{t-1} + \beta_2 Y_{t-2} + \cdots + \beta_{p} Y_{t-p} + \epsilon_t$$

## Multivariate

On the other hand, in multivariate time-series data, each timestamp index corresponds to multiple columns. The algorithms cover that manner are VAR (vector auto-regression), VMA (vector moving-avergae), VARMA (vector auto-regression moving average), VARIMA (vector auto-regression integrated moving average) and VECM (vector error correction model) etc.

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

If the auto regression involves two time steps, then we have

$${\left( \matrix{ Y_{1,t} \cr Y_{2,t} } \right)} 
= {\left( \matrix{ \alpha_1 \cr \alpha_2 } \right)} + 
  \left( \matrix{\beta_{11,1} & \beta_{12,1} \cr \beta_{21,1} & \beta_{22,1}} \right)
  {\left( \matrix{ Y_{1,t-1} \cr Y_{2,t-1} } \right)} + 
  \left( \matrix{\beta_{11,2} & \beta_{12,2} \cr \beta_{21,2} & \beta_{22,2}} \right)
  {\left( \matrix{ Y_{1,t-2} \cr Y_{2,t-2} } \right)} +
  {\left( \matrix{ \epsilon_{1,t} \cr \epsilon_{2,t} } \right)}.
$$

Therefore, we can generalize the VAR model to $m$ variable and $n$-lag:


$${\left( \matrix{ Y_{1,t} \cr Y_{2,t} \cr \vdots \cr Y_{m,t} } \right)} 
= {\left( \matrix{ \alpha_1 \cr \alpha_2 } \cr \vdots \cr Y_{m,t} \right)} + 
  \left( \matrix{\beta_{11,1} & \beta_{12,1} \cr \beta_{21,1} & \beta_{22,1}} \right)
  {\left( \matrix{ Y_{1,t-1} \cr Y_{2,t-1} } \right)} + 
  \left( \matrix{\beta_{11,2} & \beta_{12,2} \cr \beta_{21,2} & \beta_{22,2}} \right)
  {\left( \matrix{ Y_{1,t-2} \cr Y_{2,t-2} } \right)} +
  {\left( \matrix{ \epsilon_{1,t} \cr \epsilon_{2,t} } \cr \vdots \cr \epsilon_{m,t} } \right)}.
$$



## 1. Time-Series Models

### 1.1 Exponentially Weighted Average


### 1.5 ARIMAX model




# Reference

* [Anomaly Detection in Multivariate Time Series with VAR]: https://towardsdatascience.com/anomaly-detection-in-multivariate-time-series-with-var-2130f276e5e9
[[Marco Cerliani] Anomaly Detection in Multivariate Time Series with VAR](https://towardsdatascience.com/anomaly-detection-in-multivariate-time-series-with-var-2130f276e5e9)

* [Vector Autoregression (VAR) – Comprehensive Guide with Examples in Python]: https://www.machinelearningplus.com/time-series/vector-autoregression-examples-python/
[[Selva Prabhakaran] Vector Autoregression (VAR) – Comprehensive Guide with Examples in Python](https://www.machinelearningplus.com/time-series/vector-autoregression-examples-python/)
