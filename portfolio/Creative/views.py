from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Creative.serializer import CreativeSectionSerializer, CreativeSerializer
from Creative.models import CreativeModel, CreativeSectionModel

# Create your views here.
class CreativeSectionView(APIView):
    def get (self, request, format=None):
        data = CreativeSectionModel.objects.all()
        serializer = CreativeSectionSerializer(data, many=True)
        return Response(serializer.data)


    def post (self, request, format=None):

        if request.user.is_authenticated:
            serializer = CreativeSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        content = {'please login': 'nothing to see here'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)

class EditCreativeSectionView(APIView):
    def put(self, request, pk, format=None):
        if request.user.is_authenticated:
            obj = CreativeSectionModel.objects.get(id = pk)
            serializer = CreativeSectionSerializer(obj, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'You are not allowed to proceed with that action!'})

class CreativeView(APIView):
    def get(self, request, format=None):
        data = CreativeModel.objects.all()
        serializer = CreativeSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, format=None):
        if request.user.is_authenticated:
            serializer = CreativeSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({'Success'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'You are not allowed to proceed with this action!'}, status=status.HTTP_404_NOT_FOUND)

class EditCreativeView(APIView):
    def put(self, request, pk, format=None):
        if request.user.is_authenticated:
            obj = CreativeModel.objects.get(id = pk)
            serializer = CreativeSerializer(obj, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'You are not allowed to proceed with that action!'})