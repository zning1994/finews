---
layout: default
title:  "首页"
permalink: /
---

{% for tag in site.tags %}
  <h2 id="{{ tag[0] }}">{{ tag[0] }}</h2>
  <ul>
    {% if tag[0] == '东财滚动新闻' %}
    {% for post in tag[1] limit:20 %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
    {% else %}
    {% for post in tag[1] limit:5 %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
    {% endif %}
  </ul>
  ---
{% endfor %}
