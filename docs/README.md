# Enterprise Event Bus

## What is the Enterprise Event Bus? 
Event-driven architecture enables systems to share data changes in real time across multiple, decoupled teams. It offers an alternative to the coupled, system-to-system API paradigm.

An event bus allows a system to publish a stream of changes to its data. Systems who are interested in those data changes can receive the information in real time and use it to send updates to trigger actions, send updates to Veterans, communicate with other internal teams, and more.
 

## Why use the Enterprise Event Bus?
Teams can use the Enterprise Event Bus to generate events based on state changes to the data they own and publish them on an event bus. Consumers are free to consume those events and react accordingly. More specifically, with the Enterprise Event Bus:

- Event producers don’t need to know who the interested consumers are and therefore don’t need to keep growing their outbound complexity. 
- Multiple consumers may receive and act on an event; it’s not just an asynchronous queue sitting between a single producer and consumer.

## Getting Started
Teams can use the Enterprise Event Bus to produce events for other systems to consume, or, subscribe to events and react accordingly.

To learn more about becoming a producer on the Enterprise Event Bus, check out the [producer onboarding documentation](producer-onboarding.md) or [contact us](support/get-support.md) for a consultation. 

To learn more about becoming a consumer on the Enterprise Event Bus, check out the [consumer onboarding documentation](consumer-onboarding.md) or [contact us](support/get-support.md) for a consultation. 

## Event Catalog
The Event Catalog lists all events currently available on the Enterprise Event Bus. In the catalog teams will be able to view details about specific events including event structure, which system produces the event, and what other systems may be subscribing to the event. From within the VA network, check out the Event Catalog on the [Lighthouse Hub]().

**The Event Bus system is still in an experimental status. Information will be updated as it's available. Please reach out to use with questions. 
