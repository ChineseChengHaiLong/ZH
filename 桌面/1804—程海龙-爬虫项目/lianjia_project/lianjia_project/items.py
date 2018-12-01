# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()
    reddess = scrapy.Field()
    geju = scrapy.Field()
    acreage = scrapy.Field()
    degree = scrapy.Field()
    gzrs = scrapy.Field()
    liulanshu = scrapy.Field()
    price = scrapy.Field()
    unit_price = scrapy.Field()
    urls =scrapy.Field()
    chaoxiang = scrapy.Field()

    def insert_sql_data_by_dictdata(self, dictdata):
        """
        step1:写一个数据插入的sql语句
        step2:数据库要存储的数据提取出来
        :param dictdata: 字典类型的数据
        :return:
        """
        sql = """
        INSERT INTO lianjiaA (%s)
        VALUES (%s)
        """ % (
            ','.join(dictdata.keys()),
            ','.join(['%s'] * len(dictdata))
        )

        data = list(dictdata.values())
        # data = [value for key,value in dictdata.items()]

        return sql, data



class Lianjiazhufang(scrapy.Item):
    # 房屋户型
    types = scrapy.Field()

    # 所在楼层
    louceng = scrapy.Field()
    # 建筑面积
    mianji = scrapy.Field()
    # 户型结构
    jieguo =scrapy.Field()
    # 套内面积
    taofang_mianji = scrapy.Field()
    # 建筑类性
    jianzhu_leixing = scrapy.Field()
    # 房屋朝向
    jianzhu_chaoxiang = scrapy.Field()
    # 建筑结构
    jianzhu_jiegou = scrapy.Field()
    # 装修情况
    jianzhu_xiushan = scrapy.Field()
    # 醍醐比例
    jianzhu_tihu = scrapy.Field()
    # 供暖方式
    jianzhu_gongnuan = scrapy.Field()
    # 配备电梯
    jianzhu_dianti = scrapy.Field()
    # 产权年限
    jianzhu_nianxian = scrapy.Field()

    # 小取的名字
    name = scrapy.Field()
    #地址
    reddesss = scrapy.Field()
    # 看房时间
    time = scrapy.Field()
    # 链家编号
    number =scrapy.Field()
    # 住房标题
    title = scrapy.Field()

    # 挂牌时间
    guapai_time = scrapy.Field()
    # 交易属性
    jiaoyi_shuxing = scrapy.Field()

    # 上次交易时间
    shang_time = scrapy.Field()
    # 房屋用途
    yongtu = scrapy.Field()
    # 房屋年限
    nianxian = scrapy.Field()
    # 产权所有
    chanquan_suoyou = scrapy.Field()
    # 抵押信息
    diya = scrapy.Field()

    def insert_sql_data_by_dictdata(self, dictdata):
        """
        step1:写一个数据插入的sql语句
        step2:数据库要存储的数据提取出来
        :param dictdata: 字典类型的数据
        :return:
        """
        sql = """
        INSERT INTO lianjiaB (%s)
        VALUES (%s)
        """ % (
            ','.join(dictdata.keys()),
            ','.join(['%s'] * len(dictdata))
        )

        data = list(dictdata.values())
        # data = [value for key,value in dictdata.items()]

        return sql, data