from DataBaseOperator import DataBaseCreator, DBConnector
from DataGetter import ContentGetter, TitleGetter


class GetData:
    def __init__(self):
        # 获取金融文本的四个板块
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
                # 将数据写入数据库
                self.DBConnector.writeTitle(d)
        print("Title Get!")

        # 获取金融文本正文
        IDs = self.DBConnector.selectTitleId()
        for i in IDs:
            titleID = i[0]
            url = self.DBConnector.selectUrl(titleID)[0][0]
            contentGetter = ContentGetter.ContentGetter(url)
            tmpContent = contentGetter.getContent()
            contentData = [titleID, tmpContent[0], tmpContent[1]]
            # 将数据写入数据库
            self.DBConnector.writeContent(contentData)
        print("Content Get!")


if __name__ == '__main__':
    test = GetData()
    test.getData()
