package task

import (
	"github.com/godatastructure/conductor/task"
)

// Implementation for "task_1"
func Task_1_Execution_Function(t *task.Task) (taskResult *task.TaskResult, err error) {
	LOG.Infof("Executing Task_1_Execution_Function for %s", t.TaskType)

	//user := new(model.User)
	//user.Age = 88
	//user.Name = "sadlfjlds"
	//model.DBOrm.Insert(user)

	taskResult = task.NewTaskResult(t)

	output := map[string]interface{}{"task":"task_1", "name": ""}
	taskResult.OutputData = output
	taskResult.Status = task.COMPLETED
	err = nil
	taskResult.AppendToLogs("nice")
	panic("some error panic")
	return taskResult, err
}
