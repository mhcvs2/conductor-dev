package com.mhc.conductor.test2_spring_worker.service;

import com.mhc.conductor.test2_spring_worker.mapper.UserMapper;
import com.mhc.conductor.test2_spring_worker.model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserService {

    @Autowired
    UserMapper userMapper;

    public int addUser(User user){
        return userMapper.insert(user);
    }

    public int addUser2(User user) {
        User u = new User();
        u.setPassword(user.getPassword());
        u.setPhone(user.getPhone());
        u.setName(user.getName());
        userMapper.insertSelective(u);
        System.out.println(u.getPassword());
        return u.getId();
    }


}
