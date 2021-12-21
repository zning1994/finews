
import json
import requests
import math
import time, threading
import os
import shutil
from datetime import datetime, timedelta

from xpinyin import Pinyin

def make_calender():
    time_list = []
    d = datetime.today()
    delta = timedelta(days=-1)
    time_list.append(d.strftime("%Y-%m-%d"))
    time_list.append((d+delta).strftime("%Y-%m-%d"))
    time_list.append((d+delta+delta).strftime("%Y-%m-%d"))
    print(time_list)
    return time_list

def mv_files(time_list):
    file_list = os.listdir('./_posts/')
    for i in file_list:
        if i[0:10] not in time_list and i != "2021-12-01-init.md":
            shutil.copy(os.path.join("./_posts/",i),"./old_post/")
            os.remove(os.path.join("./_posts/",i))

def get_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    }
    page = requests.get(url, headers = headers).content
    page = page.decode('utf-8')
    return page

def get_esnews():
    print("start get_esnews")
    result = get_url("http://183.136.162.242/web/webapi?type=102&count=100&newsid=1")
    result = json.loads(result)['records']
    for i in result:
        contents = json.loads(get_url("http://finews.zning.xyz/NewsData/GetNewsText.do?id="+i['infoCode']))['content']
        # print(i['title'], i['digest'].split("】")[-1], i['id'], i['url_w'], i['showtime'], i['showtime'].split(" ")[0])
        with open("./_posts/"+str(i['showtime'].split(" ")[0])+"-"+str(i['id'])+".md", "w", encoding="utf-8") as f:
            f.write("""---
layout: post
title: \""""+i['title']+"""\"
date: """+i['showtime']+""" +0800
categories: emnews
tags: 东财滚动新闻
---
> """+i['digest'].split("】")[-1]+"\n\n"+contents.replace("　　","")+"\n\n<"+i['url_w']+">\n\n[返回东财滚动新闻](//finews.withounder.com/emnews/)｜[返回首页](//finews.withounder.com/)")

def get_esnews_2():
    print("start get_esnews_2")
    p = Pinyin()
    result = get_url("http://183.136.162.242/web/webapi?type=45&count=100&newsid=1")
    result = json.loads(result)['nodeList']
    for i in result:
        pinyin = p.get_pinyin(i['from']).replace("-","")
        contents = json.loads(get_url("http://finews.zning.xyz/NewsData/GetNewsText.do?id="+i['infocode']))['text']
        with open("./_posts/"+str(i['showtime'].split(" ")[0])+"-"+str(i['infocode'])+".md", "w", encoding="utf-8") as f:
            f.write("""---
layout: post
title: \""""+i['title']+"""\"
date: """+i['showtime']+""" +0800
categories: """+pinyin+"""
tags: """+i['from']+"""新闻
---
"""+contents.replace("　　","")+"\n\n<http://finews.zning.xyz/html_News/NewsShare.html?infoCode="+i['infocode']+">\n\n[返回"+i['from']+"新闻](//finews.withounder.com/category/"+pinyin+".html)｜[返回首页](//finews.withounder.com/)")

def get_market_news(market_type_list):
    print("start get_market_news"+market_type_list[0])
    p = Pinyin()
    # market_type_list = ["37","38","39"]
    for mt in market_type_list:
        result = get_url("http://43.240.125.15:1818/information/newmarket/web/webapi?marketType="+mt+"&count=100")
        result = json.loads(result)['record']
        for i in result:
            pinyin = p.get_pinyin(i['medianame']).replace("-","")
            contents = json.loads(get_url("http://finews.zning.xyz/NewsData/GetNewsText.do?id="+i['infoCode']))['text']
            with open("./_posts/"+str(i['datetime'].split(" ")[0])+"-"+str(i['infoCode'])+".md", "w", encoding="utf-8") as f:
                f.write("""---
layout: post
title: \""""+i['title']+"""\"
date: """+i['datetime']+""" +0800
categories: """+pinyin+"""
tags: """+i['medianame']+"""新闻
---
"""+contents.replace("　　","")+"\n\n<http://finews.zning.xyz/html_News/NewsShare.html?infoCode="+i['infoCode']+">\n\n[返回"+i['medianame']+"新闻](//finews.withounder.com/category/"+pinyin+".html)｜[返回首页](//finews.withounder.com/)")

if __name__ == '__main__':
    mv_files(make_calender())
    for i in range(0,5):
        t1 = threading.Thread(target=get_esnews, name='get_esnews')
        t1.start()
        t2 = threading.Thread(target=get_esnews_2, name='get_esnews_2')
        t2.start()
        t3 = threading.Thread(target=get_market_news, name='get_market_news', args=(["37"],))
        t3.start()
        t4 = threading.Thread(target=get_market_news, name='get_market_news', args=(["38"],))
        t4.start()
        t5 = threading.Thread(target=get_market_news, name='get_market_news', args=(["39"],))
        t5.start()
        time.sleep(30)
