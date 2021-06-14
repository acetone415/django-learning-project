from django import forms
from django.conf import settings
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
import re
from .models import Song, Order


class TracklistImportForm(forms.Form):
    tracklist_upload = forms.FileField()


class SongAdmin(admin.ModelAdmin):
    list_display = ('author', 'title')
    list_display_links = ('author', 'title')
    search_fields = ('author', 'title')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-tracklist/', self.upload_tracklist), ]
        return new_urls + urls

    def upload_tracklist(self, request):

        if request.method == "POST":
            tracklist_file = request.FILES["tracklist_upload"]
            file_data = tracklist_file.read().decode('utf-8-sig')
            with open(settings.MEDIA_ROOT / 'tracklist.txt', 'w') as f:
                f.write(file_data)
            file_data = file_data.splitlines()

            sep = ' - '

            Song.objects.all().delete()
            for line in file_data:
                line = re.sub(r'\d+\. ', '', line)
                author_song = line.rstrip().split(sep=sep)
                # read pair "author - song title"  and write to tuple (author, song)
                Song.objects.update_or_create(
                    author=author_song[0],
                    title=author_song[1]
                )

        form = TracklistImportForm()
        data = {'form': form}

        return render(request, "admin/upload_tracklist.html", data)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('song', 'congratulation', 'published')
    list_display_links = ('congratulation',)


admin.site.register(Song, SongAdmin)
admin.site.register(Order, OrderAdmin)
