from django.db import models

from datetime import date, datetime

# Create your models here.

class Grade(models.Model):
    name = models.CharField(verbose_name="年级名",max_length=100)
    addtime = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '年级'
        verbose_name_plural = verbose_name

class ClassOne(models.Model):
    name = models.CharField(verbose_name='班级名',max_length=50)
    desc = models.TextField(verbose_name='班级介绍',null=True,blank=True)
    course = models.TextField(verbose_name='课程设置',null=True,blank=True)
    grade = models.ForeignKey(Grade,verbose_name='所属年级',null=True,blank=True,on_delete=models.CASCADE)
    addtime = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = '班级'
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.name

class Prize(models.Model):
    desc = models.CharField(max_length=300,verbose_name='奖项描述')
    p_class = models.ForeignKey(ClassOne,verbose_name='所属班级',on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='照片',upload_to="prize/%Y/%m",null=True,blank=True)
    addtime = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = '班级奖项'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.desc

class ClassImage(models.Model):
    desc = models.CharField(max_length=100,verbose_name='照片描述')
    image = models.ImageField(verbose_name='照片',upload_to="class/%Y/%m")
    p_class = models.ForeignKey(ClassOne, verbose_name='所属班级',on_delete=models.CASCADE)
    addtime = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = '班级风采'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.p_class.name + self.desc

