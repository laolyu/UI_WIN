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


def close_shadu(jpg="close_shadu.jpg"):
    if exists(jpg, 1):
        # find(jpg).highlight(1)
        # type(Key.F11)
        # wait(0.2)
        click(Pattern(jpg).targetOffset(80, 0))
        wait(0.2)
        logger.info(':***关闭,闪电杀毒******')
        click_it('qued.jpg')


def click_it(jpg):
    if exists(jpg, 1):
        # find(jpg).highlight(1)
        type(Key.F11)
        wait(0.5)
        click(jpg)
        logger.info(f'++click-{jpg}++')


def explorer(jpg='explorer.jpg'):
    if exists(jpg, 1):
        # find(jpg).highlight(1)
        click(jpg)
        wait(0.5)
        type(Key.F11)
        logger.info('*******explorer stopped*********')
        wait(0.1)
        click(Pattern(jpg).targetOffset(0, 100))
        wait(0.1)
    if not exists('player.jpg', 4):
        type(Key.F11)
        logger.info('++explorer&playernot found++')
        try:
            subprocess.Popen('explorer', shell=True)
        except Exception as e:
            logger.info(e)
        try:
            subprocess.Popen('powershell.exe Stop-Process -name explorer', shell=True)
        except Exception as e:
            logger.info(e)


def UI():
    t = threading.Timer(50, UI)
    t.setDaemon(True)
    t.start()
    try:
        explorer()
        click_it('yunxu.jpg')
        click_it('zuzhi.jpg')
        click_it('haode.jpg')
        click_it('crash.jpg')
        close_shadu()
    except Exception as e:
        logger.info(e)


def cmd_send(path, vc_list):
    logger.info('thread ->>%s is running...' % (threading.current_thread().name))
    now = datetime.datetime.now()
    s1 = now.strftime('%Y-%m-%d %H:%M:%S')

    for x in range(len(vc_list)):
        cmd = vc_list[x]
        sleep(30)
        for i in range(0, 3):
            logger.info(f' {x + 1}, {cmd}')
            p = subprocess.Popen(cmd, cwd=path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            try:
                out, err = p.communicate(timeout=180)
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
    v = random.sample(version(), len(version()))
    cmd_send(path, v)
    logger.info('thread %s is ended...' % threading.current_thread().name)
