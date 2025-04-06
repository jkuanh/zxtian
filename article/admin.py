from django.contrib import admin
from article.models import Article, Image, Travel, Video, User


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'views', "publish_time")


admin.site.register(Article, ArticleAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'views', 'publish_time')


admin.site.register(Image, ImageAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'register_time')


admin.site.register(User, UserAdmin)


class TravelAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'views', 'publish_time')


admin.site.register(Travel, TravelAdmin)


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'video_file', 'uploaded_at')


admin.site.register(Video, VideoAdmin)


# 全局
admin.site.site_header = '平台管理'
admin.site.site_title = '个人博客后台管理'
