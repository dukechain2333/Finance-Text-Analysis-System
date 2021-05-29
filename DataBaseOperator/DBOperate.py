import pymysql


class DBOperate:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.passwd = 'qian258046'

    def connect(self):
        db = pymysql.connect(host=self.host, user=self.user, password=self.passwd)
        cursor = db.cursor()
        return db, cursor

    def writeTitle(self, data):
        pass

    def writeContent(self, data):
        pass
