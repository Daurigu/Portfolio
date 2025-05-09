"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import TemplateView

import Start
import Tech
import Creative
import Certifications
import authentication

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='index.html')),
    path('<path>',TemplateView.as_view(template_name='index.html')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/start/', include('Start.urls')),
    path('api/tech/', include('Tech.urls')),
    path('api/creative/', include('Creative.urls')),
    path('api/certification/', include('Certifications.urls')),
    path('api/', include('authentication.urls')),
]
