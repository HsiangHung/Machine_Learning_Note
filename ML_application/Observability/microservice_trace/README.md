
# Microservice Observability and Distributed Traces 


## Business Transaction 

In the AppDynamics application model [[AppDynamics]][Business Transaction@AppDynamics], a business transaction (BT) represents an **end-to-end**, **cross-tier processing path** used to fulfill a request for a service provided by the application. 

It consists of **all** required services within your environment such as login, search, and checkout that are utilized to fulfill and respond to a user-initiated request. These transactions reflect the logical way users interact with your applications. 

For example, activities such as adding an item to a shopping cart and then checking out various applications, databases, third-party APIs, and web services.

In some blogs, we may see people define as transactions. For example, in Uzziah Eyee's blog [[Uzziah Eyee]][Microservices Observability with Distributed Tracing], a **Transaction** is an **end-to-end** request-response flow, i.e from making the user’s initial request to receiving the final weather response. A transaction often involves the interaction of multiple services.

Note, so a BT should be considered by an **end-to-end** request flow, and usually involves multiple services.


Various business customers have various definition on critical business concern. For example, a retail website may choose to focus on its **checkout** or **catalog** operation; whereas a financial services firms may focus on the **most-used APIs** provided for their mobile clients. By prioritizing your business goals early in the process, BTs are much easier to configure [[AppDynamics]][Business Transaction@AppDynamics].


**AppDynamics automatically discovers and maps business transactions for you**. For example, a business activity, such as `Add to Cart`, is tagged and traced across every component of your application and visualized on a topology map, helping you to better understand performance across an **entire application**. From a BT, we can identify:
* If there is a performance issue with a **service endpoint**
* Is the Edge service at fault? 
* If not, then identify which **downstream service** may be at fault?



## Service Triage on BT and RCA

To conduct service triage on performance anomalies, you must first identify the root cause of the problem. 


## Sample BT


As the first example, AppD has the fictional ACME online application exposes a **checkout** service at `http://acmeonline.example.com/checkout`, and a user request to the service triggers these distributed processing flow and actions [[AppDynamics]][Business Transaction@AppDynamics]:

![](images/bt_processflow.png)

1. The BT **entry point** at the originating tier is `/checkout` URI, which is mapped to a Servlet called `CheckoutServlet.`
2. The request results in the originating tier invoking the `createOrder` method on a downstream tier, the `ECommerce-Services` server.
3. The inventory tier application calls a **backend database**, which is an **exit point** for the BT. The request context is maintained across tiers, including calls to backend tiers.
4. Any user request on the entry point is similarly categorized as this `Checkout` BT. 






## Reference

* [Business Transaction@AppDynamics]: https://docs.appdynamics.com/appd/22.x/22.3/en/application-monitoring/business-transactions
[[AppDynamics] Business Transaction@AppDynamics](https://docs.appdynamics.com/appd/22.x/22.3/en/application-monitoring/business-transactions)

* [Microservices Observability with Distributed Tracing]: https://medium.com/swlh/microservices-observability-with-distributed-tracing-32ae467bb72a
[[Uzziah Eyee] Microservices Observability with Distributed Tracing](https://medium.com/swlh/microservices-observability-with-distributed-tracing-32ae467bb72a)

