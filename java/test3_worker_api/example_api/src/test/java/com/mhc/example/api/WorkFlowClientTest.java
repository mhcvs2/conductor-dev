package com.mhc.example.api;

import com.mhc.example.common.utils.PrintUtil;
import com.netflix.conductor.client.http.WorkflowClient;
import com.netflix.conductor.common.run.Workflow;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import java.util.List;

@RunWith(SpringRunner.class)
@SpringBootTest
public class WorkFlowClientTest {

    @Autowired
    WorkflowClient workflowClient;

    @Test
    public void  testGetWorkflow(){
        Workflow workflow = workflowClient.getWorkflow("0d8e55fc-758b-43a3-90ec-452686907603", false);
        PrintUtil.print(workflow.toString());
    }
//    kitchensink.1/0d8e55fc-758b-43a3-90ec-452686907603.RUNNING

    @Test
    public void testGetRunningWorkflow(){
        List<String> workFlowIds = workflowClient.getRunningWorkflow("kitchensink", 1);
        workFlowIds.forEach(PrintUtil::print);
    }
//    0d8e55fc-758b-43a3-90ec-452686907603
}
