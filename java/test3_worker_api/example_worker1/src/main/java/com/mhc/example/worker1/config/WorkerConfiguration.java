package com.mhc.example.worker1.config;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@MapperScan(value = "com.mhc.example.worker1.mapper")
@ComponentScan(value = "com.mhc.example.common")
public class WorkerConfiguration {
}
