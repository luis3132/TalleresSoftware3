package com.rabbitmq.consumer;

import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.stereotype.Component;

@Component
public class ConsumerService
{
    private final StringBuilder builder;
    public ConsumerService()
    {
        String info = "[Java-Spring] no messages for now";
        builder = new StringBuilder(info).append("<br>");
    }

    @RabbitListener(queues = { "${queue.name}" })
    public void consume(@Payload String message)
    {
        String info = "[Java-Spring] message consumed = \""+ message + "\"";
        builder.append(info).append("<br>");
    }

    public String getInfo() { return builder.toString(); }
}