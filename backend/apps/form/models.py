from django.db import models

class FormField(models.Model):
    FIELD_TYPES = [
        ('char', 'Pole tekstowe'),
        ('email', 'Pole email'),
        ('phone', 'Pole telefoniczne'),
        ('textarea', 'Pole tekstowe (wielowierszowe)'),
        ('checkbox', 'Pole wyboru'),
        ('multiselect', 'Pole wielokrotnego wyboru'),
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

class FormFieldOption(models.Model):
    form_field = models.ForeignKey(FormField, related_name='options', on_delete=models.CASCADE)
    option_text = models.CharField(max_length=100, verbose_name="Opcja")

    def __str__(self):
        return self.option_text

    class Meta:
        verbose_name = "Opcja pola formularza"
        verbose_name_plural = "Opcje pola formularza"