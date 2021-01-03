from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Tech.models import TechModel, TechSectionModel
from Tech.serializer import TechSerializer, TechSectionSerializer
# Create your views here.

class TechView(APIView):
    def get(self, request, format=None):
        data = TechModel.objects.all()
        serializer = TechSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.user.is_authenticated:
            serializer = TechSectionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'You are not allowed to proceed with that action!'})

class TechSectionView(APIView):
    def get(self, request, format=None):
        data = TechSectionModel.objects.all()
        serializer = TechSectionSerializer(data, many = True)
        return Response(serializer.data)