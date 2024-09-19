# Versión de Consumidor y Productor en Java con Docker-Compose

**Levantar la infraestructura deseada:**  
* **(CASO 1 - JAVA) 1 broker, 1 consumidor, 1 productor:**  
  Ejecutar: `docker-compose -f broker-consumer-producer-[java].yml up -d`
* **(CASO 1 - PYTHON) 1 broker, 1 consumidor, 1 productor:**  
  Ejecutar: `docker-compose -f broker-consumer-producer-[python].yml up -d`
* **(CASO 2 - JAVA) 1 broker, 2 consumidores, 2 produtores:**  
  Ejecutar: `docker-compose -f broker-consumer[2]-producer[2]-[java].yml up -d`
* **(CASO 2 - PYTHON) 1 broker, 2 consumidores, 2 produtores:**  
  Ejecutar: `docker-compose -f broker-consumer[2]-producer[2]-[python].yml up -d`
* **(CASO 3 - JAVA+PYTHON) 1 broker, 2 consumidores, 2 produtores:**  
  Ejecutar: `docker-compose -f broker-consumer[2]-producer[2]-[java-python].yml up -d`

**Nota:**  
* Usar una version de docker compose actualizada (minimo v2)
* No levantar más de una infraestructura en simultaneo (Conflictos de nombres y puertos). Si desea probar otra usar el comando `down` primero.

**(CASO 1) Acceder a los contenedores:**  
* Broker: http://localhost:15672/  
* Productor: http://localhost:8081/publish/{message}  
* Consumidor: http://localhost:8082/consumed/messages

**(CASO 2-3) Acceder a los contenedores:**  
* Broker: http://localhost:15672/  
* Productor-1: http://localhost:8081/publish/{message}
* Productor-2: http://localhost:8082/publish/{message}  
* Consumidor-1: http://localhost:8083/consumed/messages
* Consumidor-2: http://localhost:8084/consumed/messages

**Nota:**  
* Se deben recargar los Consumidores para ver los nuevos mensajes recibidos.  
* Cuando hay más de un Consumidor los mensajes siguen el Round-Robin-Protocol (Se turnaran para recibir los mensajes).

**(CASO 4) Inicializar contenedores en maquinas independientes:**  
* **Máquina Broker:**  
`docker run --name broker-1 -e BROKER_NAME=localhost -e QUEUE_NAME=cola1 -p5672:5672 -p15672:15672 -d rabbitmq:management`  
`docker exec broker-1 /bin/bash -c 'rabbitmqadmin -u guest -p guest -H ${BROKER_NAME} -P 15672 declare queue name=${QUEUE_NAME} durable=true'`  
* **Máquina Productor (JAVA):**  
`docker build -t java-producer .producer`  
`docker run --name java-producer-1 -e BROKER_NAME=host -e QUEUE_NAME=cola1 -p8081:8081 -d java-producer`  
* **Máquina Consumidor (JAVA):**  
`docker build -t java-consumer .consumer`  
`docker run --name java-consumer-1 -e BROKER_NAME=host -e QUEUE_NAME=cola1 -p8082:8082 -d java-consumer`
* **Máquina Productor (PYTHON):**  
`docker build -t python-producer .producer-py`  
`docker run --name python-producer-1 -e BROKER_NAME=host -e QUEUE_NAME=cola1 -p8081:8081 -d python-producer`  
* **Máquina Consumidor (PYTHON):**  
`docker build -t python-consumer .consumer-py`  
`docker run --name python-consumer-1 -e BROKER_NAME=host -e QUEUE_NAME=cola1 -p8082:8082 -d python-consumer`

**Nota:**  
* La variable de entorno `BROKER_NAME` tanto del Consumidor como del Productor debe ser reemplazada por la `ip` de la `Máquina Broker`.
