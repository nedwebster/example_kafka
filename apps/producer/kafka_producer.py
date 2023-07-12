from settings import HOST, PORT
from confluent_kafka import Producer
from faker import Faker
import json
import time
import logging
import random

# create Faker to fake streaming data
fake = Faker()


# create logger
logging.basicConfig(
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='producer.log',
    filemode='w',
)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# create Kafka Producer
producer = Producer({'bootstrap.servers': f'{HOST}:{PORT}'})
print('Kafka Producer has been initiated...')


# Define error callback function
def receipt(err, msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
        print(message)


def main():
    while True:
        input("press enter to create message\n")
        data = {
           'user_id': fake.random_int(min=20000, max=100000),
           'user_name': fake.name(),
           'user_address': fake.street_address() + ' | ' + fake.city() + ' | ' + fake.country_code(),
           'platform': random.choice(['Mobile', 'Laptop', 'Tablet']),
           'signup_at': str(fake.date_time_this_month())
           }
        message = json.dumps(data)
        producer.poll(1)
        producer.produce('user-tracker', message.encode('utf-8'), callback=receipt)
        producer.flush()


if __name__ == "__main__":
    main()
