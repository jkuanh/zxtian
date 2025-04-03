from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'video_file', 'uploaded_at')


admin.site.register(Video, VideoAdmin)
