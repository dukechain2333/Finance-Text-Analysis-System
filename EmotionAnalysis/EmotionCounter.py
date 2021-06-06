# -*- coding: UTF-8 -*-
from pyhanlp import *
from DataBaseOperator import DBConnector
import numpy as np


class EmotionCounter:
    def __init__(self):
        # 随机挑一篇文章
        self.id = np.random.randint(1, 1001)
        self.negativeWords_path = r'EmotionBasedDic/TsingHua/tsinghua.negative.gb.txt'
        self.positiveWords_path = r'EmotionBasedDic/TsingHua/tsinghua.positive.gb.txt'
        self.report_path = r'EmotionAnalysis/EmotionReport.txt'

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

    def load_dic(self):
        """
        载入感情词典

        :return: negativeWords, positiveWords
        """
        with open(self.negativeWords_path, encoding='gbk') as file:
            negativeWords = file.readlines()
        for i in range(len(negativeWords)):
            negativeWords[i] = negativeWords[i].strip()

        with open(self.positiveWords_path, encoding='gbk') as file:
            positiveWords = file.readlines()
        for i in range(len(positiveWords)):
            positiveWords[i] = positiveWords[i].strip()

        return negativeWords, positiveWords

    def split_content(self, data):
        """
        为文章分词

        :param data:传入待切分文章
        :return: [分词,]
        """
        tmp = HanLP.segment(data)
        worldList = []
        for i in tmp:
            worldList.append(str(i).split('/')[0])

        return worldList

    def emotion_count(self, data):
        """
        统计情感信息

        :param data:传入原文本
        :return: Negative/Positive/Neutral
        """
        negativeWords, positiveWords = self.load_dic()
        negative = 0
        positive = 0
        for d in data:
            if d in negativeWords:
                negative += 1
            elif d in positiveWords:
                positive += 1
        if negative > positive:
            return 'Negative'
        elif negative < positive:
            return 'Positive'
        else:
            return 'Neutral'

    def generalize_emotion_report(self):
        """
        生成情感分析报告
        """
        title = self.loadTitle()[0][0]
        content = self.loadContent()[0][0]
        keyword = HanLP.extractKeyword(content, 3)
        splitWords = self.split_content(content)
        ans = self.emotion_count(splitWords)

        firstRow = '文章标题:\t' + title
        secondRow = '关键词:\t' + str(keyword)
        thirdRow = '正文内容:\t' + content
        fourthRow = '情感评估结果:\t' + ans

        with open(self.report_path, encoding='utf-8', mode='w') as file:
            file.write(firstRow + '\n')
            file.write(secondRow + '\n')
            file.write(thirdRow + '\n')
            file.write(fourthRow + '\n')

        print('文本情感分析报告已生成！')
        print(firstRow)
        print(secondRow)
        print(thirdRow)
        print(fourthRow)

# if __name__ == '__main__':
#     test = EmotionCounter()
#     test.generalize_emotion_report()
