from django.urls import path, include
from . import views

app_name = 'analysis'
urlpatterns = [
    path('', views.index),
    path('submit_files', views.submit_files, name='submit_files'),
]
