import re
from typing import List, Tuple

from django import forms
from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import path, reverse_lazy

from .models import Order, Song

TRACKLIST_FILENAME = settings.MEDIA_ROOT / 'tracklist.txt'


class TracklistImportForm(forms.Form):
    tracklist_upload = forms.FileField()


class SongAdmin(admin.ModelAdmin):
    list_display = ('author', 'title')
    list_display_links = ('author', 'title')
    search_fields = ('author', 'title')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path('upload-tracklist/', self.upload_tracklist,
                 name='upload_tracklist'),
            path('update-tracklist/', SongAdmin.update_tracklist,
                 name='update_tracklist'),
        ]
        return new_urls + urls

    @staticmethod
    def tracklist_parser(filename: str) -> List[Tuple[str, str]]:
        """Load new tracklist from file to DB.

        :param filename: Tracklist filename
        """
        sep, tracklist = ' - ', []
        with open(filename) as file:
            for line in file:
                line = re.sub(r'\d+\. ', '', line)
                author_song = line.rstrip().split(sep=sep)
                # read pair "author - song title"  and write to tuple (author, song)
                tracklist.append(author_song)
        return tracklist

    @staticmethod
    def update_tracklist(*args):
        tracklist = SongAdmin.tracklist_parser(TRACKLIST_FILENAME)
        Song.objects.all().delete()
        for pair in tracklist:
            Song.objects.update_or_create(author=pair[0], title=pair[1])
        if args:
            return redirect(reverse_lazy('admin:congratulation_song_changelist'))

    def upload_tracklist(self, request):
        """Upload trcklist file to admin panel"""

        if request.method == "POST":
            tracklist_file = request.FILES["tracklist_upload"]
            file_data = tracklist_file.read().decode('utf-8-sig')
            with open(TRACKLIST_FILENAME, 'w') as f:
                f.write(file_data)
            SongAdmin.update_tracklist()

        form = TracklistImportForm()
        data = {'form': form}

        return render(request, "admin/upload_tracklist.html", data)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('song', 'congratulation', 'published')
    list_display_links = ('congratulation',)


admin.site.register(Song, SongAdmin)
admin.site.register(Order, OrderAdmin)
