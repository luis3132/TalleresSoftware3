#!/bin/bash
set -e
curl -u guest:guest -H "Content-Type: application/json" -X PUT -d '{"durable":true}' http://localhost:15672/api/queues/%2f/cola1
echo "done"
