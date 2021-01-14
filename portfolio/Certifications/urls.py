from django.urls import path

from Certifications.views import CertificationView, EditCertificationView, AddCertificationView

urlpatterns = [
    path('card', CertificationView.as_view()),
    path('card/add', AddCertificationView.as_view()),
    path('card/<int:pk>', EditCertificationView.as_view()),
]