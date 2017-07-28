#! /usr/local/bin python3
# -*- coding:utf-8 -*-

import requests
import os
from bs4 import BeautifulSoup

class Mzitu(object):

    def start(self):
        # 网页url
        start_url  = 'http://www.mzitu.com/all'

        # 解析网页
        soup = self.request_soup(start_url)

        # 在解析后的信息中找标签
        all_a = soup.find('div', class_ = 'all').find_all('a')
        for a in all_a:
            title = a.get_text()  # 获取标签对应文本
            folder_name  = str(title).strip()
            
            success = self.create_folder(folder_name)
            if success:
                href  = a['href']    # 获取标签的href属性
                sub_html_soup = self.request_soup(href)
                max_page_num  = sub_html_soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()  # 这里的-2，是因为倒数第一个是下一页，倒数第二个才是最后一页
    
                for page in range(1, int(max_page_num)+1):
                    page_url = href + '/' + str(page)
                    img_soup = self.request_soup(page_url)
                    img_url  = img_soup.find('div', class_='main-image').find('img')['src']
                    self.save_img(img_url)     

    # 获取网页解析结果
    def request_soup(self, url):
        html = self.request_html(url)
        soup = BeautifulSoup(html.text, 'lxml')
        return soup
    
    # 请求网页信息
    def request_html(self, url):
        # 浏览器的请求头
        headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        # 请求url对应的网页信息
        html = requests.get(url, headers=headers)
        print(f"正在请求网页信息，网页url为{url}")
        return html
    
    # 创建文件夹
    def create_folder(self, folder_name):
        folder_name = folder_name.strip()
        folder_path = os.path.join("/Users/xiaotao/python/mzitu/mzitu", folder_name)
        is_exist = os.path.exists(folder_path)

        if not is_exist:
            print(f"创建文件夹{folder_name}")
            os.makedirs(folder_path)
            os.chdir(folder_path) 
            return True
        else:
            print(f'文件夹{folder_name}已经存在了！')
            return False
    
    # 保存图片
    def save_img(self, img_url): ##这个函数保存图片
        name = img_url[-9:-4]
        img  = self.request_html(img_url)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()
        print(f"保存图片{name}.jag成功")

mzitu = Mzitu()
mzitu.start()
