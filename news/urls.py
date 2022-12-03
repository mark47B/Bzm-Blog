from django.urls import path, include
from news import views

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path("logout/", views.user_logout, name="logout"),
    path('feedback/', views.feedback, name='feedback'),
    # path('', views.index, name='home'),
    path('', views.HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', views.NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', views.view_news.as_view(), name='view_news'),
    path('news/add-news/', views.CreateNews.as_view(), name='add_news'),
]
