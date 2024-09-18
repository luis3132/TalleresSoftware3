#!/bin/bash
set -e

if [-z "$1"]; then
	echo "Error: No queue name provided."
	echo "Usage: $0 <queue_name>"
	exit 1
fi

until curl -s -f -u guest:guest http://localhost:15672/api/overview > /dev/null; do
	echo "Waiting for RabbitMQ to be available..."
	sleep 1
done
echo "RabbitMQ is now available."

curl -u guest:guest -H "Content-Type: application/json" -X PUT -d '{"durable":true}' http://localhost:15672/api/queues/%2f/$1
echo "The queue \"$1\" was created successfully."
