# -*- coding: utf-8 -*-

import subprocess
from lackey import *
import sys
import psutil
from time import sleep
from loguru import logger

Settings.InfoLogs = False
sys.path.append(r'C:\woods\script')  # 先加入绝对路径，否则会报错，注意__file__表示的是当前执行文件的路径


def proc_exist(process_name):
    pl = psutil.pids()
    for pid in pl:
        try:
            if psutil.Process(pid).name() == f'{process_name}.exe':
                # type(Key.F11)
                # time.sleep(2)
                subprocess.check_call(f'taskkill /F /IM {process_name}.exe', shell=True)
                logger.info(f'taskkill /F /IM {process_name}.exe, successed')
                sleep(10)
        except Exception as e:
            pass


def close_TV():
    logger.info('***close TV******')
    # type(Key.F11)
    if exists("TV.png", 10):
        logger.info('***click TV close******')
        click(Pattern("TV.png").targetOffset(180, 65))


def vm_int():
    logger.info('***restart vm******')
    # type(Key.F11)
    proc_exist('vmware-vmx')
    proc_exist('vmware')


def vm(x, y):
    logger.info('***start vm******')
    type(Key.F11)
    for i in range(10):
        if exists("huany.png", 10):
            logger.info('found 还原')
            sleep(10)
        else:
            break
    if exists("guanli.png", 10):
        logger.info('***click x******')
        click(Pattern("guanli.png").targetOffset(x, y))
    if exists("guanli.png", 10):
        logger.info('***click 管理******')
        click(Pattern("guanli.png"))
        wait(0.2)
    if exists("dqwz.png", 10):
        logger.info('***click 快照*****')
        click(Pattern("dqwz.png").targetOffset(-60, 0))
        wait(0.2)
    if exists("zhuand.png", 10):
        logger.info('***click 转到******')
        click(Pattern("zhuand.png"))
        wait(0.2)
    if exists("yes.png", 10):
        logger.info('***click 是******')
        click(Pattern("yes.png"))
        wait(0.2)
    else:
        type(Key.F11)
        logger.info('not found')
    sleep(30)
    logger.info('sleep end')


if __name__ == '__main__':
    logger.add("gjl_log_{time}.log", rotation="500MB", encoding="utf-8", enqueue=True, compression="zip", retention="10 days")
    sleep(10)
    close_TV()
    vm_int()
    subprocess.Popen('start vmware', shell=True)
    vm(-500, 30)
    vm(-400, 30)
    vm(-300, 30)
