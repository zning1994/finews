---
layout: default
title:  "东财滚动新闻"
permalink: /emnews/
---

{% for tag in site.tags %}
{% if tag[0] == '东财滚动新闻' %}
<h2 id="{{ tag[0] }}">{{ tag[0] }}</h2>
<ul>
  {% for post in tag[1] limit:100 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
{% endif %}
{% endfor %}

[此页仅展示最近100条滚动新闻，如需访问全量新闻请点击此处](../achieves/emnews/)
