from django.urls import path
from .views import register_view, login_view, logout_view

# app_name = "accounts"

urlpatterns = [
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path('login/', login_view, name='login'),
]