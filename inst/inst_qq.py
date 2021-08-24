# -*- coding: utf-8 -*-
import datetime
import random
import subprocess
import threading
# from mouse import click, wait
from lackey import *
import time
import sys

sys.path.append(r'C:\liangdamou\script\gjl')  # 先加入绝对路径，否则会报错，注意__file__表示的是当前执行文件的路径
from ver_qq import version


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


def set_close():
    t = time.strftime("%H:%M:%S")
    print(t, '>>set-close', end=',')
    type(Key.F11)
    wait(1)
    click(Pattern("set_close.png").targetOffset(12, 0))
    wait(1)


def UI():
    t = threading.Timer(60, UI)
    t.setDaemon(True)
    t.start()
    try:
        if exists("yunxu.png", 10):
            yunxu()
        elif exists("haode.png", 10):
            haode()
        # elif exists("close.png", 10):
        #     close()
        # elif exists("set_close.png", 10):
        #     set_close()
        # elif exists("yiTingZhiGZ.png", 10):
        #     yiTingZhiGZ()
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
    projects = ['mxiaoyu', 'lszip', 'mxiaohei', 'mkuai', 'mguangsu', 'mllq', 'mabc', 'gjl', 'qjpdf']
    UI()
    for i in range(len(projects)):
        project = projects[i]
        path = path_0 + project
        vc_list = version(project)
        t = threading.Thread(target=cmd_send, args=(project, path, vc_list), name='LoopThread')
        t.start()
        time.sleep(i * 10)
    print('thread %s is ended...' % threading.current_thread().name)
