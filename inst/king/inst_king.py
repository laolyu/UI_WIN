# -*- coding: utf-8 -*-
import datetime
import random
import subprocess
import threading
import lackey
from lackey import *
import sys
from loguru import logger
from time import sleep

Settings.InfoLogs = False
sys.path.append(r'C:\zm\script\gjl')  # 先加入绝对路径，否则会报错，注意__file__表示的是当前执行文件的路径
from ver_king import version


def explorer(jpg='explorer.jpg'):
    if exists(jpg, 1):
        # find(jpg).highlight(1)
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
            subprocess.Popen('powershell.exe Stop-Process -name explorer', shell=True)
        except Exception as e:
            logger.info(e)
        try:
            subprocess.Popen('explorer', shell=True)
        except Exception as e:
            logger.info(e)


def sysp(jpg='sysp.jpg'):
    if exists(jpg, 1):
        new_reg = find(jpg).right(400)
        # new_reg.highlight(1)
        wait(0.5)
        type(Key.F11)
        try:
            #     new_reg.findText('Task'.encode('utf-8').decode('utf-8'))
            #     logger.info('++系统保护:可疑计划++')
            #     wait(0.2)
            #     click(Pattern(jpg).targetOffset(420, 130))
            #     wait(0.2)
            #     click(Pattern(jpg).targetOffset(420, 150))
            # except lackey.Exceptions.FindFailed as e:
            logger.info(f'++-->>系统保护:发现病毒++')
            wait(0.2)
            click(Pattern(jpg).targetOffset(150, 80))
        except Exception as e:
            logger.info(e)


def ddr(jpg='ddr.jpg'):
    if exists(jpg, 1):
        try:
            wait(0.2)
            type(Key.F11)
            logger.info(f'++-->>内存防护:发现病毒++')
            wait(0.2)
            click(Pattern(jpg).targetOffset(115, 165))  # 记住操作
            wait(0.2)
            click(Pattern(jpg).targetOffset(190, 115))  # 暂不处理
        except Exception as e:
            logger.info(e)


def remind(jpg):
    if exists(jpg, 1):
        type(Key.F11)
        wait(0.5)
        if jpg == 'quanxian.jpg':
            x = 104
        else:
            x = 114
        click(Pattern(jpg).targetOffset(x, 0))
        wait(0.2)
        click(Pattern(jpg).targetOffset(x, 35))
        wait(0.2)
        logger.info('++不再提醒++')


def update(up='up.jpg', up2='up2.jpg', reboot='reboot.jpg', rb='rb.jpg'):
    try:
        cmd = '"C:\program files (x86)\kingsoft\kingsoft antivirus\kislive.exe" -vip -level:0'
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        logger.info(e)
    try:
        if exists(up2, 10):
            # find(up2).highlight(1)
            logger.info('++检查更新++')
            wait(0.5)
            click(Pattern(up2).targetOffset(0, 140))
            logger.info('++立即升级++')
            sleep(2)
            if exists(rb, 180):
                # find(rb).highlight(1)
                # wait(0.5)
                type(Key.F11)
                wait(0.5)
                click(Pattern(rb).targetOffset(90, 250))
                logger.info('++重启1++')
                wait(0.5)
                click(Pattern(rb).targetOffset(90, 250))
                logger.info('++重启2++')
                wait(0.5)
                click(Pattern(rb).targetOffset(0, 250))
                logger.info('++无需更新++')
    except Exception as e:
        logger.info(e)


def UI():
    t = threading.Timer(30, UI)
    t.setDaemon(True)
    t.start()
    try:
        sysp()
        ddr()
        explorer()
        remind('quanxian.jpg')
        remind('youjian.jpg')
    except Exception as e:
        logger.info(e)


def cmd_send(path, vc_list):
    logger.info('thread ->>%s is running...' % (threading.current_thread().name))
    now = datetime.datetime.now()
    s1 = now.strftime('%Y-%m-%d %H:%M:%S')

    for x in range(len(vc_list)):
        cmd = vc_list[x]
        sleep(20)
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
    update()
    UI()
    v = random.sample(version(), len(version()))
    cmd_send(path, v)
    logger.info('thread %s is ended...' % threading.current_thread().name)
