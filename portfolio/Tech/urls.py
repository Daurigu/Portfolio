from django.contrib import admin
from django.urls import path

from Tech.views import TechView, TechSectionView

urlpatterns = [
    path('card/', TechView.as_view()),
    path('section/', TechSectionView.as_view()),
]
