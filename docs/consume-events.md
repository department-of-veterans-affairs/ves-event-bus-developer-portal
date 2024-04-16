---
title: Consuming Events
---

# Consuming Events

## What’s a consumer?

A consumer is an application that is set up to receive messages or events in an event-driven system. The Event Bus exposes streams of events, called topics, to consumers. The events capture significant occurrences taking place in an external system. A list of currently available topics can be found in our [Event Catalog](./use-events.md).

To access messages in a particular topic, an event consumer would subscribe to the topic and receive events as they occur in real time. This allows consumers to perform actions based on the event data, such as updating internal state, triggering other processes, etc. The content below outlines the steps needed to start consuming events. These steps can also be visualized on the <a href="https://app.mural.co/t/adhoccorporateworkspace2583/m/adhoccorporateworkspace2583/1678744533321/6e9663e9ba0295865de5f094a62d427affc22f5e?sender=ucc14575938bb14be79634773">Enterprise Event Bus Service Blueprint</a>. Learn more about the components and processes involved in event-based systems on our [Introduction to Event-Driven Architecture](./intro-to-eda.md) page.

## Steps to become a consumer

### Find events/topics to consume

The first step to consuming an event is to [reach out to the Enterprise Event Bus Team](./get-support.md) about your interest in events. From there, you can either subscribe to an existing topic with relevant events, or else identify a team able to provide the topic that is of interest to you. At this point in time, we are unable to identify producers for consumers that do not have a source for their desired events, but we will do our best to work with your chosen producing team.
See also our [Produce Events](./produce-events.md) page.

### Determine if you need an ESECC request

Depending on the location of a consumer application, you may need to obtain an ESECC (Enterprise Security External Change Council) request. ESECC requests are required to open certain non-standard ports between different systems and allow traffic to flow over those ports.

The diagram below illustrates the relationship between consumer locations and ESECC requirements. If you’re unsure which category your use case fits in, please reach out to the Event Bus Team for help. However, please also note that while the Event Bus Team is happy to give direction and assist with some aspects of the ESECC process, consumers are ultimately responsible for initiating and monitoring the request.

This [example documentation](https://github.com/department-of-veterans-affairs/checkin-devops/blob/master/docs/esecc-requests.md) provides a starting point that outlines the steps and processes involved in an ESECC request. Note that we have not verified that the document is complete and would be applicable in all situations. Please do your own research and be sure to get started as early as possible, as this can be a lengthy process.

![A diagram showing various scenarios indicating whether a system would need an ESECC. If you are already on the Lighthouse Delivery Infrastructure (LHDI), no ESECC is required. If you are on AWS GovCloud but outside of LHDI, check to see if an ESECC is required. If you are on Non-AWS Cloud (e.g. Azure), check to see if an ESECC is required. If you are on-premises, e.g., VistA, an ESECC is required.](img/Client-Environments-ESECC-Decision-Circles.svg)

### Set up authorization and authentication

To subscribe to specific topics on the Event Bus, consumers need to be authenticated and have the appropriate permissions. The Event Bus MSK cluster is only accessible from the VA Network, and we use AWS IAM (Identity and Access Management) Roles and Policies to control access to different resources. If your consuming application is within the AWS environment, you will need to let us know to which IAM Role(s) or IAM User(s) we should grant access. We will then set up the corresponding IAM Policies on our end and assign a named role for consumers to authenticate with AWS MSK in their application code.

If your consuming application is outside of the AWS environment, we will request an IAM User to be created on your behalf. You will then be able to access the requested topic(s) using those credentials.

### Connect to the Event Bus in the development environment

Once the authentication and authorization steps have been completed, you will receive the Kafka bootstrap server addresses and port numbers with which you can connect to the Event Bus MSK cluster. The following ports are open for consumers and producers that are authenticated with AWS IAM:

* 9098 (for access from AWS)
* 9198 (for access from outside of AWS)

### Develop and deploy Your consumer application

Many programming languages and frameworks offer libraries designed to interact with Kafka. To ensure full compatibility with the Event Bus, your code needs to authenticate with the AWS MSK cluster using the assigned role provided during the onboarding process. Additionally, consumers should reference the Confluent Schema Registry and use the appropriate schema to deserialize messages in Avro.

See for instance this Java code that consumes messages from a topic named “test”:

!!! info
    To see this Java consumer code in context, please check out the [kafka-client-sample](https://github.com/department-of-veterans-affairs/ves-event-bus-sample-code/tree/main/kafka-client-sample) in the `ves-event-bus-sample-code` repository.

???+ example
    ```java
        package gov.va.eventbus.example;

        import org.apache.avro.generic.GenericRecord;
        import org.apache.kafka.clients.CommonClientConfigs;
        import org.apache.kafka.clients.consumer.ConsumerConfig;
        import org.apache.kafka.clients.consumer.ConsumerRecord;
        import org.apache.kafka.clients.consumer.ConsumerRecords;
        import org.apache.kafka.clients.consumer.KafkaConsumer;
        import org.apache.kafka.common.config.SaslConfigs;
        import org.apache.kafka.common.config.SslConfigs;
        import org.apache.kafka.common.errors.WakeupException;
        import org.slf4j.Logger;
        import org.slf4j.LoggerFactory;
        import java.util.concurrent.atomic.AtomicBoolean;

        import io.confluent.kafka.serializers.KafkaAvroDeserializer;
        import io.confluent.kafka.serializers.KafkaAvroDeserializerConfig;

        import java.time.Duration;
        import java.util.Collections;
        import java.util.Properties;

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

            private final KafkaConsumer<Long, User> consumer;

            public TestConsumer() {
                this.consumer = createConsumer();
            }

            public void run() {
                try {

                    consumer.subscribe(Collections.singletonList(TOPIC));

                    while (!shutdown.get()) {
                        ConsumerRecords<Long, User> records = consumer.poll(Duration.ofMillis(100));

                        for (ConsumerRecord<Long, User> record : records) {
                            User user = record.value();
                            // Process the received Avro record
                            LOG.info("Received record: {}", user.toString());
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

            private KafkaConsumer<Long, User> createConsumer() {
                final Properties props = new Properties();

                props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, EB_BOOTSTRAP_SERVERS);
                props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, KafkaAvroDeserializer.class.getName());
                props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, KafkaAvroDeserializer.class.getName());
                props.put(KafkaAvroDeserializerConfig.SCHEMA_REGISTRY_URL_CONFIG, SCHEMA_REGISTRY_URL);
                // ensure records with a schema are converted.
                props.put(KafkaAvroDeserializerConfig.SPECIFIC_AVRO_READER_CONFIG, true);
                props.put(ConsumerConfig.GROUP_ID_CONFIG, "test-consumer-group"); // Set your consumer group ID

                // Use SASL_SSL in production but PLAINTEXT in local environment
                // w/docker_compose
                if ("SASL_SSL".equals(EB_SECURITY_PROTOCOL)) {
                    props.put(CommonClientConfigs.SECURITY_PROTOCOL_CONFIG, EB_SECURITY_PROTOCOL);
                    props.put(SslConfigs.SSL_TRUSTSTORE_LOCATION_CONFIG, "/tmp/kafka.client.truststore.jks");
                    props.put(SaslConfigs.SASL_MECHANISM, "OAUTHBEARER");
                    props.put(SaslConfigs.SASL_JAAS_CONFIG,
                            "org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required awsRoleArn=\""
                                    + AWS_ROLE // use the role name provided to you
                                    + "\" awsStsRegion=\"us-gov-west-1\";");
                    props.put(SaslConfigs.SASL_LOGIN_CALLBACK_HANDLER_CLASS,
                            "software.amazon.msk.auth.iam.IAMOAuthBearerLoginCallbackHandler");
                } else if (!"PLAINTEXT".equals(EB_SECURITY_PROTOCOL)) {
                    LOG.error("Unknown EB_SECURITY_PROTOCOL '{}'", EB_SECURITY_PROTOCOL);
                }

                return new KafkaConsumer<>(props);
            }
        }
    ```

### Register with CODE VA

[CODE VA](https://code.va.gov/) (must be on VA network to view) is a software catalog that houses information about software entities from across the VA. Once your consumer application is up and running, it's important to register with the catalog so event producers are aware of how their events are being used and which systems are consuming them.

To register with CODE VA:

1. Create a file named `catalog-info.yaml` at the root of your source code repository.
2. Backstage offers built-in [Component](https://backstage.io/docs/features/software-catalog/descriptor-format/#kind-component) and [System](https://backstage.io/docs/features/software-catalog/descriptor-format#kind-system) Entity Kinds. Populate your new `catalog-info.yaml` file with the applicable template, updating `metadata` and `spec` with values that correspond to your component or system:

    ??? Component Example
        ``` { .yaml .copy }
            apiVersion: backstage.io/v1alpha1
            kind: Component
            metadata:
                name: component-name
                description: Component description.
                title: Component Name
                links:
                  - url: https://sample-slack-link.com
                    title: Event Consumer Slack Channel
                  - url: https://sample-link.com
                    title: Component Documentation
            spec:
                type: service
                lifecycle: production
                owner: owning-team
                subscribesToEvent: [event-name, event-name-two]
        ```

    ??? System Example
        ``` { .yaml .copy }
            apiVersion: backstage.io/v1alpha1
            kind: System
            metadata:
                name: system-name
                description: System description.
                title: System Name
                links:
                  - url: https://sample-slack-link.com
                    title: Event Consumer Slack Channel
                  - url: https://sample-link.com
                    title: System Documentation
            spec:
                owner: owning-team
                domain: health
                subscribesToEvent: [event-name, event-name-two]
        ```

    Here is some additional information on individual fields:

    ??? info "Component Fields"
        **apiVersion** [required]: This value must be set to `backstage.io/v1alpha1`.

        **kind** [required]:  This value must be set to `Component`.

        **metadata** [required]: A structure that contains information about the entity. The `metadata` structure includes the following properties.
        
        * **name** [required]: A machine-readable name for the component. This value will be used in CODE VA urls, so it should be all lowercase and use hypens as separators.
        * **description** [required]: A concise, high-level description of the event-consuming component.
        * **title** [required]: A human-readable representation of the `name` to be used in CODE VA user interfaces.
        * **links** [optional]: A list of links related to the component. Each link consists of a `url` and a `title`.
            * **url** [required]: The external url that will be opened when the link is clicked.
            * **title** [required]: Display text for the link.

        **spec** [required]: A structure that contains information about the component. The `spec` structure includes the following properties.

        * **type** [required]: The component type. Possible values include: `website`, `service`, `library`, etc.
        * **lifecycle** [required]: The current development status for the component. Possible values include: `experimental`, `production`, `deprecated`, etc.
        * **owner** [required]: The team that owns the event-consuming component. If this is set to the name of a GitHub team within the VA's GitHub organization, this field will link to a page with details about the team in CODE VA.
        * **subscribesToEvent** [required]: An array of strings. Each string corresponds to the `name` of an event entity in CODE VA.

        See [Backstage's Component documentation](https://backstage.io/docs/features/software-catalog/descriptor-format/#kind-component) for more information about additional optional fields.

    ??? info "System Fields"
        **apiVersion** [required]: This value must be set to `backstage.io/v1alpha1`.

        **kind** [required]:  This value must be set to `System`.

        **metadata** [required]: A structure that contains information about the entity. The `metadata` structure includes the following properties.
        
        * **name** [required]: A machine-readable name for the system. This value will be used in CODE VA urls, so it should be all lowercase and use hypens as separators.
        * **description** [required]: A concise, high-level description of the event-consuming system.
        * **title** [required]: A human-readable representation of the `name` to be used in CODE VA user interfaces.
        * **links** [optional]: A list of links related to the system. Each link consists of a `url` and a `title`.
            * **url** [required]: The external url that will be opened when the link is clicked.
            * **title** [required]: Display text for the link.

        **spec** [required]: A structure that contains information about the system. The `spec` structure includes the following properties.

        * **owner** [required]: The team that owns the event-consuming system. If this is set to the name of a GitHub team within the VA's GitHub organization, this field will link to a page with details about the team in CODE VA.
        * **domain** [optional]: The VA domain in which a particular system exists. Possible values might be: `claims status`, `health`, `appointments`, `benefits`, etc.
        * **subscribesToEvent** [required]: An array of strings. Each string corresponds to the `name` of an event entity.

3. If you are unsure whether to classify your consumer as a Component or a System, see the [Backstage System Model](https://backstage.io/docs/features/software-catalog/system-model/).

4. Once your `catalog-info.yaml` file has been committed it will be automatically picked up after some time and the software entity will be viewable on [CODE VA](https://code.va.gov/) (must be on the VA network to view). If you would like to the event to display quicker, log into [CODE VA](https://code.va.gov/) while on the VA network and follow the [default Backstage provided method](https://backstage.io/docs/features/software-catalog/#adding-components-to-the-catalog) for adding entries to the catalog.

**NOTE**: As a consumer, it is imperative that you include the `subscribesToEvent` property in your `catalog-info.yaml` file, in the `spec` object. `subscribesToEvent` is an array containing strings. Each string corresponds to a `name` specified in a producer's `catalog-info.yaml` file [metadata object](https://backstage.io/docs/features/software-catalog/descriptor-format#common-to-all-kinds-the-metadata). This metadata name property can not always be derived from the event or the topic, so it will require referencing the producer's `catalog-info.yaml` file, e.g.:

    apiVersion: backstage.io/v1alpha1
    kind: Event
    metadata:
        name: event-name // <== This is what needs to be referenced
        description: Event description
        title: Event Name
        // ...

We use the `subscribesToEvent` property to generate [Backstage relations](https://backstage.io/docs/features/software-catalog/extending-the-model#adding-a-new-relation-type) between consumers and producers. These relations are displayed on Event Overview pages in a table. Without this property, there will be no visual representation of what systems or components are subscribing to a given event.

## Logs

Logs are stored within a LightHouse Delivery Infrastructure (LHDI) AWS S3 bucket. Only LHDI admins with AWS access can access this bucket and its content. Although producers and consumers will not have access to the S3 bucket directly, logs are available via [Datadog](https://lighthousedi.ddog-gov.com/). Event bus broker logs are available through [this query](https://lighthousedi.ddog-gov.com/logs?query=host%3A%22arn%3Aaws%3As3%3A%3A%3Aeventbus-msk-logs%22%20&cols=host%2Cservice&index=%2A&messageDisplay=inline&stream_sort=desc&viz=stream&from_ts=1684858340160&to_ts=1684859240160&live=true) and application logs are available through [this query](https://lighthousedi.ddog-gov.com/logs?query=kube_namespace%3Aves-event-bus-infra-dev%20&cols=host%2Cservice&index=%2A&messageDisplay=inline&refresh_mode=sliding&stream_sort=desc&viz=stream&from_ts=1695939680975&to_ts=1696544480975&live=true). 

Datadog is a monitoring and analytics tool that is used within VA and is hosted by the Devops Transformation Services (DOTS) team. LHDI team members are admins within the Datadog space where the Event Bus metrics and logs are available. In order for Event Bus users to [request access to Datadog](https://animated-carnival-57b3e7f5.pages.github.io/datadog-observability-tools/datadog-access/), they must have a VA email address. To request access to Datadog, complete the HelpDesk form on the ServiceNow Portal at [ECC (Enterprise Command Center) Monitoring Services - your IT Service Portal](https://gcc02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fyourit.va.gov%2Fva%3Fid%3Dsc_cat_item%26sys_id%3D4cdf488b1ba4fcd412979796bc4bcb74&data=05%7C01%7C%7Ccb701e4e7fc944b6041308dbeacea9aa%7Ce95f1b23abaf45ee821db7ab251ab3bf%7C0%7C0%7C638361945550254440%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=sJfq3j8vnXwdtuQrfY%2FBaRttaqyOpKA6X17O8TMK9ug%3D&reserved=0). This must be accessed from the VA Network.

## Troubleshooting

If you have questions or run into difficulties with any of these steps, please [contact the Enterprise Event Bus Team](./get-support.md).
