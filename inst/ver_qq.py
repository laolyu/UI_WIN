# -*- coding: utf-8 -*-
import random
import threading
import time


def version(project):
    version = {'mxiaoyu': ['xiaoyu_v3.2.1.7_guanwang_1.exe -wjm', 'xiaoyu_v3.2.1.7_guanwang_2.exe -wjm', 'xiaoyu_v3.2.1.7_guanwang_3.exe -wjm',
                           'xiaoyu_v3.2.1.7_guanwang_4.exe -wjm', 'xiaoyu_v3.2.1.7_guanwang_5.exe -wjm',
                           'xiaoyu_v3.3.0.2_guanwang_1.exe -wjm', 'xiaoyu_v3.3.0.2_guanwang_2.exe -wjm', 'xiaoyu_v3.3.0.2_guanwang_3.exe -wjm',
                           'xiaoyu_v3.3.0.2_guanwang_4.exe -wjm', 'xiaoyu_v3.3.0.2_guanwang_5.exe -wjm',
                           'xiaoyu_v3.3.0.3_guanwang_1.exe -wjm', 'xiaoyu_v3.3.0.3_guanwang_2.exe -wjm', 'xiaoyu_v3.3.0.3_guanwang_3.exe -wjm',
                           'xiaoyu_v3.3.0.3_guanwang_4.exe -wjm', 'xiaoyu_v3.3.0.3_guanwang_5.exe -wjm',
                           'xiaoyu_v3.3.0.4_guanwang_1.exe -wjm', 'xiaoyu_v3.3.0.4_guanwang_2.exe -wjm', 'xiaoyu_v3.3.0.4_guanwang_3.exe -wjm',
                           'xiaoyu_v3.3.0.4_guanwang_4.exe -wjm', 'xiaoyu_v3.3.0.4_guanwang_5.exe -wjm',
                           'xiaoyu_v3.3.0.6_guanwang_1.exe -wjm', 'xiaoyu_v3.3.0.6_guanwang_2.exe -wjm', 'xiaoyu_v3.3.0.6_guanwang_3.exe -wjm',
                           'xiaoyu_v3.3.0.6_guanwang_4.exe -wjm', 'xiaoyu_v3.3.0.6_guanwang_5.exe -wjm',
                           # 'xiaoyu_v3.3.0.7_guanwang_1.exe -wjm', 'xiaoyu_v3.3.0.7_guanwang_2.exe -wjm', 'xiaoyu_v3.3.0.7_guanwang_3.exe -wjm',
                           # 'xiaoyu_v3.3.0.7_guanwang_4.exe -wjm', 'xiaoyu_v3.3.0.7_guanwang_5.exe -wjm'
                           ],  # 3306,3307金山不测
               'mkuai': [
                   'KuaiZip_Setup_v3.2.3.8_guanwang_1.exe -wjm', 'KuaiZip_Setup_v3.2.3.8_guanwang_2.exe -wjm', 'KuaiZip_Setup_v3.2.3.8_guanwang_3.exe -wjm',
                   'KuaiZip_Setup_v3.2.3.8_guanwang_4.exe -wjm', 'KuaiZip_Setup_v3.2.3.8_guanwang_5.exe -wjm',
                   'KuaiZip_Setup_v3.2.3.9_guanwang_1.exe -wjm', 'KuaiZip_Setup_v3.2.3.9_guanwang_2.exe -wjm', 'KuaiZip_Setup_v3.2.3.9_guanwang_3.exe -wjm',
                   'KuaiZip_Setup_v3.2.3.9_guanwang_4.exe -wjm', 'KuaiZip_Setup_v3.2.3.9_guanwang_5.exe -wjm',
                   'KuaiZip_Setup_v3.3.0.3_guanwang_1.exe -wjm', 'KuaiZip_Setup_v3.3.0.3_guanwang_2.exe -wjm', 'KuaiZip_Setup_v3.3.0.3_guanwang_3.exe -wjm',
                   'KuaiZip_Setup_v3.3.0.3_guanwang_4.exe -wjm', 'KuaiZip_Setup_v3.3.0.3_guanwang_5.exe -wjm',
                   'KuaiZip_Setup_v3.3.0.5_guanwang_1.exe -wjm', 'KuaiZip_Setup_v3.3.0.5_guanwang_2.exe -wjm', 'KuaiZip_Setup_v3.3.0.5_guanwang_3.exe -wjm',
                   'KuaiZip_Setup_v3.3.0.5_guanwang_4.exe -wjm', 'KuaiZip_Setup_v3.3.0.5_guanwang_5.exe -wjm',
                   'KuaiZip_Setup_v3.3.0.7_guanwang_1.exe -wjm', 'KuaiZip_Setup_v3.3.0.7_guanwang_2.exe -wjm', 'KuaiZip_Setup_v3.3.0.7_guanwang_3.exe -wjm',
                   'KuaiZip_Setup_v3.3.0.7_guanwang_4.exe -wjm', 'KuaiZip_Setup_v3.3.0.7_guanwang_5.exe -wjm',
                   'KuaiZip_Setup_v3.3.1.2_guanwang_1.exe -wjm', 'KuaiZip_Setup_v3.3.1.2_guanwang_2.exe -wjm', 'KuaiZip_Setup_v3.3.1.2_guanwang_3.exe -wjm',
                   'KuaiZip_Setup_v3.3.1.2_guanwang_4.exe -wjm', 'KuaiZip_Setup_v3.3.1.2_guanwang_5.exe -wjm',
               ],

               'mabc': [
                   # 'PhotoViewer_Setup_v3.2.2.8_guanwang_1.exe -wjm', 'PhotoViewer_Setup_v3.2.2.8_guanwang_2.exe -wjm',
                   # 'PhotoViewer_Setup_v3.2.2.8_guanwang_3.exe -wjm', 'PhotoViewer_Setup_v3.2.2.8_guanwang_4.exe -wjm',
                   # 'PhotoViewer_Setup_v3.2.2.8_guanwang_5.exe -wjm',
                   # 'PhotoViewer_Setup_v3.3.0.2_guanwang_1.exe -wjm', 'PhotoViewer_Setup_v3.3.0.2_guanwang_2.exe -wjm',
                   # 'PhotoViewer_Setup_v3.3.0.2_guanwang_3.exe -wjm',
                   # 'PhotoViewer_Setup_v3.3.0.2_guanwang_4.exe -wjm', 'PhotoViewer_Setup_v3.3.0.2_guanwang_5.exe -wjm',
                   'PhotoViewer_Setup_v3.3.0.3_guanwang_1.exe -wjm', 'PhotoViewer_Setup_v3.3.0.3_guanwang_2.exe -wjm',
                   'PhotoViewer_Setup_v3.3.0.3_guanwang_3.exe -wjm', 'PhotoViewer_Setup_v3.3.0.3_guanwang_4.exe -wjm',
                   'PhotoViewer_Setup_v3.3.0.3_guanwang_5.exe -wjm',
                   # 'PhotoViewer_Setup_v3.3.0.4_guanwang_1.exe -wjm', 'PhotoViewer_Setup_v3.3.0.4_guanwang_2.exe -wjm',
                   # 'PhotoViewer_Setup_v3.3.0.4_guanwang_3.exe -wjm', 'PhotoViewer_Setup_v3.3.0.4_guanwang_4.exe -wjm',
                   # 'PhotoViewer_Setup_v3.3.0.4_guanwang_5.exe -wjm',
                   'PhotoViewer_Setup_v3.3.0.6_guanwang_1.exe -wjm', 'PhotoViewer_Setup_v3.3.0.6_guanwang_2.exe -wjm',
                   'PhotoViewer_Setup_v3.3.0.6_guanwang_3.exe -wjm', 'PhotoViewer_Setup_v3.3.0.6_guanwang_4.exe -wjm',
                   'PhotoViewer_Setup_v3.3.0.6_guanwang_5.exe -wjm'
               ],
               'mxiaohei': ['Heinote_v3.2.2.5_guanwang_1.exe -wjm', 'Heinote_v3.2.2.5_guanwang_2.exe -wjm', 'Heinote_v3.2.2.5_guanwang_3.exe -wjm',
                            'Heinote_v3.2.2.5_guanwang_4.exe -wjm', 'Heinote_v3.2.2.5_guanwang_5.exe -wjm',
                            # 'Heinote_v3.3.0.1_guanwang_1.exe -wjm',
                            # 'Heinote_v3.3.0.1_guanwang_2.exe -wjm', 'Heinote_v3.3.0.1_guanwang_3.exe -wjm', 'Heinote_v3.3.0.1_guanwang_4.exe -wjm',
                            # 'Heinote_v3.3.0.1_guanwang_5.exe -wjm',
                            'Heinote_v3.3.0.2_guanwang_1.exe -wjm', 'Heinote_v3.3.0.2_guanwang_2.exe -wjm', 'Heinote_v3.3.0.2_guanwang_3.exe -wjm',
                            'Heinote_v3.3.0.2_guanwang_4.exe -wjm', 'Heinote_v3.3.0.2_guanwang_5.exe -wjm',
                            'xinnote_v2.1.0.1_guanwang_1.exe -wjm', 'xinnote_v2.1.0.1_guanwang_2.exe -wjm', 'xinnote_v2.1.0.1_guanwang_3.exe -wjm',
                            'xinnote_v2.1.0.1_guanwang_4.exe -wjm', 'xinnote_v2.1.0.1_guanwang_5.exe -wjm',
                            'xinnote_v2.1.0.4_guanwang_1.exe -wjm', 'xinnote_v2.1.0.4_guanwang_2.exe -wjm', 'xinnote_v2.1.0.4_guanwang_3.exe -wjm',
                            'xinnote_v2.1.0.4_guanwang_4.exe -wjm', 'xinnote_v2.1.0.4_guanwang_5.exe -wjm'],
               'mguangsu': [
                   'Finder_Setup_3.2.2.6_guanwang_1.exe -wjm', 'Finder_Setup_3.2.2.6_guanwang_2.exe -wjm', 'Finder_Setup_3.2.2.6_guanwang_3.exe -wjm',
                   'Finder_Setup_3.2.2.6_guanwang_4.exe -wjm', 'Finder_Setup_3.2.2.6_guanwang_5.exe -wjm',
                   'Finder_Setup_3.3.0.1_guanwang_1.exe -wjm',
                   'Finder_Setup_3.3.0.1_guanwang_2.exe -wjm', 'Finder_Setup_3.3.0.1_guanwang_3.exe -wjm', 'Finder_Setup_3.3.0.1_guanwang_4.exe -wjm',
                   'Finder_Setup_3.3.0.1_guanwang_5.exe -wjm',
                   'Finder_Setup_3.3.0.5_guanwang_1.exe -wjm', 'Finder_Setup_3.3.0.5_guanwang_2.exe -wjm', 'Finder_Setup_3.3.0.5_guanwang_3.exe -wjm',
                   'Finder_Setup_3.3.0.5_guanwang_4.exe -wjm', 'Finder_Setup_3.3.0.5_guanwang_5.exe -wjm',
                   'CalfWallpaper_v1.0.3.5_guangwang_1.exe -wjm', 'CalfWallpaper_v1.0.3.5_guangwang_2.exe -wjm',
                   'CalfWallpaper_v1.0.3.5_guangwang_3.exe -wjm', 'CalfWallpaper_v1.0.3.5_guangwang_4.exe -wjm',
                   'CalfWallpaper_v1.0.3.5_guangwang_5.exe -wjm',
                   'JCWallpaper_v1.0.1.0_guanwang_1.exe  -wjm', 'JCWallpaper_v1.0.1.0_guanwang_2.exe  -wjm', 'JCWallpaper_v1.0.1.0_guanwang_3.exe  -wjm',
                   'JCWallpaper_v1.0.1.0_guanwang_4.exe  -wjm', 'JCWallpaper_v1.0.1.0_guanwang_5.exe  -wjm',
                   'JCWallpaper_v1.1.0.3_guanwang_1.exe  -wjm', 'JCWallpaper_v1.1.0.3_guanwang_2.exe  -wjm', 'JCWallpaper_v1.1.0.3_guanwang_3.exe  -wjm',
                   'JCWallpaper_v1.1.0.3_guanwang_4.exe  -wjm', 'JCWallpaper_v1.1.0.3_guanwang_5.exe  -wjm',

                   # 'JCWallpaper_v1.1.0.7_guanwang_1.exe  -wjm', 'JCWallpaper_v1.1.0.7_guanwang_2.exe  -wjm', 'JCWallpaper_v1.1.0.7_guanwang_3.exe  -wjm',
                   # 'JCWallpaper_v1.1.0.7_guanwang_4.exe  -wjm','JCWallpaper_v1.1.0.7_guanwang_5.exe  -wjm'# 1107只测金山
               ],
               'mllq': [
                   '7654Browser_v3.1.1.2_guanwang_1.exe -wjm', '7654Browser_v3.1.1.2_guanwang_2.exe -wjm', '7654Browser_v3.1.1.2_guanwang_3.exe -wjm',
                   '7654Browser_v3.1.1.2_guanwang_4.exe -wjm', '7654Browser_v3.1.1.2_guanwang_5.exe -wjm',  # 金山不测

                   'haotu_v2.0.3.8_guanwang_1.exe -wjm', 'haotu_v2.0.3.8_guanwang_2.exe -wjm', 'haotu_v2.0.3.8_guanwang_3.exe -wjm',
                   'haotu_v2.0.3.8_guanwang_4.exe -wjm', 'haotu_v2.0.3.8_guanwang_5.exe -wjm',
                   'haotu_v2.1.0.3_guanwang_1.exe -wjm', 'haotu_v2.1.0.3_guanwang_2.exe -wjm', 'haotu_v2.1.0.3_guanwang_3.exe -wjm',
                   'haotu_v2.1.0.3_guanwang_4.exe -wjm', 'haotu_v2.1.0.3_guanwang_5.exe -wjm',
                   'haotu_v2.1.0.4_guanwang_1.exe -wjm', 'haotu_v2.1.0.4_guanwang_2.exe -wjm', 'haotu_v2.1.0.4_guanwang_3.exe -wjm',
                   'haotu_v2.1.0.4_guanwang_4.exe -wjm', 'haotu_v2.1.0.4_guanwang_5.exe -wjm',
                   'haotu_v2.1.0.5_guanwang_1.exe -wjm', 'haotu_v2.1.0.5_guanwang_2.exe -wjm', 'haotu_v2.1.0.5_guanwang_3.exe -wjm',
                   'haotu_v2.1.0.5_guanwang_4.exe -wjm', 'haotu_v2.1.0.5_guanwang_5.exe -wjm',  # 2105,360不测
                   'haotu_v2.1.0.6_guanwang_1.exe -wjm', 'haotu_v2.1.0.6_guanwang_2.exe -wjm', 'haotu_v2.1.0.6_guanwang_3.exe -wjm',
                   'haotu_v2.1.0.6_guanwang_4.exe -wjm', 'haotu_v2.1.0.6_guanwang_5.exe -wjm'
               ],
               'lszip': ['LsZip_Setup_v1.0.1.3_guanwang_1.exe -wjm', 'LsZip_Setup_v1.0.1.3_guanwang_2.exe -wjm', 'LsZip_Setup_v1.0.1.3_guanwang_3.exe -wjm',
                         'LsZip_Setup_v1.0.1.3_guanwang_4.exe -wjm', 'LsZip_Setup_v1.0.1.3_guanwang_5.exe -wjm',
                         'LsZip_Setup_v1.1.0.2_guanwang_1.exe -wjm', 'LsZip_Setup_v1.1.0.2_guanwang_2.exe -wjm', 'LsZip_Setup_v1.1.0.2_guanwang_3.exe -wjm',
                         'LsZip_Setup_v1.1.0.2_guanwang_4.exe -wjm', 'LsZip_Setup_v1.1.0.2_guanwang_5.exe -wjm',
                         'LsZip_Setup_v1.1.0.4_guanwang_1.exe -wjm', 'LsZip_Setup_v1.1.0.4_guanwang_2.exe -wjm', 'LsZip_Setup_v1.1.0.4_guanwang_3.exe -wjm',
                         'LsZip_Setup_v1.1.0.4_guanwang_4.exe -wjm', 'LsZip_Setup_v1.1.0.4_guanwang_5.exe -wjm',
                         'XFPdf_Setup_v1.0.3.7_guanwang_1.exe -wjm', 'XFPdf_Setup_v1.0.3.7_guanwang_2.exe -wjm', 'XFPdf_Setup_v1.0.3.7_guanwang_3.exe -wjm',
                         'XFPdf_Setup_v1.0.3.7_guanwang_4.exe -wjm', 'XFPdf_Setup_v1.0.3.7_guanwang_5.exe -wjm',
                         'XFPdf_Setup_v1.0.3.8_guanwang_1.exe -wjm', 'XFPdf_Setup_v1.0.3.8_guanwang_2.exe -wjm', 'XFPdf_Setup_v1.0.3.8_guanwang_3.exe -wjm',
                         'XFPdf_Setup_v1.0.3.8_guanwang_4.exe -wjm', 'XFPdf_Setup_v1.0.3.8_guanwang_5.exe -wjm',
                         'XFPdf_Setup_v1.0.4.0_guanwang_1.exe -wjm', 'XFPdf_Setup_v1.0.4.0_guanwang_2.exe -wjm', 'XFPdf_Setup_v1.0.4.0_guanwang_3.exe -wjm',
                         'XFPdf_Setup_v1.0.4.0_guanwang_4.exe -wjm', 'XFPdf_Setup_v1.0.4.0_guanwang_5.exe -wjm',  # 360旋风pdf不测
                         ],
               'gjl': ['preview_Setup_1.0.2.9_guanwang_1.exe -wjm', 'preview_Setup_1.0.2.9_guanwang_2.exe -wjm', 'preview_Setup_1.0.2.9_guanwang_3.exe -wjm',
                       'preview_Setup_1.0.2.9_guanwang_4.exe -wjm', 'preview_Setup_1.0.2.9_guanwang_5.exe -wjm',

                       'clouds_setup_v1.1.0.8_guanwang_1.exe -wjm', 'clouds_setup_v1.1.0.8_guanwang_2.exe -wjm', 'clouds_setup_v1.1.0.8_guanwang_3.exe -wjm',
                       'clouds_setup_v1.1.0.8_guanwang_4.exe -wjm', 'clouds_setup_v1.1.0.8_guanwang_5.exe -wjm',
                       # gjl,1105只测金山环境

                       'Sesame_Setup_v1.0.1.6_guangwang_1.exe -wjm', 'Sesame_Setup_v1.0.1.6_guangwang_2.exe -wjm', 'Sesame_Setup_v1.0.1.6_guangwang_3.exe -wjm',
                       'Sesame_Setup_v1.0.1.6_guangwang_4.exe -wjm', 'Sesame_Setup_v1.0.1.6_guangwang_5.exe -wjm'  # 金山已知报毒
                       ],
               'qjpdf': ['QingJiePdf_Setup_v1.0.1.4_guanwang_1.exe  -wjm', 'QingJiePdf_Setup_v1.0.1.4_guanwang_2.exe  -wjm',
                         'QingJiePdf_Setup_v1.0.1.4_guanwang_3.exe  -wjm', 'QingJiePdf_Setup_v1.0.1.4_guanwang_4.exe  -wjm',
                         'QingJiePdf_Setup_v1.0.1.4_guanwang_5.exe  -wjm',
                         'QingJiePdf_Setup_v1.0.1.5_guanwang_1.exe  -wjm', 'QingJiePdf_Setup_v1.0.1.5_guanwang_2.exe  -wjm',
                         'QingJiePdf_Setup_v1.0.1.5_guanwang_3.exe  -wjm', 'QingJiePdf_Setup_v1.0.1.5_guanwang_4.exe  -wjm',
                         'QingJiePdf_Setup_v1.0.1.5_guanwang_5.exe  -wjm',
                         'QingJiePdf_Setup_v1.1.0.2_guanwang_1.exe  -wjm', 'QingJiePdf_Setup_v1.1.0.2_guanwang_2.exe  -wjm',
                         'QingJiePdf_Setup_v1.1.0.2_guanwang_3.exe  -wjm', 'QingJiePdf_Setup_v1.1.0.2_guanwang_4.exe  -wjm',
                         'QingJiePdf_Setup_v1.1.0.2_guanwang_5.exe  -wjm',
                         'QingJiePdf_Setup_v1.1.0.3_guanwang_1.exe  -wjm', 'QingJiePdf_Setup_v1.1.0.3_guanwang_2.exe  -wjm',
                         'QingJiePdf_Setup_v1.1.0.3_guanwang_3.exe  -wjm', 'QingJiePdf_Setup_v1.1.0.3_guanwang_4.exe  -wjm',
                         'QingJiePdf_Setup_v1.1.0.3_guanwang_5.exe  -wjm',  # 1102 1103金山不测
                         ],
               }

    return version[project]


if __name__ == '__main__':
    version(project='no_vc_project')
