# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.


class Tag(models.Model):
    tag_name = models.CharField(max_length=20, verbose_name=u"标签名")

    def __unicode__(self):
        return self.tag_name

    class Meta:
        verbose_name = u"文章标签"
        verbose_name_plural = verbose_name


class Article(models.Model):
    article_title = models.CharField(max_length=50, verbose_name=u"文章标题")
    article_content = UEditorField(verbose_name=u'文章正文', width=600, height=300, imagePath="blog/ueditor/", filePath="blog/ueditor/", default="")
    article_add_time = models.DateTimeField(auto_now=True, verbose_name=u"发布时间")
    article_tag = models.ManyToManyField(Tag, verbose_name=u"标签")

    def __unicode__(self) :
        return self.article_title.encode('utf-8')

    class Meta:
        verbose_name = u"文章"
        verbose_name_plural = verbose_name
        ordering = ['-article_add_time']