from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Song


def index(request):
    return render(request, 'index.html')


def show_tracklist(request):
    template = loader.get_template('tracklist.html')
    songs = Song.objects.order_by('author')
    context = {'songs': songs}
    return HttpResponse(template.render(context, request))


def make_order(request):
    return HttpResponse('Soon you will order here)')
