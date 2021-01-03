from django.contrib import admin
from django.urls import path

from Certifications.views import CertificationView

urlpatterns = [
    path('card/', CertificationView.as_view()),
]