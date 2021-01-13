from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from Certifications.models import CertificationModel
from Certifications.serializer import CertificationSerializer

# Create your views here.

class CertificationView(APIView):
    def get(self, request, format=None):
        obj = CertificationModel.objects.all()
        serializer = CertificationSerializer(obj, many=True)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    def post(self, request, format=None):
        if request.user.is_authenticated:
            serializer = CertificationSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'You are not allowed to proceed with this action!'})

class EditCertificationView(APIView):
    def put(self, request, pk, format=None):
        if request.user.is_authenticated:
            obj = CertificationModel.objects.get(id = pk)
            serializer = CertificationSerializer(obj, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'You are not allowed to proceed with this action!'})