from django.urls import path
from BlogApp.views import index

urlpatterns = [
    path("", index),
    ]