package com.mhc.conductor.test1;

import com.netflix.conductor.client.worker.Worker;
import com.netflix.conductor.common.metadata.tasks.Task;
import com.netflix.conductor.common.metadata.tasks.TaskResult;

import java.util.HashMap;
import java.util.LinkedHashMap;

public class M1Worker implements Worker {

    private String taskDefName = "mhc1";

    public String getTaskDefName() {
        return taskDefName;
    }

    public TaskResult execute(Task task) {
        System.out.printf("Executing %s%n", taskDefName);
        System.out.printf("input m1: %s%n", task.getInputData().get("m1"));
        TaskResult result = new TaskResult(task);
        result.setStatus(TaskResult.Status.COMPLETED);
        //Register the output of the task
        result.getOutputData().put("r1", "from mhc1");
        return result;
    }

}
