package com.mhc.test.springbootpg.dao;

import com.mhc.test.springbootpg.metadata.TaskDef;
import com.mhc.test.springbootpg.metadata.WorkflowDef;

import java.util.List;
import java.util.Optional;

public interface MetadataDAO {

    /**
     * @param taskDef task definition to be created
     */
    void createTaskDef(TaskDef taskDef);

    /**
     * @param taskDef task definition to be updated.
     * @return name of the task definition
     */
    String updateTaskDef(TaskDef taskDef);

    /**
     * @param name Name of the task
     * @return Task Definition
     */
    TaskDef getTaskDef(String name);

    /**
     * @return All the task definitions
     */
    List<TaskDef> getAllTaskDefs();

    /**
     * @param name Name of the task
     */
    void removeTaskDef(String name);

    /**
     * @param def workflow definition
     */
    void createWorkflowDef(WorkflowDef def);

    /**
     * @param def workflow definition
     */
    void updateWorkflowDef(WorkflowDef def);

    /**
     * @param name Name of the workflow
     * @return Workflow Definition
     */
    Optional<WorkflowDef> getLatestWorkflowDef(String name);

    /**
     * @param name    Name of the workflow
     * @param version version
     * @return workflow definition
     */
    Optional<WorkflowDef> getWorkflowDef(String name, int version);

    /**
     * @param name    Name of the workflow definition to be removed
     * @param version Version of the workflow definition to be removed
     */
    void removeWorkflowDef(String name, Integer version);

    /**
     * @return List of all the workflow definitions
     */
    List<WorkflowDef> getAllWorkflowDefs();
}
