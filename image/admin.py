from django.contrib import admin
from image.models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'views', 'publish_time')


admin.site.register(Image, ImageAdmin)
