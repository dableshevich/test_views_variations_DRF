from django.contrib import admin

from .models import Post, Group, Comment

# Register your models here.
@admin.register(Post, Group, Comment)
class CustomAdmin(admin.ModelAdmin):
    pass