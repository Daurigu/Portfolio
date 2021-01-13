from rest_framework import serializers

from django.contrib.auth.models import User

# Serializers
class AuthenticationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)