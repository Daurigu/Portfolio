from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from Start.models import StartModel
from Start.serializer import StartSerializer

class StartView(APIView):
    def get(self, request, format=None):
        data = StartModel.objects.all()
        serializer = StartSerializer(data, many=True)
        return Response(serializer.data)

class AddStartview(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = StartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditStartView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk, format=None):
        obj = StartModel.objects.get(id = pk)
        serializer = StartSerializer(obj, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
