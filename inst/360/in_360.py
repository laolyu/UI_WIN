# -*- coding: utf-8 -*-
import datetime
import subprocess
# import threading
from lackey import *
import sys
from loguru import logger
from random import sample

Settings.InfoLogs = False
sys.path.append(r'C:\zm\script\gjl')


def version():
    vc = ['xiaoyu_v3.2.1.7_guanwang_1.exe -wjm', 'xiaoyu_v3.2.1.7_guanwang_2.exe -wjm', 'xiaoyu_v3.2.1.7_guanwang_3.exe -wjm',
          'xiaoyu_v3.2.1.7_guanwang_4.exe -wjm', 'xiaoyu_v3.2.1.7_guanwang_5.exe -wjm',
          'xiaoyu_v3.3.0.2_guanwang_1.exe -wjm', 'xiaoyu_v3.3.0.2_guanwang_3.exe -wjm',
          'xiaoyu_v3.3.1.0_guanwang_1.exe -wjm', 'xiaoyu_v3.3.1.0_guanwang_2.exe -wjm', 'xiaoyu_v3.3.1.0_guanwang_3.exe -wjm',
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

          'JCWallpaper_v1.1.0.3_guanwang_1.exe  -wjm', 'JCWallpaper_v1.1.0.3_guanwang_2.exe  -wjm', 'JCWallpaper_v1.1.0.3_guanwang_3.exe  -wjm',
          'JCWallpaper_v1.1.0.3_guanwang_4.exe  -wjm', 'JCWallpaper_v1.1.0.3_guanwang_5.exe  -wjm',
          'JCWallpaper_Setup_v1.1.1.1_guanwang_1.exe -wjm', 'JCWallpaper_Setup_v1.1.1.1_guanwang_2.exe -wjm',
          'JCWallpaper_Setup_v1.1.1.1_guanwang_3.exe -wjm',  # 'JCWallpaper_Setup_v1.1.1.1_guanwang_4.exe -wjm',
          # 'JCWallpaper_Setup_v1.1.1.1_guanwang_5.exe -wjm',

          '7654Browser_v3.1.1.2_guanwang_1.exe -wjm', '7654Browser_v3.1.1.2_guanwang_2.exe -wjm', '7654Browser_v3.1.1.2_guanwang_3.exe -wjm',
          '7654Browser_v3.1.1.2_guanwang_4.exe -wjm', '7654Browser_v3.1.1.2_guanwang_5.exe -wjm',  # 金山不测

          'haotu_v2.1.0.6_guanwang_1.exe -wjm', 'haotu_v2.1.0.6_guanwang_2.exe -wjm', 'haotu_v2.1.0.6_guanwang_3.exe -wjm',
          'haotu_v2.1.0.6_guanwang_4.exe -wjm', 'haotu_v2.1.0.6_guanwang_5.exe -wjm',

          'Heinote_v3.3.0.2_guanwang_1.exe -wjm', 'Heinote_v3.3.0.2_guanwang_2.exe -wjm', 'Heinote_v3.3.0.2_guanwang_3.exe -wjm',
          'Heinote_v3.3.0.2_guanwang_4.exe -wjm', 'Heinote_v3.3.0.2_guanwang_5.exe -wjm',
          'Heinote_v3.3.0.6_guanwang_1.exe -wjm', 'Heinote_v3.3.0.6_guanwang_2.exe -wjm', 'Heinote_v3.3.0.6_guanwang_3.exe -wjm',
          'Heinote_v3.3.0.6_guanwang_4.exe -wjm', 'Heinote_v3.3.0.6_guanwang_5.exe -wjm',

          'xinnote_v2.1.0.4_guanwang_1.exe -wjm', 'xinnote_v2.1.0.4_guanwang_2.exe -wjm', 'xinnote_v2.1.0.4_guanwang_3.exe -wjm',
          'xinnote_v2.1.0.4_guanwang_4.exe -wjm', 'xinnote_v2.1.0.4_guanwang_5.exe -wjm',
          'Finder_Setup_3.3.0.5_guanwang_1.exe -wjm', 'Finder_Setup_3.3.0.5_guanwang_2.exe -wjm',
          # 'Finder_Setup_3.3.0.5_guanwang_3.exe -wjm',
          'Finder_Setup_3.3.0.5_guanwang_4.exe -wjm', 'Finder_Setup_3.3.0.5_guanwang_5.exe -wjm',

          'CalfWallpaper_v1.0.3.5_guangwang_1.exe -wjm', 'CalfWallpaper_v1.0.3.5_guangwang_2.exe -wjm',
          'CalfWallpaper_v1.0.3.5_guangwang_3.exe -wjm', 'CalfWallpaper_v1.0.3.5_guangwang_4.exe -wjm',
          'CalfWallpaper_v1.0.3.5_guangwang_5.exe -wjm',

          'LsZip_Setup_v1.0.1.3_guanwang_1.exe -wjm', 'LsZip_Setup_v1.0.1.3_guanwang_2.exe -wjm', 'LsZip_Setup_v1.0.1.3_guanwang_3.exe -wjm',
          'LsZip_Setup_v1.0.1.3_guanwang_4.exe -wjm', 'LsZip_Setup_v1.0.1.3_guanwang_5.exe -wjm',
          # 'LsZip_Setup_v1.1.0.2_guanwang_1.exe -wjm', 'LsZip_Setup_v1.1.0.2_guanwang_2.exe -wjm', 'LsZip_Setup_v1.1.0.2_guanwang_3.exe -wjm',
          # 'LsZip_Setup_v1.1.0.2_guanwang_4.exe -wjm', 'LsZip_Setup_v1.1.0.2_guanwang_5.exe -wjm',
          'LsZip_Setup_v1.1.0.4_guanwang_1.exe -wjm', 'LsZip_Setup_v1.1.0.4_guanwang_2.exe -wjm', 'LsZip_Setup_v1.1.0.4_guanwang_3.exe -wjm',
          'LsZip_Setup_v1.1.0.4_guanwang_4.exe -wjm', 'LsZip_Setup_v1.1.0.4_guanwang_5.exe -wjm',

          'xlpreview_Setup_v1.0.0.7_guanwang_1.exe -wjm', 'xlpreview_Setup_v1.0.0.7_guanwang_2.exe -wjm',
          'xlpreview_Setup_v1.0.0.7_guanwang_3.exe -wjm', 'xlpreview_Setup_v1.0.0.7_guanwang_4.exe -wjm',
          'xlpreview_Setup_v1.0.0.7_guanwang_5.exe -wjm',

          'clouds_setup_v1.1.0.8_guanwang_1.exe -wjm', 'clouds_setup_v1.1.0.8_guanwang_2.exe -wjm', 'clouds_setup_v1.1.0.8_guanwang_3.exe -wjm',
          'clouds_setup_v1.1.0.8_guanwang_4.exe -wjm', 'clouds_setup_v1.1.0.8_guanwang_5.exe -wjm',  # 不测金山

          'Sesame_Setup_v1.0.1.6_guangwang_1.exe -wjm', 'Sesame_Setup_v1.0.1.6_guangwang_2.exe -wjm', 'Sesame_Setup_v1.0.1.6_guangwang_3.exe -wjm',
          'Sesame_Setup_v1.0.1.6_guangwang_4.exe -wjm', 'Sesame_Setup_v1.0.1.6_guangwang_5.exe -wjm',  # 金山已知报毒

          'KuaiZip_Setup_v3.3.0.3_guanwang_1.exe -wjm', 'KuaiZip_Setup_v3.3.0.3_guanwang_2.exe -wjm', 'KuaiZip_Setup_v3.3.0.3_guanwang_3.exe -wjm',
          'KuaiZip_Setup_v3.3.0.3_guanwang_4.exe -wjm', 'KuaiZip_Setup_v3.3.0.3_guanwang_5.exe -wjm',
          'KuaiZip_Setup_v3.3.0.7_guanwang_1.exe -wjm', 'KuaiZip_Setup_v3.3.0.7_guanwang_2.exe -wjm', 'KuaiZip_Setup_v3.3.0.7_guanwang_3.exe -wjm',
          'KuaiZip_Setup_v3.3.0.7_guanwang_4.exe -wjm', 'KuaiZip_Setup_v3.3.0.7_guanwang_5.exe -wjm',
          'KuaiZip_Setup_v3.3.1.2_guanwang_1.exe -wjm', 'KuaiZip_Setup_v3.3.1.2_guanwang_2.exe -wjm', 'KuaiZip_Setup_v3.3.1.2_guanwang_3.exe -wjm',
          'KuaiZip_Setup_v3.3.1.2_guanwang_4.exe -wjm', 'KuaiZip_Setup_v3.3.1.2_guanwang_5.exe -wjm',
          'KuaiZip_Setup_v3.3.1.4_guanwang_1.exe -wjm', 'KuaiZip_Setup_v3.3.1.4_guanwang_2.exe -wjm', 'KuaiZip_Setup_v3.3.1.4_guanwang_3.exe -wjm',
          'KuaiZip_Setup_v3.3.1.4_guanwang_4.exe -wjm', 'KuaiZip_Setup_v3.3.1.4_guanwang_5.exe -wjm',
          'KuaiZip_Setup_v3.3.1.8_guanwang_1.exe -wjm', 'KuaiZip_Setup_v3.3.1.8_guanwang_2.exe -wjm', 'KuaiZip_Setup_v3.3.1.8_guanwang_3.exe -wjm',
          'KuaiZip_Setup_v3.3.1.8_guanwang_4.exe -wjm', 'KuaiZip_Setup_v3.3.1.8_guanwang_5.exe -wjm',
          ]
    return vc


def UI():
    try:
        if exists("explorer.jpg", 1):
            logger.info('*******explorer stopped*********')
            type(Key.F11)
            wait(0.1)
            click(Pattern("explorer.jpg").targetOffset(0, 100))
            wait(0.1)
        if not exists("player.jpg", 1):
            try:
                subprocess.Popen('powershell.exe Stop-Process -name explorer', shell=True)
            except Exception as e:
                logger.info(e)
            try:
                subprocess.Popen('explorer', shell=True)
            except Exception as e:
                logger.info(e)
        if exists("install.jpg", 1):
            wait(0.1)
            click(Pattern("install.jpg").targetOffset(422, 126))
            wait(0.1)
            click(Pattern("install.jpg").targetOffset(422, 150))
            wait(0.1)
        elif exists("procp.jpg", 1):
            logger.info('********process protection********')
            type(Key.F11)
            wait(0.1)
            click(Pattern("procp.jpg").targetOffset(422, 150))
            wait("zuzhi.jpg")
            click(Pattern("zuzhi.jpg"))
            wait(0.1)
        if exists("bingdu.jpg", 1):
            logger.info('*********Virus removal***********')
            type(Key.F11)
            wait(0.1)
            click(Pattern("bingdu.jpg").targetOffset(159, -21))
            wait(0.1)
        else:
            pass
            # logger.info('no safe messages'
    except Exception as e:
        logger.info(e)


def cmd_send(path, vc_list):
    # logger.info('thread ->>%s is running...' % (threading.current_thread().name))
    now = datetime.datetime.now()
    s1 = now.strftime('%Y-%m-%d %H:%M:%S')

    for x in range(len(vc_list)):
        try:
            cmd = vc_list[x]
            logger.info(f'{cmd}')
        subprocess.Popen(cmd, cwd=path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except Exception as e:
        logger.info(e)


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
    UI()
    v = sample(version(), len(version()))
    cmd_send(path, v)
    logger.info('thread %s is ended...' % threading.current_thread().name)
