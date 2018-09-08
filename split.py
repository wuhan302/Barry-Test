#!/usr/bin/python
#coding:utf-8
import re
import os

  
if __name__ == "__main__":
    f1 = open('with_module_50_to_70_split.txt', 'w')
    f2 = open('with_module_50_to_70.txt')
    lines = f2.readlines()
    for line in lines:
        str_tmp = line.split()
        r = str_tmp[0]
        if r=='287':
            f1.write(line) 
        elif r=='42A':
            f1.write(line)
        elif r=='364':
            f1.write(line)         
            
    f1.close()
    f2.close()
