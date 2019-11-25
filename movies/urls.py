from django.urls import path

from movies.views import MoviesListView

app_name = 'movies'

urlpatterns = [
    path('', MoviesListView.as_view(), name='movies-list'),
]
