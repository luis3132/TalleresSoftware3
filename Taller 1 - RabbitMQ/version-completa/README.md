# Versión de Consumidor y Productor en Java con Docker-Compose

**Levantar la infraestructura deseada:**  
* **(CASO 1) 1 broker, 1 consumidor, 1 productor:**  
  Ejecutar: `docker-compose -f broker-consumer-producer-[java].yml up -d`  
* **(CASO 2) 1 broker, 2 consumidores, 2 produtores:**  
  Ejecutar: `docker-compose -f broker-consumer[2]-producer[2]-[java].yml up -d`  

**Nota:**  
* No levantar ambas infraestructuras (Conflictos de nombres y puertos). Si desea probar la otra usar el comando `down` primero.

**(CASO 1) Acceder a los contenedores:**  
* Broker: http://localhost:15672/  
* Productor: http://localhost:8081/publish/{message}  
* Consumidor: http://localhost:8082/consumed/messages

**(CASO 2) Acceder a los contenedores:**  
* Broker: http://localhost:15672/  
* Productor-1: http://localhost:8081/publish/{message}
* Productor-2: http://localhost:8082/publish/{message}  
* Consumidor-1: http://localhost:8083/consumed/messages
* Consumidor-2: http://localhost:8084/consumed/messages

**Nota:**  
* Se deben recargar los Consumidores para ver los nuevos mensajes recibidos.  
* Cuando hay más de un Consumidor los mensajes siguen el Round-Robin-Protocol (Se turnaran para recibir los mensajes).
