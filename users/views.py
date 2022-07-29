from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.views import APIView, Response, status

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from .permissions import IsUserOwner
from .models import User
from .serializers import UserSerializer, UserLoginSerializer


class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetriveUpdateDestroyUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsUserOwner]


class LoginUserView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(username=email, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({"token": token.key, "user_id": user.id})

        return Response(
            {"message": "Invalid credentials"}, status.HTTP_401_UNAUTHORIZED
        )


class SendMailView(APIView):
    def post(self, request):

        html_content = render_to_string(
            "email.html",
            {
                "nome": request.data["name"],
                "message": request.data["message"],
                "from_email": request.data["from_email"],
            },
        )

        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            request.data["subject"],
            text_content,
            settings.EMAIL_HOST_USER,
            [request.data["to_email"]],
            reply_to=[request.data["from_email"]],
        )

        email.attach_alternative(html_content, "text/html")

        email.send()

        return Response(
            {"message": "Email successfully sent"}, status.HTTP_202_ACCEPTED
        )
