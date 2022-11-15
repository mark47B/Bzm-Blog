from django.urls import path
from news import views

urlpatterns = [
    # path('', views.index, name='home'),
    path('', views.HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', views.NewsByCategory.as_view(extra_context={'title': 'ffff'}), name='category'),
    path('news/<int:pk>/', views.view_news.as_view(), name='view_news'),
    path('news/add-news/', views.CreateNews.as_view(), name='add_news'),
]
