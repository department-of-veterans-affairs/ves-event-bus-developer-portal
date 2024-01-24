# Enterprise Event Bus

## What is the Enterprise Event Bus?
Event-driven architecture enables systems to share data changes in real time across multiple, decoupled teams. It offers an alternative to the coupled, system-to-system API paradigm.

An Event Bus allows a system to publish a stream of changes to its data. Systems that are interested in those data changes can receive the information in real time and use it to send updates to trigger actions, send updates to Veterans, communicate with other internal teams, and more.

<video width="640" height="400" crossorigin="anonymous" controls poster="../img/phase3_demo_poster.png">
  <source src="../videos/phase3_demo.mp4" type="video/mp4">
</video>

The Event Bus system is currently in a pre-production state. Information will be updated as it's available. Please [reach out](https://department-of-veterans-affairs.github.io/ves-event-bus-developer-portal/get-support/) to us with questions.

## Why use the Enterprise Event Bus?
Teams can use the Enterprise Event Bus to generate events based on state changes to the data they own and publish them on an event bus. Consumers are free to consume those events and react accordingly. More specifically, with the Enterprise Event Bus:
* Event producers don’t need to know who the interested consumers are and therefore don’t need to keep growing their outbound complexity.
* Multiple consumers may receive and act on an event; it’s not just an asynchronous queue sitting between a single producer and consumer.

## Next steps
Take the next steps to explore and begin using the Enterprise Event Bus:

* Learn more about [which teams would benefit from using event-driven architecture](https://department-of-veterans-affairs.github.io/ves-event-bus-developer-portal/get-started/),
* [Dive deeper into a technical explanation of events](https://department-of-veterans-affairs.github.io/ves-event-bus-developer-portal/intro-to-eda/),
* Learn how to [produce events](https://department-of-veterans-affairs.github.io/ves-event-bus-developer-portal/produce-events/),
* Learn how to [consume events](https://department-of-veterans-affairs.github.io/ves-event-bus-developer-portal/consume-events/), or 
* [Reach out](https://department-of-veterans-affairs.github.io/ves-event-bus-developer-portal/get-support/) to us with questions. 
