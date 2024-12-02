from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.registeruser, name='user_register'),
    path('login/', views.LoginUser.as_view(), name='user_login'),  # This line points to your custom login view
    path('complete-profile/', views.complete_profile, name='complete_profile'),
]