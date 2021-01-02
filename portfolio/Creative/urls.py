from django.contrib import admin
from django.urls import path

from Creative.views import CreativeView, CreativeSectionView

urlpatterns = [
    path('', CreativeSectionView.as_view()),
]
