from rest_framework import serializers
from .models import Anime

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['id', 'titulo', 'sinopsis', 'episodios', 'visto', 'agregado_en']
        read_only_fields = ['id', 'agregado_en']

    # Validación a nivel de campo: episodios positivos
    def validate_episodios(self, value):
        if value < 0:
            raise serializers.ValidationError('La cantidad de episodios no puede ser negativa.')
        return value