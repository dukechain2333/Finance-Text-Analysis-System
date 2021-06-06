from pyhanlp import *
from DataBaseOperator import DBConnector


class DicBuilder:
    def __init__(self, id=-1):
        """
        构建金融行业字典

        :param id: 从数据库中通过index选择文本，默认-1即全选
        """
        self.id = id
        self.stopWords_path = r'../EmotionBasedDic/stopwords.txt'
        self.negativeWords_path = r'../EmotionBasedDic/TsingHua/tsinghua.negative.gb.txt'
        self.positiveWords_path = r'../EmotionBasedDic/TsingHua/tsinghua.positive.gb.txt'
        self.financeDic_path = r'../EmotionBasedDic/FinanceWordDic.txt'

    def loadContent(self):
        """
        加载数据库中的文本

        :return: （（文本,）,）
        """
        dbConnector = DBConnector.DBConnector()
        data = dbConnector.selectContent(self.id)

        return data

    def split_word(self, data):
        """
        使用hanlp进行分词

        :param data:传入文本
        :return:
        """
        splitWords = HanLP.segment(data)
        tmp = []
        for i in splitWords:
            tmp.append(str(i).split('/'))

        return tmp

    def remove_attribute(self, data):
        """
        去除词性

        :param data:传入[[文本,词性],]的列表
        :return: [文本,]
        """
        wordList = []
        for i in data:
            wordList.append(i[0])

        return wordList

    def rubbish_dic(self):
        """
        生成需要去除的词汇列表（停止词，感情词汇，标点符号）

        :return:[无用词汇,]
        """
        with open(self.stopWords_path, encoding='utf8') as file:
            stopWords = file.readlines()
        for i in range(len(stopWords)):
            stopWords[i] = stopWords[i].strip()

        with open(self.negativeWords_path, encoding='gbk') as file:
            negativeWords = file.readlines()
        for i in range(len(negativeWords)):
            negativeWords[i] = negativeWords[i].strip()

        with open(self.positiveWords_path, encoding='gbk') as file:
            positiveWords = file.readlines()
        for i in range(len(positiveWords)):
            positiveWords[i] = positiveWords[i].strip()

        punctuationList = list(r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~“”？，！【】（）、。：；’‘……￥·""")

        emptyList = ['']

        return stopWords + negativeWords + positiveWords + punctuationList + emptyList

    def remove_rubbish(self, data, rubbishList):
        """
        移除文本列表中的垃圾词汇

        :param data: 待移除垃圾词汇的列表[文本,]
        :param rubbishList: 垃圾词汇列表
        :return: 移除垃圾词汇后的文本列表
        """
        tmp = data
        for i in tmp:
            if i.strip() in rubbishList or self.is_number(i.strip()):
                tmp.remove(i)

        return tmp

    def is_number(self, n):
        """
        判断参数是否为数字

        :param n:传入待判断参数
        :return: 若为数字则True,其他False
        """
        try:
            float(n)
        except:
            return False

        return True

    def remove_duplicate(self, data):
        """
        去除列表重复值

        :param:data:传入待去重列表
        :return: 返回去重后的列表
        """
        tmp = set(data)
        return list(tmp)

    def write_dic(self, data):
        """
        将金融词典写入FinanceWordDic.txt

        :param data: 去除垃圾词后的词汇列表
        """
        with open(self.financeDic_path, 'w') as file:
            for i in data:
                file.write(i + '\n')

    def build_dic(self):
        """
        建立金融行业相关字典

        :return: 字典
        """
        data = self.loadContent()
        rubbishDic = self.rubbish_dic()
        wordList = []
        for d in data:
            print(d)
            wordList += self.split_word(d[0])
        wordList = self.remove_attribute(wordList)
        wordList = self.remove_duplicate(wordList)
        self.remove_rubbish(wordList, rubbishDic)
        self.write_dic(wordList)
        print('字典构建已完成！')
        return wordList

# if __name__ == '__main__':
#     test = DicBuilder()
#     test.build_dic()
