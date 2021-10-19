# coding:utf-8
import os
import re

lua_xiaoyu = r'F:\svn\Lua\xiaoyu\uc.lua'
lua_kuaizip = r'F:\svn\Lua\kuaizip\uc.lua'
lua_kantu = r'F:\svn\Lua\ABCkantu\uc.lua'
lua_heinote = r'F:\svn\Lua\heinote\uc.lua'
lua_finder = r'F:\svn\Lua\finder\uc.lua'
lua_browser = r'F:\svn\Lua\7654browser\v1.0.0.2\uc.lua'
lua_lszip = r'F:\svn\Lua\lszip\uc.lua'
lua_xinnote = r'F:\svn\Lua\xinnote\uc.lua'
lua_qjpdf = r'F:\svn\Lua\qingjiepdf\uc.lua'
lua_smartlook = r'F:\svn\Lua\smartlook\uc.lua'
lua_cloudbar = r'F:\svn\Lua\CloudsToolbar\uc.lua'
lua_haotu = r'F:\svn\Lua\haotukankan\uc.lua'
lua_xxbz = r'F:\svn\Lua\xxbz\new.lua'
lua_xfpdf = r'F:\svn\Lua\xuanfengpdf\bundle_updatechecker.lua'
lua_jcbz = r'F:\svn\Lua\jcwallpaper\new.lua'
lua_sesame = r'F:\svn\Lua\srf\uc.lua'

p_xiaoyu = ['bgdcvn', 'bqpb', 'bqtp', 'bqyptp', 'fjvuhhwuvr', 'fregnhfwew', 'instrument', 'jafreqfrq', 'melancholy', 'mkiuhn', 'qwaszx', 'sfrhhgt2345Uninst',
            'spoiler', 'srzy2345setting', 'sysssnew', 'wfreqhfure', 'xymn', 'xytipsxhVV12', 'xytipsxytt', 'xytpopoth', 'yb32345setting']
p_kuaizip = ['aghghf', 'kzyptp', 'Jxohft', 'enthusiastic', 'YVyVcPZzs', 'hdagf', 'kuaiyatuop', 'alkanePanda', 'gshuhg', 'kwGOkLeLvH', 'Alcohol', 'basin',
             'polarbear', 'restless', 'tghfsdg', 'wbdyl', 'lakesi', 'Selenarctos', 'Kuaipb', 'vbvcxf', 'Eg_NNIfiu', 'VLscDaseKX', 'kuaiyatipsrytx', 'qbylwl',
             'kuaiyatpopxxrl', 'kuaiyatpopxktt', 'ghsauk', 'pineapple', 'torque', 'hfhsbv', 'kuaiyaminixktt']
p_kantu = ['gtwfrgt2345Uninst.exe', 'ABCminixktt', 'tbadjswsr', 'sceuhfure', 'okquery', 'topether', 'lavenderhi', 'gnwgd2345Uninst', 'Shawnmend',
           'sfrhwg12345setting', 'ktpb', 'ABCtpopxktt', 'ABCtpoprytx', 'viewmnqtqd', 'armois', 'Xiralimy', 'Danuvius', 'Cuttings']
p_heinote = ['fddgfuwgfywjd', 'dvwertbtf', 'qywtgj', 'Jsbyptp', 'siuywteinbg', 'stone', 'xiaoheitipsrytx', 'xiaoheiminixhtt', 'xiaoheitipsxhtt', 'bhajiy',
             'heipan', 'pbxhone', 'ejtspfs2345setting', 'fhreywfysa', 'mkiayhb', 'hfbrwfrg2345Uninst', '62345setting', 'xiaoheitpopxhtt', 'jrwpvfn2345setting',
             'njaiah', 'nbxvchidi']
p_finder = ['GStipsrytx', 'BaWrnG', 'WtZTlg', 'bdjsq', 'Sisrwl', 'GStpoprytx', 'ssyptp', 'TEnMhP', '22345setting', 'IEKmKY', 'ssfloattip', '12345setting',
            'GSscreensaver', 'asajksa', 'GStipsxktt', 'gsurl', 'diploma', 'SNss', 'vvhTdX', 'srpanka', 'gstpopgstt']
p_browser = ['7654llqtips', 'thrill', 'fracturesl', 'reunion', '7654weather', '7654renwulan', 'kk', 'changes', '7654llqtuopan', 'llqfloattip', 'aiouniya',
             'llqyptips', '7654llqurl', 'borealis', '7654pb']
p_lszip = ['Lstpopzip', 'lshighzip', 'vYZjaDIRY', 'Zzhwqfdfg', 'yxJLQvVM', 'Lshenzip', '12345ShellPro', 'IhdbzaAq', 'cbxOKVlhA', 'Lstrayzip', 'yGdcOyvz',
           'Dyaqxzp', 'HYbnhjkxs', 'cSskSwZ', 'a2345NetFlow', 'XxndaD']
p_xinnote = ['vfplaw2345setting', 'dsdnfjrbef', 'jskugi', 'bhagywi', 'cjblue', 'nhefbredf2345Uninst', 'xinnotegjsnsf', 'usfrbzq2345setting', 'xknllabwrk',
             'xinnotemini', 'xintray', 'xinnotetips', 'fsbtesadfg']
p_qjpdf = ['sWXluJ', 'dqsPl', 'crevice', '22345LSPFix', 'mxqjPO', 'a2345NetFlow', 'Jskjdi', 'sxcde', 'mxLK', 'llpokj', 'mBErTV', 'peimg', 'update', 'ZFCEa']
p_smartlook = ['uDLGUe', 'rsgaBg', 'dailyfresh', 'hardware', 'rsvaBg', 'kDLGUe', 'dessertcookies', 'G2y6S', 'personalcare', 'NyVBT', 'LznGsZ', 'rlwid',
               'AjFitD', 'extider', 'ZiQSGY', 'seasonalfresh', 'ghierh']
p_cloudbar = ['episode', 'superb', 'Gjlground', 'humidity', 'stitch', 'minor', 'chord']
p_haotu = ['baizhe', 'htkktpoprytx', 'mqtyrp', 'xwView', 'zztpopkk', 'Lolzzcxx', 'Hyzus', 'Weather', 'amkfiopg', 'E240.TMP', 'gajfgk', 'Update', 'htkktp',
           'xiaomitao', 'jgklfdgu']
p_xxbz = ['Calftp', 'Pasture', 'Calendar', 'NVIDIRNM', 'routine', 'xxbztpopxx', 'bztp', 'beard', 'participate', 'sunjuly']
p_xfpdf = ['xftpopxftt', 'LUxNQvY', 'nbhgbd', 'xfminixftt', 'Gijmkxuf', 'xftipspdf', 'tvPPlZ', 'FGxWFah', 'xftrayflash', 'WzsklOG', 'xfwJmu7Y', 'ghDSQgF',
           'mMNOcV', 'oJiyZjS', 'XFtnewsxftt']
p_jcbz = ['yearn', 'expat', 'Jcbztips', 'celery', '32345Uninst', 'anthem', 'respond', 'Jcbztray', 'flexible', 'Weaver', 'Jcbzmini', '42345Unist', 'cjblue',
          'chord', '52345Uninst']
p_sesame = ['dessertcookies', 'srfminiwwt', 'hardware', 'srftipsWV23', 'srftpopwwm']


def get_p(project=None):
    p_list = []
    lua_project = globals()['lua_' + project]
    if os.path.isfile(lua_project):
        with open(lua_project, encoding="utf-8") as file:
            for line in file:
                # urls = re.compile(r'localname = "(.*?)"',line)
                pattern = re.compile(r'localname = "(.*?)"')
                result = pattern.findall(line)
                if result:
                    p = result[-1]
                    p_list.append(p)
            p_list_new = sorted(list(set(p_list)))
    else:
        print('文件不存在')
    # print(p_list_new)
    return p_list_new


def change():
    projects = ['xiaoyu', 'kuaizip', 'kantu', 'heinote', 'finder', 'browser', 'lszip', 'xinnote', 'qjpdf', 'cloudbar', 'haotu', 'xxbz', 'smartlook', 'xfpdf',
                'jcbz', 'sesame']
    for i in range(len(projects)):
        project = projects[i]
        p_list_new = get_p(project)
        p_list_old = sorted(globals()['p_' + project])
        if p_list_new != p_list_old:
            print(f'{project} 进程有更新', p_list_new)
        else:
            print(f'{project} no change')


if __name__ == '__main__':
    change()
