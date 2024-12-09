from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.registeruser, name='user_register'),
    path('login/', views.LoginUser, name='user_login'),  # This line points to your custom login view
    path('complete-profile/', views.complete_profile, name='complete_profile'),
    path('logout/', views.logoutuser, name='user_logout'),
    path('profile/<str:username>/' , views.profile_view , name='dashboard')
    ]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
