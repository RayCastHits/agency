from django.contrib import admin

from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish')


admin.site.register(News, NewsAdmin)