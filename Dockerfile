FROM python:3.8

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY run.sh kafka_consumer.py kafka_producer.py settings.py ./

RUN chmod +x ./run.sh

CMD ["bash", "/run.sh"]