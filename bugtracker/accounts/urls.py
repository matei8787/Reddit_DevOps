from django.urls import path
from .views import login_api, register_api, login_view, register_view
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("api/login/", login_api, name="login_api"),
    path("api/register/", register_api, name="register_api"),
    path("login/", login_view, name="login_view"),
    path("register/", register_view, name="register_view"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh")
]