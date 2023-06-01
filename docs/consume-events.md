---
title: Consume Events
---
# What’s a Consumer?
A consumer is an application that is set up to receive messages or events in an event-driven system. The Event Bus exposes streams of events, called topics, to consumers. The events capture significant occurrences taking place in an external system. A list of currently available topics can be found in our [Event Catalog]. 

To access messages in a particular topic, an event consumer would subscribe to the topic and receive events as they occur in real time. This allows consumers to perform actions based on the event data, such as updating internal state, triggering other processes, etc. Learn more about the components and processes involved in event-based systems on our [Introduction to Event-Driven Architecture](link) page.

## Steps For Becoming a Consumer
### Find Events/Topics to Consume
The first step to consuming an event is to [reach out to the Enterprise Event Bus Team](get-support.md) about your interest in events. From there, you can either subscribe to an existing topic with relevant events, or else identify a team able to provide the topic that is of interest to you. At this point in time, we are unable to identify producers for consumers that do not have a source for their desired events, but we will do our best to work with your chosen producing team. 
See also our [Producer Onboarding](produce-events.md) page.

### Determine If You Need an ESECC Request
Depending on the location of a consumer application, you may need to obtain an ESECC (Enterprise Security External Change Council) request. The diagram below illustrates the relationship between consumer locations and ESECC requirements. It shows that as a general rule, consumers located within the VAEC (VA Enterprise Cloud) AWS Organization do not need to file an ESECC request. For consumers who are in other AWS organizations, or outside of AWS, an ESECC process will likely be needed. If you’re unsure which category your use case fits in, please reach out to the Event Bus Team for help. However, please also note that while the Event Bus Team is happy to give direction and assist with some aspects of the ESECC process, consumers are ultimately responsible for initiating and monitoring the request.

This [example documentation](https://github.com/department-of-veterans-affairs/checkin-devops/blob/master/docs/esecc-requests.md) provides a summary of the steps and processes involved in an ESECC request. Please be sure to get started as early as possible, as this can be a lengthy process.

![Client Environments ESECC Decision Circles](img/Client%20Environments%20ESECC%20Decision%20Circles.svg)
### Set up Authorization and Authentication
To subscribe to specific topics on the Event Bus, consumers need to be authenticated and have the appropriate permissions. The Event Bus MSK cluster is only accessible from the VA Network, and we use AWS IAM (Identity and Access Management) Roles and Policies to control access to different resources. If your consuming application is within the AWS environment, you will need to let us know which IAM Role(s) or IAM User(s) we should grant access to, and set up the applicable IAM Policies on your end.

If your consuming application is outside of the AWS environment, we will request an IAM User to be created on your behalf. You will then be able to access the requested topic(s) using those credentials. 

### Connect to the Event Bus in the Development Environment
Once the authentication and authorization steps have been completed, you will receive the Kafka bootstrap server addresses and port numbers with which you can connect to the Event Bus MSK cluster. The following ports are open for consumers and producers that are authenticated with AWS IAM:
- 9098 (for access from AWS)
- 9198 (for access from outside of AWS).

### Develop and Deploy Your Consumer Application
Many programming languages and frameworks have libraries designed to interact with Kafka clusters. This allows consumer applications to be written in your language of choice. For reference, here is a Python example that consumes events from a topic called “appointments:”

```python
from confluent_kafka import Consumer, KafkaException
from confluent_kafka.admin import AdminClient, NewTopic

# Configuration
bootstrap_servers = 'event_bus_msk_bootstrap_servers' # Replace with the MSK cluster's bootstrap servers
topic_name = 'appointments' # Name of the topic to consume from

# IAM Role and AWS credentials
aws_access_key_id = 'your_aws_access_key_id'
aws_secret_access_key = 'your_aws_secret_access_key'
aws_session_token = 'your_aws_session_token'  # Required for temporary credentials

# Configure the consumer
conf = {
    'bootstrap.servers': bootstrap_servers,
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'AWS_MSK_IAM',
    'sasl.username': aws_access_key_id,
    'sasl.password': aws_secret_access_key,
    'sasl.aws_session_token': aws_session_token,
    'group.id': 'your_consumer_group_id',
    'auto.offset.reset': 'earliest',
}

# Create a Kafka consumer
consumer = Consumer(conf)

# Subscribe to the topic
consumer.subscribe([topic_name])

# Consume events
try:
    while True:
        msg = consumer.poll(1.0)  # Poll for new messages
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaException._PARTITION_EOF:
                # Reached the end of a partition, handle as needed
                continue
            else:
                # Handle other errors
                print('Error occurred: {}'.format(msg.error().str()))
                break

        # Process the consumed event
        print('Received message: {}'.format(msg.value().decode('utf-8')))

except KeyboardInterrupt:
    # Gracefully stop the consumer on keyboard interrupt
    pass

finally:
    # Close the consumer
    consumer.close()
```

### Troubleshooting
If you have questions or run into difficulties with any of these steps, please [contact the Enterprise Event Bus Team](get-support.md).
