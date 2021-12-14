import json
import requests
import math

def get_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    }
    page = requests.get(url, headers = headers).content
    page = page.decode('utf-8')
    return page


if __name__ == '__main__':
    result = get_url("http://183.136.162.242/web/webapi?type=102&count=500&newsid=1")
    result = json.loads(result)['records']
    for i in result:
        contents = json.loads(get_url("http://choicewzp1.eastmoney.com/NewsData/GetNewsText.do?id="+i['infoCode']))['content']
        # print(i['title'], i['digest'].split("】")[-1], i['id'], i['url_w'], i['showtime'], i['showtime'].split(" ")[0])
        with open("./_posts/"+str(i['showtime'].split(" ")[0])+"-"+str(i['id'])+".md", "w", encoding="utf-8") as f:
            f.write("""---
layout: post
title: \""""+i['title']+"""\"
date: """+i['showtime']+""" +0800
categories: emnews
tags: 东财滚动新闻
---
> """+i['digest'].split("】")[-1]+"\n\n"+contents+"\n\n<"+i['url_w']+">\n\n[返回东财滚动新闻](//finews.withounder.com/emnews/)｜[返回首页](//finews.withounder.com/)")
    # print(result)
