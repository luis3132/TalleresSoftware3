package com.rabbitmq.producer;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
public class ProducerController
{
    @Autowired private ProducerService producer;

    @GetMapping("/publish/{message}")
    public String publish(@PathVariable String message)
    {
        String info = "[Java-Spring] message published = \""+ message + "\"";
        producer.publish(message);
        System.out.println(info);
        return info;
    }
}