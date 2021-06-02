package com.mhc.test.springbootpg.service;

import com.mhc.test.springbootpg.dao.MetadataDAO;
import com.mhc.test.springbootpg.metadata.TaskDef;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class MetadataService {

    @Autowired
    MetadataDAO metadataDAO;

    public List<TaskDef> getTaskDefs() {
        return metadataDAO.getAllTaskDefs();
    }

}
