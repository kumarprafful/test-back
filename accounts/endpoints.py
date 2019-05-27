from django.urls import path, include
from accounts.viewset import *
from knox import views as knox_views


urlpatterns = [
    path('register/', UserRegisterViewset.as_view(), name="register"),
    path('login/', LoginAPI.as_view(), name="login"),
    path('user/', UserAPI.as_view(), name="user"),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
]
