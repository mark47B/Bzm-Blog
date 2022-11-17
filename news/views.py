from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login, logout
from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm
from .utils import MyMixin


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid(): 
            # news = News.objects.create(**form.cleaned_data) # Если форма не связана с моделью
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def test(request):
    objects = ['john1', 'paul2', 'george3', 'ringo4', 'john2', 'paul_2', 'george2', 'ringo2',]
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'news/test.html', {'page_obj': page_objects, 'title': 'TEST'})


# CBV - class based views
class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'

    # extra_context = {'title': 'Main page'} # Только для статических данных
    mixin_prob = 'Probe!'
    paginate_by = 5


    def get_context_data(self, *, object_list=None, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Main page')
        context['mixin_prob'] = self.get_prob()
        return context
    
    def get_queryset(self):
        return News.objects.filter(is_published = True).select_related('category')

# def index(request: HttpRequest):
#     news = News.objects.all()
#     context = {'news': news, 
#     'title': 'Список записей'
#     }
#     return render(request,  'news/index.html', context)

class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'news/category_list.html'
    context_object_name = 'news_cat'
    allow_empty = False
    def get_context_data(self, *, object_list=None, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        context['category'] = context['title']
        return context
    def get_queryset(self):
        return News.objects.filter(is_published = True, category_id=self.kwargs['category_id']).select_related('category')
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

class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add-news.html'
    success_url =  reverse_lazy('home')
    login_url = '/admin/'

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
