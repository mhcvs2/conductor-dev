package com.mhc.conductor.test1;

import com.netflix.conductor.client.http.TaskClient;
import com.netflix.conductor.client.task.WorkflowTaskCoordinator;
import com.netflix.conductor.client.worker.Worker;

public class Main {

    public static void main(String[] args){

        TaskClient taskClient = new TaskClient();
        taskClient.setRootURI("http://tx2:8080/api/");
        int threadCount = 2;

        Worker worker1 = new SampleWorker("task_1");
        Worker worker2 = new SampleWorker("task_5");

        WorkflowTaskCoordinator.Builder builder = new WorkflowTaskCoordinator.Builder();
        WorkflowTaskCoordinator coordinator = builder
                .withWorkers(worker1, worker2)
                .withThreadCount(threadCount)
                .withTaskClient(taskClient)
                .build();
        coordinator.init();
    }

}
