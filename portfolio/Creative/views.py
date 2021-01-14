from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from Creative.serializer import CreativeSectionSerializer, CreativeSerializer
from Creative.models import CreativeModel, CreativeSectionModel

# ----- SECTIONS
class CreativeSectionView(APIView):
    def get (self, request, format=None):
        data = CreativeSectionModel.objects.all()
        serializer = CreativeSectionSerializer(data, many=True)

        return Response(serializer.data)

class AddCreativeSectionView(APIView):
    permission_classes = (IsAuthenticated,)

    def post (self, request, format=None):
        serializer = CreativeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditCreativeSectionView(APIView):
    permission_classes = (IsAuthenticated,)
    def put(self, request, pk, format=None):
        obj = CreativeSectionModel.objects.get(id = pk)
        serializer = CreativeSectionSerializer(obj, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ----- CARDS
class CreativeView(APIView):
    def get(self, request, format=None):
        data = CreativeModel.objects.all()
        serializer = CreativeSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AddCreativeView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, format=None):
        serializer = CreativeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'Success'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditCreativeView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk, format=None):
        obj = CreativeModel.objects.get(id = pk)
        serializer = CreativeSerializer(obj, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)