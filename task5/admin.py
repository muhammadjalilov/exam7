from django.contrib import admin

from task5.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass