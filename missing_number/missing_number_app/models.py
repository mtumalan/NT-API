from django.db import models

class ExtractedNumber(models.Model):
    """Modelo para almacenar el número extraído"""
    number = models.IntegerField(unique=True)

    def __str__(self):
        return f"Número extraído: {self.number}"