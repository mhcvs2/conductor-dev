package com.mhc.example.api.config;

import com.mhc.example.common.config.ConductorConfig;
import com.netflix.conductor.client.http.MetadataClient;
import com.netflix.conductor.client.http.TaskClient;
import com.netflix.conductor.client.http.WorkflowClient;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan(value = "com.mhc.example.common")
public class ApiConfiguration {

    @Autowired
    ConductorConfig conductorConfig;

    @Bean
    public TaskClient getTaskClient(){
        TaskClient taskClient = new TaskClient();
        taskClient.setRootURI(conductorConfig.getServerUrl());
        return taskClient;
    }

    @Bean
    WorkflowClient getWorkflowClient() {
        WorkflowClient workflowClient = new WorkflowClient();
        workflowClient.setRootURI(conductorConfig.getServerUrl());
        return workflowClient;
    }

    @Bean
    MetadataClient getMetadataClient() {
        MetadataClient metadataClient = new MetadataClient();
        metadataClient.setRootURI(conductorConfig.getServerUrl());
        return metadataClient;
    }

}
