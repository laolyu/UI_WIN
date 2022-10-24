# coding:utf-8

import subprocess
from lackey import *
import sys
import psutil
from time import sleep
from loguru import logger

# Settings.InfoLogs = False
sys.path.append(r'E:\woods\script')  # 先加入绝对路径，否则会报错，注意__file__表示的是当前执行文件的路径


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
    subprocess.Popen('shutdown -r -t 100', shell=True)
    sleep(80)
    proc_exist('vmware-vmx')
    proc_exist('vmware')


if __name__ == '__main__':
    logger.add("E:/woods/log/gjl_log_{time}.log", rotation="500MB", encoding="utf-8", enqueue=True, compression="zip", retention="10 days")
    try:
        close_TV()
        vm_int()
    except Exception as e:
        logger.info(e)
