package com.mhc.test.springbootpg;

import com.mhc.test.springbootpg.dao.MetadataDAO;
import com.mhc.test.springbootpg.metadata.TaskDef;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@Slf4j
public class Main implements CommandLineRunner {

    @Autowired
    MetadataDAO dao;

    public static void main(String[] args) {
        SpringApplication.run(Main.class, args);
    }

    @Override
    public void run(String... args) throws Exception {
        log.info("run-------------------------------");
        t2();
        log.info("run end-----------------------");
    }

    void t1(){
        TaskDef tdf = new TaskDef("task2", "test task");
        dao.createTaskDef(tdf);
    }

    void t2() {
        dao.getAllTaskDefs().forEach(taskDef -> log.info(taskDef.getName()));
    }
}
