from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    path('signup/', views.signupview, name='signup'),
    path('login/', views.loginview, name='login')
]
