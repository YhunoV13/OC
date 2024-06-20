from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Updated from url to path
    path('create', views.create, name='create'),  # Updated from url to path
    re_path(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),  # Updated from url to re_path
    re_path(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),  # Updated from url to re_path
    re_path(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),  # Updated from url to re_path
]
