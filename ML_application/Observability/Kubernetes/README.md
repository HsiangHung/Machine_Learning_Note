
# Kubernetes  

## Monolith vs Microservices architectures

The microservices architecture is an architecture approach allowing many applications to have tangible benefits including flexibility, agility, and scalability.

### Monolith Architecture

Monolith architecture is the traditional design for software applications. As its name suggests, it follows a **single**, **unified** “rock” style, but with software rather than rocks. This means that all the components and functionalities of the service are gathered and self-contained as one, meaning that everything is interconnected and interdependent, so everything must be present in order for it all to work [[ClearPeaks]][Kubernetes for Managing Microservices].
 

The biggest problem of the monolith architecture is: updating a component means updating the entire service; scaling is done as a whole, although it might only be needed in some components – and this is why microservices appeared.

### Microservice Architecture

Microservices aim for a loosely coupled approach, where the components are **isolated** and **deployed independently**. This architecture enables services to be highly maintainable and testable, fast to update, and reliable – and with this separation, companies can speed up their innovations and the commercialisation of new features, being able to implement, update or scale each component on demand [[ClearPeaks]][Kubernetes for Managing Microservices]. 

 

Currently, there are two main approaches to isolate applications or services: virtualisation and containerisation.


## What is Kubernetes (K8s)?


### Pod

