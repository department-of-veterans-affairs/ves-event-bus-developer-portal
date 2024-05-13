---
title: Environments
---

# Environments

## Descriptions

Event Bus [Kafka](https://kafka.apache.org/) and applications are deployed into several environments for different purposes. The environments are described below.

- **`Sandbox`** is a stable environment that external teams can connect to. It is a "customer dev" environment.
- **`Pre-prod`** is a testing environment that has been cleared for PHI and PII. `Pre-prod` may be used for performance tests.
- **`Prod`** is our production environment.

## Deployment Schedule

We deploy any new releases to all environments on Wednesdays.

## Properties

| Environment<br>Name | Kafka<br>endpoints                                                                                                                       | PHI, PII<br>Allowed |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| sandbox             | TBD                                                                                                                                      | No                  |
| pre-prod            | TBD                                                                                                                                      | Yes                 |
| prod                | b-1.eventbuskafka.m1c2oj.c3.kafka.us-gov-west-1.amazonaws.com:9098<br>b-2.eventbuskafka.m1c2oj.c3.kafka.us-gov-west-1.amazonaws.com:9098 | Yes                 |
