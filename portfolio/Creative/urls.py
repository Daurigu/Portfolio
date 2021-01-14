from django.contrib import admin
from django.urls import path

from Creative.views import CreativeView, CreativeSectionView, EditCreativeView, EditCreativeSectionView, AddCreativeSectionView, AddCreativeView

urlpatterns = [
    path('section', CreativeSectionView.as_view()),
    path('card', CreativeView.as_view()),
    path('section/add', AddCreativeSectionView.as_view()),
    path('card/add', AddCreativeView.as_view()),
    path('section/<int:pk>', EditCreativeSectionView.as_view()),
    path('card/<int:pk>', EditCreativeView.as_view()),
]
