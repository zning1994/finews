import json
import requests
from xpinyin import Pinyin

def get_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    }
    page = requests.get(url, headers = headers).content
    page = page.decode('utf-8')
    return page

if __name__ == '__main__':
    p = Pinyin()
    market_type_list = ["37","38","39"]
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
"""+contents+"\n\n<http://finews.zning.xyz/html_News/NewsShare.html?infoCode="+i['infoCode']+">\n\n[返回"+i['medianame']+"新闻](//finews.withounder.com/"+pinyin+"/)｜[返回首页](//finews.withounder.com/)")


