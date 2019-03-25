#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:xiye
# datetime:2019/3/26 2:47
# software: PyCharm

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()