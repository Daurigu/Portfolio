from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from Tech.models import TechModel, TechSectionModel
from Tech.serializer import TechSerializer, TechSectionSerializer

# ----- CARDS
class TechView(APIView):
    def get(self, request, format=None):
        data = TechModel.objects.all()
        serializer = TechSerializer(data, many=True)
        return Response(serializer.data)

class AddTechView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = TechSectionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditTechView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk, format=None):
        obj = TechModel.objects.get(id = pk)
        serializer = TechSerializer(obj, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
# ----- SECTIONS
class TechSectionView(APIView):
    def get(self, request, format=None):
        data = TechSectionModel.objects.all()
        serializer = TechSectionSerializer(data, many = True)
        return Response(serializer.data)
    
class AddTechSectionView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = TechSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditTechSectionView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def put(self, request, pk, format=None):
        obj = TechSectionModel.objects.get(id = pk)
        serializer = TechSectionSerializer(obj, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
