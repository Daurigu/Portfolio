from django.contrib import admin
from django.urls import path

from Start.views import StartView

urlpatterns = [
    path('', StartView.as_view()),
]