from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Tytuł zdjęcia")
    image = models.ImageField(upload_to='photos/', verbose_name="Zdjęcie")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data dodania")

    def __str__(self):
        return self.title
      
    class Meta:
        verbose_name = "Zdjęcie"
        verbose_name_plural = "Zdjęcia"

class Video(models.Model):
    title = models.CharField(max_length=100, verbose_name="Tytuł filmu")
    video_url = models.URLField(verbose_name="URL filmu", blank=True, null=True)
    embed_code = models.TextField(verbose_name="Kod osadzenia", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data dodania")

    def __str__(self):
        return self.title
      
    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Filmy"