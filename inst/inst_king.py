# -*- coding: utf-8 -*-
import datetime
import random
import subprocess
import threading
from mouse import click, wait
from lackey import *
import time
import sys

sys.path.append(r'C:\liangdamou\script\gjl')  # 先加入绝对路径，否则会报错，注意__file__表示的是当前执行文件的路径
from ver_king import version


def install():
    t = time.strftime("%H:%M:%S")
    print(t, '********find install action**********', end=',')
    type(Key.F11)
    wait(0.2)
    click(Pattern("install.png").targetOffset(147, -55))
    wait(0.2)
    click(Pattern("install.png").targetOffset(162, -25))
    wait(0.2)


def sysp():
    t = time.strftime("%H:%M:%S")
    print(t, '*******System protection*******', end=',')
    type(Key.F11)
    wait(0.2)
    click(Pattern("sysp.png").targetOffset(180, 90))
    wait(0.2)


def quanxian():
    t = time.strftime("%H:%M:%S")
    print(t, ':*******find quanxian action..*******', end=',')
    type(Key.F11)
    wait(0.2)
    click(Pattern("quanxian.png").targetOffset(104, 0))
    wait(0.2)
    click(Pattern("quanxian.png").targetOffset(104, 40))
    wait(0.2)


def guanlian():
    t = time.strftime("%H:%M:%S")
    print(t, ':****find guanlian action..*********', end=',')
    type(Key.F11)
    wait(0.2)
    click(Pattern("install.png").targetOffset(70, -55))
    wait(0.2)


def allow():
    t = time.strftime("%H:%M:%S")
    print(t, ':*******allow>>*************', end=',')
    type(Key.F11)
    wait(0.2)
    click("allow.png")
    wait(0.2)


def qinngc():
    t = time.strftime("%H:%M:%S")
    print(t, ':*************Virus removal at once***************', end=',')
    type(Key.F11)
    wait(0.2)
    click("qingchu.png")
    wait(0.2)


def bkq():
    t = time.strftime("%H:%M:%S")
    print(t, ':donnot turn on', end=',')
    type(Key.F11)
    wait(0.2)
    click("bukaiqi.png")
    wait(0.2)
    time.sleep(10)


def UI():
    t = threading.Timer(60, UI)
    t.setDaemon(True)
    t.start()
    try:
        if exists("install.png", 1):
            install()
        elif exists("sysp.png", 1):
            sysp()
        elif exists("quanxian.png", 1):
            quanxian()
        elif exists("qingchu.png", 1):
            qinngc()
        elif exists("guanlian.png", 1):
            guanlian()
        elif exists("allow.png", 1):
            allow()
        elif exists("bukaiqi.png", 1):
            bkq()
        else:
            pass
            # print 'no safe messages'
    except Exception as e:
        print('UI-error:', e)


def cmd_send(project, path, vc_list):
    print('thread %s >>%s is running...' % (threading.current_thread().name, project))
    now = datetime.datetime.now()
    s1 = now.strftime('%Y-%m-%d %H:%M:%S')

    for x in range(len(vc_list)):
        cmd = vc_list[x]
        m = random.randint(20, 60)
        time.sleep(m)
        for i in range(0, 3):
            p = subprocess.Popen(cmd, cwd=path, shell=True)
            try:
                p.communicate(timeout=90)
            except subprocess.TimeoutExpired as e:
                print(e, 'retry', '***********')
                subprocess.call(['taskkill', '/F', '/T', '/PID', str(p.pid)])
                continue
            break
        t = time.strftime("%H:%M:%S")
        print(f'{t}, {project}, {x + 1}, {vc_list[x]}')

    print('thread %s >>%s is ended...' % (threading.current_thread().name, project))
    now = datetime.datetime.now()
    e1 = now.strftime('%Y-%m-%d %H:%M:%S')
    print(f"%s,start time: %s" % (project, s1), end=',')
    print("%s,end time: %s：" % (project, e1), end=',')

    start = datetime.datetime.strptime(s1, '%Y-%m-%d %H:%M:%S')
    end = datetime.datetime.strptime(e1, '%Y-%m-%d %H:%M:%S')
    total = end - start
    if (total.seconds) > 60:
        m = float(total.seconds) / 60
        print("%s,total(min)：%s" % (project, m))
    else:
        m = total.seconds
        print("%s total(s)：%s" % (project, m))


if __name__ == '__main__':
    print('thread %s is running...' % threading.current_thread().name)
    path_0 = r'C:\liangdamou\package\\'
    projects = ['mguangsu', 'lszip', 'mkuai', 'mxiaohei', 'mabc', 'mllq',  'gjl', 'qjpdf','mxiaoyu']
    UI()
    for i in range(len(projects)):
        project = projects[i]
        path = path_0 + project
        vc_list = version(project)
        t = threading.Thread(target=cmd_send, args=(project, path, vc_list), name='LoopThread')
        t.start()
        time.sleep(i * 10)
    print('thread %s is ended...' % threading.current_thread().name)
