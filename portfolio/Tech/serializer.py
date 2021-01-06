from rest_framework import serializers
from Tech.models import TechModel, TechSectionModel


class TechSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechSectionModel
        fields = ['id', 'section', 'description']

class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechModel
        fields = ['section', 'name', 'description', 'image', 'link']