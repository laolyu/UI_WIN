# -*- coding: UTF-8 -*-
import psutil
from lackey import *

Settings.InfoLogs = False
import datetime
import time
import subprocess
import threading
from loguru import logger

sys.path.append(r'C:\liangdamou\script\gjl')
from config import *


def haode():
    logger.info(':**************Virus removal***************', end=',')
    type(Key.F11)
    wait(0.2)
    click("haode.png")
    wait(0.2)


def yunxu():
    logger.info('-->>allow*************', end=',')
    type(Key.F11)
    wait(0.2)
    click("yunxu.png")
    wait(0.2)


def yes():
    logger.info('-->>确定*****', end=',')
    type(Key.F11)
    wait(0.2)
    click("yes.png")
    wait(0.2)


def UI():
    t = threading.Timer(30, UI)
    t.setDaemon(True)
    t.start()
    try:
        if exists("yunxu.png", 1):
            yunxu()
            if exists("yunxu.png", 1):
                yunxu()
            if exists("yunxu.png", 1):
                yunxu()
        elif exists("haode.png", 1):
            haode()
        elif exists("yes.png", 1):
            yes()
        else:
            pass
            # logger.info 'no safe messages'
    except Exception as e:
        logger.info('UI-error:', e)


def inst(package):
    try:
        subprocess.check_call(r'net use \\172.18.15.3 "2020"  /user:"administrator"')
        subprocess.check_call(r'net time \\172.18.15.3 /set /y')
        date = (datetime.datetime.now() + datetime.timedelta(days=-3)).strftime("%Y-%m-%d %H:%M:%S")
        t = '06.00.00'
        subprocess.check_call(f'date {date} && time {t}', shell=True)
        time.sleep(5)
    except Exception as e:
        logger.info(e)

    for i in range(0, 2):
        p = subprocess.Popen(package, shell=True)
        try:
            p.communicate(timeout=60)
        except subprocess.TimeoutExpired as e:
            logger.info('***timeout>>retry>***', e)
            subprocess.call(['taskkill', '/F', '/T', '/PID', str(p.pid)])
            continue
        break
    time.sleep(10)


def setTime2M():
    try:
        subprocess.check_call(r'net use \\172.18.15.3 "2020"  /user:"administrator"')
        subprocess.check_call(r'net time \\172.18.15.3 /set /y')

        # try:
        #     date = (datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y-%m-%d %H:%M:%S")
        #     t = '10.58.00'
        #     subprocess.check_call(f'date {date} && time {t}', shell=True)
        time.sleep(5)
    except Exception as e:
        logger.info(e)


def setTime2T():
    try:
        date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
        t = '16.58.00'
        subprocess.check_call(f'date {date} && time {t}', shell=True)
        time.sleep(5)
    except Exception as e:
        logger.info(e)


def proc_exist(process_name):
    pl = psutil.pids()
    for pid in pl:
        try:
            if psutil.Process(pid).name() == f'{process_name}.exe':
                type(Key.F11)
                time.sleep(2)
                subprocess.check_call(f'taskkill /F /IM {process_name}.exe')
                logger.info(f'taskkill /F /IM {process_name}.exe, successed')
        except Exception as e:
            pass


def kill_p(p_list, updc):
    updc_proc = updc.split('/')[-1]
    proc_exist(updc_proc)

    for i in range(len(p_list)):
        process_name = p_list[i]
        proc_exist(process_name)
        time.sleep(0.4)


def pb():
    pb_list = ['bqpb', 'xypbuninst', 'Kuaipb', 'parpbuninst', 'ktpb', 'ktpbuninst', 'pbxhone', 'xhpbuninst', 'GSscreensaver', 'sspbuninst', '7654pb']
    try:
        subprocess.check_call('@reg add "HKEY_CURRENT_USER\Software\ScreenSaver" /v "ScreenSaveTimeOut" /t REG_DWORD /d "15" /f>nul', shell=True)
    except Exception as e:
        logger.info(e)
    finally:
        time.sleep(20)

    for i in range(len(pb_list)):
        process_name = pb_list[i]
        proc_exist(process_name)


def b4hand(project, package, updc, p_list):
    UI()
    inst(package)
    setTime = [setTime2M]
    for i in range(len(setTime)):
        try:
            logger.info('*****city.bat********')
            subprocess.check_call("C:\liangdamou\script\city.bat")
        except Exception as e:
            pass

        setTime[i]()
        try:
            subprocess.Popen(f'{updc}.exe', shell=True)
            logger.info(f'**1***{updc}.exe********')
        except Exception as e:
            logger.info(f'*1**{updc}.exe****', e)
        time.sleep(10)
        try:
            subprocess.Popen(f'{updc}.exe', shell=True)
            logger.info(f'**2***{updc}.exe********')
        except Exception as e:
            logger.info(f'*2**{updc}.exe****', e)
        finally:
            time.sleep(180)
        if project in [xiaoyu, kuaizip, kantu, heinote, finder, browser]:
            pb()
        try:
            kill_p(p_list, updc)
        except Exception as e:
            logger.info('kill_p(p_list, updc)', e)
        try:
            logger.info('delete.bat')
            subprocess.check_call("C:\liangdamou\script\delete.bat")
        except Exception as e:
            pass


if __name__ == '__main__':
    logger.add("gjl_log_{time}.log", rotation="500MB", encoding="utf-8", enqueue=True, compression="zip", retention="10 days")
    projects = [xiaoyu, kuaizip, kantu, heinote, finder, browser, lszip, xinnote, qjpdf, cloudbar, haotu, xxbz, smartlook, xfpdf, jcbz, sesame]
    for i in range(len(projects)):
        project = projects[i]
        package = project['package']
        updc = project['updc']
        p_list = project['p_list']
        b4hand(project, package, updc, p_list)
