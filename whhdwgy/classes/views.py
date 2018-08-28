import json

from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect

from .models import Grade, ClassOne, ClassImage, Prize


# Create your views here.

class getClassListView(View):

    def get(self, request):
        grades = Grade.objects.all()
        result = []
        for item in grades:
            tmp = []
            classes = ClassOne.objects.filter(grade=item)
            for oneclass in classes:
                tmp.append(dict(name=oneclass.name, id=oneclass.id))
            result.append(dict(id=item.id, name=item.name, classlist=tmp))
        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json')


class getClassInfoView(View):

    def get(self, request, id):
        classinfo = ClassOne.objects.get(id=id)
        prize = Prize.objects.filter(p_class=classinfo)
        reprize = []
        for item in prize:
            reprize.append(item.desc)
        images = ClassImage.objects.filter(p_class=classinfo)
        imagelist = []
        for item2 in images:
            imagelist.append(
                dict(id=item2.id, desc=item2.desc, image='http://localhost:8000/media/' + str(item2.image)))
        result = dict(id=classinfo.id, name=classinfo.name, desc=classinfo.desc.split('\r\n'), course=classinfo.course.split('\r\n'),
                      prizes=reprize, images=imagelist)
        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json')
