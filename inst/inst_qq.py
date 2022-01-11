# -*- coding: utf-8 -*-
import datetime
import random
import subprocess
import threading
# from mouse import click, wait
from lackey import *
import sys
from loguru import logger
from time import sleep

Settings.InfoLogs = False
sys.path.append(r'C:\zm\script\gjl')  # 先加入绝对路径，否则会报错，注意__file__表示的是当前执行文件的路径
from ver_qq import version


def bingdu():
    logger.info(':***拦截木马****Virus removal*******')
    type(Key.F11)
    wait(0.2)
    click(Pattern("bingdu.png").targetOffset(60, 395))
    wait(0.2)


def shishifh():
    logger.info(':***实时防护报毒****Virus removal*******')
    type(Key.F11)
    wait(0.2)
    click(Pattern("shishifh.png").targetOffset(400, 275))
    wait(0.2)


def gaowei():
    logger.info(':***高危状态****Virus removal*******')
    type(Key.F11)
    wait(0.2)
    click(Pattern("gaowei.png").targetOffset(148, 48))
    wait(0.2)


# def yunxu():
#     logger.info('-->>allow')
#     type(Key.F11)
#     wait(0.2)
#     click("yunxu.png")
#     wait(0.2)


def yes():
    logger.info('-->>确定*****')
    type(Key.F11)
    wait(0.2)
    click("yes.png")
    wait(0.2)


def explorer():
    if exists("explorer.png", 1):
        logger.info('*******explorer stopped*********')
        type(Key.F11)
        wait(0.1)
        click(Pattern("explorer.png").targetOffset(0, 100))
        wait(0.1)
    if not exists("windows.png", 2):
        try:
            subprocess.call('explorer', shell=True)
        except Exception as e:
            logger.info(e)
        try:
            subprocess.call('powershell.exe Stop-Process -name explorer', shell=True)
        except Exception as e:
            logger.info(e)


def UI():
    t = threading.Timer(60, UI)
    t.setDaemon(True)
    t.start()
    try:
        explorer()
        if exists("bingdu.png", 1):
            bingdu()
        elif exists("shishifh.png", 1):
            shishifh()
        elif exists("gaowei.png", 1):
            shishifh()
        elif exists("yes.png", 1):
            yes()
        # elif exists("close.png", 10):
        #     close()
        # elif exists("set_close.png", 10):
        #     set_close()
        # elif exists("yiTingZhiGZ.png", 10):
        #     yiTingZhiGZ()
        else:
            pass
            # logger.info 'no safe messages'
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
                subprocess.call(['taskkill', '/F', '/T', '/PID', str(p.pid)], shell=True)
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
    v = random.sample(version(), len(version()))
    cmd_send(path, v)
    logger.info('thread %s is ended...' % threading.current_thread().name)
