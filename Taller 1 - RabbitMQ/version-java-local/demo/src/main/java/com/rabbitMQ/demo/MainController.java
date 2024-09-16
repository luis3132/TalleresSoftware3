package com.rabbitMQ.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
public class MainController
{
    @Autowired private Producer producer;

    @GetMapping("/publish/{message}")
    public String publish(@PathVariable String message)
    {
        String info = "[Java-Spring] message published = \""+ message + "\"";
        producer.publish(message);
        System.out.println(info);
        return info;
    }
}
