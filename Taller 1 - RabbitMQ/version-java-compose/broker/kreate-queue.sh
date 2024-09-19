#!/bin/sh
rabbitmq-server &
while ! nc -z localhost 15672; do
	echo "Waiting for RabbitMQ..."
	sleep 1
done
rabbitmqadmin -u guest -p guest -H localhost -P 15672 declare queue name=$QUEUE_NAME durable=true
wait
