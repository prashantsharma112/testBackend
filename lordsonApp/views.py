from rest_framework import viewsets, status
from django.http import HttpResponse
from .models import Banner
from .serializers import BannerSerializer
def home(request):
    return HttpResponse("<h1>✅ Lordson Backend Running Successfully</h1>")

# 🖼️ Banner Viewset
class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all().order_by('-created_at')
    serializer_class = BannerSerializer
