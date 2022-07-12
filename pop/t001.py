# coding:utf-8
import os
import re


# lua_browser = r'F:\svn\Lua\7654browser\v1.0.0.2\uc.lua'

def get_p(project=None):
    p_list = []
    lua_project = r'F:\svn\Lua\7654browser\v1.0.0.2\uc.lua'
    if os.path.isfile(lua_project):
        with open(lua_project, encoding="utf-8") as file:
            for line in file:
                # urls = re.compile(r'localname = "(.*?)"',line)
                pattern = re.compile(r'localname = "(.*?)"')
                p2 = re.compile(r'localname="(.*?)"')
                for i in [pattern, p2]:
                    result = i.findall(line)
                    if result:
                        p = result[-1]
                        p_list.append(p)
            p_list_new = sorted(list(set(p_list)))
    else:
        print(f'{project}文件不存在')
    print(p_list_new)
    # return p_list_new


get_p()
