from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SearchForm
import requests
import environ
env = environ.Env()
environ.Env.read_env()


# Create your views here.
def movie_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            url = '/results/?query=' + request.POST['query']
            return HttpResponseRedirect(url)
    else:
        form = SearchForm()

    return render(request, 'movies/search.html', {'form': form})


def search_results(request):
    if request.method == 'GET':
        query = request.GET.get('query')
    r = requests.get('https://api.themoviedb.org/3/search/multi?api_key=' + env('TMDB_API_KEY') + '&page=1&query=' + query)
    print(env('TMDB_API_KEY'))
    data = r.json()
    titles = []
    for key in data['results']:
        try:
            titles.append(key['title'])
        except:
            titles.append('No title')

    return render(request, 'movies/results.html', {'titles': titles})
