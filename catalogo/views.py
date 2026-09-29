from django.http import JsonResponse
from .models import Anime

def anime_list(request):
    """Devuelve en JSON la lista de animes."""
    # Obtenemos los campos clave del modelo
    animes = list(
        Anime.objects.values(
            "id", "titulo", "sinopsis", "episodios", "visto", "agregado_en"
        )
    )
    # Formateamos agregado_en a texto para serializarlo sin problemas
    for item in animes:
        if item["agregado_en"]:
            item["agregado_en"] = item["agregado_en"].strftime("%Y-%m-%d %H:%M")

    return JsonResponse({"count": len(animes), "results": animes})
