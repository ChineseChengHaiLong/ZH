from django.db import models

# Create your models here.

class Lianjiaa(models.Model):
    title = models.CharField(unique=True, max_length=255, blank=True, null=True)
    reddess = models.CharField(max_length=255, blank=True, null=True)
    acreage = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=255, blank=True, null=True)
    gzrs = models.CharField(max_length=255, blank=True, null=True)
    liulanshu = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    unit_price = models.CharField(max_length=255, blank=True, null=True)
    urls = models.CharField(max_length=255, blank=True, null=True)
    chaoxiang = models.CharField(max_length=255, blank=True, null=True)
    geju = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lianjiaA'


class Lianjiab(models.Model):
    types = models.CharField(max_length=255, blank=True, null=True)
    louceng = models.CharField(max_length=255, blank=True, null=True)
    mianji = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(unique=True, max_length=255, blank=True, null=True)
    jieguo = models.CharField(max_length=255, blank=True, null=True)
    taofang_mianji = models.CharField(max_length=255, blank=True, null=True)
    jianzhu_leixing = models.CharField(max_length=255, blank=True, null=True)
    jianzhu_chaoxiang = models.CharField(max_length=255, blank=True, null=True)
    jianzhu_jiegou = models.CharField(max_length=255, blank=True, null=True)
    jianzhu_xiushan = models.CharField(max_length=255, blank=True, null=True)
    jianzhu_tihu = models.CharField(max_length=255, blank=True, null=True)
    jianzhu_gongnuan = models.CharField(max_length=255, blank=True, null=True)
    jianzhu_dianti = models.CharField(max_length=255, blank=True, null=True)
    jianzhu_nianxian = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    reddesss = models.CharField(max_length=255, blank=True, null=True)
    time = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    guapai_time = models.CharField(max_length=255, blank=True, null=True)
    jiaoyi_shuxing = models.CharField(max_length=255, blank=True, null=True)
    shang_time = models.CharField(max_length=255, blank=True, null=True)
    yongtu = models.CharField(max_length=255, blank=True, null=True)
    nianxian = models.CharField(max_length=255, blank=True, null=True)
    chanquan_suoyou = models.CharField(max_length=255, blank=True, null=True)
    diya = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lianjiaB'