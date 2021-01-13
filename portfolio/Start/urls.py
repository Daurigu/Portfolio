from django.contrib import admin
from django.urls import path

from Start.views import StartView, EditStartView

urlpatterns = [
    path('', StartView.as_view()),
    path('<int:pk>', EditStartView.as_view()),
]