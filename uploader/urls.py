from django.urls import path

from . import views

urlpatterns = [
    # /
    path('', views.index, name='index'),
    # /upload
    path('upload', views.upload, name='upload'),
]