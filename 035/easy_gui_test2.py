#!/usr/bin/env python
# -*- coding:utf-8 -*-

from easygui import *

# input_msg = enterbox(msg='Enter something.', title=' ', default='', strip=True, image=None, root=None)
# print(input_msg)
#
# list1= ['用户名:', 'full name:', 'telephone:', 'mobile:', 'QQ:', 'E-mail:', '密码:']
# msg = multenterbox(msg='请输入用户名和密码', title='登录', fields=(list1))
# print(msg)
#
# list2= ['用户名:', 'full name:', 'telephone:', 'mobile:', 'QQ:', 'E-mail:', '密码:']
# msg = multpasswordbox(msg='请输入用户名和密码', title='登录', fields=(list2))
# print(msg)

# msg = codebox(msg='', title=' ', text='')
# print(msg)

# diropenbox(msg=None, title=None, default=None)

# fileopenbox(msg=None, title=None, default='/Users/zhengaihua/aa', filetypes="*.txt")

msg = "Enter your personal information"
title = "Credit Card Application"
fieldNames = ["Name","Street Address","City","State","ZipCode"]
fieldValues = []  # we start with blanks for the values
fieldValues = multenterbox(msg,title, fieldNames)

# make sure that none of the fields was left blank
while 1:
    if fieldValues == None: break
    errmsg = ""
    for i in range(len(fieldNames)):
      if fieldValues[i].strip() == "":
        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
    if errmsg == "": break # no problems found
    fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
print("Reply was:", fieldValues)

try:
    someFunction()  # this may raise an exception
except:
    exceptionbox()