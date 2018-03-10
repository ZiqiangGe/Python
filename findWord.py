#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#传入文件夹路径和查找内容,在该文件夹下遍历所有含查找内容的文件,并输出文件路径
#python3 findWord.py /Users/mac/Desktop/java Person

__author__ = "gzq"

import os
import sys

path = '.'
search = "a"
if len(sys.argv)>1:
    path = sys.argv[1]
if len(sys.argv)>2:
    search = sys.argv[2]

def findFile(path):

    for x in os.listdir(path):
        p = os.path.join(path,x)
        if os.path.isdir(p):
            findFile(p)
        else:
            if containKey(p,search) :
                print(p)

def containKey(p,key):
    try:
        f = open(p, 'r')
        if f.read().__contains__(key):
            return True
    except Exception  as e:
        return False
    finally:
        if f:
            f.close()


findFile(path)