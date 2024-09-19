FROM python:3.11

WORKDIR /app

COPY consumer.py .

RUN pip install --no-cache-dir Flask==2.3.3 pika==1.3.1

EXPOSE 8082

CMD ["python", "/app/consumer.py"]
