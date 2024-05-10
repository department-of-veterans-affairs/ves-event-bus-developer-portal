---
title: Environments
---

# Environments

## Descriptions

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
