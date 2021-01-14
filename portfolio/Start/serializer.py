from rest_framework import serializers
from Start.models import StartModel


class StartSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartModel
        fields = ['name', 'description']
