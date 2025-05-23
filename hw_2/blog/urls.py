from django.urls import path
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('', ArticleListView.as_view(), name='movie-list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='movie-detail'),
]
