from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BannerViewSet

# Create a router and register your API endpoints
router = DefaultRouter()
router.register(r'banners', BannerViewSet, basename='banner')
# router.register(r'products', ProductViewSet, basename='product')


urlpatterns = [
    path('', include(router.urls)),
]
