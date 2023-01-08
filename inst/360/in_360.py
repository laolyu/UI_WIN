# -*- coding: utf-8 -*-
import datetime
import os
import time
from lackey import *
import sys

sys.path.append(r'C:\zm\script\gjl')


def version():
    vc = ['xiaoyu_v3.2.1.7_guanwang_1.exe -wjm', 'xiaoyu_v3.2.1.7_guanwang_2.exe -wjm',
          'xiaoyu_v3.2.1.7_guanwang_3.exe -wjm',
          'xiaoyu_v3.2.1.7_guanwang_4.exe -wjm', 'xiaoyu_v3.2.1.7_guanwang_5.exe -wjm',
          'xiaoyu_v3.3.0.2_guanwang_1.exe -wjm', 'xiaoyu_v3.3.0.2_guanwang_3.exe -wjm',
          'xiaoyu_v3.3.1.0_guanwang_1.exe -wjm', 'xiaoyu_v3.3.1.0_guanwang_2.exe -wjm',
          'xiaoyu_v3.3.1.0_guanwang_3.exe -wjm',
          'xiaoyu_v3.3.1.0_guanwang_4.exe -wjm', 'xiaoyu_v3.3.1.0_guanwang_5.exe -wjm',

          'QingJiePdf_Setup_v1.1.0.2_guanwang_1.exe  -wjm', 'QingJiePdf_Setup_v1.1.0.2_guanwang_2.exe  -wjm',
          'QingJiePdf_Setup_v1.1.0.2_guanwang_3.exe  -wjm', 'QingJiePdf_Setup_v1.1.0.2_guanwang_4.exe  -wjm',
          'QingJiePdf_Setup_v1.1.0.2_guanwang_5.exe  -wjm',
          'QingJiePdf_Setup_v1.1.0.3_guanwang_1.exe  -wjm', 'QingJiePdf_Setup_v1.1.0.3_guanwang_2.exe  -wjm',
          'QingJiePdf_Setup_v1.1.0.3_guanwang_3.exe  -wjm', 'QingJiePdf_Setup_v1.1.0.3_guanwang_4.exe  -wjm',
          'QingJiePdf_Setup_v1.1.0.3_guanwang_5.exe  -wjm',  # 1102 1103金山不测

          'PhotoViewer_Setup_v3.3.0.3_guanwang_1.exe -wjm', 'PhotoViewer_Setup_v3.3.0.3_guanwang_2.exe -wjm',
          'PhotoViewer_Setup_v3.3.0.3_guanwang_3.exe -wjm', 'PhotoViewer_Setup_v3.3.0.3_guanwang_4.exe -wjm',
          'PhotoViewer_Setup_v3.3.0.3_guanwang_5.exe -wjm',
          'PhotoViewer_Setup_v3.3.0.6_guanwang_1.exe -wjm', 'PhotoViewer_Setup_v3.3.0.6_guanwang_2.exe -wjm',
          'PhotoViewer_Setup_v3.3.0.6_guanwang_3.exe -wjm', 'PhotoViewer_Setup_v3.3.0.6_guanwang_4.exe -wjm',
          'PhotoViewer_Setup_v3.3.0.6_guanwang_5.exe -wjm',
          'PhotoViewer_Setup_v3.3.1.5_guanwang_1.exe -wjm',

          'JCWallpaper_v1.1.0.3_guanwang_1.exe  -wjm', 'JCWallpaper_v1.1.0.3_guanwang_2.exe  -wjm',
          'JCWallpaper_v1.1.0.3_guanwang_3.exe  -wjm',
          'JCWallpaper_v1.1.0.3_guanwang_4.exe  -wjm', 'JCWallpaper_v1.1.0.3_guanwang_5.exe  -wjm',
          'JCWallpaper_Setup_v1.1.1.1_guanwang_1.exe -wjm', 'JCWallpaper_Setup_v1.1.1.1_guanwang_2.exe -wjm',
          'JCWallpaper_Setup_v1.1.1.1_guanwang_3.exe -wjm',  # 'JCWallpaper_Setup_v1.1.1.1_guanwang_4.exe -wjm',
          # 'JCWallpaper_Setup_v1.1.1.1_guanwang_5.exe -wjm',

          '7654Browser_v3.1.1.2_guanwang_1.exe -wjm', '7654Browser_v3.1.1.2_guanwang_2.exe -wjm',
          '7654Browser_v3.1.1.2_guanwang_3.exe -wjm',
          '7654Browser_v3.1.1.2_guanwang_4.exe -wjm', '7654Browser_v3.1.1.2_guanwang_5.exe -wjm',  # 金山不测

          'haotu_v2.1.0.6_guanwang_1.exe -wjm', 'haotu_v2.1.0.6_guanwang_2.exe -wjm',
          'haotu_v2.1.0.6_guanwang_3.exe -wjm',
          'haotu_v2.1.0.6_guanwang_4.exe -wjm', 'haotu_v2.1.0.6_guanwang_5.exe -wjm',

          'Heinote_v3.3.0.2_guanwang_1.exe -wjm', 'Heinote_v3.3.0.2_guanwang_2.exe -wjm',
          'Heinote_v3.3.0.2_guanwang_3.exe -wjm',
          'Heinote_v3.3.0.2_guanwang_4.exe -wjm', 'Heinote_v3.3.0.2_guanwang_5.exe -wjm',
          'Heinote_v3.3.0.6_guanwang_1.exe -wjm', 'Heinote_v3.3.0.6_guanwang_2.exe -wjm',
          'Heinote_v3.3.0.6_guanwang_3.exe -wjm',
          'Heinote_v3.3.0.6_guanwang_4.exe -wjm', 'Heinote_v3.3.0.6_guanwang_5.exe -wjm',

          'xinnote_v2.1.0.4_guanwang_1.exe -wjm', 'xinnote_v2.1.0.4_guanwang_2.exe -wjm',
          'xinnote_v2.1.0.4_guanwang_3.exe -wjm',
          'xinnote_v2.1.0.4_guanwang_4.exe -wjm', 'xinnote_v2.1.0.4_guanwang_5.exe -wjm',
          'Finder_Setup_3.3.0.5_guanwang_1.exe -wjm', 'Finder_Setup_3.3.0.5_guanwang_2.exe -wjm',
          # 'Finder_Setup_3.3.0.5_guanwang_3.exe -wjm',
          'Finder_Setup_3.3.0.5_guanwang_4.exe -wjm', 'Finder_Setup_3.3.0.5_guanwang_5.exe -wjm',

          'CalfWallpaper_v1.0.3.5_guangwang_1.exe -wjm', 'CalfWallpaper_v1.0.3.5_guangwang_2.exe -wjm',
          'CalfWallpaper_v1.0.3.5_guangwang_3.exe -wjm', 'CalfWallpaper_v1.0.3.5_guangwang_4.exe -wjm',
          'CalfWallpaper_v1.0.3.5_guangwang_5.exe -wjm',

          'LsZip_Setup_v1.0.1.3_guanwang_1.exe -wjm', 'LsZip_Setup_v1.0.1.3_guanwang_2.exe -wjm',
          'LsZip_Setup_v1.0.1.3_guanwang_3.exe -wjm',
          'LsZip_Setup_v1.0.1.3_guanwang_4.exe -wjm', 'LsZip_Setup_v1.0.1.3_guanwang_5.exe -wjm',
          # 'LsZip_Setup_v1.1.0.2_guanwang_1.exe -wjm', 'LsZip_Setup_v1.1.0.2_guanwang_2.exe -wjm', 'LsZip_Setup_v1.1.0.2_guanwang_3.exe -wjm',
          # 'LsZip_Setup_v1.1.0.2_guanwang_4.exe -wjm', 'LsZip_Setup_v1.1.0.2_guanwang_5.exe -wjm',
          'LsZip_Setup_v1.1.0.4_guanwang_1.exe -wjm', 'LsZip_Setup_v1.1.0.4_guanwang_2.exe -wjm',
          'LsZip_Setup_v1.1.0.4_guanwang_3.exe -wjm',
          'LsZip_Setup_v1.1.0.4_guanwang_4.exe -wjm', 'LsZip_Setup_v1.1.0.4_guanwang_5.exe -wjm',

          'xlpreview_Setup_v1.0.0.7_guanwang_1.exe -wjm', 'xlpreview_Setup_v1.0.0.7_guanwang_2.exe -wjm',
          'xlpreview_Setup_v1.0.0.7_guanwang_3.exe -wjm', 'xlpreview_Setup_v1.0.0.7_guanwang_4.exe -wjm',
          'xlpreview_Setup_v1.0.0.7_guanwang_5.exe -wjm',

          'clouds_setup_v1.1.0.8_guanwang_1.exe -wjm', 'clouds_setup_v1.1.0.8_guanwang_2.exe -wjm',
          'clouds_setup_v1.1.0.8_guanwang_3.exe -wjm',
          'clouds_setup_v1.1.0.8_guanwang_4.exe -wjm', 'clouds_setup_v1.1.0.8_guanwang_5.exe -wjm',  # 不测金山

          'Sesame_Setup_v1.0.1.6_guangwang_1.exe -wjm', 'Sesame_Setup_v1.0.1.6_guangwang_2.exe -wjm',
          'Sesame_Setup_v1.0.1.6_guangwang_3.exe -wjm',
          'Sesame_Setup_v1.0.1.6_guangwang_4.exe -wjm', 'Sesame_Setup_v1.0.1.6_guangwang_5.exe -wjm',  # 金山已知报毒

          'KuaiZip_Setup_v3.3.0.3_guanwang_1.exe -wjm', 'KuaiZip_Setup_v3.3.0.3_guanwang_2.exe -wjm',
          'KuaiZip_Setup_v3.3.0.3_guanwang_3.exe -wjm',
          'KuaiZip_Setup_v3.3.0.3_guanwang_4.exe -wjm', 'KuaiZip_Setup_v3.3.0.3_guanwang_5.exe -wjm',
          'KuaiZip_Setup_v3.3.0.7_guanwang_1.exe -wjm', 'KuaiZip_Setup_v3.3.0.7_guanwang_2.exe -wjm',
          'KuaiZip_Setup_v3.3.0.7_guanwang_3.exe -wjm',
          'KuaiZip_Setup_v3.3.0.7_guanwang_4.exe -wjm', 'KuaiZip_Setup_v3.3.0.7_guanwang_5.exe -wjm',
          'KuaiZip_Setup_v3.3.1.2_guanwang_1.exe -wjm', 'KuaiZip_Setup_v3.3.1.2_guanwang_2.exe -wjm',
          'KuaiZip_Setup_v3.3.1.2_guanwang_3.exe -wjm',
          'KuaiZip_Setup_v3.3.1.2_guanwang_4.exe -wjm', 'KuaiZip_Setup_v3.3.1.2_guanwang_5.exe -wjm',
          'KuaiZip_Setup_v3.3.1.4_guanwang_1.exe -wjm', 'KuaiZip_Setup_v3.3.1.4_guanwang_2.exe -wjm',
          'KuaiZip_Setup_v3.3.1.4_guanwang_3.exe -wjm',
          'KuaiZip_Setup_v3.3.1.4_guanwang_4.exe -wjm', 'KuaiZip_Setup_v3.3.1.4_guanwang_5.exe -wjm',
          'KuaiZip_Setup_v3.3.1.8_guanwang_1.exe -wjm', 'KuaiZip_Setup_v3.3.1.8_guanwang_2.exe -wjm',
          'KuaiZip_Setup_v3.3.1.8_guanwang_3.exe -wjm',
          'KuaiZip_Setup_v3.3.1.8_guanwang_4.exe -wjm', 'KuaiZip_Setup_v3.3.1.8_guanwang_5.exe -wjm',
          ]
    return vc


def allow():
    t = time.strftime("%H:%M:%S")
    print(t, ':allow')
    type(Key.F11)
    wait(1)
    click("allow.png")
    time.sleep(20)


def qinngc():
    t = time.strftime("%H:%M:%S")
    print(t, ':Virus removal at once', )
    type(Key.F11)
    wait(1)
    click("qingchu.png")
    wait(1)


def bkq():
    t = time.strftime("%H:%M:%S")
    print(t, ':donnot turn on', )
    type(Key.F11)
    wait(1)
    click("bukaiqi.png")
    wait(1)
    time.sleep(10)


def close():
    print('关闭')
    type(Key.F11)
    wait(1)
    click("close.png")
    wait(1)


def set_close():
    print('设置-关闭')
    type(Key.F11)
    wait(1)
    click(Pattern("set_close.png").targetOffset(12, 0))
    wait(1)


def UI():
    time.sleep(10)
    try:
        if exists("install.jpg", 1):
            """
            检查安装弹窗是否存在
            """
            wait(1)
            click(Pattern("install.jpg").targetOffset(422, 126))
            wait(1)
            click(Pattern("install.jpg").targetOffset(422, 150))
        elif exists("procp.jpg", 1):
            '''
            检查安装弹窗是否存在系统保护弹窗
            '''
            print('********系统保护弹窗********')
            type(Key.F11)
            wait(1)
            click(Pattern("procp.jpg").targetOffset(422, 150))
            wait("zuzhi.jpg")
            click(Pattern("zuzhi.jpg"))
        if exists("bingdu.jpg", 1):
            """
            检查报毒弹窗是否存在
            """
            print('*********发现病毒弹窗***********')
            type(Key.F11)
            wait(1)
            click(Pattern("bingdu.jpg").targetOffset(159, -21))
    except Exception as e:
        print(e)


def cmd_send():
    now = datetime.datetime.now()
    s1 = now.strftime('%Y-%m-%d %H:%M:%S')
    keyDown(Key.WIN)
    type("d")
    wait(1)
    keyUp(Key.WIN)
    # 隐藏窗口防止影响运行
    vc_list = version()
    for x in range(len(vc_list)):
        try:
            time.sleep(20)
            UI()
            t = time.strftime("%H:%M:%S")
            cmd = vc_list[x]
            print(t, cmd)
            os.popen('C:/zm/package/' + cmd)
            UI()
        except Exception as e:
            time.sleep(30)
            print(e)

    now = datetime.datetime.now()
    e1 = now.strftime('%Y-%m-%d %H:%M:%S')
    print("start time: ", s1)
    print("end time: ", e1)

    start = datetime.datetime.strptime(s1, '%Y-%m-%d %H:%M:%S')
    # 开始时间
    end = datetime.datetime.strptime(e1, '%Y-%m-%d %H:%M:%S')
    # 结束时间
    total = end - start
    if (total.seconds) > 60:
        m = float(total.seconds) / 60
        # 转化成分钟
        print("total(min)：%s" % m)
    else:
        m = total.seconds
        print("total(s)：%s" % m)


if __name__ == '__main__':
    now = int(time.time())
    log_file = open(os.path.join('C:/zm/log/', '%s.txt') % now, "w")
    sys.stdout = log_file
    cmd_send()
    log_file.close()
