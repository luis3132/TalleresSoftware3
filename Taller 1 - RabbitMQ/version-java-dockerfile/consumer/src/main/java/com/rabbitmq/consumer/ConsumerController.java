package com.rabbitmq.consumer;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
public class ConsumerController
{
    @Autowired private ConsumerService consumer;

    @GetMapping("consumed/messages")
    public String consumedMessages()
    {
        return consumer.getInfo();
    }
}