from rest_framework import serializers

from Creative.models import CreativeModel, CreativeSectionModel

# Serializers
class CreativeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreativeSectionModel
        fields = ['section', 'description']

class CreativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreativeModel
        fields = ['section', 'name', 'description', 'image', 'link']