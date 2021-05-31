package com.mhc.conductor.test1;

import com.netflix.conductor.client.automator.TaskRunnerConfigurer;
import com.netflix.conductor.client.http.TaskClient;
import com.netflix.conductor.client.worker.Worker;

import java.util.Arrays;

public class Main {

    public static void main(String[] args){

        TaskClient taskClient = new TaskClient();
        taskClient.setRootURI("http://39.105.162.171:8080/api/");
        int threadCount = 2;

        Worker worker1 = new M1Worker();
        Worker worker2 = new M2Worker();

        TaskRunnerConfigurer configurer = new TaskRunnerConfigurer.Builder(
                taskClient,
                Arrays.asList(worker1, worker2)
        ).withThreadCount(threadCount).build();
        configurer.init();
    }

}
