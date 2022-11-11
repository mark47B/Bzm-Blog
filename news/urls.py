from django.urls import path
from news import views

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<int:category_id>/', views.get_category, name='category'),
    path('news/<int:news_id>/', views.view_news, name='view_news'),
    path('news/add-news/', views.add_news, name='add_news'),
]
