from django.urls import path
from . import views


app_name = 'news'
urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<slug:slug>/', views.article_detail, name='article_detail'),
    path('news/', views.article_list, name='article_list'),
    path('article_search/', views.article_search, name='article_search'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<slug:slug>/', views.category_article, name='category_article'),
    path('tag/<str:title>/', views.article_tag, name='article_tag'),
    path('contact/', views.contact, name='contact'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
