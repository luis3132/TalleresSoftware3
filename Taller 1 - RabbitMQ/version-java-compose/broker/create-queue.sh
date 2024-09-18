#!/bin/bash
set -e

# Espera a que RabbitMQ esté completamente disponible
until curl -s -f -u guest:guest http://localhost:15672/api/overview > /dev/null; do
  echo "Waiting for RabbitMQ to be available..."
  sleep 1
done

# Ejecuta el script de creación de colas
curl -u guest:guest -H "Content-Type: application/json" -X PUT -d '{"durable":true}' http://localhost:15672/api/queues/%2f/cola1