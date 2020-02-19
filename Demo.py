#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.01.19
author: wangxiaojie
'''

import os, sys

codePath = os.path.abspath(os.path.join(__file__, "..", "Code"))
if os.path.exists(codePath):
    sys.path.append(codePath)
from EmailSender import *

if __name__ == "__main__":
    attach1 = os.path.abspath(os.path.join(__file__, "../README.md"))
    sendEmail('smtp.qq.com', '***@qq.com', '***', ['***@qq.com', '***@qq.com'], '**<***@qq.com>, **<***@qq.com>', "测试邮件", "这是一封测试邮件", {attach1: "log1"})