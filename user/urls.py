from django.conf.urls import url
from . import views

urlpatterns = [
    url('register', views.RegistrationView.as_view()),
    url('login', views.LoginView.as_view()),
    url('logout', views.LogoutView.as_view())
]