# -*- coding: utf-8 -*-
"""Import Public modules."""
from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    """Customized Admin Page."""

    # list_display 定制列表页显示的字段
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    # list_filter 定制右侧过滤栏
    list_filter = ('status', 'created', 'publish', 'author')
    # search_fields 定制搜索框
    search_fields = ('title', 'body')
    # 自动填充slug字段
    prepopulated_fields = {'slug': ('title',)}
    # 改为搜索控件
    raw_id_fields = ('author',)
    # 添加时间快速导航栏
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


class CommentAdmin(admin.ModelAdmin):
    """Customized Comment Admin Page."""

    list_display = ('name', 'email', 'post', 'created', 'updated', 'active')
    list_filter = ('created', 'updated', 'active')
    search_fields = ('name', 'email', 'body')


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
