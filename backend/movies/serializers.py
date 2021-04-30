from rest_framework.serializers import ModelSerializer

from .models import Movies


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movies
        fields = ['id', 'name', 'director', 'genere', 'rating', 'release_date']

        #id name director genere rating release date
