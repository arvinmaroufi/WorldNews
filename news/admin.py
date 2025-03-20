from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'views', 'created_at', 'publish']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['publish']
    list_editable = ['publish']
    search_fields = ['title']


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    search_fields = ['name']


@admin.register(models.Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_at']
    search_fields = ['email']
