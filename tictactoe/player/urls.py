from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView

from .views import home

urlpatterns = [
    re_path(r'home$', home, name="player_home"),
    re_path(r'login$',
            LoginView.as_view(template_name="player/login_form.html"),
            name="player_login"),
    re_path(r'logout$',
            LogoutView.as_view(),
            name="player_logout")

]