from django.urls import path

from . import views

urlpatterns = [
    path("techs/", views.ListTechsView.as_view()),
    path("techs/<pk>", views.UpdateDestroyView.as_view()),
]
