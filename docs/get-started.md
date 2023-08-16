---
title: Get Started
---

# Get Started

## What the Enterprise Event Bus Is

The VES Enterprise Event Bus is an asynchronous event processing system that allows producers to publish business events based on data changes and consumers to subscribe to those events. The system uses Kafka as its core event streaming platform, with [AWS MSK](https://aws.amazon.com/msk/) (Managed Streaming for Apache Kafka) as the management layer.

To learn more about the Event Bus, check out the presentation and demo below. An accompanying [slide deck](https://github.com/department-of-veterans-affairs/VES/blob/master/research/Event%20Bus/Phase%203%20Artifacts/Event%20Bus%20-%20State%20of%20the%20System.pdf) is also available.

<video width="640" height="400" controls poster="../img/phase3_demo_poster.png">
  <source src="../videos/phase3_demo.mp4" type="video/mp4">
</video>

### An Opinionated Conduit

We often refer to the Enterprise Event Bus as an **opinionated conduit** between event consumers and producers across the VA ecosystem. Why are we opinionated?

* We have opinions about the **type of events** that would be suitable for an enterprise event bus (more on that below)
* We have opinions about the **choice of technologies** with which we implement the Enterprise Event Bus and have done the legwork to set up the most suitable infrastructure according to our research
* We have (proven) opinions about [**Kafka best practices**](https://github.com/department-of-veterans-affairs/VES/blob/master/research/Event%20Bus/ADR/ADR%20event%20design.md) which enable us to provide clear guidance to [producers](./produce-events.md) and [consumers](./consume-events.md) and assist with onboarding and learning about the underlying technologies

### Role Within the VA Enterprise Environment

We define **enterprise events** as those that capture significant occurrences within the VA, such as when a Veteran’s benefit claim reaches certain meaningful milestones.

We strive to enable **connecting previously disparate systems** that live across different business lines within the VA, such as the Veteran Benefit Administration (VBA) and the Veteran Health Administration (VHA). As such, we are **not limited to a specific business line or domain** within the VA.

It should be noted that Enterprise Event Bus does **not aspire to be the only event streaming platform within the VA**, but one that is available to any team that wants to produce or consume enterprise events. This would allow teams who don’t have the **time or resources** to set up their own event streaming platform to take advantage of event-driven technologies. In summary, the Event Bus does not attempt to subsume or replace any existing event platforms, or replicate their functionality.

## The Enterprise Event Bus Is a Good Fit If ...

Your system relies on **heavy orchestration**:<br/>
Coordinating multiple systems or services can become a challenging task, especially when some individual components lack reliability. This can lead to (partial) failures due to delayed status responses, unclear errors, or frequent retry attempts. A well-considered event-driven solution can greatly enhance the quality and performance of such systems.

Your system relies on **polling, due to high latency or infrequent processes**:<br/>
Repeatedly querying resources can lead to unnecessary resource consumption and increased network traffic. Instead of periodically checking for updates, systems can be designed to react to events as they occur. This reduces overall latency and ensures that actions, such as user notifications, are taken promptly.

Your system needs to perform **batch processing**:<br/>
Batch processing introduces delays, as data changes accumulate before being processed as a group. Allocating resources to perform the batch process can also lead to resource spikes and inefficient usage of resources. Making real-time data available in such systems can greatly improve the timeliness of insights and actions.

Your system is characterized by **tightly coupled components**:<br/>
Instead of direct and synchronous interactions between components, producing and consuming systems operate independently. Consuming systems can act upon events as they are streamed, instead of needing to maintain 1:1 connections and await responses from the producing system. This leads to improved maintainability, scalability, and overall system resilience.

Your system has **delayed or no user notifications**:<br/>
Although there are many systems that would benefit from events, almost any scenario where a side effect of the business event is “to notify the Veteran” could be a candidate for an event stream.

## The Enterprise Event Bus Is Not a Good Fit If ...

You are interested in a **one-time data sweep**<br/>
If you just need to search through a data source to identify specific cases for further processing, event-driven systems would introduce unnecessary complexity and overhead. The Enterprise Event Bus is geared towards handling ongoing event streams rather than singular, one-time data analysis tasks.

Your system deals with **simple, linear workflows**<br/>
If you are dealing with a system that has no significant interaction between components, the overhead of event handling might outweigh the benefits.

Your system is based on a **different programming paradigm**<br/>
There are many valid reasons to use other architectures, such as synchronous API-based technologies. Event-driven architecture is not the best solution in every scenario.

Your system **lacks well-defined components, or has constantly changing interactions**<br/>
Systems that are continuously in flux, or don't have well-established boundaries or communication patters would make it difficult to introduce event-driven designs.

## Reach Out To Us
If you think the Enterprise Event Bus would be a good fit for your situation, or help you solve a problem, then please get in touch with us to discuss further.

The best way to reach out to the Event Bus Team is via the [#ves-event-bus](https://dsva.slack.com/archives/C042ZQ7JUAX) Slack channel in the Digital Service VA workspace.
