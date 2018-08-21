"""whhdwgy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from django.views.static import serve
import xadmin

from .settings import MEDIA_ROOT

from mainapp.views import HistoryView,SightView,SightInfoView,PartView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    re_path('media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    path('gethistory/', HistoryView.as_view()),
    path('getsights/',SightView.as_view()),
    path('getsightinfo/<str:id>',SightInfoView.as_view()),
    path('getparts/',PartView.as_view()),
]
