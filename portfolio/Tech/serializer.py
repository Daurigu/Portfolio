from rest_framework import serializers
from Tech.models import TechModel, TechSectionModel


class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechModel
        fields = ['id', 'section', 'description']

class TechSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechSectionModel
        fields = ['id', 'section', 'name', 'description', 'image']