from django.contrib import admin
from django.urls import path
from .views import home, new_search

urlpatterns = [
    path('', home, name="Home"),
    path('new_search', new_search, name="new_search")
]
