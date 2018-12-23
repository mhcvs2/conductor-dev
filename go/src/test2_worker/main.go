package main

import (
	"github.com/godatastructure/conductor"
	"test2_worker/task"
)

func main() {
	c := conductor.NewConductorWorker("http://tx2:8080/api", 2, 10000)

	c.Start("task_1", task.Task_1_Execution_Function, false)
	c.Start("task_5", task.Task_2_Execution_Function, true)
}
