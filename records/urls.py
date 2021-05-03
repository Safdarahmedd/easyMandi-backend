from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'history', views.RecordView)
router.register(r'livebid', views.LiveView)

urlpatterns = [
    path('', include(router.urls))
]
