from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from Certifications.models import CertificationModel
from Certifications.serializer import CertificationSerializer

# ----- CARDS
class CertificationView(APIView):
    def get(self, request, format=None):
        obj = CertificationModel.objects.all()
        serializer = CertificationSerializer(obj, many=True)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
class AddCertificationView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):    
        serializer = CertificationSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditCertificationView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk, format=None):
        obj = CertificationModel.objects.get(id = pk)
        serializer = CertificationSerializer(obj, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
