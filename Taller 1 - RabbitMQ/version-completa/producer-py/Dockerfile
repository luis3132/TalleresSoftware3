FROM python:3.11

RUN pip install --no-cache-dir Flask==2.3.3 pika==1.3.1

WORKDIR /app

ENV BROKER_NAME=broker-1
ENV QUEUE_NAME=cola1

COPY producer.py .

CMD ["python", "/app/producer.py"]

EXPOSE 8081
