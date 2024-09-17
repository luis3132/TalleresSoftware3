# Versión de Consumidor y Productor en Java
Falta usar docker-compose para evitar ingresar tantos comandos manualmente...  

**1. Crear las imagenes de Consumidor y Productor:**  
* En la carpeta **consumer** ejecutar: `docker build -t java-consumer .`
* En la carpeta **producer** ejecutar: `docker build -t java-producer .`

**2. Crear la red de comunicación de los contenedores:**  
`docker network create red-1`

**3. Crear los contenedores que desee:**  
* Crear contenedor de Broker: `docker run --network red-1 --name broker-1 -p5672:5672 -p15672:15672 -d rabbitmq:management`
* Crear contenedor de Productor: `docker run --network red-1 --name java-producer-1 -p8081:8081 -d java-producer`
* Crear contenedor de Consumidor: `docker run --network red-1 --name java-consumer-1 -p8082:8082 -d java-consumer`
**Nota:**  
* Si desea crear más Productores o Consumidores cambiar el nombre y el puerto.
* No es posible crear más Brokers o cambiarle el nombre (Se le llamo "broker-1" en el application.properties)

**4. Configurar la cola de mensajes del Broker:**  
* Entrar a: http://localhost:15672/  
* Iniciar sesión en RabbitMQ:  
user: guest  
pass: guest  

* Ir a la pestaña: [Queues]  
Seleccionar: [Add a new queue]  
Solo ingresar el campo [Name: cola1] (Se le llamo "cola1" en el application.properties)  
Y oprimir el botón: [Add queue]  

**5. Acceder a los contenedores:**  
* Broker: http://localhost:15672/  
* Productor: http://localhost:8081/publish/{message}  
* Consumidor: http://localhost:8082/consumed/messages  
**Nota:**  
* Se debe recargar el Consumidor para ver los nuevos mensajes recibidos.  
* Si crea más de un Consumidor los mensajes seguiran un Round-Robin-Protocol (Se turnaran para recibir los mensajes).
