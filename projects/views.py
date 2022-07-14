from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import FormParser, MultiPartParser

from .models import Project
from .serializers import ProjectSerializer


class ListCreateProjectView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [TokenAuthentication]
    parser_classes = [FormParser, MultiPartParser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RetriveUpdateDestroyProjectView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
