import pymysql
from DataBaseOperator.DBOperate import *


class DBConnector(DBOperate):
    def __init__(self):
        super().__init__()
        self.dataBase = 'finance_text'

    def connect(self):
        db = pymysql.connect(host=self.host, user=self.user, password=self.passwd, database=self.dataBase)
        cursor = db.cursor()
        return db, cursor

    def writeTitle(self, data):
        db, cursor = self.connect()
        sql = 'INSERT INTO title_url(Class,Title,URL) values(%s,%s,%s);'
        try:
            cursor.execute(sql, data)
            db.commit()
            print('数据写入成功')
            cursor.close()
            db.close()
        except:
            db.rollback()
            print('数据写入不成功，数据库已回滚')

    def writeContent(self, data):
        db, cursor = self.connect()
        sql = 'INSERT INTO text_content(Title_index,Content,Abstract) values (%s,%s,%s);'
        try:
            cursor.execute(sql, data)
            db.commit()
            print('数据写入成功')
            cursor.close()
            db.close()
        except:
            db.rollback()
            print('数据写入不成功，数据库已回滚')

    def selectTitleId(self):
        """
        获取标题在title_url中的id

        :return:((id,),)的数据结构
        """
        db, cursor = self.connect()
        sql = 'SELECT `Index` FROM title_url;'
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    def selectUrl(self, id):
        """

        :param id:
        :return:((URL,),)的数据结构
        """
        db, cursor = self.connect()
        sql = 'SELECT `URL` FROM title_url WHERE `Index` = %s'
        cursor.execute(sql, id)
        data = cursor.fetchall()
        cursor.close()
        db.close()

        return data
