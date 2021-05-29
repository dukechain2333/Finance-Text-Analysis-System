import requests
import re
from bs4 import BeautifulSoup


class TitleGetter:
    def __init__(self, blockChoice):
        """

        :param blockChoice:选择板块
        """
        self.blockDic = {
            '港股': 'http://hk.eastmoney.com/a/cggdd.html',
            '外汇': 'http://forex.eastmoney.com/a/cwhdd.html',
            '期货': 'http://futures.eastmoney.com/a/cqhdd.html',
            '黄金': 'http://gold.eastmoney.com/a/chjdd.html'
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66 '
        }
        self.blockChoice = blockChoice
        self.urlOrigin = self.blockDic.get(blockChoice)
        # 每个板块爬取25页,每页20篇文章
        self.page = 25

    def getTitleUrl(self):
        """
        获取金融文本的链接和标题
        :return:返回[[blockChoice,title,url]]的数据结构
        """
        data = []
        for page in range(self.page + 1):
            # 拼接url实现翻页爬取
            url = self.urlOrigin[:-5] + '_' + str(page) + self.urlOrigin[-5:]
            pageData = requests.get(headers=self.headers, url=url).text.encode('utf-8')
            # BeautifulSoup库解析爬取的html
            soup = BeautifulSoup(pageData, 'html.parser')
            newsContent = soup.find_all('p', class_='title')
            for content in newsContent:
                href = content.a['href']
                # print(content.a['href'])
                title = content.a.text.strip()
                # print(content.a.text.strip())
                data.append([self.blockChoice, title, href])

        return data
