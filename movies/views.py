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
    counter = 0
    results = []
    for key in data['results']:
        if counter == 5:
            break
        result = {}
        result['type'] = key['media_type']
        if key['media_type'] == 'movie':
            result['name'] = key['title']
        else:
            result['name'] = key['name']
        if key['media_type'] == 'person':
            result['poster_url'] = 'https://image.tmdb.org/t/p/w300' + key['profile_path']
        else:
            result['poster_url'] = 'https://image.tmdb.org/t/p/w300' + key['poster_path']
        # print("")
        results.append(result)
        counter += 1

    return render(request, 'movies/results.html', {'results': results})
