from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import News

def index(request: HttpRequest):
    news = News.objects.all()
    return render(request,  'news/index.html', {'news': news, 'title': 'Список новостей'})