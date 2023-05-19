FROM python:3.8

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY run_consumer.sh kafka_consumer.py settings.py ./

RUN chmod +x ./run_consumer.sh

CMD ["bash", "/run_consumer.sh"]