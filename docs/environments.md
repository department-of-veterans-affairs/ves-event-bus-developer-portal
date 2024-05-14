---
title: Environments
---

# Environments

Event Bus [Kafka](https://kafka.apache.org/) and applications are deployed into several environments for different purposes. We deploy any new releases to all environments on Wednesdays. The environments are described in the table below.

| Environment Name | Description                                                                                                | PHI, PII<br>Allowed |
|------------------|------------------------------------------------------------------------------------------------------------|---------------------|
| `sandbox`        | A stable environment that external teams can connect to. It is a "customer dev" environment.               | No                  |
| `pre-prod`       | A testing environment that has been cleared for PHI and PII. `Pre-prod` may be used for performance tests. | Yes                 |
| `prod`           | Our production environment.                                                                                | Yes                 |
