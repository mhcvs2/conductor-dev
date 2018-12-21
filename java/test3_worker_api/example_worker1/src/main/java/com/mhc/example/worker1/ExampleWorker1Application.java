package com.mhc.example.worker1;

import com.mhc.example.common.config.ConductorConfig;
import com.netflix.conductor.client.http.TaskClient;
import com.netflix.conductor.client.task.WorkflowTaskCoordinator;
import com.netflix.conductor.client.worker.Worker;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.util.List;

@SpringBootApplication
public class ExampleWorker1Application implements CommandLineRunner {

    @Autowired
    ConductorConfig config;

    @Autowired
    List<Worker> workers;

    public static void main(String[] args) {
        SpringApplication.run(ExampleWorker1Application.class, args);
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
