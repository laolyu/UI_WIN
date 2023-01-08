# -*- coding: utf-8 -*-
import datetime
import subprocess
import threading
from lackey import *
import sys
from loguru import logger
from time import sleep
from random import sample

Settings.InfoLogs = False
sys.path.append(r'C:\zm\script\gjl')  # 先加入绝对路径，否则会报错，注意__file__表示的是当前执行文件的路径
from ver_360 import version


def UI():
    t = threading.Timer(10, UI)
    t.setDaemon(True)
    t.start()
    try:
        if exists("explorer.jpg", 1):
            click(jpg)
            wait(0.5)
            logger.info('*******explorer stopped*********')
            type(Key.F11)
            wait(0.1)
            click(Pattern("explorer.jpg").targetOffset(0, 100))
            wait(0.1)
        if not exists("player.jpg", 1):
            try:
                subprocess.Popen('powershell.exe Stop-Process -name explorer', shell=True)
            except Exception as e:
                logger.info(e)
            try:
                subprocess.Popen('explorer', shell=True)
            except Exception as e:
                logger.info(e)
        if exists("install.jpg", 1):
            wait(0.1)
            click(Pattern("install.jpg").targetOffset(422, 126))
            wait(0.1)
            click(Pattern("install.jpg").targetOffset(422, 150))
            wait(0.1)
        elif exists("procp.jpg", 1):
            logger.info('********process protection********')
            click(jpg)
            wait(0.5)
            type(Key.F11)
            wait(0.1)
            click(Pattern("procp.jpg").targetOffset(422, 150))
            wait("zuzhi.jpg")
            click(Pattern("zuzhi.jpg"))
            wait(0.1)
        if exists("bingdu.jpg", 1):
            logger.info('*********Virus removal***********')
            click(jpg)
            wait(0.5)
            type(Key.F11)
            wait(0.1)
            click(Pattern("bingdu.jpg").targetOffset(159, -21))
            wait(0.1)
        else:
            pass
            # logger.info('no safe messages'
    except Exception as e:
        logger.info(e)


def cmd_send(path, vc_list):
    logger.info('thread ->>%s is running...' % (threading.current_thread().name))
    now = datetime.datetime.now()
    s1 = now.strftime('%Y-%m-%d %H:%M:%S')

    for x in range(len(vc_list)):
        cmd = vc_list[x]
        # sleep(2)
        for i in range(0, 3):
            logger.info(f' {x + 1}, {cmd}')
            p = subprocess.Popen(cmd, cwd=path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            try:
                out, err = p.communicate(timeout=100)
                err_info = err.decode('gbk')
                logger.info(err_info)
            except subprocess.TimeoutExpired as e:
                logger.info(e)
                subprocess.Popen(['taskkill', '/F', '/T', '/PID', str(p.pid)], shell=True)
                continue
            break

    logger.info('thread >>%s is ended...' % (threading.current_thread().name))
    now = datetime.datetime.now()
    e1 = now.strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f"start time: {s1}")
    logger.info(f"end time: {e1}")

    start = datetime.datetime.strptime(s1, '%Y-%m-%d %H:%M:%S')
    end = datetime.datetime.strptime(e1, '%Y-%m-%d %H:%M:%S')
    total = end - start
    if (total.seconds) > 60:
        m = float(total.seconds) / 60
        logger.info("total(min)：%s" % m)
    else:
        m = total.seconds
        logger.info("total(s)：%s" % m)


if __name__ == '__main__':
    logger.add("C:/zm/log/gjl_log_{time}.log", rotation="500MB", encoding="utf-8", enqueue=True, compression="zip", retention="10 days")
    logger.info('thread %s is running...' % threading.current_thread().name)
    path = r'C:\zm\package'
    UI()
    v = sample(version(), len(version()))
    cmd_send(path, v)
    logger.info('thread %s is ended...' % threading.current_thread().name)
