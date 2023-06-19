from django.urls import path

from movies.views import *

urlpatterns = [
    path('movies/', MovieView.as_view()),
    path('movies/<int:movie_id>/', MovieDetailView.as_view()),
]