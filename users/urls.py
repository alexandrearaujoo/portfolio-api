from django.urls import path

from . import views

urlpatterns = [
    path('users/register/', views.CreateUserView.as_view()),
    path('users/login/', views.LoginUserView.as_view()),
    path('users/', views.ListUsersView.as_view())
]