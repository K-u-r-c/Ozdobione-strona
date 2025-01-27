from django.db import models
from django.core.exceptions import ValidationError

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nazwa tagu")
    order = models.PositiveIntegerField(default=0, verbose_name="Kolejność")

    def delete(self, *args, **kwargs):
        if self.name in ['Wesele', 'Urodziny', 'Chrzciny']:
            raise ValidationError(f"Tag '{self.name}' nie może być usunięty.")
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tagi"
        ordering = ['order']

class Photo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Tytuł zdjęcia")
    image = models.ImageField(upload_to='photos/', verbose_name="Zdjęcie")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data dodania")
    tags = models.ManyToManyField(Tag, related_name='photos', blank=True, verbose_name="Tagi")

    def clean(self):
        super().clean()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Zdjęcie"
        verbose_name_plural = "Zdjęcia"
        
class FAQ(models.Model):
    question = models.CharField(max_length=255, verbose_name="Pytanie")
    answer = models.TextField(verbose_name="Odpowiedź")
    order = models.PositiveIntegerField(default=0, verbose_name="Kolejność")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"
        ordering = ['order']