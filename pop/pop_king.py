# -*- coding: UTF-8 -*-
import datetime
from lackey import *
import time, os, sys
from config import *

sys.path.append(r'C:\AI\script\gjl')


def UI():
    time.sleep(10)
    try:
        if exists('sysp.jpg', 1):
            type(Key.F11)
            wait(0.5)
            print('++-->>系统保护:发现病毒++')
            wait(0.2)
            click(Pattern('sysp.jpg').targetOffset(150, 80))
        if exists('ddr.jpg', 1):
            type(Key.F11)
            print('++-->>内存防护:发现病毒++')
            wait(0.2)
            click(Pattern('ddr.jpg').targetOffset(115, 165))  # 记住操作
            wait(0.2)
            click(Pattern('ddr.jpg').targetOffset(190, 115))  # 暂不处理
    except Exception as e:
        print(e)


def inst(package):
    try:
        os.popen('net use \\172.18.15.3 "2020"  /user:"administrator"')
        os.popen(r'net time \\172.18.15.3 /set /y')
        UI()
        date = (datetime.datetime.now() + datetime.timedelta(days=-3)).strftime("%Y-%m-%d %H:%M:%S")
        t = '06.00.00'
        os.popen(f'date {date} && time {t}')
        time.sleep(5)
    except Exception as e:
        print(e)
    try:
        t = time.strftime("%H:%M:%S")
        print(t, package)
        os.popen(package)
        UI()
    except Exception as e:
        time.sleep(30)
        print(e)
    time.sleep(10)


def setTime2M():
    try:
        os.popen(r'net use \\172.18.15.3 "2020"  /user:"administrator"')
        os.popen(r'net time \\172.18.15.3 /set /y')
        UI()
        time.sleep(5)
    except Exception as e:
        print(e)


def kill_p(p_list, updc):
    updc_proc = updc.split('/')[-1]
    p_list.append(updc_proc)
    type(Key.F11)
    wait(1)
    for i in range(len(p_list)):
        name = p_list[i]
        os.popen('taskkill /F /IM %s.exe' % name)
        time.sleep(2)
    print('杀掉弹窗进程, successed')


def pb():
    pb_list = ['bqpb', 'xypbuninst', 'Kuaipb', 'parpbuninst', 'ktpb', 'ktpbuninst', 'pbxhone', 'xhpbuninst',
               'GSscreensaver', 'sspbuninst', '7654pb']
    try:
        os.popen(
            '@reg add "HKEY_CURRENT_USER\Software\ScreenSaver" /v "ScreenSaveTimeOut" /t REG_DWORD /d "15" /f>nul')
    except Exception as e:
        print(e)
    time.sleep(30)
    type(Key.F11)
    wait(1)
    for i in range(len(pb_list)):
        os.popen('taskkill /F /IM %s.exe' % pb_list[i])
        time.sleep(2)
    print('杀掉pb进程, successed')


def b4hand(project, package, updc, p_list):
    inst(package)
    UI()
    try:
        print('*****city.bat********')
        os.popen("C:\AI\script\city.bat")
    except Exception as e:
        print(e)
    setTime2M()
    try:
        os.popen(f'{updc}.exe')
        print('**点击updc*')
    except Exception as e:
        print(e)
    UI()
    time.sleep(10)
    try:
        os.popen(f'{updc}.exe')
        print('**点击updc*')
    except Exception as e:
        print(e)
    UI()
    time.sleep(180)

    if project in [xiaoyu, kuaizip, kantu, heinote, finder, browser]:
        pb()
    try:
        kill_p(p_list, updc)
    except Exception as e:
        print(e)
    try:
        print('delete.bat')
        os.popen("C:\AI\script\delete.bat")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    keyDown(Key.WIN)
    type("d")
    wait(1)
    keyUp(Key.WIN)
    # 隐藏窗口防止影响运行
    now = int(time.time())
    log_file = open(os.path.join('C:/AI/log/', '%s.txt') % now, "w")
    sys.stdout = log_file
    projects = [xiaoyu, kuaizip, kantu, heinote, finder, browser, lszip, xinnote, qjpdf, cloudbar, haotu, xxbz, sesame,
                jcbz]
    for i in range(len(projects)):
        project = projects[i]
        package = project['package']
        updc = project['updc']
        p_list = project['p_list']
        b4hand(project, package, updc, p_list)
    log_file.close()
