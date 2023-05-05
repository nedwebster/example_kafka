FROM python:3.8

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY docker/producer/run_producer.sh docker/producer/kafka_producer.py settings.py ./

RUN chmod +x ./run_producer.sh

CMD ["bash", "/run_producer.sh"]