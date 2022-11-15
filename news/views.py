from typing import List
from unicodedata import category
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import News, Category
from .forms import NewsForm


# CBV - class based views
class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Main page'} # Только для статических данных

    def get_context_data(self, *, object_list=None, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        return context
    
    def get_queryset(self):
        return News.objects.filter(is_published = True)

# def index(request: HttpRequest):
#     news = News.objects.all()
#     context = {'news': news, 
#     'title': 'Список записей'
#     }
#     return render(request,  'news/index.html', context)

class NewsByCategory(ListView):
    model = News
    template_name = 'news/category_list.html'
    context_object_name = 'news_cat'
    allow_empty = False
    def get_context_data(self, *, object_list=None, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        context['category'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context
    def get_queryset(self):
        return News.objects.filter(is_published = True, category_id=self.kwargs['category_id'])
# def get_category(request: HttpRequest, category_id: int):
#     news_cat = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     context={'news_cat': news_cat,
#     'category': category,
#     'title': category.title}
#     return render(request, template_name='news/category.html', context=context)

class view_news(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    

# def view_news(request: HttpRequest, news_id: int):
#     news_item = get_object_or_404(News, pk=news_id)
#     context = {
#         'title': news_item.title,
#         'news_item': news_item
#         }
#     return render(request, template_name='news/view_news.html', context=context)

class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add-news.html'
    success_url =  reverse_lazy('home')

# def add_news(request: HttpRequest):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # news = News.objects.create(**form.cleaned_data) # Если форма не связана с моделью
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     context = {'title': 'Добавление новости',
#     'form': form}
#     return render(request, template_name='news/add-news.html', context=context)
