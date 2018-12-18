package com.mhc.conductor.test2_spring_worker;
import com.mhc.conductor.test2_spring_worker.config.ConductorServerConfig;
import com.netflix.conductor.client.http.TaskClient;
import com.netflix.conductor.client.task.WorkflowTaskCoordinator;
import com.netflix.conductor.client.worker.Worker;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.util.List;

@SpringBootApplication
@MapperScan("com.mhc.conductor.test2_spring_worker.mapper")
public class FlywayApplication implements CommandLineRunner {

    @Autowired
    ConductorServerConfig config;

    @Autowired
    List<Worker> workers;

    public static void main(String[] args) {
        SpringApplication.run(FlywayApplication.class, args);
    }

    @Override
    public void run(String... args) throws Exception {
        TaskClient taskClient = new TaskClient();
        taskClient.setRootURI(config.getServerUrl());
        int threadCount = 2;

        WorkflowTaskCoordinator.Builder builder = new WorkflowTaskCoordinator.Builder();
        WorkflowTaskCoordinator coordinator = builder
                .withWorkers(workers)
                .withThreadCount(threadCount)
                .withTaskClient(taskClient)
                .build();
        coordinator.init();
    }
}

