// Copyright 2017 Netflix, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
package task

import (
	"github.com/godatastructure/conductor/task"
	"go-worker/model"
)

// Implementation for "task_2"
func Task_2_Execution_Function(t *task.Task) (taskResult *task.TaskResult, err error) {
	LOG.Infof("Executing Task_2_Execution_Function for %s", t.TaskType)

	user := new(model.User)
	user.Id = 5

	model.DBOrm.Read(user)
	//Do some logic
	taskResult = task.NewTaskResult(t)

	output := map[string]interface{}{"task":"task_2", "name":user.Name, "key3":3, "key4":false}
	taskResult.OutputData = output
	taskResult.Status = "COMPLETED"
	err = nil

	return taskResult, err
}
