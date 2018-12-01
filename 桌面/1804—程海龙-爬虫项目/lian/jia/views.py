from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from jia import models
import json
from django.http import HttpResponse
from django.forms.models import model_to_dict

#查询A表里面所有的数据
def category_list(request):
    """
    通过这个接口获取分类的列表
    :param request:
    :return:
    """

    if request.method == "GET":

        query = models.Lianjiaa.objects.all()

        datalist = [model_to_dict(model) for model in query]
        result = {
            'code':200,
            'list':datalist
        }

        return HttpResponse(
            json.dumps(result,ensure_ascii=False),
            content_type='application/json'
        )

#查询A表里面根据title查询房屋数据
def company_detail(request):
    """
    通过这个接口获取公司详情
    :param request:
    :return:
    """

    if request.method == "GET":
        #根据公司名称查询,获取公司名称
        name = request.GET.get('title')

        print('11111',name)

        query = models.Lianjiaa.objects.filter(title=name)

        datalist = [model_to_dict(model) for model in query]

        result = {
            'code': 200,
            'list': datalist
        }

        return HttpResponse(
            json.dumps(result, ensure_ascii=False),
            content_type='application/json'
        )

#查询B表里面所有的数据
def company_list_all(request):
    """
    通过这个接口获取公司列表
    :param request:
    :return:
    """

    if request.method == "GET":
        # 返回QuerySet结果集,里面存放的是字典
        query = models.Lianjiab.objects.values('types','louceng','mianji','jieguo','taofang_mianji','jianzhu_leixing','jianzhu_chaoxiang','jianzhu_jiegou','number','shang_time','title')
        #遍历得到列表
        datalist = [i for i in query]

        result = {
            'code': 200,
            'list': datalist
        }

        return HttpResponse(
            json.dumps(result, ensure_ascii=False),
            content_type='application/json'
        )

#查询B表里面根据title查询房屋数据
def company_list_by_sign(request):
    """
    通过这个接口获取分类下的公司列表
    :param request:
    :return:
    """

    if request.method == "GET":
        #获取关键字
        sign = request.GET.get('title')
        #返回QuerySet结果集,里面存放的是字典
        query = models.Lianjiab.objects.filter(title=sign).values('types','louceng','mianji','jieguo','taofang_mianji','jianzhu_leixing','jianzhu_chaoxiang','jianzhu_jiegou','number','shang_time','title')
        datalist = [i for i in query]

        result = {
            'code': 200,
            'list': datalist,
            'count':len(datalist),
            'sign':sign,
        }

        return HttpResponse(
            json.dumps(result, ensure_ascii=False),
            content_type='application/json'
        )


