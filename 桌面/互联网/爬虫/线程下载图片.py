import threading
from lxml import etree
import requests
from urllib import request
from queue import Queue

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
#创建请求类
class Qingqiu(threading.Thread):
    def __init__(self,page_url,img_url,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.page_url = page_url
        self.img_url = img_url

    #创建运行方法
    def run(self):
        while True:
            #判断队列是否为空，为空返回True,停止响应
            if self.page_url.empty():
                break
            #取出队列里面的url
            url = self.page_url.get()
            #返回给下一个方法解析数据
            self.parse(url)

    def parse(self,url):
        #获取响应
        response = requests.get(url)
        #获取解析文本
        html = etree.HTML(response.text)
        #获取图片链接
        imgs = html.xpath("//*[@class='page-content text-center']/div/a/img[2]/@data-original")
        #获取图片名字
        name = html.xpath("//*[@class='page-content text-center']/div/a/p/text()")

        #zip函数可以准确放入
        for type_,url_name in zip(imgs,name):
            #拼接图片名字
            type_1 = str(type_).split(r".")[-1]
            typeses = url_name + ".{}".format(type_1)
            #把图片链接，和名字放入到图片的队列里面
            self.img_url.put((type_,typeses))

#写另一个图片下载的类
class Con(threading.Thread):
    def __init__(self,page_url,img_url,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.page_url = page_url
        self.img_url = img_url

    #写下载图片的方法
    def run(self):
        while True:
            if self.page_url.empty() and self.img_url.empty():
                break
            type_,typeses = self.img_url.get()
            request.urlretrieve(type_, "image/" + typeses)
            print(typeses,"图片已经下载完毕")

            
def main():
    page_url = Queue(100)
    img_url =  Queue(500)
    for i in range(1,101):
        url = "https://www.doutula.com/photo/list/?page={}".format(i)
        #这里要输入url到请求队列
        page_url.put(url)
    #创建线程,把队列放入线程里面
    for a in range(15):
        p = Qingqiu(page_url,img_url)
        #开启线程
        p.start()

    for a in range(15):
        c = Con(page_url,img_url)
        c.start()


if __name__ == "__main__":
    main()


    

