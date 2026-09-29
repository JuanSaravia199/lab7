from django.contrib import admin
from .models import Anime

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ("titulo", "episodios", "visto", "agregado_en") # columnas del listado
    list_filter = ("visto",) # filtro lateral
    search_fields = ("titulo",) # barra de búsqueda