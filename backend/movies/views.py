
from .models import Movies
from rest_framework.viewsets import ModelViewSet
from .serializers import MovieSerializer



class MoviesViewSet(ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


