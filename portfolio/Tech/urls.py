from django.contrib import admin
from django.urls import path

from Tech.views import TechView, TechSectionView, EditTechView, EditTechSectionView, AddTechSectionView, AddTechView

urlpatterns = [
    path('card', TechView.as_view()),
    path('section', TechSectionView.as_view()),
    path('card/add', AddTechView.as_view()),
    path('section/add', AddTechSectionView.as_view()),
    path('card/<int:pk>', EditTechView.as_view()),
    path('section/<int:pk>', EditTechSectionView.as_view()),
]
