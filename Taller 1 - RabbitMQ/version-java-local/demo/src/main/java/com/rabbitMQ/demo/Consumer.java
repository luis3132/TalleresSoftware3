package com.rabbitMQ.demo;

import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.stereotype.Component;

@Component
public class Consumer
{
    @RabbitListener(queues = { "${queue.name}" })
    public void consume(@Payload String message)
    {
        String info = "[Java-Spring] message consumed = \""+ message + "\"";
        System.out.println(info);
    }
}
