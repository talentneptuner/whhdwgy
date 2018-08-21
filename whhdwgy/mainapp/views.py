import json

from django.shortcuts import render

from django.views.generic.base import View
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect

from .models import History, Sight, SightImage, Part


# Create your views here.

class HistoryView(View):

    def get(self, request):
        history = History.objects.all()
        historylist = []
        for item in history:
            one = dict(date=str(item.date), title=item.title, imageurl='http://localhost:8000/media/' + str(item.image))
            historylist.append(one)
            # print(item.title)
        return HttpResponse(json.dumps(historylist, ensure_ascii=False), content_type='application/json')


class SightView(View):

    def get(self, request):
        sights = Sight.objects.all()
        sightlist = []
        for item in sights:
            one = dict(id=item.id, name=item.name, left=item.left, top=item.top)
            sightlist.append(one)
            print(item.name)
        return HttpResponse(json.dumps(sightlist, ensure_ascii=False), content_type='application/json')


class SightInfoView(View):

    def get(self, request, id):
        sight = Sight.objects.get(id=id)
        imagelist = []
        temp_imagelist = SightImage.objects.filter(sight=sight)
        for item in temp_imagelist:
            imagelist.append('http://localhost:8000/media/' + str(item.image))
        desc = ""
        if sight.desc:
            desc = sight.desc
        else:
            desc = "暂无介绍"
        info = dict(title=sight.name, imagelist=imagelist, desc=desc)
        return HttpResponse(json.dumps(info, ensure_ascii=False), content_type='application/json')


class PartView(View):

    def get(self, request):
        parts_1 = Part.objects.filter(cataglory='sc')
        parts_2 = Part.objects.filter(cataglory='zn')
        parts_3 = Part.objects.filter(cataglory='jx')
        a_list = []
        result = []
        for item in parts_1:
            dict_temp = dict(id=item.id, name=item.name)
            a_list.append(dict_temp)
        dict_1 = dict(id=0, name='领导层', list=a_list)
        result.append(dict_1)
        a_list = []
        for item in parts_2:
            dict_temp = dict(id=item.id, name=item.name)
            a_list.append(dict_temp)
        dict_2 = dict(id=1, name='职能部', list=a_list)
        result.append(dict_2)
        a_list = []
        for item in parts_3:
            dict_temp = dict(id=item.id, name=item.name)
            a_list.append(dict_temp)
        dict_3 = dict(id=2, name='教学部', list=a_list)
        result.append(dict_3)
        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json')
