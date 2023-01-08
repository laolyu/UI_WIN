# -*- coding: UTF-8 -*-
import os
import sys
from lackey import *
import datetime
import time
from config import *

sys.path.append(r'C:\AI\script\gjl')


def UI():
    time.sleep(10)
    try:
        if exists("install.png", 1):
            """
            检查安装弹窗是否存在
            """
            wait(1)
            click(Pattern("install.png").targetOffset(422, 126))
            wait(1)
            click(Pattern("install.png").targetOffset(422, 150))
        if exists("procp.png", 1):
            type(Key.F11)
            wait(0.1)
            click(Pattern("procp.png").targetOffset(116, 124))  # no mention188*320
            wait(0.1)
            click(Pattern("procp.png").targetOffset(326, 124))
            wait(0.1)
        if exists("bingdu.png", 1):
            """
            检查报毒弹窗是否存在
            """
            print('*********发现病毒弹窗***********')
            type(Key.F11)
            wait(1)
            click(Pattern("bingdu.png").targetOffset(159, -21))
        if exists("reg.png", 1):
            print('')
            type(Key.F11)
            wait(0.1)
            click(Pattern("reg.png").targetOffset(116, 150))  # no mention188*370
            wait(0.1)
            click(Pattern("reg.png").targetOffset(478, 150))  # ^-188*370
            wait(0.1)
            click(Pattern("reg.png").targetOffset(478, 230))
            wait(0.1)
    except Exception as e:
        print(e)


def inst(package):
    try:
        os.popen('net use \\172.18.15.3 "2020"  /user:"administrator"')
        os.popen(r'net time \\172.18.15.3 /set /y')
        UI()
        time.sleep(5)
        date = (datetime.datetime.now() + datetime.timedelta(days=-3)).strftime("%Y-%m-%d %H:%M:%S")
        t = '06.00.00'
        os.popen(f'date {date} && time {t}')
        UI()
        time.sleep(5)
    except Exception as e:
        print(e)
    try:
        t = time.strftime("%H:%M:%S")
        print(t, package)
        os.popen(package)
        UI()
    except Exception as e:
        time.sleep(30)
        print(e)
    time.sleep(10)


def setTime2M():
    try:
        os.popen(r'net use \\172.18.15.3 "2020"  /user:"administrator"')
        os.popen(r'net time \\172.18.15.3 /set /y')
        UI()
        time.sleep(5)
    except Exception as e:
        print(e)


def kill_p(p_list, updc):
    updc_proc = updc.split('/')[-1]
    p_list.append(updc_proc)
    type(Key.F11)
    wait(1)
    for i in range(len(p_list)):
        name = p_list[i]
        os.popen('taskkill /F /IM %s.exe' % name)
        time.sleep(2)
    print('杀掉弹窗进程, successed')


def pb():
    pb_list = ['bqpb', 'xypbuninst', 'Kuaipb', 'parpbuninst', 'ktpb', 'ktpbuninst', 'pbxhone', 'xhpbuninst',
               'GSscreensaver', 'sspbuninst', '7654pb']
    try:
        os.popen(
            '@reg add "HKEY_CURRENT_USER\Software\ScreenSaver" /v "ScreenSaveTimeOut" /t REG_DWORD /d "15" /f>nul')
    except Exception as e:
        print(e)
    time.sleep(30)
    type(Key.F11)
    wait(1)
    for i in range(len(pb_list)):
        os.popen('taskkill /F /IM %s.exe' % pb_list[i])
        time.sleep(2)
    print('杀掉pb进程, successed')


def b4hand(project, package, updc, p_list):
    inst(package)
    UI()
    try:
        print('*****city.bat********')
        os.popen("C:\AI\script\city.bat")
    except Exception as e:
        print(e)
    setTime2M()
    try:
        os.popen(f'{updc}.exe')
        print('**点击updc*')
    except Exception as e:
        print(e)
    time.sleep(10)
    try:
        os.popen(f'{updc}.exe')
        print('**点击updc*')
    except Exception as e:
        print(e)
    time.sleep(180)

    if project in [xiaoyu, kuaizip, kantu, heinote, finder, browser]:
        pb()
    try:
        kill_p(p_list, updc)
    except Exception as e:
        print(e)
    try:
        print('delete.bat')
        os.popen("C:\AI\script\delete.bat")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    keyDown(Key.WIN)
    type("d")
    wait(1)
    keyUp(Key.WIN)
    # 隐藏窗口防止影响运行
    now = int(time.time())
    log_file = open(os.path.join('C:/AI/log/', '%s.txt') % now, "w")
    sys.stdout = log_file
    projects = [xiaoyu, kuaizip, kantu, heinote, finder, browser, lszip, xinnote, qjpdf, cloudbar, haotu, xxbz, sesame,
                jcbz]
    for i in range(len(projects)):
        project = projects[i]
        package = project['package']
        updc = project['updc']
        p_list = project['p_list']
        b4hand(project, package, updc, p_list)
    log_file.close()
