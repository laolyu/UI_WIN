# -*- coding: utf-8 -*-
import datetime
import os
import time
from lackey import *
import sys

sys.path.append(r'C:\zm\script\gjl')  # 先加入绝对路径，否则会报错，注意__file__表示的是当前执行文件的路径


def version():
    vc = ['xiaoyu_v3.2.1.7_guanwang_1.exe -wjm', 'xiaoyu_v3.2.1.7_guanwang_2.exe -wjm',
          # 'xiaoyu_v3.2.1.7_guanwang_3.exe -wjm',
          'xiaoyu_v3.2.1.7_guanwang_4.exe -wjm', 'xiaoyu_v3.2.1.7_guanwang_5.exe -wjm',
          'xiaoyu_v3.3.0.2_guanwang_1.exe -wjm', 'xiaoyu_v3.3.0.2_guanwang_3.exe -wjm',
          'xiaoyu_v3.3.1.0_guanwang_1.exe -wjm', 'xiaoyu_v3.3.1.0_guanwang_2.exe -wjm',
          'xiaoyu_v3.3.1.0_guanwang_3.exe -wjm',
          'xiaoyu_v3.3.1.0_guanwang_4.exe -wjm', 'xiaoyu_v3.3.1.0_guanwang_5.exe -wjm',

          # 'QingJiePdf_Setup_v1.0.1.4_guanwang_1.exe  -wjm', 'QingJiePdf_Setup_v1.0.1.4_guanwang_2.exe  -wjm',
          # 'QingJiePdf_Setup_v1.0.1.4_guanwang_3.exe  -wjm', 'QingJiePdf_Setup_v1.0.1.4_guanwang_4.exe  -wjm',
          # 'QingJiePdf_Setup_v1.0.1.4_guanwang_5.exe  -wjm',
          # 'QingJiePdf_Setup_v1.0.1.5_guanwang_1.exe  -wjm', 'QingJiePdf_Setup_v1.0.1.5_guanwang_2.exe  -wjm',
          # 'QingJiePdf_Setup_v1.0.1.5_guanwang_3.exe  -wjm', 'QingJiePdf_Setup_v1.0.1.5_guanwang_4.exe  -wjm',
          # 'QingJiePdf_Setup_v1.0.1.5_guanwang_5.exe  -wjm',

          'KuaiZip_Setup_v3.3.0.3_guanwang_1.exe -wjm', 'KuaiZip_Setup_v3.3.0.3_guanwang_3.exe -wjm',
          'KuaiZip_Setup_v3.3.0.3_guanwang_4.exe -wjm', 'KuaiZip_Setup_v3.3.0.3_guanwang_5.exe -wjm',
          'KuaiZip_Setup_v3.3.0.7_guanwang_1.exe -wjm', 'KuaiZip_Setup_v3.3.0.7_guanwang_2.exe -wjm',
          'KuaiZip_Setup_v3.3.0.7_guanwang_3.exe -wjm',
          'KuaiZip_Setup_v3.3.0.7_guanwang_4.exe -wjm', 'KuaiZip_Setup_v3.3.0.7_guanwang_5.exe -wjm',
          'KuaiZip_Setup_v3.3.1.2_guanwang_1.exe -wjm', 'KuaiZip_Setup_v3.3.1.2_guanwang_2.exe -wjm',
          'KuaiZip_Setup_v3.3.1.2_guanwang_3.exe -wjm',
          'KuaiZip_Setup_v3.3.1.2_guanwang_4.exe -wjm', 'KuaiZip_Setup_v3.3.1.2_guanwang_5.exe -wjm',
          'KuaiZip_Setup_v3.3.1.4_guanwang_1.exe -wjm', 'KuaiZip_Setup_v3.3.1.4_guanwang_2.exe -wjm',
          'KuaiZip_Setup_v3.3.1.4_guanwang_4.exe -wjm', 'KuaiZip_Setup_v3.3.1.4_guanwang_5.exe -wjm',
          'KuaiZip_Setup_v3.3.1.8_guanwang_1.exe -wjm', 'KuaiZip_Setup_v3.3.1.8_guanwang_2.exe -wjm',
          'KuaiZip_Setup_v3.3.1.8_guanwang_3.exe -wjm',
          'KuaiZip_Setup_v3.3.1.8_guanwang_4.exe -wjm', 'KuaiZip_Setup_v3.3.1.8_guanwang_5.exe -wjm',

          # 'PhotoViewer_Setup_v3.3.0.3_guanwang_1.exe -wjm', 'PhotoViewer_Setup_v3.3.0.3_guanwang_2.exe -wjm',
          # 'PhotoViewer_Setup_v3.3.0.3_guanwang_3.exe -wjm', 'PhotoViewer_Setup_v3.3.0.3_guanwang_4.exe -wjm',
          # 'PhotoViewer_Setup_v3.3.0.3_guanwang_5.exe -wjm',
          'PhotoViewer_Setup_v3.3.0.6_guanwang_1.exe -wjm', 'PhotoViewer_Setup_v3.3.0.6_guanwang_2.exe -wjm',
          'PhotoViewer_Setup_v3.3.0.6_guanwang_3.exe -wjm', 'PhotoViewer_Setup_v3.3.0.6_guanwang_4.exe -wjm',
          'PhotoViewer_Setup_v3.3.0.6_guanwang_5.exe -wjm',
          'PhotoViewer_Setup_v3.3.1.5_guanwang_1.exe -wjm',
          # 'PhotoViewer_Setup_v3.3.1.6_guanwang_1.exe -wjm', 'PhotoViewer_Setup_v3.3.1.6_guanwang_2.exe -wjm',
          # 'PhotoViewer_Setup_v3.3.1.6_guanwang_3.exe -wjm', 'PhotoViewer_Setup_v3.3.1.6_guanwang_4.exe -wjm',
          # 'PhotoViewer_Setup_v3.3.1.6_guanwang_5.exe -wjm',

          'JCWallpaper_v1.1.0.3_guanwang_1.exe  -wjm', 'JCWallpaper_v1.1.0.3_guanwang_2.exe  -wjm',
          'JCWallpaper_v1.1.0.3_guanwang_3.exe  -wjm',
          'JCWallpaper_v1.1.0.3_guanwang_4.exe  -wjm', 'JCWallpaper_v1.1.0.3_guanwang_5.exe  -wjm',
          'JCWallpaper_Setup_v1.1.1.1_guanwang_1.exe -wjm', 'JCWallpaper_Setup_v1.1.1.1_guanwang_2.exe -wjm',
          'JCWallpaper_Setup_v1.1.1.1_guanwang_3.exe -wjm',  # 'JCWallpaper_Setup_v1.1.1.1_guanwang_4.exe -wjm',
          # 'JCWallpaper_Setup_v1.1.1.1_guanwang_5.exe -wjm',

          'LsZip_Setup_v1.0.1.3_guanwang_1.exe -wjm', 'LsZip_Setup_v1.0.1.3_guanwang_2.exe -wjm',
          'LsZip_Setup_v1.0.1.3_guanwang_3.exe -wjm',
          'LsZip_Setup_v1.0.1.3_guanwang_4.exe -wjm', 'LsZip_Setup_v1.0.1.3_guanwang_5.exe -wjm',
          # 'LsZip_Setup_v1.1.0.2_guanwang_1.exe -wjm', 'LsZip_Setup_v1.1.0.2_guanwang_2.exe -wjm', 'LsZip_Setup_v1.1.0.2_guanwang_3.exe -wjm',
          # 'LsZip_Setup_v1.1.0.2_guanwang_4.exe -wjm', 'LsZip_Setup_v1.1.0.2_guanwang_5.exe -wjm',
          'LsZip_Setup_v1.1.0.4_guanwang_1.exe -wjm', 'LsZip_Setup_v1.1.0.4_guanwang_2.exe -wjm',
          'LsZip_Setup_v1.1.0.4_guanwang_3.exe -wjm',
          'LsZip_Setup_v1.1.0.4_guanwang_4.exe -wjm', 'LsZip_Setup_v1.1.0.4_guanwang_5.exe -wjm',

          'haotu_v2.1.0.6_guanwang_1.exe -wjm', 'haotu_v2.1.0.6_guanwang_2.exe -wjm',
          'haotu_v2.1.0.6_guanwang_3.exe -wjm',
          'haotu_v2.1.0.6_guanwang_4.exe -wjm', 'haotu_v2.1.0.6_guanwang_5.exe -wjm',
          # 'Heinote_v3.3.0.1_guanwang_1.exe -wjm',
          # 'Heinote_v3.3.0.1_guanwang_2.exe -wjm', 'Heinote_v3.3.0.1_guanwang_3.exe -wjm', 'Heinote_v3.3.0.1_guanwang_4.exe -wjm',
          # 'Heinote_v3.3.0.1_guanwang_5.exe -wjm',
          'Heinote_v3.3.0.2_guanwang_1.exe -wjm', 'Heinote_v3.3.0.2_guanwang_2.exe -wjm',
          'Heinote_v3.3.0.2_guanwang_3.exe -wjm',
          'Heinote_v3.3.0.2_guanwang_4.exe -wjm', 'Heinote_v3.3.0.2_guanwang_5.exe -wjm',
          'Heinote_v3.3.0.6_guanwang_1.exe -wjm', 'Heinote_v3.3.0.6_guanwang_2.exe -wjm',
          'Heinote_v3.3.0.6_guanwang_3.exe -wjm',
          'Heinote_v3.3.0.6_guanwang_4.exe -wjm', 'Heinote_v3.3.0.6_guanwang_5.exe -wjm',

          'xinnote_v2.1.0.4_guanwang_1.exe -wjm', 'xinnote_v2.1.0.4_guanwang_2.exe -wjm',
          'xinnote_v2.1.0.4_guanwang_3.exe -wjm',
          'xinnote_v2.1.0.4_guanwang_4.exe -wjm', 'xinnote_v2.1.0.4_guanwang_5.exe -wjm',

          # 'Finder_Setup_3.2.2.6_guanwang_1.exe -wjm', 'Finder_Setup_3.2.2.6_guanwang_2.exe -wjm', 'Finder_Setup_3.2.2.6_guanwang_3.exe -wjm',
          # 'Finder_Setup_3.2.2.6_guanwang_4.exe -wjm', 'Finder_Setup_3.2.2.6_guanwang_5.exe -wjm',
          # 'Finder_Setup_3.3.0.1_guanwang_1.exe -wjm',
          # 'Finder_Setup_3.3.0.1_guanwang_2.exe -wjm', 'Finder_Setup_3.3.0.1_guanwang_3.exe -wjm', 'Finder_Setup_3.3.0.1_guanwang_4.exe -wjm',
          # 'Finder_Setup_3.3.0.1_guanwang_5.exe -wjm',
          # 'Finder_Setup_3.3.0.5_guanwang_1.exe -wjm', #'Finder_Setup_3.3.0.5_guanwang_2.exe -wjm',
          'Finder_Setup_3.3.0.5_guanwang_4.exe -wjm',  # 'Finder_Setup_3.3.0.5_guanwang_5.exe -wjm',

          'CalfWallpaper_v1.0.3.5_guangwang_1.exe -wjm', 'CalfWallpaper_v1.0.3.5_guangwang_2.exe -wjm',
          'CalfWallpaper_v1.0.3.5_guangwang_3.exe -wjm', 'CalfWallpaper_v1.0.3.5_guangwang_4.exe -wjm',
          'CalfWallpaper_v1.0.3.5_guangwang_5.exe -wjm',

          # 'preview_Setup_1.0.2.9_guanwang_1.exe -wjm', 'preview_Setup_1.0.2.9_guanwang_2.exe -wjm', 'preview_Setup_1.0.2.9_guanwang_3.exe -wjm',
          # 'preview_Setup_1.0.2.9_guanwang_4.exe -wjm', 'preview_Setup_1.0.2.9_guanwang_5.exe -wjm',

          'xlpreview_Setup_v1.0.0.7_guanwang_1.exe -wjm', 'xlpreview_Setup_v1.0.0.7_guanwang_2.exe -wjm',
          'xlpreview_Setup_v1.0.0.7_guanwang_3.exe -wjm', 'xlpreview_Setup_v1.0.0.7_guanwang_4.exe -wjm',
          'xlpreview_Setup_v1.0.0.7_guanwang_5.exe -wjm',

          # 'clouds_setup_v1.1.0.8_guanwang_1.exe -wjm', 'clouds_setup_v1.1.0.8_guanwang_2.exe -wjm', 'clouds_setup_v1.1.0.8_guanwang_3.exe -wjm',
          # 'clouds_setup_v1.1.0.8_guanwang_4.exe -wjm', 'clouds_setup_v1.1.0.8_guanwang_5.exe -wjm',
          # gjl,不测金山环境

          # 'Sesame_Setup_v1.0.1.6_guangwang_1.exe -wjm', 'Sesame_Setup_v1.0.1.6_guangwang_2.exe -wjm', 'Sesame_Setup_v1.0.1.6_guangwang_3.exe -wjm',
          # 'Sesame_Setup_v1.0.1.6_guangwang_4.exe -wjm', 'Sesame_Setup_v1.0.1.6_guangwang_5.exe -wjm',  # 金山已知报毒
          ]

    return vc


def guanlian():
    t = time.strftime("%H:%M:%S")
    print(t, ':find guanlian action..')
    type(Key.F11)
    wait(1)
    click(Pattern("install.png").targetOffset(70, -55))
    wait(1)


def allow():
    t = time.strftime("%H:%M:%S")
    print(t, ':allow')
    type(Key.F11)
    wait(1)
    click("allow.png")
    time.sleep(20)


def qinngc():
    t = time.strftime("%H:%M:%S")
    print(t, ':Virus removal at once')
    type(Key.F11)
    wait(1)
    click("qingchu.png")
    wait(1)


def bkq():
    t = time.strftime("%H:%M:%S")
    print(t, ':donnot turn on')
    type(Key.F11)
    wait(1)
    click("bukaiqi.png")
    wait(1)
    time.sleep(10)


def UI():
    try:
        if exists('sysp.jpg', 1):
            try:
                wait(1)
                type(Key.F11)
                print('++-->>系统保护:发现病毒++')
                wait(1)
                click(Pattern('sysp.jpg').targetOffset(150, 80))
            except Exception as e:
                print(e)
        if exists('ddr.jpg', 1):
            try:
                wait(1)
                type(Key.F11)
                print('++-->>内存防护:发现病毒++')
                wait(1)
                click(Pattern('ddr.jpg').targetOffset(115, 130))  # 记住操作
                wait(1)
                click(Pattern('ddr.jpg').targetOffset(190, 80))  # 暂不处理
            except Exception as e:
                print(e)

        if exists('quanxian.jpg', 1):
            type(Key.F11)
            wait(1)
            click(Pattern('quanxian.jpg').targetOffset(104, 0))
            wait(1)
            click(Pattern('quanxian.jpg').targetOffset(104, 35))
            wait(1)
            print('++不再提醒++')

        if exists('youjian.jpg', 1):
            type(Key.F11)
            wait(1)
            click(Pattern('youjian.jpg').targetOffset(114, 0))
            wait(1)
            click(Pattern('youjian.jpg').targetOffset(114, 35))
            wait(1)
            print('++不再提醒++')
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
            print(e)
            time.sleep(30)
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
