from django.contrib import admin

from task1.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass