from niomic.views import datamanipulation
from django.urls import path
from . import views

urlpatterns = [
    path('', views.datamanipulation, name='datamanipulation')
]