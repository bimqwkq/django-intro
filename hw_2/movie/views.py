from rest_framework import generics 
from .models import Movie 
from .serializers import MovieSerializer

class MovieListview(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializers_class = MovieSerializer

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    