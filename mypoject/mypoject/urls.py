"""mypoject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
import xadmin
import settings
from blog.views import IndexView, DetailView, TagView, SearchView
from django.conf.urls.static import static

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls, name="xadmin"),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}, name="media"),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^(?P<id>\d+)/$', DetailView.as_view(), name='detail'),
    url(r'^tag/(?P<tagId>.*)/$', TagView.as_view(), name='tag'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
