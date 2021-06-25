from django.urls import path

from . import views

urlpatterns = [
    path('tracklist/', views.show_tracklist, name='tracklist'),
    path('order/', views.OrderCreateView.as_view(), name='order')
]
