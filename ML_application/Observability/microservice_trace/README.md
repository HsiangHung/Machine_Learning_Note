
# Microservice Observability and Distributed Traces 

## 1. Distributed Traces

What is a distributed trace? The following definition is from O'reilly book [[O'Reilly]][Introduction: What Is Distributed Tracing?]:

Distributed tracing (also called distributed request tracing) is a type of correlated logging that helps you gain visibility into the operation of a **distributed software system** for use cases such as performance profiling, debugging in production, and **root cause analysis** of failures or other incidents. It gives you the ability to understand exactly what a particular individual service is doing as part of the whole, enabling you to ask and answer questions about the performance of your services and your distributed system as a whole.

The O'Reilly book also explains why distributed software is so popular?:

* **Scalability**: A distributed application can more easily respond to demand, and its scaling can be more efficient. If a lot of people are trying to log in to your application, you could scale out only the login services, for example.

* **Reliability**: Failures in one component shouldn’t bring down the entire application. Distributed applications are more resilient because they split up functions through a variety of service processes and hosts, ensuring that even if a dependent service goes offline, it shouldn’t impact the rest of the application.

* **Maintainability**: Distributed software is more easily maintainable for a couple of reasons. Dividing services from each other can increase how maintainable each component is by allowing it to focus on a smaller set of responsibilities. In addition, you’re freer to add features and capabilities without implementing (and maintaining) them yourself—for example, adding a speech-to-text function in an application by relying on some cloud provider’s speech-to-text service.

In other words, in a **microservices architecture**, a request can travel across **multiple microservices** to build the response and send it to the user [[Dineshchandgr]][Distributed Tracing in Microservices / Spring Boot]. Distributed Tracing is the process of tracing every single request from the point of origin up to all the services it touches by analyzing the data. Every request will have a Trace ID, timestamp, and other useful metadata. With this, we can see how long the request spans across a particular microservice, and also we can get the metrics to improve the latency.

![](images/trace_and_graph.png)


### 1.2 The difference between distributed tracing and logging

Before the advent of containers, Kubernetes, and microservices, gaining visibility into monolithic systems was simple. However, in distributed environment, distributed tracing provides comprehensive visibility into application performance across microservices and containers.

Log aggregation may give a snapshot of the activity within a collection of individual services, but the logs lack contextual metadata to provide the full picture of a request as it travels downstream through possibly millions of application dependencies. On its own, this method simply isn’t sufficient for troubleshooting in distributed systems.[[Dynatrace]][What is distributed tracing and why does it matter?]

In comparison, distributed tracing is the process of following a single transaction from endpoint to endpoint in context. 



### Reference


* [Distributed Tracing in Microservices / Spring Boot]: https://medium.com/javarevisited/distributed-tracing-in-microservices-spring-boot-125272b58ad8
[[Dineshchandgr] Distributed Tracing in Microservices / Spring Boot](https://medium.com/javarevisited/distributed-tracing-in-microservices-spring-boot-125272b58ad8)
* [What is distributed tracing and why does it matter?]: https://www.dynatrace.com/news/blog/what-is-distributed-tracing/
[[Dynatrace] What is distributed tracing and why does it matter?](https://www.dynatrace.com/news/blog/what-is-distributed-tracing/)
* [Distributed Tracing in Microservices]: https://manoj-bhagwat60.medium.com/distributed-tracing-in-microservices-4c6fac8d941e
[[Manoj Bhagwat] Distributed Tracing in Microservices](https://manoj-bhagwat60.medium.com/distributed-tracing-in-microservices-4c6fac8d941e)
* [Introduction: What Is Distributed Tracing?]: https://www.oreilly.com/library/view/distributed-tracing-in/9781492056621/preface01.html
[[O'Reilly] Introduction: What Is Distributed Tracing?](https://www.oreilly.com/library/view/distributed-tracing-in/9781492056621/preface01.html)
* [Microservices Observability with Distributed Tracing]: https://medium.com/swlh/microservices-observability-with-distributed-tracing-32ae467bb72a
[[Uzziah Eyee] Microservices Observability with Distributed Tracing](https://medium.com/swlh/microservices-observability-with-distributed-tracing-32ae467bb72a)



## 2. Business Transaction 

Business Transactions (BT) are a model to monitoring performance of an application.

In the AppDynamics application model [[AppDynamics]][Business Transaction@AppDynamics], a BT represents an **end-to-end**, **cross-tier processing path** used to fulfill a request for a service provided by the application. 

It consists of **all** required services within your environment such as login, search, and checkout that are utilized to fulfill and respond to a user-initiated request. These transactions reflect the logical way users interact with your applications. 

For example, activities such as adding an item to a shopping cart and then checking out various applications, databases, third-party APIs, and web services.

In some blogs, we may see people define as transactions. For example, in Uzziah Eyee's blog [[Uzziah Eyee]][Microservices Observability with Distributed Tracing], a **Transaction** is an **end-to-end** request-response flow, i.e from making the user’s initial request to receiving the final weather response. A transaction often involves the interaction of multiple services.

Note, so a BT should be considered by an **end-to-end** request flow, and usually involves multiple services.


Various business customers have various definition on critical business concern. For example, a retail website may choose to focus on its **checkout** or **catalog** operation; whereas a financial services firms may focus on the **most-used APIs** provided for their mobile clients. By prioritizing your business goals early in the process, BTs are much easier to configure [[AppDynamics]][Business Transaction@AppDynamics].


**AppDynamics automatically discovers and maps business transactions for you**. For example, a business activity, such as `Add to Cart`, is tagged and traced across every component of your application and visualized on a topology map, helping you to better understand performance across an **entire application**. From a BT, we can identify:
* If there is a performance issue with a **service endpoint**
* Is the Edge service at fault? 
* If not, then identify which **downstream service** may be at fault?

### 2.1 Transaction entry and exit points


Typically, more than one tier participates in the processing of a BT. Outbound requests from an instrumented application tier are called **exit points**. Downstream tiers may, in turn, have exit points that invoke other services or backend requests (see [View Business Transactions@Appdynamics](https://docs.appdynamics.com/appd/22.x/22.3/en/application-monitoring/business-transactions/view-business-transactions)). 

![](images/exit_point_BT.png)

App agents tag exit point calls with metadata describing the existing transaction. When an agent on a downstream tier detects an entry point that includes transaction metadata from another AppDynamics app agent, it treats the entry point as a continuation of the transaction initiated on the **upstream** tier. 

This linking of upstream exit points to downstream entry points is called **correlation**. Correlation maintains the client request context as it is processed by various tiers in your business application.


### 2.2 Sample BTs

As the first example, AppD has the fictional ACME online application exposes a **checkout** service at `http://acmeonline.example.com/checkout`, and a user request to the service triggers these distributed processing flow and actions [[AppDynamics]][Business Transaction@AppDynamics]:

![](images/bt_processflow.png)

1. The BT **entry point** at the originating tier is `/checkout` URI, which is mapped to a Servlet called `CheckoutServlet.`
2. The request results in the originating tier invoking the `createOrder` method on a downstream tier, the `ECommerce-Services` server.
3. The inventory tier application calls a **backend database**, which is an **exit point** for the BT. The request context is maintained across tiers, including calls to backend tiers.
4. Any user request on the entry point is similarly categorized as this `Checkout` BT. 



### 2.3 Practices to Create BT@AppDynamics

The default BT name is based on the **first two segments of a URI**. More URI or segments may result in the overflow of BTs (see [Best Practices to Create Business Transactions](https://docs.appdynamics.com/appd/22.x/22.3/en/application-monitoring/business-transactions/best-practices-to-create-business-transactions)). For example, you want to monitor these URIs for `/eCommerce/login`:

* `/eCommerce/order`
* `/eCommerce/checkout`
* `/eCommerce/feedback`

However, `/order` contains many URI patterns and if it uses more than two segments, then it may reach the `200 BT limit`. Additionally, `/order` results in many URIs that need to be monitored, which are not required for the users:

* `/eCommerce/order/1/add`
* `/eCommerce/order/list`
* `/eCommerce/order/2/add`

Exclude BTs that are not required- Agent snapshots collection depends on the number of unique BTs in the BT list monitored from the target tier. Therefore, it is recommended to review the Business transactions list to check if any BTs listed as part of the auto-discovered transactions are not required. You can use the Exclude Transactions option to temporarily exclude such BTs. If you do not want to collect the snapshots but want only the KPI metrics, then you can monitor the BTs as Service Endpoint.


### Reference

* [Business Transaction@AppDynamics]: https://docs.appdynamics.com/appd/22.x/22.3/en/application-monitoring/business-transactions
[[AppDynamics] Business Transaction@AppDynamics](https://docs.appdynamics.com/appd/22.x/22.3/en/application-monitoring/business-transactions)


* [Microservices Observability with Distributed Tracing]: https://medium.com/swlh/microservices-observability-with-distributed-tracing-32ae467bb72a
[[Uzziah Eyee] Microservices Observability with Distributed Tracing](https://medium.com/swlh/microservices-observability-with-distributed-tracing-32ae467bb72a)


### 2.4 BTs and Traces

A BT can be recorded in a trace. It captures the work done by each service as a collection of Spans all sharing the same Trace ID. More granular **operations of a service** can be captured as Children Spans which have a `childOf` reference pointing to their parent Span. Hence the tuple (`TraceID`, `SpanID`, `ParentID`) sufficiently describes a Span’s position in a Trace so this is called the SpanContext [[Uzziah Eyee]][Microservices Observability with Distributed Tracing].

OpenTelemetry, is a widely popular observability framework for cloud-native software to distributed tracing. Currently, organizations can use OpenTelemetry to send collected telemetry data to a third-party system for analysis. By running [opentelemetry-demo repo](https://github.com/open-telemetry/opentelemetry-demo) repo (using docker), **Jaeger** provides a UI to visualize collected trace data in the backend. 


As an example, consider that another app enables a user to request weather information about their location [[Uzziah Eyee]][Microservices Observability with Distributed Tracing]:

![](images/ip_weather_api_request.png)

1. First the request is handled by an api-service which translates the user’s **IP address** to a city name using a 3rd party `ip-service`. 
2. Then, it obtains the latest weather information for that city from another 3rd party `weather-service`. 
3. Finally, the weather information is returned to the user.


Using the above ip-weather api service, the Jaeger UI can visualize a trace as follows [[Uzziah Eyee]][Microservices Observability with Distributed Tracing]:

![](images/Jaeger_trace_example.png)


A recent global survey of 700 CIOs found that 86% of companies are now using cloud-native technologies and platforms, such as Kubernetes, microservices, and containers. With the rise of service-oriented architectures, however, it became harder to understand how specific transactions traveled through the various tiers of an application. If the organization was unable to identify the affected microservice, then it could not determine which team was responsible for addressing the issue [[Dynatrace]][What is distributed tracing and why does it matter?].

Distributed tracing now meets this need, allowing companies to better understand the performance issues affecting their microservices environments.



## 3. Root Cause Analysis Using Traces

## 3.1 Troubleshoot BT Performance with Transaction Snapshots

[Troubleshoot Business Transaction Performance with Transaction Snapshots@Appdynamics](https://docs.appdynamics.com/appd/22.x/22.3/en/application-monitoring/business-transactions/troubleshoot-business-transaction-performance-with-transaction-snapshots)

AppDynamics monitors every execution of a business transaction in the instrumented environment, and the metrics reflect all such executions. For troubleshooting purposes, AppDynamics takes **snapshots** of specific instances of a transaction. A transaction snapshot gives you a **cross-tier view** of the processing flow for a single invocation of a transaction.

**Call drill downs** detail key information including **slowest methods**, **errors**, and **remote service calls** for the transaction execution on a tier. A drill down may include a partial or complete **call graph**. Call graphs reflect the code-level view of the processing of the BT on a particular tier. 


## Service Triage on BT and RCA

To conduct service triage on performance anomalies, you must first identify the root cause of the problem. 



## Visualization for Flow Map

Reference: [Flowcharts PyDot](https://www.kaggle.com/code/kmader/flowcharts-pydot/notebook)

To run it, we may need to refer:
* [Exception: "dot" not found in path in python on mac](https://stackoverflow.com/questions/40243753/exception-dot-not-found-in-path-in-python-on-mac)
* [FileNotFoundError: [Errno 2] "dot" not found in path #257](https://github.com/pydot/pydot/issues/257)
Install `gprof2dot`:
* [After installing Homebrew I get `zsh: command not found: brew`](https://stackoverflow.com/questions/36657321/after-installing-homebrew-i-get-zsh-command-not-found-brew)


```Python
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from io import StringIO
from IPython.display import SVG
import pydot # import pydot or you're not going to get anywhere my friend :D
```
### Define DAG

```Python
dot_graph = pydot.Dot(graph_type='digraph')
```
### Define Nodes
```Python
sd_node = pydot.Node('Structured\nData\n(ODBC, CSV, XLS)')
sd_node.set_shape('box3d')
dot_graph.add_node(sd_node)
```
### Define Edges
```Python
iedge = pydot.Edge(sd_node,riq_node)
iedge.set_label('Tables')
dot_graph.add_edge(iedge)
```
In the end, put
```Python
dot_graph.write_svg('big_data.svg')
dot_graph.write_ps2('big_data.ps2')
SVG('big_data.svg')
```



## Reference

* [Business Transaction@AppDynamics]: https://docs.appdynamics.com/appd/22.x/22.3/en/application-monitoring/business-transactions
[[AppDynamics] Business Transaction@AppDynamics](https://docs.appdynamics.com/appd/22.x/22.3/en/application-monitoring/business-transactions)


* [What is distributed tracing and why does it matter?]: https://www.dynatrace.com/news/blog/what-is-distributed-tracing/
[[Dynatrace] What is distributed tracing and why does it matter?](https://www.dynatrace.com/news/blog/what-is-distributed-tracing/)


* [System Comprehension and Root Cause Analysis With Distributed Tracing]: https://www.shkuro.com/talks/2018-12-10-system-comprehension-and-root-cause-analysis-with-distributed-tracing/
[[YURI SHKURO] System Comprehension and Root Cause Analysis With Distributed Tracing](https://www.shkuro.com/talks/2018-12-10-system-comprehension-and-root-cause-analysis-with-distributed-tracing/)

