# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class LianjiaProjectPipeline(object):

    def __init__(self,host,user,pwd,db,charset):
        #穿件数据库连接
        self.client = pymysql.Connect(host,user,pwd,db,charset=charset)
        #创建游标执行sql语句
        self.cursor = self.client.cursor()

    def start_spider(self,spider):
        #爬虫开启是调用一次
        pass

    @classmethod
    def from_crawler(cls,crawler):
        host = crawler.settings['MYSQL_HOST']
        user = crawler.settings['MYSQL_USER']
        pwd = crawler.settings['MYSQL_PWD']
        db = crawler.settings['MYSQL_DB']
        charset = crawler.settings['MYSQL_CHARSET']

        return cls(host,user,pwd,db,charset)

    def process_item(self, item, spider):
        sql,data = item.insert_sql_data_by_dictdata(dict(item))

        try:
            self.cursor.execute(sql,data)
            self.client.commit()
        except Exception as err:
            print(err)
            self.client.rollback()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.client.close()
