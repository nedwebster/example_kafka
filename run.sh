export HOST=kafka
export PORT=9092

sleep 30
python kafka_producer.py
python kafka_consumer.py
