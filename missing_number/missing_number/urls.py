from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path

def root_view(request):
    return JsonResponse({"message": "API is running"}, status=200)

urlpatterns = [
    path("", root_view),
    path('admin/', admin.site.urls),
    path('api/', include('missing_number_app.urls')),
]
