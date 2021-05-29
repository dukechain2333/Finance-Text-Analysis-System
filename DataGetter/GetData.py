from DataBaseOperator import DataBaseCreator, DBConnector, DBOperate
import TitleGetter, ContentGetter
import requests
import re
from bs4 import BeautifulSoup


class GetData:
    def __init__(self):
        self.blockChoice = ['港股', '外汇', '期货', '黄金']
        self.DBConnector = DBConnector.DBConnector()
        self.DBCreator = DataBaseCreator.DBCreator()

    def getData(self):
        # 创建数据库
        self.DBCreator.create()
        # 获取标题与URL
        for choice in self.blockChoice:
            titleGetter = TitleGetter.TitleGetter(choice)
            data = titleGetter.getTitleUrl()
            for d in data:
                self.DBConnector.writeTitle(d)
        print("Title Get!")

        IDs = self.DBConnector.selectTitleId()
        for i in IDs:
            id = i[0]
            url = self.DBConnector.selectUrl(id)[0][0]
            contentGetter = ContentGetter.ContentGetter(url)
            tmpContent = contentGetter.getContent()
            contentData = [id, tmpContent[0], tmpContent[1]]
            self.DBConnector.writeContent(contentData)
        print("Content Get!")


if __name__ == '__main__':
    test = GetData()
    test.getData()
