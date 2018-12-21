package com.mhc.example.common.utils;

import java.util.Arrays;

public class PrintUtil {

    public static void print(String ...s){
        StringBuilder sb = new StringBuilder();
        Arrays.stream(s).forEach(sb::append);
        System.out.println(sb.toString());
    }

}
