FROM python:3.11

WORKDIR /app

COPY producer.py .

RUN pip install --no-cache-dir Flask==2.3.3 pika==1.3.1

EXPOSE 8081

CMD ["python", "/app/producer.py"]
