package com.mhc.conductor.test1;

import com.netflix.conductor.client.worker.Worker;
import com.netflix.conductor.common.metadata.tasks.Task;
import com.netflix.conductor.common.metadata.tasks.TaskResult;

public class M2Worker implements Worker {

    private String taskDefName = "mhc2";

    public String getTaskDefName() {
        return taskDefName;
    }

    public TaskResult execute(Task task) {
        System.out.printf("Executing %s%n", taskDefName);
        System.out.printf("input m2: %s%n", task.getInputData().get("m2"));
        TaskResult result = new TaskResult(task);
        result.setStatus(TaskResult.Status.COMPLETED);
        //Register the output of the task
        result.getOutputData().put("r2", "from mhc2");
        return result;
    }

}
