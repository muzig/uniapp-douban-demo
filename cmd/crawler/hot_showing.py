#!/bin/env python3
# coding=utf-8

from bs4 import BeautifulSoup
import pprint

soup = BeautifulSoup(open('../src/index.html', 'r'), 'lxml')

collector = []
for tag in soup.find_all('li'):
    if tag.get('class') is None:
        continue
    if "ui-slide-item" in tag.get('class'):
        # 解析基本信息
        data = {
            "title": tag.get('data-title'),
            "release": tag.get('data-release'),
            "director": tag.get('data-director'),
            "actors": tag.get('data-actors'),
        }
        if data['title'] is None:
            continue
        # 解析图片信息
        img = tag.find('img')
        if img is None:
            continue
        if img.get('src') is None:
            continue
        data['img'] = img.get('src')
        collector.append(data)

# pprint.pprint(collector)

with open('../src/hot_showing.json', 'w') as f:
    f.write(collector.__str__().replace('\'','\"'))
