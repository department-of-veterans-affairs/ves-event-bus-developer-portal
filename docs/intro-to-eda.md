---
title: Event-Driven Architecture at VA
---

# Event-Driven Architecture at VA

## Introduction

The Enterprise Event Bus is an asynchronous event processing system that spans systems and lines of business at VA. Event-driven architecture uses events &mdash; types of actions, such as a Veteran creating a medical appointment or updating their beneficiaries &mdash; to communicate with systems that are subscribed to the stream of events. The systems that are producing the events, also known as Producers, are decoupled from the systems that are consuming their events, also known as Consumers.

_The following conceptual diagram illustrates how producers and consumers might interact with the Enterprise Event Bus. Producers publish many different kinds of events. Consumers may do many different things with event data, such as notify a Veteran or kick off a workflow. [View the full-sized diagram (must be part of VA GitHub organization to view).](https://github.com/department-of-veterans-affairs/VES/blob/master/research/Event%20Bus/Diagrams/future%20state%20whole.png)_

![A conceptual diagram illustrating how producers publish various events to the Event Bus and how consumers may use the event data for different purposes.](https://github.com/department-of-veterans-affairs/ves-event-bus-developer-portal/assets/95644573/f0dfe62a-8509-459c-bd9a-074e0babb22b)


## Role within the VA enterprise environment

We define enterprise events as those that capture significant occurrences within VA, such as when a Veteran’s benefit claim reaches certain meaningful milestones.

We strive to enable connecting previously disparate systems that live across different business lines within VA, such as the Veteran Benefit Administration (VBA) and the Veteran Health Administration (VHA). As such, we are not limited to a specific business line or domain within VA.

It should be noted that Enterprise Event Bus does not aspire to be the only event streaming platform within VA, but one that is available to any team that wants to produce or consume enterprise events. This would allow teams who don’t have the time or resources to set up their own event streaming platform to take advantage of event-driven technologies. It is not intended to subsume or replace any existing VA API ecosystems, nor is it a one-stop shop or mandatory runtime environment for all VA data services; instead, it is intended to enable event-based architecture for current and future integrations between systems.

## An opinionated conduit

We often refer to the Enterprise Event Bus team as an opinionated conduit between event consumers and producers across the VA ecosystem. That’s because our research, hands-on experience, and deep knowledge of [Apache Kafka best practices](https://github.com/department-of-veterans-affairs/VES/blob/master/research/Event%20Bus/Engineering/ADR/ADR%20event%20design.md) have led us to definite opinions regarding:

* the type of events that best fit an _Enterprise_ Event Bus architecture (more on that below)
* the choice of technologies with which we implement the Enterprise Event Bus across different contexts of use 
* and the most suitable infrastructure for implementing it. 

These enable us to provide producers and consumers with clear guidance to and assist with onboarding and learning about the underlying technologies.

## Enterprise events versus data events

The focus of the Enterprise Event Bus is enterprise events rather than data events. As described above, an event is a specific action that involves a change in data. An _enterprise_ event is a business event that is of potential interest to a broad scope of consuming systems. 

For example, when Veterans apply for benefits, they are issued a benefits decision letter detailing VA’s decision about what benefits they are eligible for. The benefits decision letter becoming available is an _enterprise_ event. The specific changes in the underlying data that indicate this document has become available are _data_ events. Teams producing events onto the Enterprise Event Bus are encouraged to frame their events as enterprise events; that is, broadly speaking, an event that describes a concrete business event has the potential to be more useful to a broader audience than specific data change events. 

When determining what information an event should contain, a guiding principle is that consumers need events to at least contain enough information to know whether the event is of interest to them, while minimizing the amount of sensitive data in the event payload. In general it is easier to add new pieces of information to a schema than it is to later remove it; thus the system should trend towards leaner events.

##  Technology overview

Enterprise Event Bus, like most other event-based systems in VA, is based on [Apache Kafka](https://kafka.apache.org/), an open-source distributed event streaming platform. It is considered the industry standard for handling real-time data feeds, and is capable of handling the kinds of large scale, high-throughput loads we would expect an enterprise-wide event bus in VA to be able to handle. In addition to being a proven technology, Kafka is already used in a production capacity by other teams in VA, such as the [Benefits Integration Platform](https://confluence.devops.va.gov/pages/viewpage.action?spaceKey=VAExternal&title=Benefits+Integration+Events).

The Enterprise Event Bus uses [AWS Managed Streams for Kafka (MSK)](https://docs.aws.amazon.com/msk/), a hosted version of Kafka that runs in the VA Enterprise Cloud. Producer systems publish events to Kafka topics that are available on AWS MSK. Events in a single topic are distributed across multiple brokers and partitions in order to balance load. Metadata managed by the cluster informs producing and consuming systems which broker they need to connect to. The data on AWS MSK is stored in [AWS Elastic Block Store (EBS)](https://docs.aws.amazon.com/ebs/). Consumer systems can subscribe to topics to pull streams of events. The diagram below shows how events are stored in AWS MSK and how events are distributed from producers to consumers via AWS MSK.

![Diagram showing a high-level overview of AWS MSK and how events are distributed from producers to consumers using multiple brokers in AWS MSK.](https://github.com/department-of-veterans-affairs/ves-event-bus-developer-portal/assets/95644573/61c8f134-7228-4735-b9df-c0e1985d9eaa)

## Learn more

* Find definitions for acronyms and event-related terms on the [Terminology page](./terminology.md).
* <a href="https://www.youtube.com/watch?v=R6tUoxx2gVY">Watch this brief video on YouTube</a> for a quick overview of event-driven architecture.
* <a href="https://developer.confluent.io/patterns/">Learn about event streaming patterns on the Confluent Developer website</a>.
* <a href="https://www.confluent.io/resources/presentation/one-year-in-lessons-learned-and-plans-for-the-future/">Watch a presentation on the Confluent Developer website</a> about “Lessons Learned and Plans for the Future” by Robert Ezekiel from Booz Allen Hamilton.
* <a href="https://www.confluent.io/events/kafka-summit-americas-2021/improving-veteran-benefit-services-through-efficient-data-streaming/">Watch a presentation on the Confluent Developer website</a> about “Improving Veteran Benefit Services Through Efficient Data Streaming” by Robert Ezekiel from Booz Allen Hamilton
* The Enterprise Event Bus Team offers consultations and is happy to answer questions. [Reach out to us](./get-support.md).
