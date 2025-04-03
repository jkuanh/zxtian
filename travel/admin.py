from django.contrib import admin
from .models import Travel


class TravelAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'views', 'publish_time')


admin.site.register(Travel, TravelAdmin)
