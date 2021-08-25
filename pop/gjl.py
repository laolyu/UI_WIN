# -*- coding: UTF-8 -*-
import subprocess
import threading

from lackey import *
import datetime
import os
import sys

def haode():
    t = time.strftime("%H:%M:%S")
    print(t, ':**************Virus removal***************', end=',')
    type(Key.F11)
    wait(0.2)
    click("haode.png")
    wait(0.2)


def yunxu():
    t = time.strftime("%H:%M:%S")
    print(t, '-->>allow', end=',')
    type(Key.F11)
    wait(0.2)
    click("yunxu.png")
    wait(0.2)

def UI():
    t = threading.Timer(60, UI)
    t.setDaemon(True)
    t.start()
    try:
        if exists("yunxu.png", 10):
            yunxu()
        elif exists("haode.png", 10):
            haode()
        else:
            pass
            # print 'no safe messages'
    except Exception as e:
        print('UI-error:', e)

def setTime2Y():
    date=(datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d %H:%M:%S")
    time = '10.0.0'
    os.system('date {} && time {}'.format(date,time))

def setTime2N():
    date=(datetime.datetime.now()+datetime.timedelta(days=0)).strftime("%Y-%m-%d %H:%M:%S")
    time = '21.0.0'
    os.system('date {} && time {}'.format(date,time))

def setTime2T():
    date=(datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    time = '10.0.0'
    os.system('date {} && time {}'.format(date,time))

def m():
    setTime2Y()
    subprocess.check_call('C:\liangdamou\package\clouds_setup_v1.0.1.9_da_1.exe -wjm',shell=True)
    subprocess.check_call('start updc.exe', cwd=r'C:\Users\Administrator\AppData\Local\CloudsToolbar', shell=True)
    # os.system("C:\liangdamou\script\mgjl.bat");








for x in range(2):
    a=Location(182, 4);click(a)
    wait(0.5);type(Key.F5);wait(1)


setTimeToTomorrow()





setTimeToTomorrow()
for x in range(1):
    os.system("C:\liangdamou\script\mgjl.bat");
    wait(150)
    os.system('taskkill /F /IM clouds.exe')

try:
    click(Pattern("1585130091138.png").targetOffset(12,3))
except:
    wait(0.1)

wait(1);type(Key.F11);wait(1)
os.system('taskkill /F /IM Gjlground.exe') #mini
os.system('taskkill /F /IM superb.exe') #tpop
wait(1);type(Key.F11);wait(1)
os.system('taskkill /F /IM stitch.exe') #tips
os.system('taskkill /F /IM humidity.exe') #tnews
os.system('taskkill /F /IM iexplore.exe')



for x in range(2):
    os.system("C:\liangdamou\script\city.bat");wait(1)
setTimeToTomorrow()
for x in range(2):
    os.system("C:\liangdamou\script\city.bat");wait(1)
for x in range(1):
    os.system("C:\liangdamou\script\mgjl.bat");wait(150)
    os.system('taskkill /F /IM clouds.exe')

wait(1);type(Key.F11);wait(1)
os.system('taskkill /F /IM Gjlground.exe') #mini
os.system('taskkill /F /IM superb.exe') #tpop
wait(1);type(Key.F11);wait(1)
os.system('taskkill /F /IM stitch.exe') #tips
os.system('taskkill /F /IM humidity.exe') #tnews

os.system('taskkill /F /IM iexplore.exe')
os.system("C:\liangdamou\script\delete.bat")

os.system('taskkill /F /IM Gjlground.exe') #mini
os.system('taskkill /F /IM superb.exe') #tpop
os.system('taskkill /F /IM stitch.exe') #tips
os.system('taskkill /F /IM humidity.exe') #tnews

