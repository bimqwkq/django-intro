from django.urls import path
from .views import MovieListview, MovieDetailView

urlpatterns = [
    path('movies/', MovieListview.as_view(), name='article-list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='article-detail'),
]

