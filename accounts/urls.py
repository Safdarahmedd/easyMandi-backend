from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'bidder', views.BidderView)


urlpatterns = [
    path('signup/', views.signupview, name='signup'),
    path('login/', views.loginview, name='login'),
    path('', include(router.urls))
]
