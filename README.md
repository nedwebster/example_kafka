# Guide

## Running the Kafka Broker
To run the kafka broker, use the following command:
```
docker-compose up --force-recreate
```

This will start the kafka broker in a docker container.


## Running the consumer/producer

(Note: All steps here are the same for the producer and consumer, just modify the code with the appropriate name)

First, navigate to the following directory
```
./apps/consumer/
```

To run the consumer locally, simply run the following command:

```
python kafka_consumer.py
```

To run the consumer within a docker container, first build the image by running:

```
docker build --platform linux/amd64 -t test-consumer .
```

Then run the consumer in a docker container using:
```
docker run --platform linux/amd64 --network=kafka_docker_example_net -e PYTHONUNBUFFERED=1 test-consumer 
```
