from django.db import models

class FormField(models.Model):
    FIELD_TYPES = [
        ('char', 'Pole tekstowe'),
        ('email', 'Pole email'),
        ('phone', 'Pole telefoniczne'),
        ('textarea', 'Pole tekstowe (wielowierszowe)'),
        ('checkbox', 'Pole wyboru'),
    ]

    label = models.CharField(max_length=100, verbose_name="Etykieta")
    field_type = models.CharField(max_length=20, choices=FIELD_TYPES, verbose_name="Typ pola")
    required = models.BooleanField(default=True, verbose_name="Wymagane")
    order = models.PositiveIntegerField(default=0, verbose_name="Kolejność")

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "Pole formularza"
        verbose_name_plural = "Pola formularza"
        ordering = ['order']