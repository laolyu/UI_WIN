# -*- coding: UTF-8 -*-

from lackey import *
import datetime
import time
import subprocess
import threading
from loguru import logger

sys.path.append(r'C:\liangdamou\script\gjl')
from config import *


def haode():
    t = time.strftime("%H:%M:%S")
    logger.info(t, ':**************Virus removal***************', end=',')
    type(Key.F11)
    wait(0.2)
    click("haode.png")
    wait(0.2)


def yunxu():
    t = time.strftime("%H:%M:%S")
    logger.info(t, '-->>allow*************', end=',')
    type(Key.F11)
    wait(0.2)
    click("yunxu.png")
    wait(0.2)


def UI():
    t = threading.Timer(60, UI)
    t.setDaemon(True)
    t.start()
    try:
        if exists("yunxu.png", 5):
            yunxu()
            if exists("yunxu.png", 5):
                yunxu()
            if exists("yunxu.png", 5):
                yunxu()
        elif exists("haode.png", 5):
            haode()
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
            logger.info('retry', '****', e)
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


def kill_p(p_list, updc):
    updc_proc = updc.split('/')[-1]
    try:
        logger.info(f'taskkill /F /IM {updc_proc}')
        subprocess.check_call(f'taskkill /F /IM {updc_proc}')
    except Exception as e:
        logger.info(e)

    for i in range(len(p_list)):
        time.sleep(0.1)
        try:
            # logger.info(f'taskkill /F /IM {p_list[i]}.exe')
            result = subprocess.check_call(f'taskkill /F /IM {p_list[i]}.exe')
            if result == 0:
                type(Key.F11)
                time.sleep(1)
                logger.info(f'taskkill /F /IM {p_list[i]}.exe, successed')
        except Exception as e:
            pass


def pb():
    pb_list = ['bqpb', 'Kuaipb', 'Jxohft', 'hdagf', 'gshuhg', 'vbvcxf', 'aghghf', 'ktpb', 'pbxhone', 'GSscreensaver', '7654pb']

    try:
        subprocess.check_call('@reg add "HKEY_CURRENT_USER\Software\ScreenSaver" /v "ScreenSaveTimeOut" /t REG_DWORD /d "5" /f>nul', shell=True)
    except Exception as e:
        logger.info(e)
    finally:
        time.sleep(20)
        type(Key.F11)
        time.sleep(1)

    for i in range(len(pb_list)):
        try:
            result = subprocess.check_call(f'taskkill /F /IM {pb_list[i]}.exe')
            if result == 0:
                type(Key.F11)
                time.sleep(1)
                logger.info(f'*******{pb_list[i]}.exe is killed*********')
        except Exception as e:
            pass


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
        logger.info('*****updc********')
        try:
            subprocess.Popen(updc, shell=True)
        except Exception as e:
            logger.info(f'***kill {updc}****', e)
        finally:
            time.sleep(160)
            try:
                result = subprocess.check_call(f'taskkill /F /IM {updc}.exe')
                if result == 0:
                    logger.info(f'***{updc}.exe is killed*****')
            except Exception as e:
                pass

        if project in [xiaoyu, kuaizip, kantu, heinote, finder, browser]:
            pb()
        try:
            kill_p(p_list, updc)
        except Exception as e:
            logger.info(e)

        try:
            subprocess.check_call(r"taskkill /F /IM explorer.exe")
        except Exception as e:
            logger.info('******stop explorer*******', e)
        time.sleep(1)
        try:
            subprocess.check_call('start explorer.exe', shell=True)
        except Exception as e:
            logger.info('******restart explorer*******,e')

    try:
        logger.info('delete.bat')
        subprocess.check_call("C:\liangdamou\script\delete.bat")
    except Exception as e:
        pass
    time.sleep(10)


if __name__ == '__main__':
    logger.add("gjl_log_{time}.log", rotation="500MB", encoding="utf-8", enqueue=True, compression="zip", retention="10 days")
    projects = [xiaoyu, kuaizip, kantu, heinote, finder, browser, lszip, xinnote, qjpdf, cloudbar, haotu, xxbz, smartlook, xfpdf, jcbz, sesame]
    for i in range(len(projects)):
        project = projects[i]
        package = project['package']
        updc = project['updc']
        p_list = project['p_list']
        b4hand(project, package, updc, p_list)
