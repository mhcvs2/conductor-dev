package com.mhc.example.worker1.mapper;

import com.mhc.example.worker1.model.User;
import org.springframework.stereotype.Component;

@Component
public interface UserMapper {
    int insert(User record);

    int insertSelective(User record);
}