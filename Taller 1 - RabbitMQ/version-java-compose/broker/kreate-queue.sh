#!/bin/bash
set -e
rabbit-server &
until curl -s -f -u guest:guest http://localhost:15672/api/overview > /dev/null; do
	echo "Waiting for RabbitMQ to be available..."
	sleep 1
done
echo "RabbitMQ is now available."
curl -u guest:guest -H "Content-Type: application/json" -X PUT -d '{"durable":true}' http://localhost:15672/api/queues/%2f/cola1
echo 'The queue "cola1" was created successfully.'
wait
