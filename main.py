#!/usr/bin/python
#coding:utf-8
import re
import os

  
if __name__ == "__main__":
    f1 = open('without_module_50_to_70.txt')
    f2 = open('with_module_50_to_70.txt')
    source = f1.read()
    lines = f2.readlines()
    for line in lines:
        str_tmp = line.split()
        r = str_tmp[0]
        s = len(re.findall(r,source))
        if s==0:
            print r, s
    f1.close()
    f2.close()
