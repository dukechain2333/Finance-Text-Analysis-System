# -*- coding: UTF-8 -*-
from pyhanlp import *
from DataBaseOperator import DBConnector
import numpy as np


class TextExtract:
    def __init__(self, num):
        """
        抽取文本摘要

        :param num:文章迭代次数
        """
        self.num = num
        self.id = np.random.randint(1, 1001)
        self.extract_path = 'TextExtract/FinanceTextExtraction_' + str(self.num) + '.txt'

    def loadContent(self):
        """
        加载数据库中的文本

        :return: （（文本,）,）
        """
        dbConnector = DBConnector.DBConnector()
        data = dbConnector.selectContent(self.id)

        return data

    def loadTitle(self):
        """
        加载数据库中的标题

        :return: （（标题,）,）
        """
        dbConnector = DBConnector.DBConnector()
        title = dbConnector.selectTitle(self.id)

        return title

    def summary(self, data):
        """
        提取文本摘要

        :param data:待提取摘要的文本
        :return: 文本摘要
        """
        textSummary = HanLP.extractSummary(data, 10)
        return textSummary

    def similarity(self, summary, title):
        """
        计算摘要与原文标题的相似度

        :param summary:文本摘要
        :param title: 原文标题
        :return: 相似度
        """
        summarySplit = HanLP.segment(summary)
        titleSplit = HanLP.segment(title)

        summaryList = []
        titleList = []
        for i in summarySplit:
            summaryList.append(str(i).split('/')[0])
        for i in titleSplit:
            titleList.append(str(i).split('/')[0])

        count = 0
        for i in summaryList:
            if i in titleList:
                count += 1

        return count / len(titleList)

    def generate_report(self):
        """
        生成摘要报告
        """
        content = self.loadContent()[0][0]
        title = self.loadTitle()[0][0]
        keyword = HanLP.extractKeyword(content, 3)
        textSummary = self.summary(content)

        similarity = self.similarity(textSummary[0], title)

        firstRow = '文章标题:\t' + title
        secondRow = '关键词:\t' + str(keyword)
        thirdRow = '正文内容:\t' + content
        fourthRow = '摘要结果:\t' + textSummary[0]
        fifthRow = '相似度:\t' + str(round(similarity * 100, 2)) + '%'

        if similarity >= 0.2:
            with open(self.extract_path, mode='w', encoding='utf8') as file:
                file.write(firstRow + '\n')
                file.write(secondRow + '\n')
                file.write(thirdRow + '\n')
                file.write(fourthRow + '\n')
                file.write(fifthRow + '\n')

            print('完成第' + str(self.num) + '份摘要！')
            print(firstRow)
            print(secondRow)
            print(thirdRow)
            print(fourthRow)
            print(fifthRow)

            return self.num + 1
        else:
            return self.num


# if __name__ == '__main__':
#     times = 1
#     while times <= 10:
#         textExtract = TextExtract(times)
#         times = textExtract.generate_report()
