#!/bin/bash
set -e
until curl -s -f -u guest:guest http://localhost:15672/api/overview > /dev/null; do
	echo "waiting..."
	sleep 1
done
curl -u guest:guest -H "Content-Type: application/json" -X PUT -d '{"durable":true}' http://localhost:15672/api/queues/%2f/cola1
echo "done"
