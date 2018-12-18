package com.mhc.conductor.test2_spring_worker.worker;

import com.mhc.conductor.test2_spring_worker.model.User;
import com.mhc.conductor.test2_spring_worker.service.UserService;
import com.netflix.conductor.client.worker.Worker;
import com.netflix.conductor.common.metadata.tasks.Task;
import com.netflix.conductor.common.metadata.tasks.TaskResult;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class Worker5 implements Worker {

    @Autowired
    UserService userService;

    private String taskDefName = "task_5";

    public String getTaskDefName() {
        return taskDefName;
    }

    public TaskResult execute(Task task) {
        System.out.printf("Executing %s%n", taskDefName);

        User user = new User();
        user.setName("mhc2");
        user.setPassword("1232");
        user.setPhone("3212");
        userService.addUser(user);

        TaskResult result = new TaskResult(task);
        result.setStatus(TaskResult.Status.COMPLETED);

        //Register the output of the task
        result.getOutputData().put("outputKey5", "value");
        result.getOutputData().put("oddEven", 1);
        result.getOutputData().put("mod", 4);
        return result;
    }

}
