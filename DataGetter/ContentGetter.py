# -*- coding: UTF-8 -*-
import requests
import re
from bs4 import BeautifulSoup


class ContentGetter:
    def __init__(self, url):
        """
        获取金融文本正文

        :param url: 爬取正文的url
        """
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66 '
        }

    def getContent(self):
        """
        爬取金融文本正文内容

        :return:[news,newsAbstract]的数据结构
        """
        pageData = requests.get(url=self.url, headers=self.headers)
        pageData.encoding = 'utf-8'
        soup = BeautifulSoup(pageData.text, 'html.parser')
        # 获取文本摘要内容
        try:
            newsAbstract = soup.find_all('div', class_='b-review')[0].text.strip()
        except:
            newsAbstract = ''
        # 获取文本正文内容
        newsContent = soup.find_all('div', id='ContentBody')[0].find_all('p')
        news = ''
        # 拼接不同段落的正文
        for content in newsContent:
            if content.text:
                news += content.text.strip()
        print(newsAbstract)
        print(news)

        return [news, newsAbstract]
