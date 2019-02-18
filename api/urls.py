from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('stocks/<str:ticker>', views.stocks, name="stocks")
]
