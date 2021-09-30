# -*- coding: utf-8 -*-
import datetime
import random
import subprocess
import threading
# from mouse import click, wait
from lackey import *
import time
import sys
from loguru import logger

sys.path.append(r'C:\liangdamou\script\gjl')  # 先加入绝对路径，否则会报错，注意__file__表示的是当前执行文件的路径
from ver_qq import version


# def haode():
#     logger.info(':****报毒****Virus removal****')
#     type(Key.F11)
#     wait(0.2)
#     click("haode.png")
#     wait(0.2)


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
#     logger.info('-->>allow', end=',')
#     type(Key.F11)
#     wait(0.2)
#     click("yunxu.png")
#     wait(0.2)


def yes():
    logger.info('-->>确定*****', end=',')
    type(Key.F11)
    wait(0.2)
    click("yes.png")
    wait(0.2)


# def set_close():
#     logger.info('>>set-close', end=',')
#     type(Key.F11)
#     wait(1)
#     click(Pattern("set_close.png").targetOffset(12, 0))
#     wait(1)


def UI():
    t = threading.Timer(50, UI)
    t.setDaemon(True)
    t.start()
    try:
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
        logger.info('UI-error:', e)


def cmd_send(project, path, vc_list):
    logger.info('thread %s >>%s is running...' % (threading.current_thread().name, project))
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
                logger.info(e)
                subprocess.call(['taskkill', '/F', '/T', '/PID', str(p.pid)])
                continue
            break

        logger.info(f'{t}, {project}, {x + 1}, {vc_list[x]}')

    logger.info('thread %s >>%s is ended...' % (threading.current_thread().name, project))
    now = datetime.datetime.now()
    e1 = now.strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f"%s,start time: %s" % (project, s1), end=',')
    logger.info("%s,end time: %s：" % (project, e1), end=',')

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
    path_0 = r'C:\liangdamou\package\\'
    projects = ['mxiaoyu', 'lszip', 'mxiaohei', 'mkuai', 'mguangsu', 'mllq', 'gjl', 'qjpdf', 'mabc']
    UI()
    for i in range(len(projects)):
        project = projects[i]
        path = path_0 + project
        vc_list = version(project)
        t = threading.Thread(target=cmd_send, args=(project, path, vc_list), name='LoopThread')
        t.start()
        time.sleep(i * 10)
    logger.info('thread %s is ended...' % threading.current_thread().name)
