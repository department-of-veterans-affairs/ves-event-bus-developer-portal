---
title: Environments
---

# Environments

## Descriptions
<!--
 from ticket #2516 "Our four environments are: Dev, Sandbox, Pre Prod, Prod"

 Description of environments from Slack 
 https://dsva.slack.com/archives/C06EB8S1FT9/p1710884055935049

 https://adhoc.slack.com/archives/C042L8C962D/p1712157437377449?thread_ts=1712058858.556049&cid=C042L8C962D

 VA Profile has an environment called INT. int currently connects to EB dev. INT will connect to EB sandbox.
-->

Event Bus [Kafka](https://kafka.apache.org/) and applications are deployed into several environments for different purposes. The environments are described below.

- **`Dev`** is an unstable environment intended for Event Bus team's development work. No customer applications will be deployed here.
- **`Sandbox`** is a stable environment that external teams can connect to. It is a "customer dev" environment.
- **`Pre-prod`** is a testing environment that has been cleared for PHI and PII. `Pre-prod` may be used for performance tests.
- **`Prod`** is our production environment.

## Deployment Schedule

We deploy any new releases to `sandbox` and `prod` on Wednesdays.

## Properties

| Environment<br>Name | AWS Account  | Kubernetes<br>Cluster | Kubernetes<br>Namespace     | PHI, PII<br>Allowed |
|---------------------|--------------|-----------------------|-----------------------------|---------------------|
| dev                 | ldx-nprod    | ldx-nonprod-1         | ves-event-bus-infra-dev     | No                  |
| sandbox             | ldx-nprod    | ldx-nonprod-1         | ves-event-bus-infra-sandbox | No                  |
| pre-prod            | ldx-prod     | ldx-prod-1            | TBD                         | Yes                 |
| prod                | ldx-prod     | ldx-prod-1            | ves-event-bus-infra-prod    | Yes                 |

<!-- LHDI's dev is in ldx-dev, but the Event Bus dev that customers would connect to is in nprod. -->