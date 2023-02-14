import requests

r = requests.get('https://www.filmweb.pl/api/v1/film/526137/rating')
print(r.text)