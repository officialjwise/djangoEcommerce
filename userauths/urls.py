from django.urls import path
from userauths import views

app_name = "userauths"

urlpatterns = [
    path("register/", views.RegisterView, name="register"),
    path("login/", views.loginView, name="login"),
    path("logout/", views.logoutView, name="logout"),

]
