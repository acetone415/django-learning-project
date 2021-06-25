from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tracklist/', views.show_tracklist, name='tracklist'),
    path('order/', views.make_order, name='order')
]
