from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.parsers import FormParser, MultiPartParser

from .mixins import SerializerByMethodMixin
from .permissions import IsProjectOwner
from .models import Project
from .serializers import ProjectSerializer


class ListCreateProjectView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [FormParser, MultiPartParser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)


class RetriveUpdateDestroyProjectView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsProjectOwner | IsAuthenticated]
