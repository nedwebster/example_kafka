FROM python:3.8

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY run_producer.sh /kafka_producer.py settings.py ./

RUN chmod +x ./run_producer.sh

CMD ["bash", "/run_producer.sh"]