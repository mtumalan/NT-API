from django.http import JsonResponse
from .models import ExtractedNumber
from django.views.decorators.csrf import csrf_exempt
import json

class NaturalNumbersSet:
    """Clase que maneja el conjunto de números naturales y su extracción"""

    def extract(self, number):
        """Extrae un número del conjunto de números naturales"""
        if not (1 <= number <= 100):
            raise ValueError("Number must be between 1 and 100.")
        
        if ExtractedNumber.objects.filter(number=number).exists():
            raise ValueError("Number has already been extracted.")
        
        ExtractedNumber.objects.create(number=number)

    @staticmethod
    def get_missing_numbers():
        """Obtiene todos los números extraídos (faltantes)"""
        missing_numbers = list(ExtractedNumber.objects.values_list('number', flat=True))
        return sorted(missing_numbers)  # Sort for better readability

number_set = NaturalNumbersSet()

@csrf_exempt
def extract_number(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            number = data.get("number")

            if not isinstance(number, int) or not (1 <= number <= 100):
                return JsonResponse({"error": "Invalid number. Must be between 1 and 100."}, status=400)

            try:
                number_set.extract(number)
                return JsonResponse({"message": f"Number {number} extracted successfully."})
            except ValueError as e:
                return JsonResponse({"error": str(e)}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return JsonResponse({"error": "Only POST requests are allowed"}, status=405)

@csrf_exempt
def get_missing_numbers(request):
    """API para obtener todos los números extraídos (faltantes)"""
    missing_numbers = number_set.get_missing_numbers()
    return JsonResponse({"missing_numbers": missing_numbers}, status=200)