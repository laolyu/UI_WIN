# coding:utf-8
import re
import time

p_list = []
with open(r"F:\svn\Lua\kuaizip\uc.lua", encoding="utf-8") as file:
    for line in file:
        # urls = re.compile(r'localname = "(.*?)"',line)
        #
        pattern = re.compile(r'localname = "(.*?)"')
        result = pattern.findall(line)
        if result:
            p = result[-1]
            p_list.append(p)

    q = p_list
    w = list(set(q))
print(q)
print(w)
