# -*- coding: UTF-8 -*-
import pymysql


class DBOperate:
    def __init__(self):
        """
        所有数据库操作的父类
        """
        # 设置主机名
        self.host = 'localhost'
        # 设置用户
        self.user = 'root'
        # 设置密码
        self.passwd = ''

    def connect(self):
        db = pymysql.connect(host=self.host, user=self.user, password=self.passwd)
        cursor = db.cursor()
        return db, cursor

    def writeTitle(self, data):
        pass

    def writeContent(self, data):
        pass
