from django.urls import path

from . import views

urlpatterns = [
    path('kayit', views.kayit, name='kayit'),
    path('oturum', views.oturum, name='oturum'),
    path('ayrilma', views.ayrilma, name='ayrilma'),
    path('panel', views.panel, name='panel')
]