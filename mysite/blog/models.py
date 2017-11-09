# -*- coding: utf-8 -*-
"""Import Public modules Here."""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    """Model Post."""

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    # 字段属性添加 primary_key=True 设置为主键，默认自动创建自增id为主键
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
            max_length=10,
            choices=STATUS_CHOICES,
            default='draft')

    class Meta:
        """Meta For Post."""

        # 默认表名为 应用名前缀_模型名 小写, 如 blog_post
        # db_table = 'xxxxx' # 指定表名
        # ordering 参数必须是一个元组或列表，‘,’ 不能省！
        ordering = ('-publish',)

    def __str__(self):
        """Post Object str."""
        return self.title
