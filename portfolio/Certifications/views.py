from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from Certifications.models import CertificationModel
from Certifications.serializer import CertificationSerializer

# Create your views here.

class CertificationView(APIView):
    def get(self, request, format=None):
        data = CertificationModel.objects.all()
        serializer = CertificationSerializer(data, many=True)
        return Response(serializer.data, status = status.HTTP_201_CREATED)