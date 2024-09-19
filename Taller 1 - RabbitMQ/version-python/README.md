# Versión de Consumidor y Productor en Python
Al parecer los contenedores funcionan correctamente pero no logro ver nada en el navegador.

`docker network create red-1`  
`docker run --network red-1 --name broker-1 -p5672:5672 -p15672:15672 -d rabbitmq:management`  
`docker run --network red-1 --name python-producer-1 -p8081:8081 -d python-producer`  
`docker run --network red-1 --name python-consumer-1 -p8082:8082 -d python-consumer`  

Se deberian usar estas URLs:  
* Broker: http://localhost:15672/  
* Productor: http://localhost:8081/publish/{message}  
* Consumidor: http://localhost:8082/consumed/messages  