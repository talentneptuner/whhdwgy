import xadmin

from xadmin import views

from mainapp.models import History,  Part, Person, SightImage


class HistoryAdmin(object):
    list_display = ['date', 'title', 'addtime']
    readonly_fields = ['addtime']
    ordering = ['-addtime']


xadmin.site.register(History, HistoryAdmin)


class SightImageAdmin(object):
    list_display = ['image', 'sight']


xadmin.site.register(SightImage, SightImageAdmin)


class PartAdmin(object):
    list_display = ['name', 'cataglory']


xadmin.site.register(Part, PartAdmin)


class PersonAdmin(object):
    list_display = ['name', 'partnode']
    list_filter = ['partnode']


xadmin.site.register(Person, PersonAdmin)


class GlobalSettings(object):
    # 修改title
    site_title = '信息添加后台'
    # 修改footer
    site_footer = '武汉海淀外国语学校'
    # 收起菜单
    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, GlobalSettings)
