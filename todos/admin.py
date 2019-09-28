from django.contrib import admin

from .models import Todo, Tag


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'creator')
    list_filter = ('status',)
    search_fields = ('title', 'content', 'creator__username')


# Register your models here.
# 把資料表註冊到 admin
admin.site.register(Todo, TodoAdmin)
admin.site.register(Tag)
