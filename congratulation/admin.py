from django.contrib import admin
from .models import Song, Order


class SongAdmin(admin.ModelAdmin):
    list_display = ('author', 'title')
    list_display_links = ('author', 'title')
    search_fields = ('author', 'title')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('song', 'congratulation')
    list_display_links = ('congratulation',)


admin.site.register(Song, SongAdmin)
admin.site.register(Order, OrderAdmin)
