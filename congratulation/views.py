from django.views.generic import CreateView
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy

from .forms import OrderForm
from .models import Song


def index(request):
    return render(request, 'index.html')


def show_tracklist(request):
    template = loader.get_template('tracklist.html')
    songs = Song.objects.order_by('author')
    context = {'songs': songs}
    return HttpResponse(template.render(context, request))


class OrderCreateView(CreateView):
    template_name = 'order.html'
    form_class = OrderForm
    success_url = reverse_lazy('index')
