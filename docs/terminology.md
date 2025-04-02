---
title: Terminology
---

# **Terminology**

* **Broker**: (also called a server or node) orchestrates the storage and passing of messages. These are the machines that store and service the data.

* **Consumer**: the team, as well as the application, that subscribes to the topic and reads messages according to topic, partition and offset.

* **Domain**: a broad classification of events that corresponds to an area of business within the VA. One can think of a domain as a radio station that plays a certain type of music.
    * For example, transition events, claims/benefits events, health events, life events, memorial events, and interaction events.

* **Event**: the type of business action that has occurred.
    * For example, an appointment was created.

* **Event (instance)**: a specific instance of a business action that has occurred  (note: event, message, and record can be seen interchangeably in various Kafka-related documentation).
    * For example, an appointment was created for Karen to see an orthopedic specialist on 6/1/2023 at 10:30 am.

* **MSK**: Managed Streams for Kafka. The Enterprise Event Bus uses AWS Managed Streams for Kafka, a hosted version of Kafka that runs in the VA Enterprise Cloud.

* **Partitions**: storage units within a topic. They hold a subset of the records owned by the topic. This is a logical concept in Kafka.
    * For example, the number of partitions will impact the distribution of your data. The Enterprise Event Bus team will provide guidance on allocating partitions for a topic during the onboarding process of a producer.

* **Producer**: the team, as well as the application that appends messages to the end of the topic. Messages are written to partitions on a round robin basis, or to a specific partition based on the message key.

* **Topic**: provides a destination for the storage of data. Each topic is split into one or more partitions. Topics are where events are durably stored; this is similar to how files are stored in a distributed file system. A topic can have many producers and many consumers. Continuing the music analogy from the definition of domain, a topic can be thought of as a radio channel that plays a single band.
    * For example, appointment events can be streamed from the appointments topic.
 
Find additional terms and abbreviations on the [Event Bus terminology page in Github (must be part of VA GitHub organization to view)](https://github.com/department-of-veterans-affairs/VES/blob/master/research/Event%20Bus/Event%20Bus%20Terminology.md). 
