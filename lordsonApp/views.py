from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from django.http import HttpResponse
from .models import Banner, Product
from .serializers import BannerSerializer, ProductSerializer


def home(request):
    return HttpResponse("<h1>✅ Lordson Backend Running Successfully</h1>")

# 🖼️ Banner Viewset
class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all().order_by('-created_at')
    serializer_class = BannerSerializer




# 👕 Product Viewset
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.order_by('-created_at')
    serializer_class = ProductSerializer

    # 🔹 Get all T-Shirts
    @action(detail=False, methods=['get'], url_path='tshirts')
    def get_tshirts(self, request):
        products = Product.objects.filter(category__iexact='tshirt').order_by('-created_at')
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

    # 🔹 Get all Sweatshirts
    @action(detail=False, methods=['get'], url_path='sweatshirts')
    def get_sweatshirts(self, request):
        products = Product.objects.filter(category__iexact='sweatshirt').order_by('-created_at')
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
