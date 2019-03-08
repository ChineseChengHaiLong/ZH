


#模块一发送验证码***********************************************************************************************
#获取手机号发送验证码
import requests
import json
class YuanPian(object):
    def __init__(self, api_key):

        #个人在云片网的身份
        self.api_key = api_key

        #要请求的url  ======>>>>>>>>发短信
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self,code,mobile):
        """
            apikey	string	是	是	用户唯一标识，在管理控制台获取	9b11127a9701975c734b8aee81ee3526
            mobile	string	是	是	接收的手机号，仅支持单号码发送；	15205201314
            text	string	是	是	已审核短信模板	【云片网】您的验证码是1234
            让云片网发送短信验证 我们需要传参数
            code:短信验证码
            mobile:手机号码

        """

        params = {
            "apikey":self.api_key,
            "moblie":mobile,
            "text":"[四方科技]您的验证码是{}.如过不是本人操作，请忽略此短信".format(code)
            }

        #发起一个网络请求，得到响应
        response = requests.post(self.single_send_url,data=params)

        #提示一下
        ret = json.loads(response.text)
        return ret


#模块二（用户注册序列化）*************************************************************************************************
import re
from LeShop import settings
from rest_framework import serializers
from datetime import datetime,timedelta
#导入用户模型
from django.contrib.auth import get_user_model
from .models import VerifyCode

from rest_framework.validators import UniqueValidator #导入验证器

User = get_user_model()
#只做验证手机号
#发送验证马的时候，她传手机号
class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11,label="手机号")

    #validate + 字段名字 表示用户发mobile会调用validate_mobile这个方法
    def validate_mobile(self, mobile):
        #验证方法
        #1、验证是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已经注册")

        #2、验证号码正则表达式  是否真是
        if not  re.match(settings.REGEX_MOBILE,mobile):
            raise serializers.ValidationError("手机号不正确")

        #3、判断频率一分钟只能发一次
        one_minutes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)

        if VerifyCode.objects.filter(add_time__gt=one_minutes_ago,mobile=mobile):
            raise serializers.ValidationError("60秒内只能发送一次")

        return mobile




#用户注册
class UserRegSerializer(serializers.ModelSerializer):
    #由于user表李没有code字段，我们需要自己创造一个
    code = serializers.CharField(max_length=4,min_length=4,error_messages={
        "max_length":"验证码的格式不对",
        "min_length":"验证码的格式不对"
    },label="验证码",write_only=True)

    #对用户进行判断是否能注册 校验验证字段在模型上是否唯一
    username = serializers.CharField(
        label="用户名",
        validators=[UniqueValidator(queryset=User.objects.all(),message="用户已经存在")]
    )


    #我们要对密码明文进行加密
    # 使用 <input type="password"> 作为输入。
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )
    # 存数据库密码明文加密
    def create(self, validated_data):
        # 调用父类方法create传参数 //可以拿到模型类的对象
        user = super().create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


    def validate_code(self, code):
        # 判断 验证码是否正确、是否过期
        # initial_data是前端post过来的数据
        #获取手机号最新的验证码
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data["username"]).order_by("-add_time")

        if verify_records:
            #取出最后一个发送的验证码
            last_recode = verify_records[0]
            #发送过
            #判断时间有效期5分钟
            five_minutes_ago = datetime.now() - timedelta(hours=0,minutes=5,seconds=0)
            if five_minutes_ago > last_recode.add_time:
                raise serializers.ValidationError("验证码已过期")

            #判断验证码时候正确
            if code != last_recode.code:
                raise serializers.ValidationError("验证码错误")
        else:
            #没有发送过
            raise serializers.ValidationError("请输入正确验证码")
    #验证之后把code 删掉，因为注册表没有code字段
    def validate(self, attrs):
        #先把全端传过来的username赋值给后端的mobile
        attrs['mobile'] = attrs['username']

        del attrs['code']
        return attrs

	 #前端传过来的参数
    class Meta:
        model = User
        fields = ("username","mobile","code","password")











#模块二（发送验证码并保存，注册登录）**************************************************************************************************************

from  rest_framework import viewsets
# Create your views here.
from rest_framework import mixins
from .serializers import SmsSerializer
from random import choice
from rest_framework.response import Response
from rest_framework import status
from LeShop import settings
from utils.yuanpian import YuanPian
from .models import VerifyCode
from .serializers import UserRegSerializer,UserDetailSerializer
from .models import UserProfile
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from utils.permissions import permissions
from rest_framework_jwt.settings import api_settings
class SmsCodeViewset(mixins.CreateModelMixin,viewsets.GenericViewSet):
    serializer_class = SmsSerializer     #1\只做验证手机号  #发送验证马的时候，她传手机号


    def generate_code(self):
        """
        生成四位数字的验证码
        """

        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)
    #重写这个方法
    #1、父类做的事情 ，很简单就存一个模型到数据库，添加一个新的数据，不满足需求
    #2、我要的事情是在父类的基础上
    #2、发短信验证码（随机生成数字）
    #4、发送YunPian 接收返回值 code=0是否成功
    #5、保存这个验证ma
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data) #获取序列化的类 验证手机号 SmsSerializer
        serializer.is_valid(raise_exception=True)#验证

        #可用的手机号
        yuan_pian = YuanPian(settings.APIKEY)

        #生成验证码
        code = self.generate_code()

        #validated_data拿到序列化里面的字段
        sms_status = yuan_pian.send_sms(code,mobile=serializer.validated_data["mobile"]) # 调用yuan_pian.send_sms方法发送验证码

        if sms_status['code']!=0:
            #失败
            return Response(sms_status['msg'],status=status.HTTP_400_BAD_REQUEST)
        else:
            #成功
            VerifyCode(code=code,mobile=serializer.validated_data["mobile"])
            return Response(sms_status['msg'],status=status.HTTP_201_CREATED)




        self.perform_create(serializer)#保存
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserViewset(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    serializer_class = UserRegSerializer
    queryset = UserProfile.objects.all()

    # auth是 做用户认证的  SessionAuthentication保证后台能登lu
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)




    #注册并且登录
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data) #获取序列化的类
        serializer.is_valid(raise_exception=True)  #验证

        #最终注册的用户
        user = self.perform_create(serializer)  #调用保存

        #帮助他登录 拿到token

        #要登录成功给用户返回的数据
        ret_dict = serializer.data
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        ret_dict['token'] = token
        ret_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(ret_dict, status=status.HTTP_201_CREATED, headers=headers)

   def perform_create(self, serializer):
        return serializer.save()
