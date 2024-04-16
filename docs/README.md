# Enterprise Event Bus

## What is the Enterprise Event Bus?

Event-driven architecture enables systems to share data changes in real time across multiple, decoupled teams. It offers an alternative to the coupled, system-to-system API paradigm.

An Event Bus allows a system to publish a stream of changes to its data. Systems that are interested in those data changes can receive the information in real time and use it to send updates to trigger actions, send updates to Veterans, communicate with other internal teams, and more.

<video width="640" height="400" crossorigin="anonymous" controls poster="img/phase3_demo_poster.png">
  <source src="videos/phase3_demo.mp4" type="video/mp4">
  <track src="videos/GMT20230808-163754_Recording.transcript.vtt" label="English" kind="captions" srclang="en-us">
</video>

## Why use the Enterprise Event Bus?

Teams can use the Enterprise Event Bus to generate events based on state changes to the data they own and publish them on an event bus. Consumers are free to consume those events and react accordingly. More specifically, with the Enterprise Event Bus:
* Event producers don’t need to know who the interested consumers are and therefore don’t need to keep growing their outbound complexity.
* Multiple consumers may receive and act on an event; it’s not just an asynchronous queue sitting between a single producer and consumer.

## Next steps

Take the next steps to explore and begin using the Enterprise Event Bus:

* Learn more about [which teams would benefit from using event-driven architecture](./get-started.md),
* Understand the [administrative requirements](./administrative-requirements.md) for connecting to the Enterprise Event Bus,
* [Dive deeper into a technical explanation of events](./intro-to-eda.md),
* Learn how to [produce events](./produce-events.md),
* Learn how to [consume events](./consume-events.md), or 
* [Reach out](./get-support.md) to us with questions. 
