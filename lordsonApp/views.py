from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>✅ Lordson Backend Running Successfully</h1>")
