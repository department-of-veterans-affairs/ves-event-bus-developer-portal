---
title: Are you a good fit for the Enterprise Event Bus?
---

# Are you a good fit for the Enterprise Event Bus?

Before you make further plans to leverage enterprise events, you should evaluate if your system is the right fit for event-driven architecture. Please read the content below, which describes the sorts of systems that would benefit (or not benefit) from enterprise events.

## The Enterprise Event Bus is a good fit if ...

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

## The Enterprise Event Bus is not a good fit if ...

You are interested in a **one-time data sweep**:<br/>
If you just need to search through a data source to identify specific cases for further processing, event-driven systems would introduce unnecessary complexity and overhead. The Enterprise Event Bus is geared towards handling ongoing event streams rather than singular, one-time data analysis tasks.

Your system deals with **simple, linear workflows**:<br/>
If you are dealing with a system that has no significant interaction between components, the overhead of event handling might outweigh the benefits.

Your system is based on a **different programming paradigm**:<br/>
There are many valid reasons to use other architectures, such as synchronous API-based technologies. Event-driven architecture is not the best solution in every scenario.

Your system **lacks well-defined components, or has constantly changing interactions**:<br/>
Systems that are continuously in flux, or don't have well-established boundaries or communication patterns would make it difficult to introduce event-driven designs.

Your event data **is rated as “high” under [FISMA](https://security.cms.gov/learn/federal-information-security-management-act-fisma) and the [VA system categorization](https://jubilant-succotash-m55rqe7.pages.github.io/categorization/)**:<br/> 
The Event Bus is rated at a Medium level under FISMA and VA system categorization, and can only broker data that is rated as Low or Moderate at this time.

## Reach out to us

If you think the Enterprise Event Bus would be a good fit for your situation, please [reach out](./get-support.md)!

The best way to contact the Event Bus Team is via the [#ves-event-bus](https://dsva.slack.com/archives/C042ZQ7JUAX) Slack channel in the Office of CTO @VA workspace.

