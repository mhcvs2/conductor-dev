<pre><code>
getRunningWorkflows --wfName=

 getWorkflow --wfId 
 getTask --taskId
 get_task_logs --taskId
 
 
 
 
 获取c6573d6a-fe5b-4449-932f-a56d29cd8c3b(wf id) 的第一个task的log
  conductor-manager  get_task_logs --taskId `conductor-manager  getWorkflow --wfId c6573d6a-fe5b-4449-932f-a56d29cd8c3b|jq .tasks[0].taskId`
</code></pre>