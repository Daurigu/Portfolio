from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Start.models import StartModel
from Start.serializer import StartSerializer
# Create your views here.

class StartView(APIView):
    def get(self, request, format=None):
        data = StartModel.objects.all()
        serializer = StartSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.user.is_authenticated():
            serializer = StartSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        context = {'You cant do that action my friend! '}
        return Response(context, status=status.HTTP_404_NOT_FOUND)