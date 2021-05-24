from django.urls import path

from . import views

urlpatterns = [
    path('iletisim', views.iletisim, name='iletisim')
]