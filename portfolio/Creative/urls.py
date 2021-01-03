from django.contrib import admin
from django.urls import path

from Creative.views import CreativeView, CreativeSectionView

urlpatterns = [
    path('section/', CreativeSectionView.as_view()),
    path('card/', CreativeView.as_view()),
]
