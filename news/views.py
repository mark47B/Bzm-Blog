from re import template
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import News, Category

def index(request: HttpRequest):
    news = News.objects.all()
    category = Category.objects.all()
    context = {'news': news, 
    'title': 'Список новостей',
    'category': category
    }
    return render(request,  'news/index.html', context)

def get_category(request: HttpRequest, category_id: int):
    news_cat = News.objects.filter(category_id=category_id)
    category = Category.objects.filter(pk=category_id)
    categories = Category.objects.all()
    context={'news_cat': news_cat,
    'category': category,
    'categories': categories}
    return render(request, template_name='news/category.html', context=context)
