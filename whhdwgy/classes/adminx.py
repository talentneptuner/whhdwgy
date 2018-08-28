import xadmin

from xadmin import views

from .models import Grade, ClassOne, ClassImage, Prize


class GradeAdmin(object):
    list_display = ['name']
    ordering = ['-addtime']
    model_icon = 'fa fa-graduation-cap'


class ClassoneAdmin(object):
    list_display = ['name', 'grade']
    list_filter = ['grade']
    ordering = ['-addtime']


class ClassImageAdmin(object):
    list_display = ['desc']
    list_filter = ['p_class']
    ordering = ['-addtime']


class PrizeAdmin(object):
    list_display = ['desc']
    list_filter = ['p_class']
    ordering = ['-addtime']


xadmin.site.register(Grade,GradeAdmin)
xadmin.site.register(ClassOne,ClassoneAdmin)
xadmin.site.register(ClassImage,ClassImageAdmin)
xadmin.site.register(Prize,PrizeAdmin)
