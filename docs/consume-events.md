---
title: Consuming Events
---

# **Consuming Events**

## **What’s a consumer?**

A consumer is an application that is set up to receive messages or events in an event-driven system. The Event Bus exposes streams of events, called topics, to consumers. The events capture significant occurrences taking place in an external system. Find out how to view a list of currently available topics by visiting our [Event Catalog page](./use-events.md).

To access messages in a particular topic, an event consumer subscribes to the topic and receive events as they occur in real time. This allows consumers to perform actions based on the event data, such as updating internal state, triggering other processes, etc. The content below outlines the steps needed to start consuming events. Learn more about the components and processes involved in event-based systems on our [How Event Bus Implements Event-Driven Architecture page](./intro-to-eda.md).

## **Steps to become a consumer**

### **Find events/topics to consume**

The first step to consuming an event is to [reach out to the Enterprise Event Bus Team](./get-support.md) about your interest in events. From there, you can either subscribe to an existing topic with relevant events, or else identify a team able to provide the topic that is of interest to you. At this point in time, we are unable to identify producers for consumers that do not have a source for their desired events, but we will do our best to work with your chosen producing team.

See also our [Produce Events page](./produce-events.md).

### **Determine if you need an ESECC request**

See the [ESECC section on the Administrative Requirements page](./administrative-requirements.md#esecc).

### **For consumers of BIP-sourced Events**

Read the [documentation about requesting data access and sensitivity filtering on our Administrative Requirements page](./administrative-requirements.md#consumers-of-bip-sourced-events).

### **Set up authorization and authentication**

To subscribe to specific topics on the Event Bus, consumers need to be authenticated and have the appropriate permissions. The Event Bus MSK cluster is only accessible from the VA Network, and we use AWS IAM (Identity and Access Management) Roles and Policies to control access to different resources. If your consuming application is within the AWS environment, you will need to let us know to which IAM Role(s) or IAM User(s) we should grant access. We will then set up the corresponding IAM Policies on our end and assign a named role for consumers to authenticate with AWS MSK in their application code.

If your consuming application is outside of the AWS environment, we will request an IAM User to be created on your behalf. You will then be able to access the requested topic(s) using those credentials.

### **Connect to the Event Bus in the development environment**

Once the authentication and authorization steps have been completed, you will receive the Kafka bootstrap server addresses and port numbers with which you can connect to the Event Bus MSK cluster. The following ports are open for consumers and producers that are authenticated with AWS IAM:

* 9098 (for access from AWS)
* 9198 (for access from outside of AWS)

### **Develop and deploy your consumer application**

Many programming languages and frameworks offer libraries designed to interact with Kafka. To ensure full compatibility with the Event Bus, your code needs to authenticate with the AWS MSK cluster using the assigned role provided during the onboarding process. Additionally, consumers should reference the Confluent Schema Registry and use the appropriate schema to deserialize messages in Avro.

#### **Client properties**

To connect to the Event Bus, consumers in **all programming languages** will need to set these properties, which are required unless otherwise specified:

| Property | Value | Description | Notes |
| --- | --- | --- | --- |
| [bootstrap.servers](https://kafka.apache.org/documentation/#consumerconfigs_bootstrap.servers) | List of one or more Event Bus brokers. This will vary depending on the environment (dev, prod, etc.). | A list of host/port pairs to use for establishing the initial connection to the Kafka cluster. | Only one of the Event Bus brokers needs to be included in this list, but including more than one will ensure the application can start up if one of the Kafka servers is down. |
| [group.id](https://kafka.apache.org/documentation/#consumerconfigs_group.id) | This can be set to any value a consumer wants. | A unique string that identifies the consumer group this consumer belongs to. |  |
| [sasl.mechanism](https://kafka.apache.org/documentation/#consumerconfigs_sasl.mechanism) | `OAUTHBEARER` | SASL mechanism used for client connections. |  |
| [security.protocol](https://kafka.apache.org/documentation/#consumerconfigs_security.protocol) | `SASL_SSL` | Protocol used to communicate with brokers. |  |
| [auto.offset.reset](https://kafka.apache.org/documentation/#consumerconfigs_auto.offset.reset) (recommended) | `earliest` | What to do when there is no initial offset in Kafka or if the current offset does not exist anymore on the server. | Setting this field to "earliest" instead of the default "latest" will cause the consumer to consume older events which are still available on the Event Bus when it first deploys. If past events do not need to be processed when first connecting to the Event Bus, then consumers can use the default. Once a consumer has consumed some events, it will always pick up where it last left off even when it restarts. |
| [client.rack](https://kafka.apache.org/documentation/#consumerconfigs_client.rack) (recommended) | The AWS Availability Zone in which your application is running, eg. "usgw1-az2" | A rack identifier for this client. This can be any string value which indicates where this client is physically located. | This property is only applicable if your application is deployed to AWS (Amazon Web Services) infrastructure. Setting this to your availability zone will [reduce network traffic costs](https://aws.amazon.com/blogs/big-data/reduce-network-traffic-costs-of-your-amazon-msk-consumers-with-rack-awareness/).
| [enable.auto.commit](https://kafka.apache.org/documentation/#consumerconfigs_enable.auto.commit) (recommended) | false | If true the consumer's offset will be periodically committed in the background. | If set to true, the consumer may mark some records as consumed before they have been processed. See [Manual Offset Control](https://javadoc.io/static/org.apache.kafka/kafka-clients/3.6.0/org/apache/kafka/clients/consumer/KafkaConsumer.html#:~:text=Manual%20Offset%20Control) for more information. |

Depending on the client language used, additional properties may also be needed for authorization and connecting to the schema registry. For example, these properties are required for **Java clients**:

| Property | Value | Description | Notes |
| --- | --- | --- | --- |
| [key.deserializer](https://kafka.apache.org/documentation/#consumerconfigs_key.deserializer) | `KafkaAvroDeserializer` | Deserializer class for key. | All Event Bus records use an Avro schema, so this is required even if the key itself is a primitive type like `string` or `long`. |
| [sasl.jaas.config](https://kafka.apache.org/documentation/#consumerconfigs_sasl.jaas.config) | `OAuthBearerLoginModule` and role settings. The role will vary for each consumer. | JAAS login context parameters for SASL connections in the format used by JAAS configuration files.  | See [specifying an AWS IAM role](https://github.com/aws/aws-msk-iam-auth#specifying-an-aws-iam-role-for-a-client) for more information. |
| [sasl.login.callback.handler.class](https://kafka.apache.org/documentation/#consumerconfigs_sasl.login.callback.handler.class) | `IAMOAuthBearerLoginCallbackHandler` | The fully qualified name of a SASL login callback handler class. | See [aws-msk-iam-auth](https://github.com/aws/aws-msk-iam-auth?tab=readme-ov-file#configuring-a-kafka-client-to-use-aws-iam-with-sasl-oauthbearer-mechanism) for more information. |
| [sasl.client.callback.handler.class](https://kafka.apache.org/documentation/#consumerconfigs_sasl.client.callback.handler.class) | `IAMOAuthBearerLoginCallbackHandler` | The fully qualified name of a SASL client callback handler class. | See [aws-msk-iam-auth](https://github.com/aws/aws-msk-iam-auth?tab=readme-ov-file#configuring-a-kafka-client-to-use-aws-iam-with-sasl-oauthbearer-mechanism) for more information. |
| [value.deserializer](https://kafka.apache.org/documentation/#consumerconfigs_value.deserializer) | `KafkaAvroDeserializer` | Deserializer class for value. |  |
| schema.registry.url | Event Bus schema registry endpoint. This will vary depending on the environment (dev, prod, etc.). | Comma-separated list of URLs for Schema Registry instances that can be used to register or look up schemas. |
| use.latest.version | `false` (this is the default value) | Flag that indicates if the latest schema version should be used for deserialization. | Event Bus recommends setting this value to false to avoid issues when a new schema version is added to the schema registry. |
| latest.cache.ttl.sec | `-1` (this is the default value) | This sets a TTL for the schema registry cache. `-1` indicates that the cache has no TTL. | Event Bus recommends using the default of `-1` for this value. Schema versions do not change once they are registered. This will decrease the application's dependency on the schema registry. | |

#### **Code samples**

!!! info
    Expand the sections below to see consumer code examples in Java and Ruby. To see the consumer code samples in context, please check out the [`ves-event-bus-sample-code` repository (must be part of VA GitHub organization to view)](https://github.com/department-of-veterans-affairs/ves-event-bus-sample-code).

??? example "Java Consumer"
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
                props.put(SaslConfigs.SASL_CLIENT_CALLBACK_HANDLER_CLASS,
                        "software.amazon.msk.auth.iam.IAMOAuthBearerLoginCallbackHandler");
            } else if (!"PLAINTEXT".equals(EB_SECURITY_PROTOCOL)) {
                LOG.error("Unknown EB_SECURITY_PROTOCOL '{}'", EB_SECURITY_PROTOCOL);
            }

            return new KafkaConsumer<>(props);
        }
    }
    ```

??? example "Ruby Consumer"
    ```ruby
    require 'logger'
    require 'rdkafka'
    require 'avro_turf/messaging'
    require_relative 'oauth_token_refresher'

    logger = Logger.new(STDOUT)

    @consumers = {}

    def refresh_token(_config, consumer_name)
        consumer = @consumers[consumer_name]
        OAuthTokenRefresher.new.refresh_token(consumer)
    end

    security_protocol = ENV['SECURITY_PROTOCOL']

    properties = {
        'bootstrap.servers': ENV['KAFKA_HOST'],
        'group.id': 'sample-ruby-consumer',
        'security.protocol': security_protocol,
        'enable.auto.commit': false,
        'auto.offset.reset': 'earliest'
    }

    if 'SASL_SSL' == security_protocol.upcase
        properties['sasl.mechanisms'] = 'OAUTHBEARER'
        Rdkafka::Config.oauthbearer_token_refresh_callback = method(:refresh_token)
    end

    consumer = Rdkafka::Config.new(properties).consumer(native_kafka_auto_start: false)
    @consumers[consumer.name] = consumer
    consumer.start
    consumer.subscribe("appointments")

    avro = AvroTurf::Messaging.new(registry_url: ENV['SCHEMA_REGISTRY_URL'], registry_path_prefix: ENV['SCHEMA_REGISTRY_PATH_PREFIX'])

    logger.info "Running consumer"
    consumer.each do |message|
        logger.info "Message received: #{message}"
        logger.info "Decoded message payload: #{avro.decode(message.payload)}"
        consumer.commit
    end
    ```

### **Register with CODE VA**

[CODE VA (must be on VA network to view)](https://code.va.gov/) is a software catalog that houses information about software entities from across VA. Once your consumer application is up and running, it's important to register with the catalog so event producers are aware of how their events are being used and which systems are consuming them.

To register with CODE VA:

1. In CODE VA, an event-consuming software entity can be modeled as a [Component](https://backstage.io/docs/features/software-catalog/descriptor-format/#kind-component) or as a [System](https://backstage.io/docs/features/software-catalog/descriptor-format#kind-system). If you are unsure whether to classify your consumer as a Component or a System, see the [Backstage System Model](https://backstage.io/docs/features/software-catalog/system-model/).
2. Create a file named `catalog-info.yaml` at the root of your source code repository and populate it with the applicable template, updating `metadata` and `spec` with values that correspond to your component or system.
3. Once your `catalog-info.yaml` file has been committed it will be automatically processed and the software entity will be viewable on [CODE VA website (must be on the VA network to view)](https://code.va.gov/) within a few hours. If you would like the software entity to display quicker, follow the [Backstage documentation on the default method for adding entries to the catalog](https://backstage.io/docs/features/software-catalog/#adding-components-to-the-catalog).

#### **Component Template**
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

Here is some additional information on these fields:

* **apiVersion** [required]: This value must be set to `backstage.io/v1alpha1`.
* **kind** [required]:  This value must be set to `Component`.
* **metadata** [required]: A structure that contains information about the entity. The `metadata` structure includes the following properties.
    * **name** [required]: A machine-readable name for the component. This value will be used in CODE VA urls, so it should be all lowercase and use hyphens as separators.
    * **description** [required]: A concise, high-level description of the event-consuming component.
    * **title** [required]: A human-readable representation of the `name` to be used in CODE VA user interfaces.
    * **links** [optional]: A list of links related to the component. Each link consists of a `url` and a `title`.
        * **url** [required]: The external url that will be opened when the link is clicked.
        * **title** [required]: Display text for the link.
* **spec** [required]: A structure that contains information about the component. The `spec` structure includes the following properties.
    * **type** [required]: The component type. Possible values include: `website`, `service`, `library`, etc.
    * **lifecycle** [required]: The current development status for the component. Possible values include: `experimental`, `production`, `deprecated`, etc.
    * **owner** [required]: The team that owns the event-consuming component. If this is set to the name of a GitHub team within the VA's GitHub organization, this field will link to a page with details about the team in CODE VA.
    * **subscribesToEvent** [required]: An array of strings. Each string must match the `metadata.name` value of a producer's `catalog-info.yaml` file. This field is used to relate the component to the events that it consumes and to display the component on each related event's CODE VA catalog entry.

See [Backstage's Component documentation](https://backstage.io/docs/features/software-catalog/descriptor-format/#kind-component) for more information about additional optional fields.

#### **System Template**
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

Here is some additional information on these fields:

* **apiVersion** [required]: This value must be set to `backstage.io/v1alpha1`.
* **kind** [required]:  This value must be set to `System`.
* **metadata** [required]: A structure that contains information about the entity. The `metadata` structure includes the following properties.
    * **name** [required]: A machine-readable name for the system. This value will be used in CODE VA urls, so it should be all lowercase and use hyphens as separators.
    * **description** [required]: A concise, high-level description of the event-consuming system.
    * **title** [required]: A human-readable representation of the `name` to be used in CODE VA user interfaces.
    * **links** [optional]: A list of links related to the system. Each link consists of a `url` and a `title`.
        * **url** [required]: The external url that will be opened when the link is clicked.
        * **title** [required]: Display text for the link.
* **spec** [required]: A structure that contains information about the system. The `spec` structure includes the following properties.
    * **owner** [required]: The team that owns the event-consuming system. If this is set to the name of a GitHub team within the VA's GitHub organization, this field will link to a page with details about the team in CODE VA.
    * **domain** [optional]: The VA domain in which a particular system exists. Possible values might be: `claims status`, `health`, `appointments`, `benefits`, etc.
    * **subscribesToEvent** [required]: An array of strings. Each string must match the `metadata.name` value of a producer's `catalog-info.yaml` file. This field is used to relate the system to the events that it consumes and to display the system on each related event's CODE VA catalog entry.

## **Schema Evolution**

Eventually the schema of an event may evolve. After a new version of the schema is added to the schema registry, consumers will need to update their applications to handle the new schema version before producers update to produce events using the new schema. The Event Bus team will inform consumers about upcoming schema changes.

## **Logs**

Logs are stored within a LightHouse Delivery Infrastructure (LHDI) AWS S3 bucket. Only LHDI admins with AWS access can access this bucket and its content. Although producers and consumers will not have access to the S3 bucket directly, logs are available via [Datadog (must have VA LightHouseDI Datadog access to view)](https://lighthousedi.ddog-gov.com/):
- [Event Bus broker logs sandbox](https://lighthousedi.ddog-gov.com/logs?query=host%3A%22arn%3Aaws%3As3%3A%3A%3Aeventbus-msk-broker-logs-nprod-sandbox%22&agg_m=count&agg_m_source=base&agg_t=count&cols=host%2Cservice&fromUser=true&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1684858340160&to_ts=1684859240160&live=true)
- [Event Bus broker logs Prod](https://lighthousedi.ddog-gov.com/logs?query=host%3A%22arn%3Aaws%3As3%3A%3A%3Aeventbus-msk-broker-logs-prod%22%20&agg_m=count&agg_m_source=base&agg_t=count&cols=host%2Cservice&fromUser=true&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1684858340160&to_ts=1684859240160&live=true)
- [Event Bus app logs sandbox](https://lighthousedi.ddog-gov.com/logs?query=kube_namespace%3Aves-event-bus-infra-sandbox&agg_m=count&agg_m_source=base&agg_t=count&cols=host%2Cservice&fromUser=true&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1695939680975&to_ts=1696544480975&live=true)
- [Event Bus app logs prod](https://lighthousedi.ddog-gov.com/logs?query=kube_namespace%3Aves-event-bus-infra-prod&agg_m=count&agg_m_source=base&agg_t=count&cols=host%2Cservice&fromUser=true&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1695939680975&to_ts=1696544480975&live=true)

Datadog is a monitoring and analytics tool that is used within VA and is hosted by the Devops Transformation Services (DOTS) team. LHDI team members are admins within the Datadog space where the Event Bus metrics and logs are available. In order for Event Bus users to request access to Datadog they must have a VA email address. To request access to Datadog, complete the HelpDesk form on the ServiceNow Portal at [ECC (Enterprise Command Center) Monitoring Services - your IT Service Portal (must be on the VA network to view)](https://gcc02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fyourit.va.gov%2Fva%3Fid%3Dsc_cat_item%26sys_id%3D4cdf488b1ba4fcd412979796bc4bcb74&data=05%7C01%7C%7Ccb701e4e7fc944b6041308dbeacea9aa%7Ce95f1b23abaf45ee821db7ab251ab3bf%7C0%7C0%7C638361945550254440%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=sJfq3j8vnXwdtuQrfY%2FBaRttaqyOpKA6X17O8TMK9ug%3D&reserved=0).

## **Troubleshooting**

If you have questions or run into difficulties with any of these steps, please [contact the Enterprise Event Bus Team](./get-support.md).
