# Versión de Consumidor y Productor en Java
Solo corre en local, falta dockerizar más...

Si se quiere correr:
1. Ejecutar RabbitMQ en su maquina con:
`docker run -d --restart always --name rabbitmq -p5672:5672 -p15672:15672 rabbitmq:3.9-management`

2. Entrar a: http://localhost:15672/
Iniciar sesión en RabbitMQ:
user: guest
pass: guest

3. Ir a la pestaña: [Queues]
Seleccionar: [Add a new queue]
Solo ingresar el campo [Name: cola1] (Así se le llamo en el application.properties)
Y oprimir el botón: [Add queue]

4. Compilar y correr el proyecto de java: [demo]
Envia un mensaje entrando a: http://localhost:8080/publish/{message}
http://localhost:8080/publish/eso
Enviar el mensaje y ver como en la consola se envía y consume 
