---
layout: default
title:  "东财滚动新闻"
permalink: /emnews/
---

{% for tag in site.tags %}
  {% if tag[0] == "东财滚动新闻" %}
    <h2 id="{{ tag[0] }}">{{ tag[0] }}</h2>
    <ul>
      {% for post in tag[1] limit:20 %}
        <li><a href="{{ post.url }}" target="_blank">{{ post.title }}</a></li>
      {% endfor %}
    </ul>
  {% endif %}
{% endfor %}
