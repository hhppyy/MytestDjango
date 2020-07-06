"""MyDjango URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from xiaoyu import views
from django.views.static import serve
from . import settings
import xadmin

urlpatterns = [
    path('xadmin/', xadmin.site.urls),#xadmin后台
    path('admin/', admin.site.urls),#自带，admin后台
    url(r'^accounts/login/$',views.login_auth),
    # path('hello/', views.hello),
    url(r'^hello/$', views.hello),
    # url(r'^login/$', views.login, name="login"),
    path('han/test/<year>/<month>.html', views.archive),
    url(r'^han/(?P<year>[0-9]{4})/(?P<month>[0-9]{2}).html$', views.archive),
    url(r'^demo/$', views.demo),
    url(r'^person/$', views.personView),
    url(r'^navlist/$', views.navlistView),
    url(r'^artical/$', views.htmlView),
    url(r'^tell/$', views.get_tel),
    url(r'^create/$', views.create_info),
    url(r'^loginauth/$', views.login_auth),
    url(r'^registerauth/$', views.register_auth),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
]
