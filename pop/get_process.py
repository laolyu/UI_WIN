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

p_xiaoyu = ['avjnjmiuninst', 'bgdcvn', 'bqpb', 'bqtp', 'bqyptp', 'fregnhfwew', 'instrument', 'jafreqfrq', 'melancholy', 'mkiuhn', 'qwaszx', 'sfrhhgt2345Uninst',
            'spoiler', 'srzy2345setting', 'sysssnew', 'wfreqhfure', 'xymn', 'xypbuninst', 'xytipsxhVV12', 'xytipsxytt', 'xytpopoth', 'yb32345setting']
p_kuaizip = ['Eg_NNIfiu', 'Kuaipb', 'Selenarctos', 'VLscDaseKX', 'YVyVcPZzs', 'alkanePanda', 'kuaiyaminixktt', 'kuaiyatipsrytx', 'kuaiyatpopxktt',
             'kuaiyatpopxxrl', 'kuaiyatuop', 'kwGOkLeLvH', 'kzyptp', 'lakesi', 'leaps', 'parmiuninst', 'parpbuninst', 'partnuninst', 'polarbear', 'qbylwl',
             'restless', 'wbdyl']
p_kantu = ['ABCminixktt', 'ABCtpoprytx', 'ABCtpopxktt', 'Cuttings', 'Danuvius', 'Shawnmend', 'Xiralimy', 'armois', 'gnwgd2345Uninst', 'gtwfrgt2345Uninst.exe',
           'ktpb', 'ktpbuninst', 'ktsdmiuninst', 'lavenderhi', 'okquery', 'sceuhfure', 'sfrhwg12345setting', 'tbadjswsr', 'topether']
p_heinote = ['62345setting', 'Jsbyptp', 'bhajiy', 'djeafrhumiuninst', 'dvwertbtf', 'ejtspfs2345setting', 'fhreywfysa', 'heipan', 'hfbrwfrg2345Uninst',
             'mkiayhb', 'nbxvchidi', 'njaiah', 'pbxhone', 'qywtgj', 'siuywteinbg', 'stone', 'xhpbuninst', 'xiaoheiminixhtt', 'xiaoheitipsrytx',
             'xiaoheitipsxhtt', 'xiaoheitpopxhtt']
p_finder = ['12345setting', '22345setting', 'BaWrnG', 'GSscreensaver', 'GStipsrytx', 'GStipsxktt', 'GStpoprytx', 'IEKmKY', 'SNss', 'Sisrwl', 'Ssmiuninst',
            'TEnMhP', 'WtZTlg', 'asajksa', 'bdjsq', 'diploma', 'gstpopgstt', 'gsurl', 'srpanka', 'ssfloattip', 'sspbuninst', 'ssyptp', 'vvhTdX']
p_browser = ['7654llqtips', 'thrill', 'fracturesl', 'reunion', '7654weather', '7654renwulan', 'kk', 'changes', '7654llqtuopan', 'llqfloattip', 'aiouniya',
             'llqyptips', '7654llqurl', 'borealis', '7654pb']
p_lszip = ['12345ShellPro', 'IhdbzaAq', 'JzLtnuninst', 'KEtiuninst', 'Lshenzip', 'Lstpopzip', 'Lstrayzip', 'XxndaD', 'a2345NetFlow', 'cSskSwZ', 'cbxOKVlhA',
           'dhxmiuninst', 'lshighzip', 'vYZjaDIRY', 'yGdcOyvz', 'yxJLQvVM']
p_xinnote = ['bhagywi', 'cjblue', 'fdaggrmiuninst', 'jskugi', 'lngydemiuninst', 'nhefbredf2345Uninst', 'sfjegtmiuninst', 'sfjhafurg', 'usfrbzq2345setting',
             'vfplaw2345setting', 'xinnotemini', 'xinnotetips', 'xintray']
p_qjpdf = ['22345LeakFixer', 'Jskjdi', 'Qjqtiuninst', 'Qjqtnuninst', 'ZFCEa', 'dqsPl', 'mBErTV', 'mxLK', 'mxqjPO', 'peimg', 'qjqmiuninst', 'sWXluJ', 'update']
p_smartlook = ['uDLGUe', 'rsgaBg', 'dailyfresh', 'hardware', 'rsvaBg', 'kDLGUe', 'dessertcookies', 'G2y6S', 'personalcare', 'NyVBT', 'LznGsZ', 'rlwid',
               'AjFitD', 'extider', 'ZiQSGY', 'seasonalfresh', 'ghierh']
p_cloudbar = ['bartiuninst', 'bartnuninst', 'bartouninst', 'clomiuninst', 'episode', 'minor', 'superb']
p_haotu = ['baizhe', 'htkktpoprytx', 'mqtyrp', 'xwView', 'zztpopkk', 'Lolzzcxx', 'Hyzus', 'Weather', 'amkfiopg', 'E240.TMP', 'gajfgk', 'Update', 'htkktp',
           'xiaomitao', 'jgklfdgu']
p_xxbz = ['Calftp', 'Pasture', 'Calendar', 'NVIDIRNM', 'routine', 'xxbztpopxx', 'bztp', 'beard', 'participate', 'sunjuly']
p_xfpdf = ['xftpopxftt', 'LUxNQvY', 'nbhgbd', 'xfminixftt', 'Gijmkxuf', 'xftipspdf', 'tvPPlZ', 'FGxWFah', 'xftrayflash', 'WzsklOG', 'xfwJmu7Y', 'ghDSQgF',
           'mMNOcV', 'oJiyZjS', 'XFtnewsxftt']
p_jcbz = ['32345Uninst', '42345Uninst', '52345Uninst', 'Jcbzmini', 'Jcbztips', 'Jcbztray', 'anthem', 'celery', 'cjblue', 'flexible', 'natmiuninst',
          'nattiuninst', 'nattnuninst', 'nattouninst', 'respond']
p_sesame = ['dessertcookies', 'srfminiwwt', 'hardware', 'srftipsWV23', 'srftpopwwm']
pb_list_old = ['bqpb', 'xypbuninst', 'Kuaipb', 'parpbuninst', 'ktpb', 'ktpbuninst', 'pbxhone', 'xhpbuninst', 'GSscreensaver', 'sspbuninst', '7654pb']


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
        print(f'{project}文件不存在')
    # print(p_list_new)
    return p_list_new


def get_pb(project=None):
    pb_list_init = []
    lua_project = globals()['lua_' + project]
    if os.path.isfile(lua_project):
        with open(lua_project, encoding="utf-8") as file:
            pattern_pb = re.compile(r'function execute_screensaver.*?function')
            lua_pb = file.read().splitlines()
            lua_pb_str = ''.join(lua_pb)
            # print(pattern_pb.search(lua_pb_str))
            result = pattern_pb.findall(lua_pb_str)
            if result:
                # print(result)
                p = result[-1]
            else:
                print('未找到屏保相关lua')
            pattern = re.compile(r'localname = "(.*?)"')
            resu = pattern.findall(p)
            pb_list_init.extend(resu)
            # print(resu)
            # print(pb_list_init)
        pb_list = sorted(list(set(pb_list_init)))
        # print(pb_list)
        return pb_list

    else:
        print(f'{project}文件不存在')


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



def pb_change():
    projects = ['xiaoyu', 'kuaizip', 'kantu', 'heinote', 'finder', 'browser']
    pb_list_new = []
    for i in range(len(projects)):
        project = projects[i]
        pb_list_new_proj = get_pb(project)
        pb_list_new.extend(pb_list_new_proj)
    # print(pb_list_new)
    if pb_list_new != pb_list_old:
        print('pb进程有更新', pb_list_new)
    else:
        print('pb no change')


if __name__ == '__main__':
    change()
    pb_change()
