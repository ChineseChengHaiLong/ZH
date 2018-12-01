# -*- coding: utf-8 -*-
import scrapy
from lianjia_project.items import LianjiaProjectItem,Lianjiazhufang

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://bj.lianjia.com/ershoufang/']

    def parse(self, response):
        house_lists = response.xpath('//ul//li[@class="clear LOGCLICKDATA"]')
        print(len(house_lists))


        for i in house_lists:
            dicts = LianjiaProjectItem()
            #标题
            dicts['title'] = i.xpath('.//div[@class="title"]/a/text()').extract_first()

            #地址
            dicts['reddess'] = i.xpath('.//div[@class="address"]//text()').extract_first()

            #格局
            dicts['geju'] = i.xpath('.//div[@class="address"]//text()').extract()[2]

            #面积
            dicts['acreage'] = i.xpath('.//div[@class="address"]//text()').extract()[4]
            #朝向
            dicts['chaoxiang'] = i.xpath('.//div[@class="address"]//text()').extract()[6]
            #装修程度
            dicts['degree'] = i.xpath('.//div[@class="address"]//text()').extract()[8]
            #关注人数
            dicts['gzrs'] = i.xpath('.//div[@class="followInfo"]//text()').extract_first()
            #浏览数
            dicts['liulanshu'] = i.xpath('.//div[@class="followInfo"]//text()').extract()[2]
            #总价
            dicts['price'] = i.xpath('.//div[@class="totalPrice"]/span/text()').extract_first() + '万'
            #平方价格
            dicts['unit_price'] = i.xpath('.//div[@class="unitPrice"]/span/text()').extract_first()
            #详情链接
            dicts['urls'] = i.xpath('.//div[@class="title"]/a/@href').extract_first()


            yield dicts
            # yield scrapy.Request(url=dicts['urls'],meta={'title':dicts['title']},callback=self.xiangqingjiexi)
            # print(dicts)


        #获取它的所有的页数
        for i in range(2,101):
            urlss = 'https://bj.lianjia.com/ershoufang/pg%s/' % i
            # print(urlss)

            yield scrapy.Request(url=urlss,callback=self.parse)


    def xiangqingjiexi(self,response):


        lists = response.xpath('//div[@class="base"]//div[@class="content"]/ul')
        for i in lists:
            # print(len(lists))
            #房屋户型
            lianjia_item = Lianjiazhufang()
            lianjia_item['types'] = i.xpath('./li/text()').extract()[0]

            #所在楼层
            lianjia_item['louceng'] = i.xpath('./li/text()').extract()[1]
            #建筑面积
            lianjia_item['mianji'] = i.xpath('./li/text()').extract()[2]
            #户型结构
            lianjia_item['jieguo'] = i.xpath('./li/text()').extract()[3]
            #套内面积
            lianjia_item['taofang_mianji']  = i.xpath('./li/text()').extract()[4]
            #建筑类性
            lianjia_item['jianzhu_leixing'] = i.xpath('./li/text()').extract()[5]
            #房屋朝向
            lianjia_item['jianzhu_chaoxiang'] = i.xpath('./li/text()').extract()[6]
            #建筑结构
            lianjia_item['jianzhu_jiegou'] = i.xpath('./li/text()').extract()[7]
            #装修情况
            lianjia_item['jianzhu_xiushan'] = i.xpath('./li/text()').extract()[8]
            #醍醐比例
            lianjia_item['jianzhu_tihu'] = i.xpath('./li/text()').extract()[9]
            #供暖方式
            lianjia_item['jianzhu_gongnuan'] = i.xpath('./li/text()').extract()[10]
            #配备电梯
            lianjia_item['jianzhu_dianti'] = i.xpath('./li/text()').extract()[11]
            #产权年限
            lianjia_item['jianzhu_nianxian'] = i.xpath('./li/text()').extract()[12]

            #小取的名字
            lianjia_item['name'] = response.xpath('//div[@class="communityName"]//a[1]/text()').extract_first()

            reddess_xq = response.xpath('//div[@class="areaName"]//span[@class="info"]/a[1]/text()').extract_first()
            reddess_xqq = response.xpath('//div[@class="areaName"]//span[@class="info"]/a[2]/text()').extract_first()
            lianjia_item['reddesss'] = reddess_xq + reddess_xqq
            #看房时间

            lianjia_item['time'] = response.xpath('//div[@class="visitTime"]/span[2]/text()').extract()[0]
            #链家编号
            lianjia_item['number'] = response.xpath('//div[@class="houseRecord"]/span[2]/text()').extract()[0]
            #住房标题
            lianjia_item['title'] = response.meta['title']
            #挂牌时间

            lianjia_item['guapai_time'] = response.xpath('//div[@class="transaction"]//ul/li[1]/span[2]/text()').extract_first()
            #交易属性
            lianjia_item['jiaoyi_shuxing'] = response.xpath('//div[@class="transaction"]//ul/li[2]/span[2]/text()').extract_first()

            #上次交易时间
            lianjia_item['shang_time'] = response.xpath('//div[@class="transaction"]//ul/li[3]/span[2]/text()').extract_first()
            #房屋用途
            lianjia_item['yongtu'] = response.xpath('//div[@class="transaction"]//ul/li[4]/span[2]/text()').extract_first()
            #房屋年限
            lianjia_item['nianxian'] = response.xpath('//div[@class="transaction"]//ul/li[5]/span[2]/text()').extract_first()
            #产权所有
            lianjia_item['chanquan_suoyou'] = response.xpath('//div[@class="transaction"]//ul/li[6]/span[2]/text()').extract_first()
            #抵押信息
            lianjia_item['diya'] = response.xpath('//div[@class="transaction"]//ul/li[1]/span[7]/text()').extract_first()

            print(lianjia_item)
            yield lianjia_item
