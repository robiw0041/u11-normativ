from django.urls import path
from .views import register_view, login_view, logout_view, forgot_password, restore_password

# app_name = "accounts"

urlpatterns = [
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path('login/', login_view, name='login'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('restore-password/', restore_password, name='restore_password'),
]