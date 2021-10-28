# -*- coding: utf-8 -*-
import datetime
import random
import subprocess
import threading
from lackey import *
import time
import sys

Settings.InfoLogs = False
sys.path.append(r'C:\liangdamou\script\gjl')  # 先加入绝对路径，否则会报错，注意__file__表示的是当前执行文件的路径
from ver_360 import version


def install():
    t = time.strftime("%H:%M:%S")
    print(t, '*******allow install*********', end=',')
    # type(Key.F11)
    wait(0.1)
    click(Pattern("install.png").targetOffset(422, 126))
    wait(0.1)
    click(Pattern("install.png").targetOffset(422, 150))
    wait(0.1)


def procp():
    t = time.strftime("%H:%M:%S")
    print(t, '***************process protection************', end=',')
    type(Key.F11)
    wait(0.1)
    click(Pattern("procp.png").targetOffset(422, 150))
    wait(0.1)
    click(Pattern("zuzhi.png"))
    wait(0.1)


def bingdu():
    t = time.strftime("%H:%M:%S")
    print(t, '***************Virus removal************', end=',')
    type(Key.F11)
    wait(0.1)
    click(Pattern("bingdu.png").targetOffset(159, -21))
    wait(0.1)


def UI():
    t = threading.Timer(5, UI)
    t.setDaemon(True)
    t.start()
    try:
        if exists("install.png", 1):
            install()
        elif exists("procp.png", 1):
            procp()
        if exists("bingdu.png", 1):
            bingdu()
        else:
            pass
            # print('no safe messages'
    except Exception as e:
        print('UI-error:', e, end=',')


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
    projects = ['mxiaoyu', 'mguangsu', 'mkuai', 'mxiaohei', 'mllq', 'qjpdf', 'lszip', 'gjl', 'mabc']
    UI()
    for i in range(len(projects)):
        project = projects[i]
        path = path_0 + project
        vc_list = version(project)
        t = threading.Thread(target=cmd_send, args=(project, path, vc_list), name='LoopThread')
        t.start()
        time.sleep(i * 10)
    print('thread %s is ended...' % threading.current_thread().name)
