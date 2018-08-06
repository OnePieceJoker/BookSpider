# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# need mysql client
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi


class BookspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlTwistedPipeline(object):
    # 实现异步操作数据库
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbprms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            password=settings["MYSQL_PASSWORD"],
            charset="utf8",
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )

        dbpool = adbapi.ConnectionPool("MySQLdb", **dbprms)

        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error)  # 处理异常

    def do_insert(self, cursor, item):
        # 执行具体的插入
        sql = '''
            insert into book4biquge(title, author, label, chapter_id, bookname, content) values(%s, %s, %s, %s, %s, %s)
            '''
        cursor.execute(sql, (item["title"], item["author"], item["label"], item["chapter_id"], item["bookname"], item["content"]))

    def handle_error(self, failure):
        # 处理异步插入的异常
        print(failure)