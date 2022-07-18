from django.http import HttpResponse
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.views import APIView, Response, status

from django.core.mail import send_mail

from .models import User
from .serializers import UserSerializer, UserLoginSerializer


class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetriveUpdateDestroyUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginUserView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(username=email, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({"token": token.key})

        return Response(
            {"message": "Invalid credentials"}, status.HTTP_401_UNAUTHORIZED
        )

class SendMailView(APIView):
    def post(self,request):

        send_mail(
            subject=request.data['subject'],
            message=request.data['message'],
            from_email='manager.portfolio.api@gmail.com',
            recipient_list=[request.data['for_the']],
            fail_silently=False,        
        )

        return HttpResponse("email enviado")