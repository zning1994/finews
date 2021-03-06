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
"""+contents+"\n\n<http://finews.zning.xyz/html_News/NewsShare.html?infoCode="+i['infocode']+">\n\n[返回"+i['from']+"新闻](//finews.withounder.com/"+pinyin+"/)｜[返回首页](//finews.withounder.com/)")


