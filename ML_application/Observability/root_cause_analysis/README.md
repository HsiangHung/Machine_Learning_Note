
# Root Cause Analysis (RCA)

## Root Cause Analysis (RCA) Process

In the following, we use an example from New Relic platform to show how to use distributed traces for troubleshooting. For reference, see:
* [New Relic:Backend Root Cause Analysis with Distributed Tracing](https://www.youtube.com/watch?v=r9ImAQ5J5h4)

### Use case

Say, we got our customers' complaint, the checkout services sometimes have high latency. We are going to root cause analysis where is wrong:

1. Fetch the response time data in the past three days. Big spikes indicate high response time.
![step1](images/step1.png)
2. To further investigate, narrow down the anomaly spikes.
![step2](images/step2.png)
3. Inidcate separate transaction types contributing to the response time. Then we can select the distributed traces corresponding to the api.
![step3-1](images/step3_1.png)
![dtep3-2](images/step3_2.png)
4. Now in the trace summary page. The upper plot shows distributed traces from service A to service Z during the time. We can select one of traces which has high latency:
![dtep4](images/step4.png)
5. This shows a trace. There are three services. We see most significant latency is on "Getplan" service.
![dtep5](images/step5.png)
6. Further jump to spans. We can see the MYSQL query shows most times; and further look up what hostname is
![dtep6](images/step6.png)


