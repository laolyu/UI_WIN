# coding:utf-8
import subprocess
import yagmail
from lackey import *
import sys
import psutil
from time import sleep
from loguru import logger

Settings.InfoLogs = False
sys.path.append(r'C:\woods\script')  # 先加入绝对路径，否则会报错，注意__file__表示的是当前执行文件的路径


def sent_mail(file, subject, message):
    receiver = "b4hand@139.com"
    yag = yagmail.SMTP("b4hand@qq.com", 'okpykwvdqeczhage', 'smtp.qq.com')
    yag.send(
        to=receiver,
        subject=subject,
        contents=message,
        attachments=file,
    )
    logger.info('file = %s,subject=%s,message=%s' % (file, subject, message))


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
    subprocess.Popen('start vmware', shell=True)
    for i in range(20):
        if exists("guanli.png", 2):
            logger.info('启动完成')
            break
        else:
            logger.info('启动未完成!!')
            sleep(10)


def vm(x, y):
    logger.info(f'***start vm{x, y}******')
    type(Key.F11)
    for i in range(10):
        if exists("huany.png", 2):
            logger.info('正在还原')
            sleep(10)
        else:
            logger.info('还原已完成')
            break
    if exists("guanli.png", 10):
        logger.info('***click x******')
        click(Pattern("guanli.png").targetOffset(x, y))
        wait(0.2)
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
    for i in range(20):
        if exists('windows.png', 1):
            logger.info('已完成恢复')
            break
        else:
            logger.info('未完成恢复')
            sleep(10)
    if not exists('windows.png', 1):
        type(Key.F11)
        sleep(1)
        sent_mail(file=None, subject='vm未完成恢复', message=str(x))
        logger.info('send_mail,未完成恢复')


if __name__ == '__main__':
    logger.add("gjl_log_{time}.log", rotation="500MB", encoding="utf-8", enqueue=True, compression="zip", retention="10 days")
    sleep(10)
    try:
        close_TV()
        vm_int()
        vm(-500, 30)
        vm(-400, 30)
        vm(-300, 30)
    except Exception as e:
        logger.info(e)
