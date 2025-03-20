from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Profile)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'email', 'created_at']
    search_fields = ['user']
