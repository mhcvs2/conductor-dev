package com.mhc.example.worker1.worker;

import com.mhc.example.worker1.model.User;
import com.mhc.example.worker1.service.UserService;
import com.netflix.conductor.client.worker.Worker;
import com.netflix.conductor.common.metadata.tasks.Task;
import com.netflix.conductor.common.metadata.tasks.TaskExecLog;
import com.netflix.conductor.common.metadata.tasks.TaskResult;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class Worker1 implements Worker {

    @Autowired
    UserService userService;

    private String taskDefName = "task_1";

    public String getTaskDefName() {
        return taskDefName;
    }

    public TaskResult execute(Task task) {
        System.out.printf("Executing %s%n", taskDefName);
        User user = new User();
        user.setName("mhc");
        user.setPassword("123");
        user.setPhone("321");
        userService.addUser(user);

        TaskResult result = new TaskResult(task);
        result.log("work nice");
        result.setStatus(TaskResult.Status.COMPLETED);
        String a = "dsfdf";
        Long b = Long.parseLong(a);
        //Register the output of the task
        result.getOutputData().put("outputKey1", "value");
        result.getOutputData().put("oddEven", 1);
        result.getOutputData().put("mod", 4);
        return result;
    }

}
