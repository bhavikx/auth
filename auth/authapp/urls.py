from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name="home"),
    path('signup/', signupView, name="signup"),
    path('signin/', signinView, name="signin"),
    path('signout/', signoutView, name="signout"),
]