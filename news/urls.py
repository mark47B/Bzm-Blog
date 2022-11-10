from django.urls import path
from news import views

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<int:category_id>/', views.get_category, name='category'),
]
