---
layout: default
title:  "首页"
permalink: /
---

## [点击此处转到分类页面](../categories/ "转到分类页面")

## [点击此处转到东财滚动新闻](../emnews/ "东财滚动新闻")

<h2 id="最近100条新消息">最近100条新消息</h2>
<ul>
    {% for post in site.posts limit:100 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>
