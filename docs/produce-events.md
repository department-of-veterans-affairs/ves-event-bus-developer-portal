---
title: Producing Events
---

# **Producing Events**

## **What's a producer?**

A producer is an application designed to generate messages or events within an event-driven system. In the context of the Enterprise Event Bus, which aims to expose streams of events known as topics, producers play a crucial role. Producing teams have access to, or knowledge about, important data changes in the VA ecosystem and can send events to specific topics on the Event Bus. Find out how to view a list of currently available topics by visiting our [Event Catalog page](./use-events.md).

As producers are responsible for defining topics and their contents, they will work with the Event Bus Team to determine configuration settings such as the number of topic partitions, event versioning, and event retention rules. The content below outlines the steps needed to start producing events. To learn more about the components and processes involved in event-based systems, please visit our [How Event Bus Implements Event-Driven Architecture page](./intro-to-eda.md).

## **Steps to become a producer**

### **Define the event or topic**

The first step in producing an event is to [contact the Enterprise Event Bus Team](./get-support.md) and express your interest in contributing an event stream. An ideal event stream represents a business event within the VA that would be of interest to multiple stakeholders and have a significant impact on Veterans. Examples of such events include changes to eligibility for benefits, milestones in the claims process, or updates to a Veteran's health record, such as new appointments, prescriptions, or lab results.

While it is not a requirement to have consumers identified from the start, in an ideal scenario the events would theoretically be meaningful to multiple, independent consumers. If you do have consumers in mind, reach out to them and engage in preliminary discussions about their needs, preferences, and timelines. You can find more information on consuming events on our [Consuming Events page](./consume-events.md).

If there is a mutual interest to continue after the initial meeting, the Event Bus Team will create a one-page description of the proposed event topic, including details about the business context, event purpose, payload, and consumers. The partner team will review and provide feedback on the document and sign a Working Agreement and a Data Sharing Agreement.

### **Determine if you need an ESECC request**

See the [ESECC section on the Administrative Requirements page](./administrative-requirements.md#esecc).

### **Choose configuration settings and submit onboarding request**

Before creating a topic, you need to consider various Kafka settings. Producing teams must choose appropriate settings based on their specific use case and technical requirements. From a logistical perspective, the Event Bus Team will handle the initial creation of the topic using the Kafka CLI and make it available for production.

#### **Number of partitions**

Partitions in Kafka serve as the primary unit of storage within a topic, with each partition containing a subset of events. Determining the number of partitions is crucial, as it has implications for storage, scalability, replication, and message movement. To learn more about reasonable defaults, and other partition-related concerns, read our [guidance on topics and partitions (must be part of VA GitHub organization to view)](https://github.com/department-of-veterans-affairs/VES/blob/master/research/Event%20Bus/Engineering/ADR/ADR%20Kafka%20Partitions.md).

#### **Event retention**

Event retention refers to how long an event exists within Kafka and remains available for consumption. This setting would be especially important to consumers who need to be prepared to handle missed events before they expire. For additional information and discussion, see the section about Retention in our [Event Design Architectural Decision Record (must be part of VA GitHub organization to view)](https://github.com/department-of-veterans-affairs/VES/blob/master/research/Event%20Bus/Engineering/ADR/ADR%20event%20design.md#event-retention).

#### **Event schema and event registry**

The Event Bus utilizes the [Confluent Schema Registry](https://docs.confluent.io/platform/7.5/schema-registry/fundamentals/index.html#sr-key-concepts) to store schemas and their versions. Avro is used to define the schema format. Producers must submit an event schema representing the event payload in Avro format as part of the onboarding process. Producers must also use [Apache Avro](https://avro.apache.org/) to serialize data onto the Event Bus so that the event schema, and the data contract it represents, is enforced. Additionally, producers should consider event versioning, which involves planning how schemas will evolve. Event versions are governed by the compatibility type setting, which determines allowed schema changes and how consumers interact with different versions. For most producers, we recommend using the `BACKWARD` compatibility type. For more information, see our [article about the Confluent Schema Registry (must be part of VA GitHub organization to view)](https://github.com/department-of-veterans-affairs/VES/blob/master/research/Event%20Bus/Engineering/ADR/ADR%20schema%20registry.md), and our [article about schema versioning (must be part of VA GitHub organization to view)](https://github.com/department-of-veterans-affairs/VES/blob/master/research/Event%20Bus/Engineering/ADR/ADR%20schema%20versioning.md).

Once the producing team has communicated their decisions about the event schema, the Event Bus team will create the topic, along with the schema, and notify the producing team when everything is ready for use.

### **Set up authorization and authentication**

To produce messages to specific topics on the Event Bus, producers need to be authenticated and have the appropriate permissions. The Event Bus MSK cluster is only accessible from the VA Network, and we use AWS IAM (Identity and Access Management) Roles and Policies to control access to different resources. If your producing application is within the AWS environment, please inform us of the IAM Role(s) or IAM User(s) to which we should grant access. We will then set up the corresponding IAM Policies on our end and assign a named role for producers to authenticate with AWS MSK in their application code. If your producing application is outside of the AWS environment, we will request an IAM User to be created on your behalf. You will then be able to access the requested topic(s) using those credentials.

### **Connect to the Event Bus in the development environment**

Once the authentication and authorization steps have been completed, you will be able to connect to the Event Bus MSK cluster using the Kafka bootstrap server addresses and port numbers available in the Event Catalog. The following ports are open for consumers and producers that are authenticated with AWS IAM:

* 9098 (for access from AWS)
* 9198 (for access from outside of AWS)

### **Develop and deploy your producer application**

Many programming languages and frameworks offer libraries designed to interact with Kafka. To ensure full compatibility with the Event Bus, your code needs to authenticate with the AWS MSK cluster using the assigned role provided during the onboarding process. Additionally, producers should reference the Confluent Schema Registry and use the created schema to serialize messages in Avro.

#### **Client properties**

To connect to the Event Bus, producers in **all programming languages** will need to set these properties:

| Property | Value | Description | Notes |
| --- | --- | --- | --- |
| [bootstrap.servers](https://kafka.apache.org/documentation/#producerconfigs_bootstrap.servers) | List of one or more Event Bus brokers. This will vary depending on the environment (dev, prod, etc.). | A list of host/port pairs to use for establishing the initial connection to the Kafka cluster. | Only one of the Event Bus brokers needs to be included in this list, but including more than one will ensure the application can start up if one of the brokers is down. |
| [enable.idempotence](https://kafka.apache.org/documentation/#producerconfigs_enable.idempotence) | false | When set to 'true', the producer will ensure that exactly one copy of each message is written in the stream. If 'false', producer retries due to broker failures, etc., may write duplicates of the retried message in the stream. | If idempotence is a must-have for your application, then we will need to grant additional AWS permissions before you can set this to true. |
| [sasl.mechanism](https://kafka.apache.org/documentation/#producerconfigs_sasl.mechanism) | `OAUTHBEARER` | SASL mechanism used for client connections. |  |
| [security.protocol](https://kafka.apache.org/documentation/#producerconfigs_security.protocol) | `SASL_SSL` | Protocol used to communicate with brokers. |  |

Depending on the language client used, additional properties may also be needed for authorization and connecting to the schema registry. For example, these properties are required for **Java clients**:

| Property | Value | Description | Notes |
| --- | --- | --- | --- |
| [key.serializer](https://kafka.apache.org/documentation/#producerconfigs_key.serializer) | `KafkaAvroSerializer` | Serializer class for key. | All Event Bus records use an Avro schema, so this is required even if the key itself is a primitive type like `string` or `long`. |
| [sasl.jaas.config](https://kafka.apache.org/documentation/#producerconfigs_sasl.jaas.config) | `OAuthBearerLoginModule` and role settings. The role will vary for each producer. | JAAS login context parameters for SASL connections in the format used by JAAS configuration files.  | See [specifying an AWS IAM role](https://github.com/aws/aws-msk-iam-auth#specifying-an-aws-iam-role-for-a-client) for more information. |
| [sasl.login.callback.handler.class](https://kafka.apache.org/documentation/#producerconfigs_sasl.login.callback.handler.class) | `IAMOAuthBearerLoginCallbackHandler` | The fully qualified name of a SASL login callback handler class. | See [aws-msk-iam-auth](https://github.com/aws/aws-msk-iam-auth?tab=readme-ov-file#configuring-a-kafka-client-to-use-aws-iam-with-sasl-oauthbearer-mechanism) for more information. |
| [sasl.client.callback.handler.class](https://kafka.apache.org/documentation/#producerconfigs_sasl.client.callback.handler.class) | `IAMOAuthBearerLoginCallbackHandler` | The fully qualified name of a SASL client callback handler class. | See [aws-msk-iam-auth](https://github.com/aws/aws-msk-iam-auth?tab=readme-ov-file#configuring-a-kafka-client-to-use-aws-iam-with-sasl-oauthbearer-mechanism) for more information. |
| [value.serializer](https://kafka.apache.org/documentation/#producerconfigs_value.serializer) | `KafkaAvroSerializer` | Serializer class for value. |  |
| auto.register.schemas | `false` | Specify if the serializer should attempt to register the schema with the Schema Registry. | If set to true, the producer will attempt to register a new schema rather than using an existing one in the registry. Since writes to the Event Bus schema registry are blocked for unauthorized applications, this will result in an error which prevents the producer from producing events. |
| schema.registry.url | Event Bus schema registry endpoint. This will vary depending on the environment (dev, prod, etc.). | Comma-separated list of URLs for Schema Registry instances that can be used to register or look up schemas. | 
| use.latest.version | `false` (this is the default value) | Flag that indicates if the latest schema version should be used for serialization.| Event Bus recommends setting this value to false to avoid issues when a new schema version is added to the schema registry. |
| use.schema.id | ID of the schema in the Event Bus schema registry. This will vary depending on the environment. The Event Bus team will supply this value. | Integer ID that indicates which schema to use for serialization. | Event Bus recommends setting this value to be specific about which schema version is used to write events and to reduce ambiguity. |
| latest.cache.ttl.sec | `-1` (this is the default value) | This sets a TTL for the schema registry cache. `-1` indicates that the cache has no TTL. | Event Bus recommends using the default of `-1` for this value. Schema versions do not change once they are registered. This will decrease the application's dependency on the schema registry. | |

#### **Producer Performance Optimization**

Kafka producers can be optimized based on message size and throughput requirements. The default Kafka settings (`batch.size=16384` bytes, `linger.ms=0`) are designed for larger messages but can result in poor batch utilization for smaller messages.

##### **Environment Variable Configuration**

Configure via environment variables to allow per-environment optimization:

```java
// In your dependency provider or configuration class
public final int KAFKA_PRODUCER_BATCH_SIZE;
public final int KAFKA_PRODUCER_LINGER_MS;

public DependencyProvider() {
    // Kafka Producer optimization settings with defaults optimized for small messages
    // Default Kafka settings: batch.size=16384 (16KB), linger.ms=0
    // For small messages (104-204 bytes), this results in ~1.2% batch utilization (99% waste)
    // 
    // Recommended settings based on message size:
    // - Small messages (<500 bytes): batch.size=1024 (1KB), linger.ms=5-10ms → ~20% utilization
    // - Medium messages (500B-5KB): batch.size=8192 (8KB), linger.ms=5-10ms → ~20-60% utilization
    // - Large messages (>5KB): batch.size=16384 (16KB), linger.ms=0-5ms → ~30-100% utilization
    //
    // Trade-off: Adding linger.ms slightly increases latency but significantly improves throughput
    // Example: 10ms linger allows batching 5-10 small messages, reducing network calls by 5-10x
    KAFKA_PRODUCER_BATCH_SIZE =
        Integer.parseInt(ENV.getOrDefault("KAFKA_PRODUCER_BATCH_SIZE", "16384"));
    KAFKA_PRODUCER_LINGER_MS = 
        Integer.parseInt(ENV.getOrDefault("KAFKA_PRODUCER_LINGER_MS", "0"));
}

private Properties createProducerConfig() {
    Properties producerProps = new Properties();
    
    // ... other configuration ...
    
    // Kafka producer performance tuning parameters
    // Configured via environment variables to allow per-environment optimization
    // Monitor impact using DataDog JMX metrics: batch-size-avg, record-send-rate, request-latency-avg
    producerProps.put(ProducerConfig.BATCH_SIZE_CONFIG, KAFKA_PRODUCER_BATCH_SIZE);
    producerProps.put(ProducerConfig.LINGER_MS_CONFIG, KAFKA_PRODUCER_LINGER_MS);
    
    return producerProps;
}
```

##### **Kubernetes Deployment Configuration**

In your `deployment.yaml`:

```yaml
env:
  - name: KAFKA_PRODUCER_BATCH_SIZE
    # Producer batch size optimization for small messages
    # Default: 16384 (16KB) - results in ~1.2% utilization for 200-byte messages
    # Current: {{ .Values.producer.batchSize }} - optimized for our message sizes
    # Formula: Utilization = Avg Message Size ÷ batch.size
    # See producer config documentation for calculation details
    value: "{{ .Values.producer.batchSize }}"
  - name: KAFKA_PRODUCER_LINGER_MS
    # Producer linger time - allows batching multiple messages
    # Default: 0 (send immediately) - results in one network call per message
    # Current: {{ .Values.producer.lingerMs }}ms - balances latency vs throughput
    # Trade-off: +{{ .Values.producer.lingerMs }}ms latency for 5-10x fewer network calls
    # Monitor: record-send-rate and request-latency-avg in DataDog
    value: "{{ .Values.producer.lingerMs }}"
```

In your `values.yaml` (dev.yaml, sandbox.yaml, prod.yaml):

```yaml
producer:
  batchSize: 1024  # 1KB - Conservative optimization for small messages
  lingerMs: 5      # 5ms - Balances latency and throughput
```

#### **Code samples**

!!! info
    Expand the sections below to see producer code examples in Java and Ruby. To see the samples in context, please check out the [`ves-event-bus-sample-code` repository (must be part of VA GitHub organization to view)](https://github.com/department-of-veterans-affairs/ves-event-bus-sample-code).

??? example "Java Producer"
    ```java
    package gov.va.eventbus.example;

    import io.confluent.kafka.serializers.KafkaAvroDeserializerConfig;
    import io.confluent.kafka.serializers.KafkaAvroSerializer;
    import io.confluent.kafka.serializers.KafkaAvroSerializerConfig;
    import java.time.LocalDate;
    import java.util.Properties;
    import org.apache.avro.specific.SpecificRecord;
    import org.apache.kafka.clients.CommonClientConfigs;
    import org.apache.kafka.clients.producer.KafkaProducer;
    import org.apache.kafka.clients.producer.ProducerConfig;
    import org.apache.kafka.clients.producer.ProducerRecord;
    import org.apache.kafka.common.config.SaslConfigs;
    import org.apache.kafka.common.config.SslConfigs;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;

    public class TestProducer implements Runnable {
        private static final Logger LOG = LoggerFactory.getLogger(TestProducer.class);

        // Producer values
        private static final String TOPIC = "test";
        private static final String EB_BOOTSTRAP_SERVERS = System.getenv("EB_BOOTSTRAP_SERVERS");
        private static final String EB_SECURITY_PROTOCOL = System.getenv("EB_SECURITY_PROTOCOL");
        private static final String SCHEMA_REGISTRY_URL = System.getenv("SCHEMA_REGISTRY_URL");
        private static final String AWS_ROLE = System.getenv("AWS_ROLE");

        private final KafkaProducer<Long, SpecificRecord> producer;

        public TestProducer() {
            this.producer = createProducer();
        }

        @Override
        public void run() {
            try {
                var sequenceNumber = 0;
                while (true) {
                    sequenceNumber++;
                    // The messages in the topic adhere to a User schema
                    var user = User.newBuilder()
                            .setName("Newbie")
                            .setCompany("Ad Hoc")
                            .setDateOfBirth(LocalDate.of(2000,7,26))
                            .setSequenceNumber(sequenceNumber)
                            .build();

                    // Create producer record
                    ProducerRecord<Long, SpecificRecord> producerRecord = new ProducerRecord<>(TOPIC, user);

                    // Send the record to the Kafka topic
                    producer.send(producerRecord);
                    Thread.sleep(1000);
                }
            } catch (final Exception e) {
                LOG.error("An exception occurred while producing messages", e);
            } finally {
                producer.close();
            }
        }

        private KafkaProducer<Long, SpecificRecord> createProducer() {
            final Properties props = new Properties();

            props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, EB_BOOTSTRAP_SERVERS);
            props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, KafkaAvroSerializer.class.getName());
            props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, KafkaAvroSerializer.class.getName());
            props.put(KafkaAvroSerializerConfig.SCHEMA_REGISTRY_URL_CONFIG, SCHEMA_REGISTRY_URL);
            props.put(KafkaAvroSerializerConfig.AUTO_REGISTER_SCHEMAS, false);
            producerProps.put(KafkaAvroSerializerConfig.USE_LATEST_VERSION, true);
            props.put(ProducerConfig.ENABLE_IDEMPOTENCE_CONFIG, false);
            // * See note below about SCHEMA_ID_FROM_EB
            props.put(ProducerConfig.USE_SCHEMA_ID, <SCHEMA_ID_FROM_EB>); 

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

            return new KafkaProducer<>(props);
        }
    }
    ```
    *`SCHEMA_ID_FROM_EB`: Schema ID is an integer ID assigned by the Schema Registry.
    The Event Bus Team will provide you this value.  Reach out to them when you are ready.

??? example "Ruby Producer"
    ```ruby
    require 'logger'
    require 'rdkafka'
    require 'avro_turf/messaging'
    require_relative 'oauth_token_refresher'

    logger = Logger.new(STDOUT)

    @producers = {}

    def refresh_token(_config, producer_name)
        producer = @producers[producer_name]
        OAuthTokenRefresher.new.refresh_token(producer)
    end

    security_protocol = ENV['SECURITY_PROTOCOL']

    properties = {
        'bootstrap.servers': ENV['KAFKA_HOST'],
        'security.protocol': security_protocol,
        'enable.idempotence': false
    }

    if 'SASL_SSL' == security_protocol.upcase
        properties['sasl.mechanisms'] = 'OAUTHBEARER'
        Rdkafka::Config.oauthbearer_token_refresh_callback = method(:refresh_token)
    end

    producer = Rdkafka::Config.new(properties).producer(native_kafka_auto_start: false)
    @producers[producer.name] = producer
    producer.start

    avro = AvroTurf::Messaging.new(registry_url: ENV['SCHEMA_REGISTRY_URL'], registry_path_prefix: ENV['SCHEMA_REGISTRY_PATH_PREFIX'])

    logger.info "Running producer"
    while true do
        payload = avro.encode({"name"=>"John Smith", "appointment_time"=>"#{DateTime.now}"}, subject: 'appointments-value', version: 1)
        delivery_handle = producer.produce(topic: "appointments", payload: payload)
        delivery_handle.wait
        sleep 15
    end
    ```

### **Register with CODE VA**

[CODE VA (must be on VA network to view)](https://code.va.gov/) is a software catalog that houses information about software entities from across VA. Once you have your producer application up and running, it's important to register with the catalog to ensure that both current and future consumers can discover your event and access its details.

In Backstage, entities represent software components or resources that share a common data shape and semantics. While there are several built-in entities, we have specifically created a custom entity called "Event" for the Event Bus.

To register your event with CODE VA:

1. Create a file named `catalog-info.yaml` at the root of your source code repository.
2. Populate the `catalog-info.yaml` file with an `Event` Backstage entity based on the template below.
3. Once your `catalog-info.yaml` file has been committed it will be automatically processed and the event will be viewable on [CODE VA (must be on the VA network to view)](https://code.va.gov/) within a few hours. If you would like the event to display quicker, follow the [Backstage documentation on the default method for adding entries to the catalog](https://backstage.io/docs/features/software-catalog/#adding-components-to-the-catalog).

#### **Event Template**

``` { .yaml .copy }
apiVersion: backstage.io/v1alpha1
kind: Event
metadata:
    name: event-name
    description: Event description.
    title: Event Name
    links:
    - url: https://sample-slack-link.com
        title: Event Producer Slack Channel
    - url: https://sample-link.com
        title: Event Documentation
spec:
    type: event
    lifecycle: production
    domain: health
    sourceSystems:
    - systemName: Source System Name
        teamName: Source System Owning Team
        productOwner: Source System Product Owner
    topics:
    - topic: topic_name
        environment: development
    - topic: topic_name
        environment: production
    forwarders:
    - systemName: Forwarding System
        teamName: Forwarding System Owning Team
    retention: 20
        
```

Here is some additional information on the individual fields:

* **apiVersion** [required]: This value must be set to `backstage.io/v1alpha1`.
* **kind** [required]: This value must be set to `Event`.
* **metadata** [required]: A structure that contains information about the entity itself. The `metadata` structure includes the following properties.
    * **name** [required]: A machine-readable name for the event. This value will be used in CODE VA urls, so it should be all lowercase and use hyphens as separators.    
    * **description** [required]: A concise, high-level description of the event and the data it provides.
    * **title** [required]: A human-readable representation of the `name` to be used in CODE VA user interfaces.
    * **links** [optional]: A list of links related to the event. Each link consists of a `url` and a `title`.
        * **url** [required]: The external url that will be opened when the link is clicked.
        * **title** [required]: Display text for the link.
* **spec** [required]: A structure that contains information about the event a producer will be emitting. The `spec` structure includes the following properties.
    * **type** [required]: This value must be set to `event`.
    * **lifecycle** [required]: The current development status for the event. This value must be set to: `experimental`, `development`, `production`, or `deprecated`.
    * **removalDate** [optional]: This property should only be set if `lifecycle` is set to `deprecated`. This property specifies the date that a deprecated event will be removed.
    * **domain** [required]: The VA domain in which a particular event exists. Possible values might be: `claims status`, `health`, `appointments`, `benefits`, etc.
    * **sourceSystems** [required]: An array of objects that contain information about the sources of this event. Each source system will contain the following fields.
        * **systemName** [required]: The name of the system that sources this event.
        * **teamName** [required]: The name of the team that owns this system.
        * **productOwner** [required]: OCTODE/VA PO embedded on the team that owns this system.
    * **topics** [required]: An array of objects that contain information about the Kafka topics these events will be published to. The example above shows a topic for the development and production environments. Each topic will contain the following fields.
        * **topic** [required]: The name of the topic.
        * **environment** [required]: The environment this topic is available in. This value must be set to `development` or `production`.
    * **forwarders** [optional]: An array of objects that contain information about systems that forward this event. This property should be used if there is a system sitting in between the source data store and the Event Bus that mutates data before an event is published. Each forwarder will contain the following fields.
        * **systemName** [required]: The name of the system that forwards this event.
        * **teamName** [required]: The name of the team that owns this forwarding system.
    * **retention** [optional]: This value represents the number of days that each event is retained for. It should be set to an integer. This property only needs to be set if your topic has a custom retention policy. If it is not set, the default of 7 days will be displayed.

The `catalog.yaml` file will be validated against [this JSON schema (must be part of VA GitHub organization to view)](https://github.com/department-of-veterans-affairs/ves-event-bus-backstage-plugins/blob/main/plugins/event-kind-backend/src/schema/Event.schema.json). The required `spec.schema`, `spec.schemaCompatibilityMode`, and `spec.topics.brokerAddresses` fields included in this JSON schema will be auto-populated and should not be included in the `catalog-info.yaml` file. The optional `spec.averageDailyEvents` field will also be auto-populated and should not be included in the `catalog-info.yaml` file.

## **Schema Evolution**

Eventually the schema of an event may evolve. After a new version of the schema is added to the schema registry, consumers will need to update their applications to handle the new schema version before producers update to produce events using the new schema. The Event Bus team will coordinate these updates with producers and consumers.

## **Logs**

Logs are stored within a LightHouse Delivery Infrastructure (LHDI) AWS S3 bucket. Only LHDI admins with AWS access can access this bucket and its content. Although producers and consumers will not have access to the S3 bucket directly, logs are available via [LHDI's Datadog instance (must have VA LightHouseDI DataDog access to view)](https://lighthousedi.ddog-gov.com/).

Datadog is a monitoring and analytics tool that is used within the VA. LHDI team members are admins within the Datadog space where the Event Bus metrics and logs are available. To request access to Datadog, complete the HelpDesk form on the ServiceNow Portal at [ECC (Enterprise Command Center) Monitoring Services - your IT Service Portal (must be on the VA network to view)](https://gcc02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fyourit.va.gov%2Fva%3Fid%3Dsc_cat_item%26sys_id%3D4cdf488b1ba4fcd412979796bc4bcb74&data=05%7C01%7C%7Ccb701e4e7fc944b6041308dbeacea9aa%7Ce95f1b23abaf45ee821db7ab251ab3bf%7C0%7C0%7C638361945550254440%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=sJfq3j8vnXwdtuQrfY%2FBaRttaqyOpKA6X17O8TMK9ug%3D&reserved=0).

## **Troubleshooting**

If you have questions or run into difficulties with any of these steps, please [contact the Enterprise Event Bus Team](get-support.md).
