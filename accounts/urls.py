from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    # path('profile/', views.profile_view, name='profile_view'),

    # dashboard url
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('edit_user_profile/<str:username>/', views.edit_user_profile, name='edit_user_profile'),
    path('edit_profile/<str:username>/', views.edit_profile, name='edit_profile'),
    path('delete_profile/<str:username>/', views.delete_profile, name='delete_profile'),
    path('news/', views.article_list, name='article_list'),
    path('categories/', views.category_list, name='category_list'),
    path('tags/', views.tag_list, name='tag_list'),
    path('category_create/', views.category_create, name='category_create'),
    path('category_edit/<slug:slug>/', views.category_edit, name='category_edit'),
    path('category_delete/<slug:slug>/', views.category_delete, name='category_delete'),
    path('category_search/', views.category_search, name='category_search'),
    path('tag_create/', views.tag_create, name='tag_create'),
    path('tag_edit/<str:title>/', views.tag_edit, name='tag_edit'),
    path('tag_delete/<str:title>/', views.tag_delete, name='tag_delete'),
    path('tag_search/', views.tag_search, name='tag_search'),
    path('article_create/', views.article_create, name='article_create'),
    path('article_edit/<slug:slug>/', views.article_edit, name='article_edit'),
    path('article_delete/<slug:slug>/', views.article_delete, name='article_delete'),
    path('article_search/', views.article_search, name='article_search'),

]
