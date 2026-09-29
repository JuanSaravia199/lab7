from django.db import models

class Anime(models.Model):
    """Modelo para almacenar el historial de animes vistos."""
    titulo = models.CharField(max_length=150)
    sinopsis = models.TextField(blank=True)
    episodios = models.IntegerField(default=12)
    visto = models.BooleanField(default=False)
    agregado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["titulo"]
        verbose_name_plural = "animes"

    def __str__(self):
        return self.titulo