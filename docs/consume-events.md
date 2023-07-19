---
title: Consume Events
---
# What’s a Consumer?
A consumer is an application that is set up to receive messages or events in an event-driven system. The Event Bus exposes streams of events, called topics, to consumers. The events capture significant occurrences taking place in an external system. A list of currently available topics can be found in our [Event Catalog](https://department-of-veterans-affairs.github.io/ves-event-bus-developer-portal/use-events/).

To access messages in a particular topic, an event consumer would subscribe to the topic and receive events as they occur in real time. This allows consumers to perform actions based on the event data, such as updating internal state, triggering other processes, etc. Learn more about the components and processes involved in event-based systems on our [Introduction to Event-Driven Architecture](./intro-to-eda.md) page.

## Steps For Becoming a Consumer
### Find Events/Topics to Consume
The first step to consuming an event is to [reach out to the Enterprise Event Bus Team](./get-support.md) about your interest in events. From there, you can either subscribe to an existing topic with relevant events, or else identify a team able to provide the topic that is of interest to you. At this point in time, we are unable to identify producers for consumers that do not have a source for their desired events, but we will do our best to work with your chosen producing team.
See also our [Produce Events](./produce-events.md) page.

### Determine If You Need an ESECC Request
Depending on the location of a consumer application, you may need to obtain an ESECC (Enterprise Security External Change Council) request. ESECC requests are required to open certain non-standard ports between different systems and allow traffic to flow over those ports.

The diagram below illustrates the relationship between consumer locations and ESECC requirements. It shows that as a general rule, consumers located within the VAEC (VA Enterprise Cloud) AWS Organization do not need to file an ESECC request. For consumers who are in other AWS organizations, or outside of AWS, an ESECC process will likely be needed. If you’re unsure which category your use case fits in, please reach out to the Event Bus Team for help. However, please also note that while the Event Bus Team is happy to give direction and assist with some aspects of the ESECC process, consumers are ultimately responsible for initiating and monitoring the request.

This [example documentation](https://github.com/department-of-veterans-affairs/checkin-devops/blob/master/docs/esecc-requests.md) provides a starting point that outlines the steps and processes involved in an ESECC request. Note that we have not verified that the document is complete and would be applicable in all situations. Please do your own research and be sure to get started as early as possible, as this can be a lengthy process.

![Client Environments ESECC Decision Circles](img/Client%20Environments%20ESECC%20Decision%20Circles.svg)
### Set up Authorization and Authentication
To subscribe to specific topics on the Event Bus, consumers need to be authenticated and have the appropriate permissions. The Event Bus MSK cluster is only accessible from the VA Network, and we use AWS IAM (Identity and Access Management) Roles and Policies to control access to different resources. If your consuming application is within the AWS environment, you will need to let us know to which IAM Role(s) or IAM User(s) we should grant access. We will then set up the corresponding IAM Policies on our end and assign a named role for producers to authenticate with AWS MSK in their application code.

If your consuming application is outside of the AWS environment, we will request an IAM User to be created on your behalf. You will then be able to access the requested topic(s) using those credentials.

### Connect to the Event Bus in the Development Environment
Once the authentication and authorization steps have been completed, you will receive the Kafka bootstrap server addresses and port numbers with which you can connect to the Event Bus MSK cluster. The following ports are open for consumers and producers that are authenticated with AWS IAM:
- 9098 (for access from AWS)
- 9198 (for access from outside of AWS).

### Develop and Deploy Your Consumer Application
Many programming languages and frameworks offer libraries designed to interact with Kafka. To ensure full compatibility with the Event Bus, your code needs to authenticate with the AWS MSK cluster using the assigned role provided during the onboarding process. Additionally, consumers should reference the Confluent Schema Registry and use the appropriate schema to deserialize messages in Avro.

See for instance this Java code that consumes messages from a topic named “test”:

!!! warning
    Note that this code is a draft and might not run as it is. Once finalized, it will be accompanied by a comprehensive reference repo that can be set up locally for testing.

???+ example
    ```java
        package com.eventbus.testconsumer;

        import org.apache.avro.generic.GenericRecord;
        import org.apache.kafka.clients.CommonClientConfigs;
        import org.apache.kafka.clients.consumer.ConsumerConfig;
        import org.apache.kafka.clients.consumer.ConsumerRecord;
        import org.apache.kafka.clients.consumer.ConsumerRecords;
        import org.apache.kafka.clients.consumer.KafkaConsumer;
        import org.apache.kafka.common.config.SaslConfigs;
        import org.apache.kafka.common.config.SslConfigs;
        import org.slf4j.Logger;
        import org.slf4j.LoggerFactory;
        import java.util.concurrent.atomic.AtomicBoolean;

        import io.confluent.kafka.serializers.KafkaAvroDeserializer;
        import io.confluent.kafka.serializers.KafkaAvroDeserializerConfig;

        import java.time.Duration;
        import java.util.Collections;
        import java.util.Properties;
        import java.util.Map;

        public class TestConsumer implements Runnable {
            private static final Logger LOG = LoggerFactory.getLogger(TestConsumer.class);
            private final AtomicBoolean shutdown = new AtomicBoolean(false);

            // Consumer values

            // Set the topic you want to consume from
            private static final String TOPIC = "test";
            private static final String EB_BOOTSTRAP_SERVERS = System.getenv("EB_BOOTSTRAP_SERVERS");
            private static final String EB_SECURITY_PROTOCOL = System.getenv("EB_SECURITY_PROTOCOL");
            private static final String SCHEMA_REGISTRY_URL = System.getenv("SCHEMA_REGISTRY_URL");
            private static final String AWS_ROLE = System.getenv("AWS_ROLE");

            private final KafkaConsumer<Long, GenericRecord> consumer;

            public TestConsumer() {
                this.consumer = createConsumer();
            }

            public void run() {
                try {

                    consumer.subscribe(Collections.singletonList(TOPIC));

                    while (!shutdown.get()) {
                        ConsumerRecords<Long, GenericRecord> records = consumer.poll(Duration.ofMillis(100));

                        for (ConsumerRecord<Long, GenericRecord> record : records) {
                            GenericRecord genericRecord = record.value();
                            // Process the received Avro record
                            LOG.info("Received record: {}", genericRecord.toString());
                        }
                    }
                } catch (final WakeupException e) {
                    // Ignore exception if shutting down
                    if (!shutdown.get()) {
                        throw e;
                    }
                } catch (final Exception e) {
                    LOG.error("An exception occurred while consuming messages", e);
                } finally {
                    consumer.close();
                }
            }

            /**
            * Stops polling for new messages and wakes up the Kafka consumer.
            */
            public void shutdown() {
                shutdown.set(true);
                consumer.wakeup();
            }

            private KafkaConsumer<Long, GenericRecord> createConsumer() {
                final Properties props = new Properties();

                props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, EB_BOOTSTRAP_SERVERS);
                props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, KafkaAvroDeserializer.class.getName());
                props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, KafkaAvroDeserializer.class.getName());
                props.put(KafkaAvroDeserializerConfig.SCHEMA_REGISTRY_URL_CONFIG, SCHEMA_REGISTRY_URL);
                props.put(ConsumerConfig.GROUP_ID_CONFIG, "test-consumer-group"); // Set your consumer group ID

                // Use SASL_SSL in production but PLAINTEXT in local environment
                // w/docker_compose
                if ("SASL_SSL".equals(EB_SECURITY_PROTOCOL)) {
                    props.put(CommonClientConfigs.SECURITY_PROTOCOL_CONFIG, EB_SECURITY_PROTOCOL);
                    props.put(SslConfigs.SSL_TRUSTSTORE_LOCATION_CONFIG, "/tmp/kafka.client.truststore.jks");
                    props.put(SslConfigs.SSL_ENDPOINT_IDENTIFICATION_ALGORITHM_CONFIG, "");
                    props.put(SaslConfigs.SASL_MECHANISM, "AWS_MSK_IAM");
                    props.put(SaslConfigs.SASL_JAAS_CONFIG,
                            "software.amazon.msk.auth.iam.IAMLoginModule required awsRoleArn=\""
                                    + AWS_ROLE // use the role name provided to you
                                    + "\" awsStsRegion=\"us-gov-west-1\";");
                    props.put(SaslConfigs.SASL_CLIENT_CALLBACK_HANDLER_CLASS,
                            "software.amazon.msk.auth.iam.IAMClientCallbackHandler");
                } else if (!"PLAINTEXT".equals(EB_SECURITY_PROTOCOL)) {
                    LOG.error("Unknown EB_SECURITY_PROTOCOL '{}'", EB_SECURITY_PROTOCOL);
                }

                return new KafkaConsumer<>(props);
            }
        }
    ```

### Logs

Logs are stored within a LightHouse Delivery Infrastructure (LHDI) AWS S3 bucket. Only LHDI admins with AWS access can access this bucket and its content. Although producers and consumers will not have access to the S3 bucket directly, logs will be available via Datadog.

Datadog is a monitoring and analytics tool that is used within the VA and is hosted by the Devops Transformation Services (DOTS) team. LHDI team members are admins within the Datadog space where the Event Bus metrics and logs are available. In order for Event Bus users to [request access to Datadog](https://animated-carnival-57b3e7f5.pages.github.io/datadog-observability-tools/datadog-access/), they must have a VA email address.

Event bus logs can be found [here](https://lighthousedi.ddog-gov.com/logs?query=host%3A%22arn%3Aaws%3As3%3A%3A%3Aeventbus-msk-logs%22%20&cols=host%2Cservice&index=%2A&messageDisplay=inline&stream_sort=desc&viz=stream&from_ts=1684858340160&to_ts=1684859240160&live=true).

### Register with the Lighthouse Developer Hub
The [Lighthouse Developer Hub](https://hub.lighthouse.va.gov/) is a software catalog that houses entities from across the VA. Once your consumer application is up and running, you'll want to register with the catalog so event producers are aware of how their events are being used, and which systems are consuming them.

To register with with the Hub:

1. Create a file named `catalog-info.yaml` at the root of your source code repository.
2. Backstage offers a built in [System Entity Kind](https://backstage.io/docs/features/software-catalog/descriptor-format#kind-system). Populate your new `catalog-info.yaml` file with this template, updating `metadata` and `spec` with values that correspond to your system:


        apiVersion: backstage.io/v1alpha1
        kind: System
        metadata:
          name: your system name
          description: what the system does
        spec:
          owner: product team in charge of consuming system
          domain: domain the system falls under


3. Once your `catalog-info.yaml` file has been committed, log into the [Lighthouse Developer Hub](https://hub.lighthouse.va.gov/) while on the VA network, and follow the [default Backstage provided method](https://backstage.io/docs/features/software-catalog/#adding-components-to-the-catalog) for adding entries to the catalog.

### Troubleshooting
If you have questions or run into difficulties with any of these steps, please [contact the Enterprise Event Bus Team](get-support.md).
