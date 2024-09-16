package com.rabbitMQ.demo;

import org.springframework.amqp.rabbit.annotation.EnableRabbit;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
@EnableRabbit
public class Producer
{
    @Autowired private RabbitTemplate rabbitTemplate;
    @Value("${queue.name}") private String queue;

    public void publish(String message)
    {
        rabbitTemplate.convertAndSend(queue, message);
    }
}
