from rest_framework import serializers

from Certifications.models import CertificationModel

# Serializers
class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationModel
        fields = ['name', 'description', 'image', 'section', 'link']