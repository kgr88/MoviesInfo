from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.movie_search, name='search'),
    path('results/', views.search_results, name='results')
]
