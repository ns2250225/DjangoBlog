# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404

from .models import Article, Tag

# Create your views here.
class IndexView(View):

    def get(self, request):
        posts = Article.objects.all()
        tags = Tag.objects.all()
        paginator = Paginator(posts, 10)
        page = request.GET.get('page')

        try:
            posts_list = paginator.page(page)
        except PageNotAnInteger:
            posts_list = paginator.page(1)
        except EmptyPage:
            posts_list = paginator.page(paginator.num_pages)
        return render(request, 'index.html', {"posts_list": posts_list, "tags": tags})

    def post(self, request):
        pass


class DetailView(View):

    def get(self, request, id):
        tags = Tag.objects.all()
        try:
            posts = Article.objects.get(id=str(id))
        except Article.DoesNotExist:
            raise Http404
        return render(request, 'detail.html', {'posts': posts, 'tags': tags})

    def post(self, request):
        pass


class TagView(View):

    def get(self, request, tagId):
        # posts_list = Article.objects.get(article_tag=tagId)
        tmp = Tag.objects.get(id=tagId)
        tags = Tag.objects.all()
        posts_list = tmp.article_set.all()
        # print posts_list
        return render(request, 'tag.html', {"posts_list": posts_list, "tags": tags})

    def post(self, request):
        pass


class SearchView(View):

    def get(self, request):
        kw = request.GET.get('kw')
        if not kw:
            return redirect('/')
        else:
            posts_list = Article.objects.filter(article_title__icontains=kw)
            tags = Tag.objects.all()
            return render(request, 'search.html', {"posts_list": posts_list, "tags": tags})

    def post(self, request):
        pass