FROM rabbitmq:management

ENV QUEUE_NAME=cola1

WORKDIR /app

COPY create-queue.sh .

RUN chmod +x /app/create-queue.sh

CMD ["/bin/bash", "/app/create-queue.sh"]

EXPOSE 5672
EXPOSE 15672