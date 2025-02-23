from django.urls import path
from .views import extract_number, get_missing_numbers

urlpatterns = [
    path("extract/", extract_number, name="extract_number"),
    path('missing_number/', get_missing_numbers, name='missing_number'),
]