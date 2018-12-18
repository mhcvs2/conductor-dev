package com.mhc.conductor.test2_spring_worker.mapper;

import com.mhc.conductor.test2_spring_worker.model.User;
import org.springframework.stereotype.Component;

@Component
public interface UserMapper {
    int insert(User record);

    int insertSelective(User record);
}