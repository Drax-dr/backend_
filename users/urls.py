# from django import views
from django.contrib import admin
from django.urls import include, path
from .api import api
from .views import UserDasboardView,LecturerDashboardView, HomeView, RegisterView, StudentRegisterView
from users import views

urlpatterns = [
    path('login/', view=views.login_student, name="login"),
    path("", view=HomeView.as_view(), name="index"),
    path("register.html/", view=RegisterView.as_view(), name="register"),
    path("register/student/", view=StudentRegisterView.as_view(), name="register"),
    path('dashboard/student/', UserDasboardView.as_view(), name='user_dashboard'),
    path('dashboard/lecturer/', LecturerDashboardView.as_view(), name='lecturer_dashboard'),
]
