# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
#from bs4 import BeautifulSoup
import re
import json

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62'}

url="https://tongqu.sjtu.edu.cn/act/type?type=0&status=0&order=hotvalue"
website=r"https://tongqu.sjtu.edu.cn/act/"

response = requests.get(url,headers=headers)
#print(response.text)
res=re.search("var g_init_type_acts.*</script>",response.text)
info=re.findall('{\"actid\".*?\"}',res[0])

count=0
for sec in info:
    dict = json.loads(sec)
    pa=dict["member_count"]
    pb=dict["max_member"]
    
    act_url=f"https://tongqu.sjtu.edu.cn/act/{dict['actid']}"
    act_res=requests.get(act_url,headers=headers)
    if re.search(r"\\u65b0\\u65f6\\u4ee3\\u793e\\u4f1a\\u8ba4\\u77e5\\u5b9e\\u8df5",act_res.text):
        print('*',end="")
        
    if pa==pb:
        print("【已满】"+pa+'/'+pb,end="   ")
    else:
        print("【OK】"+pa+'/'+pb,end="   ")
    for j in ["name","location","start_time","end_time"]:
        print(dict[j],end=" ")
    print('')
    count=count+1
    if count>6:
        break
    
input("输入任意键退出")