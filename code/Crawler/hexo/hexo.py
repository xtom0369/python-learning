#! /usr/local/bin python3
# -*- coding:utf-8 -*-

import requests
import os
from bs4 import BeautifulSoup
from sys import argv

script, domain = argv
start_url = domain

# 获取网页解析结果
def request_soup(url):
    html = request_html(url)
    html = html.text.encode(html.encoding).decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    return soup

# 请求网页信息    
def request_html(url):
    # 浏览器的请求头
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    # 请求url对应的网页信息
    html = requests.get(url, headers=headers)
    print(f"正在请求网页信息，网页url为{url}")
    return html

soup = request_soup(start_url)
articles = soup.find_all("article")

for article in articles:
    a    = article.find("a")
    href = a['href']
    print(href)

    #article_url  = start_url + href
    #article_soup = request_soup(article_url)
    #page_list    = article_soup.find("article").find_all("p")
    
    #for page in page_list:
    #    text = page.get_text() + "\n"
    #    print(text)        
