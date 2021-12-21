# -*- coding: utf-8 -*-
import datetime
import random
import subprocess
import threading
from mouse import click, wait
from lackey import *
import sys
from loguru import logger
from time import sleep

Settings.InfoLogs = False
sys.path.append(r'C:\zm\script\gjl')  # 先加入绝对路径，否则会报错，注意__file__表示的是当前执行文件的路径
from ver_king import version


def install():
    logger.info('********find install action**********')
    type(Key.F11)
    wait(0.2)
    click(Pattern("install.png").targetOffset(147, -55))
    wait(0.2)
    click(Pattern("install.png").targetOffset(162, -25))
    wait(0.2)


def sysp():
    logger.info('*******System protection*******')
    type(Key.F11)
    wait(0.2)
    click(Pattern("sysp.png").targetOffset(180, 90))
    wait(0.2)


def quanxian():
    logger.info(':*******find quanxian action..*******')
    type(Key.F11)
    wait(0.2)
    click(Pattern("quanxian.png").targetOffset(104, 0))
    wait(0.2)
    click(Pattern("quanxian.png").targetOffset(104, 40))
    wait(0.2)


def guanlian():
    logger.info(':****find guanlian action..*********')
    type(Key.F11)
    wait(0.2)
    click(Pattern("install.png").targetOffset(70, -55))
    wait(0.2)


def allow():
    logger.info(':*******allow>>*************')
    type(Key.F11)
    wait(0.2)
    click("allow.png")
    wait(0.2)


def qinngc():
    logger.info(':*************Virus removal at once***************')
    type(Key.F11)
    wait(0.2)
    click("qingchu.png")
    wait(0.2)


def bkq():
    logger.info(':donnot turn on')
    type(Key.F11)
    wait(0.2)
    click("bukaiqi.png")
    wait(0.2)
    sleep(10)


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
            # logger.info 'no safe messages'
    except Exception as e:
        logger.info(e)


def cmd_send(project, path, vc_list):
    logger.info('thread %s >>%s is running...' % (threading.current_thread().name, project))
    now = datetime.datetime.now()
    s1 = now.strftime('%Y-%m-%d %H:%M:%S')

    for x in range(len(vc_list)):
        cmd = vc_list[x]
        logger.info(f'{project}, {x + 1}, {cmd}')
        m = random.randint(20, 60)
        sleep(m)
        for i in range(0, 3):
            p = subprocess.Popen(cmd, cwd=path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            try:
                out, err = p.communicate(timeout=90)
                err_info = err.decode('gbk')
                logger.info(err_info)
            except subprocess.TimeoutExpired as e:
                logger.info(e)
                subprocess.call(['taskkill', '/F', '/T', '/PID', str(p.pid)], shell=True)
                continue
            break

    logger.info('thread %s >>%s is ended...' % (threading.current_thread().name, project))
    now = datetime.datetime.now()
    e1 = now.strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f"%s,start time: %s" % (project, s1))
    logger.info("%s,end time: %s：" % (project, e1))

    start = datetime.datetime.strptime(s1, '%Y-%m-%d %H:%M:%S')
    end = datetime.datetime.strptime(e1, '%Y-%m-%d %H:%M:%S')
    total = end - start
    if (total.seconds) > 60:
        m = float(total.seconds) / 60
        logger.info("%s,total(min)：%s" % (project, m))
    else:
        m = total.seconds
        logger.info("%s total(s)：%s" % (project, m))


if __name__ == '__main__':
    logger.add("gjl_log_{time}.log", rotation="500MB", encoding="utf-8", enqueue=True, compression="zip", retention="10 days")
    logger.info('thread %s is running...' % threading.current_thread().name)
    path_0 = r'C:\zm\package\\'
    UI()
    version = version()
    projects = list(version.keys())
    for project in list(projects):
        path = path_0 + project
        vc_list = version[project]
        t = threading.Thread(target=cmd_send, args=(project, path, vc_list), name='LoopThread')
        t.start()
        sleep(30)
    logger.info('thread %s is ended...' % threading.current_thread().name)
