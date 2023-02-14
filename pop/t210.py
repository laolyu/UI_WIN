# coding:utf-8
import os

try:
    print('delete.bat')
    os.popen("C:\AI\script\delete.bat")
except Exception as e:
    print(e)
