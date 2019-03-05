# coding: utf-8
__author__ = "wengwenyu"
HISTORY_DICT = {}
import time

from rest_framework.throttling import BaseThrottle, SimpleRateThrottle


# django restframework 带一些内置的 限流模块

class MyThrottle(BaseThrottle):
    def __init__(self):
        self.history = None

    def allow_request(self, request, view):
        # 逻辑   1. ip 2.判断
        ip_addr = request._request.META["REMOTE_ADDR"]
        # 获取当前时间
        ctime = time.time()
        # 第1次 每个人有每分钟3机会
        if ip_addr not in HISTORY_DICT:
            HISTORY_DICT[ip_addr] = [ctime, ]
            return True
        # 如果有这条记录
        history = HISTORY_DICT[ip_addr]

        self.history = history
        # [9:13:10 , 9:13:10,9:14:19] []
        #
        while history and history[-1] < ctime - 60:
            # 去掉 历史记录里面的过期时间
            history.pop()

        # 访问记录 小于3次
        if len(history) < 3:
            history.insert(0, ctime)
            return True

        # 如果访问返回True表示可以继续往下走，False被限制访问
        return False

    def wait(self):
        # 这里是应该返回 剩余的 等待时间
        # 要先拿到历史记录
        # 当前时间
        ctime = time.time()
        return 60 - (ctime - self.history[-1])


# 如果我们要使用 内置的限流类
# SimpleRateThrottle 内置的 写好的 限流组件
class MyThrottle2(SimpleRateThrottle):
    scope = "myscope"

    # 缓存配置
    def get_cache_key(self, request, view):
        return self.get_ident(request)


class UserThrottle(SimpleRateThrottle):
    scope = "user_scope"

    def get_cache_key(self, request, view):
        return request.user.username
