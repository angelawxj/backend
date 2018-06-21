from django.urls import path

from . import  views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post', views.PostViewSet, base_name='posts')
router.register(r'star', views.StarViewSet, base_name='stars')
urlpatterns = router.urls
