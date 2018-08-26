from datetime import date, datetime

from django.db import models


# Create your models here.

class History(models.Model):
    date = models.DateField(verbose_name="日期", default=date.today)
    image = models.ImageField(verbose_name='照片', null=True, blank=True, upload_to="history/%Y/%m")
    title = models.CharField(verbose_name='标题', max_length=200, null=True, blank=True)
    addtime = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = '历史事件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Part(models.Model):
    name = models.CharField(verbose_name="职能名称", default='校长', max_length=50)
    # up_node = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    cataglory = models.CharField(choices=(('sc', '领导层'), ('zn', '职能部门'), ('jx', '教学部')), default='zn', max_length=10)
    addtime = models.DateTimeField(verbose_name="添加时间", default=datetime.now)
    clickable = models.BooleanField(verbose_name='可点击',default=False)

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name





class Person(models.Model):
    name = models.CharField(verbose_name="姓名", default='xxx', max_length=50)
    image = models.ImageField(verbose_name='照片', null=True, blank=True, upload_to="person/%Y/%m")
    partnode = models.ForeignKey(Part, verbose_name="所属部门",null=True,blank=True, on_delete=models.CASCADE)
    addtime = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Sight(models.Model):
    name = models.CharField(verbose_name='名称', default='未命名', max_length=100)
    left = models.IntegerField(verbose_name='左边距', default=0)
    top = models.IntegerField(verbose_name='上边距', default=0)
    desc = models.TextField(verbose_name='简介',null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '景点'
        verbose_name_plural = verbose_name


class SightImage(models.Model):
    image = models.ImageField(verbose_name='照片', null=True, blank=True, upload_to="sight/%Y/%m")
    sight = models.ForeignKey(Sight,verbose_name='景点名称',on_delete=models.CASCADE)

    class Meta:
        verbose_name = '景点照片'
        verbose_name_plural = verbose_name
