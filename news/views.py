from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import News, Category
from .forms import NewsForm

def index(request: HttpRequest):
    news = News.objects.all()
    context = {'news': news, 
    'title': 'Список записей'
    }
    return render(request,  'news/index.html', context)

def get_category(request: HttpRequest, category_id: int):
    news_cat = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context={'news_cat': news_cat,
    'category': category,
    'title': category.title}
    return render(request, template_name='news/category.html', context=context)

def view_news(request: HttpRequest, news_id: int):
    news_item = get_object_or_404(News, pk=news_id)
    context = {
        'title': news_item.title,
        'news_item': news_item
        }
    return render(request, template_name='news/view_news.html', context=context)


def add_news(request: HttpRequest):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            # news = News.objects.create(**form.cleaned_data) # Если форма не связана с моделью
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    context = {'title': 'Добавление новости',
    'form': form}
    return render(request, template_name='news/add-news.html', context=context)
