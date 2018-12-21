package com.mhc.example.worker1.service;

import com.mhc.example.worker1.mapper.UserMapper;
import com.mhc.example.worker1.model.User;
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
