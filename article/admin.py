from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'views', "publish_time")


admin.site.register(Article, ArticleAdmin)
