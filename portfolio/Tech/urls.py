from django.contrib import admin
from django.urls import path

from Tech.views import TechView

urlpatterns = [
    path('', TechView.as_view()),
]
