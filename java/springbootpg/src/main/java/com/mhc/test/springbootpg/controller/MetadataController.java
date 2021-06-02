package com.mhc.test.springbootpg.controller;

import com.mhc.test.springbootpg.metadata.TaskDef;
import com.mhc.test.springbootpg.service.MetadataService;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@Api(tags = "metadata manage")
@RestController
@RequestMapping(value = "/api/metadata")
public class MetadataController {

    @Autowired
    MetadataService metadataService;

    @ApiOperation(value = "get task def")
    @GetMapping("/taskdefs")
    public List<TaskDef> getTaskDefs(){
        return metadataService.getTaskDefs();
    }

}
