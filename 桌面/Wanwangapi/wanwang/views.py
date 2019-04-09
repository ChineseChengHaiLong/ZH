from django.shortcuts import render

# Create your views here.

#实现简单的接口展示数据（分类列表接口，论文详情接口）
from rest_framework.views import APIView
from rest_framework.response import Response
from wanwang import models
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
from rest_framework.parsers import JSONParser,FormParser
from rest_framework import serializers
from rest_framework.throttling import SimpleRateThrottle

class MyPageNumberPagination(PageNumberPagination):
    """
    http://api.example.org/accounts/?page=4
    http://api.example.org/accounts/?page=4&page_size=10
    """
    #默认每页显示的条数
    page_size = 5
    #设置要传入的页码关键字参数
    page_query_param = 'page'
    #设置要传入的每页返回数据条数的关键字参数
    page_size_query_param = 'pagesize'
    #设置每页最大的返回数据量
    max_page_size = 15

class CategroryConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Conference
        #fields = '__all__'
        fields = ['id','title', 'url']

class CategroryDegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Degree
        # fields = '__all__'
        fields = ['id','title', 'url']

class CategroryPerioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Perio
        # fields = '__all__'
        fields = ['id','title', 'url']

class CategroryTechSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tech
        # fields = '__all__'
        fields = ['id','title','url']

class CategroryArticleListView(APIView):

    parser_classes = [JSONParser,FormParser]

    def get(self,request,*args,**kwargs):
        #使用query_parmas,获取get请求的查询参数
        tag = request.query_params.get('tag')
        print(tag)

        if tag == 'conference':
            obj = models.Conference.objects.all()
            pagination = MyPageNumberPagination()
            obj = pagination.paginate_queryset(obj,request,view=self)
            ser = CategroryConferenceSerializer(instance=obj,many=True)
        elif tag == 'degree':
            obj = models.Degree.objects.all()
            pagination = MyPageNumberPagination()
            obj = pagination.paginate_queryset(obj, request, view=self)
            ser = CategroryDegreeSerializer(instance=obj, many=True)
        elif tag == 'perio':
            obj = models.Perio.objects.all()
            pagination = MyPageNumberPagination()
            obj = pagination.paginate_queryset(obj, request, view=self)
            ser = CategroryPerioSerializer(instance=obj, many=True)
        elif tag == 'tech':
            obj = models.Tech.objects.all()
            pagination = MyPageNumberPagination()
            obj = pagination.paginate_queryset(obj, request, view=self)
            ser = CategroryTechSerializer(instance=obj, many=True)

        return Response(ser.data)


class ConferenceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Conference
        fields = '__all__'

class DegreeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Degree
        fields = '__all__'

class PerioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Perio
        fields = '__all__'

class TechDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tech
        fields = '__all__'

class CategroryArticleDetailView(APIView):
    parser_classes = [JSONParser, FormParser]

    def get(self, request, *args, **kwargs):
        # 使用query_parmas,获取get请求的查询参数
        tag = request.query_params.get('tag')
        id = kwargs.get('pk')
        print(tag,id)

        if tag == 'conference':
            obj = models.Conference.objects.filter(id=id).first()
            ser = ConferenceDetailSerializer(instance=obj,many=False)
        elif tag == 'degree':
            obj = models.Degree.objects.filter(id=id).first()
            ser = DegreeDetailSerializer(instance=obj,many=False)
        elif tag == 'perio':
            obj = models.Perio.objects.filter(id=id).first()
            ser = PerioDetailSerializer(instance=obj,many=False)
        elif tag == 'tech':
            obj = models.Tech.objects.filter(id=id).first()
            ser = TechDetailSerializer(instance=obj,many=False)

        return Response(ser.data)
