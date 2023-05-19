from settings import HOST, PORT
from confluent_kafka import Consumer


consumer = Consumer({
    'bootstrap.servers': f'{HOST}:{PORT}',
    'group.id': 'python-consumer',
    'auto.offset.reset': 'earliest'
})
print('Kafka Consumer has been initiated...')


print('Available topics to consume: ', consumer.list_topics().topics)
print('Subscribing to producer "user-tracker"...')
consumer.subscribe(['user-tracker'])
print('Successfully subscribed to "user-tracker"')


def main():
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data = msg.value().decode('utf-8')
        print(data)
    consumer.close()


if __name__ == "__main__":
    main()
