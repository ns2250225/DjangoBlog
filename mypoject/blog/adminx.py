# -*- coding: utf-8 -*-

from xadmin import views
from .models import Article, Tag
import xadmin


class ArticleAdmin(object):
    style_fields = {'article_content': 'ueditor'}


class TagAdmin(object):
    pass


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "博客后台管理系统"
    site_footer = "ns2250225的博客"
    menu_style = "accordion"

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Tag, TagAdmin)
