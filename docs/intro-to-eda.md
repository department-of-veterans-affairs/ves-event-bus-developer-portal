---
title: Learn About Event Driven Architecture
---

# Introduction
The Enterprise Event Bus is an asynchronous event processing system that spans systems and lines of business at the VA. Event-driven architecture uses events, which are specific instances of something that happened, to communicate with systems that are subscribed to the stream of events. The systems that are producing the events [producers](https://department-of-veterans-affairs.github.io/ves-event-bus-developer-portal/produce-events/), are decoupled from the systems that are consuming their events [consumers](https://department-of-veterans-affairs.github.io/ves-event-bus-developer-portal/consume-events/).

See this [brief video](https://www.youtube.com/watch?v=R6tUoxx2gVY) for a quick overview of event-driven architecture.

_The following diagram illustrates how the different components of the Enterprise Event Bus come together to produce streams of events._

![future state whole](https://github.com/department-of-veterans-affairs/ves-event-bus-developer-portal/assets/95644573/f0dfe62a-8509-459c-bd9a-074e0babb22b)


# Event-driven architecture at the VA
The Enterprise Event Bus is not intended to subsume or replace any existing VA API ecosystems, nor is it a one-stop shop or mandatory runtime environment for all VA data services; instead, it is intended to enable event-based architecture for current and future integrations between systems.

The focus of the Enterprise Event Bus is enterprise events rather than data events. As described above, an event is a specific instance of something that happens. An enterprise event is a business event that is of potential interest to a broad scope of consuming systems.

For example, when Veterans apply for benefits, they are issued a benefits decision letter detailing the VA’s decision about what benefits they are eligible for. The benefits decision letter becoming available is an enterprise event. The specific changes in the underlying data that indicate this document has become available are data events. Teams producing events onto the Enterprise Event Bus are encouraged to frame their events as enterprise events; that is, broadly speaking, an event that describes a concrete business event has the potential to be more useful to a broader audience than specific data change events.

When determining what information an event should contain, a guiding principle is that consumers need events to at least contain enough information to know whether the event is of interest to them. This is the principle of [least privilege](https://www.okta.com/identity-101/minimum-access-policy/). In general it is easier to add new pieces of information to a schema than it is to later remove it; thus the system should trend towards leaner events.

#  Technology Overview
Enterprise Event Bus, like most other event-based systems in the VA, is based on [Apache Kafka](https://kafka.apache.org/), an open-source distributed event streaming platform. It is considered the industry standard for handling real-time data feeds, and is capable of handling the kinds of large scale, high-throughput loads we would expect an enterprise-wide event bus in the VA to be able to handle. In addition to being a proven technology, Kafka is already used in a production capacity by other teams in the VA, such as the [Benefits Integration Platform](https://confluence.devops.va.gov/pages/viewpage.action?spaceKey=VAExternal&title=Benefits+Integration+Events).

The Enterprise Event Bus uses [AWS Managed Streams for Kafka (MSK)](https://docs.aws.amazon.com/msk/index.html), a hosted version of Kafka that runs in the VA Enterprise Cloud.

_The following diagram illustrates how events pass through the different components of the Enterprise Event Bus system._
![Simple Flow EBus](https://github.com/department-of-veterans-affairs/ves-event-bus-developer-portal/assets/95644573/61c8f134-7228-4735-b9df-c0e1985d9eaa)

# Terminology
* **Domain**: a broad classification of events that corresponds to an area of business within the VA. One can think of a domain as a radio station that plays a certain type of music.
    * For example, transition events, claims/benefits events, health events, life events, memorial events, and interaction events.
* **Topic**: provides a destination for the storage of data. Each topic is split into one or more partitions. Topics are where events are durably stored; this is similar to how files are stored in a distributed file system. A topic can have many producers and many consumers. Continuing the music analogy from the definition of domain, a topic can be thought of as a radio channel that plays a single band.
    * For example, appointment events can be streamed from the appointments topic.
* **Partitions**: storage units within a topic. They hold a subset of the records owned by the topic. This is a logical concept in Kafka.
    * For example, the number of partitions will impact the distribution of your data. The Enterprise Event Bus team will provide guidance on allocating partitions for a topic during the onboarding process of a producer.
* **Broker**: (also called a server or node) orchestrates the storage and passing of messages. These are the machines that store and service the data.
* **Producer**: the team, as well as the application that appends messages to the end of the topic. Messages are written to partitions on a round robin basis, or to a specific partition based on the message key.
* **Consumer**: the team, as well as the application, that subscribes to the topic and reads messages according to topic, partition and offset.
* **Event**: the type of business action that has occurred.
    * For example, an appointment was created.
* **Event (instance)**: a specific instance of a business action that has occurred  (note: event, message, and record can be seen interchangeably in various Kafka-related documentation).
    * For example, an appointment was created for Karen to see an orthopedic specialist on 6/1/2023 at 10:30 am.

# Learn More
* [Event Streaming Patterns](https://developer.confluent.io/patterns/)
* [Improving Veteran Benefit Services Through Efficient Data Streaming | Robert Ezekiel, Booz Allen Hamilton](https://www.confluent.io/events/kafka-summit-americas-2021/improving-veteran-benefit-services-through-efficient-data-streaming/)
* [One Year In – Lessons Learned and Plans for the Future with Robert Ezekiel | Current 2022](https://www.confluent.io/resources/presentation/one-year-in-lessons-learned-and-plans-for-the-future/)
* The Enterprise Event Bus Team offers consultations and is happy to answer questions. Reach out to us [link to contact page](https://department-of-veterans-affairs.github.io/ves-event-bus-developer-portal/get-support/).

# Having Trouble?
If you find something wrong with the documentation, didn’t find what you’re looking for, or have a question or suggestion, please [contact us](./get-support.md).


