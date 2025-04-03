from django.contrib import admin
from home.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'register_time')


admin.site.register(User, UserAdmin)
