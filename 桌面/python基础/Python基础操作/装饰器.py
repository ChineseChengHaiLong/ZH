import time
#import datatime 


def logger(func):

    def inner(*args,**kwargs):
        print('正在调用装饰器.........')
        now = int(time.time())
        timeArray = time.localtime(now) #转化成数组
        # print (timeArray)
        otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S",timeArray) #转化时间格式
        print(otherStyleTime)
        time.sleep(2)
        return func(*args,**kwargs)
    return inner
@logger
def foo1(x,y):
    return x * y

@logger
def foo2():
    return 2

print(foo1(4,5))

print(foo2())
