# coding:utf-8
import subprocess
import time

import psutil
from loguru import logger


def proc_exist(process_name):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == f'{process_name}.exe':
            try:
                subprocess.check_call(f'taskkill /F /IM {process_name}.exe')
                logger.info(f'taskkill /F /IM {process_name}.exe, successed')
            except Exception as e:
                pass


def pb():
    # pb_list = ['bqpb', 'Kuaipb', 'Jxohft', 'hdagf', 'gshuhg', 'vbvcxf', 'aghghf', 'ktpb', 'pbxhone', 'GSscreensaver', '7654pb']

    pb_list = ['bqpb']
    for i in range(len(pb_list)):
        process_name = pb_list[i]
        proc_exist(process_name)


pb()
