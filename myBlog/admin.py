from django.contrib import admin
from django.db import models
from mdeditor.widgets import MDEditorWidget

# Register your models here.
from .models import Category,Tag,Tui,Banner,Article,Link

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 文章列表里显示想要显示的字段
    list_display = ('id', 'category', 'title', 'tui', 'user', 'views', 'create_time')
    # 文章列表里显示想要显示的字段
    list_per_page = 50

    #后台数据列表排序方式
    ordering = ('-create_time',)

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'title')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','index')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','linkurl')

