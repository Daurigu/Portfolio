from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login, logout

from authentication.serializer import AuthenticationSerializer

# Create your views here.

class LoginView(APIView):
    def post(self, request, format=None):
        if request.user.is_authenticated:
            return Response({'You are already logged in! If you want to log out go to the logout section'})
        else:
            serializer = AuthenticationSerializer(data = request.data)

            if serializer.is_valid():
                username = serializer.data.get('username')
                password = serializer.data.get('password')

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return Response({'Wellcome ' + str(username)})
                else:
                    return Response({'Error!'})
                    ret

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            

class LogoutView(APIView):
    def get(self, request, format=None):
        if request.user.is_authenticated:
            logout(request)
        return Response({'See you latter buddy!'})