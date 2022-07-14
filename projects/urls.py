from django.urls import path

from . import views

urlpatterns = [
    path("projects/", views.ListCreateProjectView.as_view()),
    path("projects/<pk>", views.RetriveUpdateDestroyProjectView.as_view()),
]
