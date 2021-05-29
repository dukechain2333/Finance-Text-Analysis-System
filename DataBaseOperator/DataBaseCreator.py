import pymysql
from DataBaseOperator.DBOperate import DBOperate


class DBCreator(DBOperate):
    def __init__(self):
        super().__init__()

    def connect(self):
        db = pymysql.connect(host=self.host, user=self.user, password=self.passwd)
        cursor = db.cursor()
        return db, cursor

    def createDB(self):
        db, cursor = self.connect()
        sql = 'CREATE DATABASE IF NOT EXISTS finance_text;'
        cursor.execute(sql)
        db.close()
        cursor.close()

    def createTitleTable(self):
        db, cursor = self.connect()
        cursor.execute('USE finance_text;')
        sql = '''
            CREATE TABLE IF NOT EXISTS title_url(
                `Index` int NOT NULL AUTO_INCREMENT PRIMARY KEY ,
                `Class` varchar(10) DEFAULT NULL,
                `Title` varchar(500) DEFAULT NULL,
                `URL` varchar(500) DEFAULT NULL
            );
        '''
        cursor.execute(sql)
        db.close()
        cursor.close()

    def createContentTable(self):
        db, cursor = self.connect()
        cursor.execute('USE finance_text;')
        sql = '''
            CREATE TABLE IF NOT EXISTS text_content(
                `Index` int NOT NULL AUTO_INCREMENT PRIMARY KEY ,
                `Title_Index` int NOT NULL ,
                `Content` TEXT DEFAULT NULL,
                `Abstract` TEXT DEFAULT NULL,
                CONSTRAINT `T_I` FOREIGN KEY (`Title_Index`) REFERENCES title_url(`Index`)
            );
        '''
        cursor.execute(sql)
        db.close()
        cursor.close()

    def create(self):
        self.createDB()
        self.createTitleTable()
        self.createContentTable()
        print('数据库建立完成')


if __name__ == '__main__':
    creator = DBCreator()
    creator.create()
