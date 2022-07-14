from rest_framework import generics

from .serializers import TechSerializer
from .models import Tech


class ListTechsView(generics.ListAPIView):
    queryset = Tech.objects.all()
    serializer_class = TechSerializer


class UpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tech.objects.all()
    serializer_class = TechSerializer
