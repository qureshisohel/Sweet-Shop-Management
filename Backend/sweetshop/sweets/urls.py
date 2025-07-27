from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SweetViewSet, SweetSearchView

router = DefaultRouter()
router.register(r'sweets', SweetViewSet, basename='sweet')

urlpatterns = [
    path('', include(router.urls)),
    path('sweets/search/', SweetSearchView.as_view(), name='sweet-search'),
]
