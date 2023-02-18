import requests

r = requests.get('https://api.themoviedb.org/3/search/multi?api_key=255f452494d013b6040ecabbb9bf1c08&query=dupa')
data = r.json()

counter = 0
results = []
for key in data['results']:
    if counter==5:
        break
    result = {}
    #print (key['media_type'],end='  ')
    result['type'] = key['media_type']
    if key['media_type'] == 'movie':
        #print(key['title'],end='  ')
        result['name'] = key['title']
    else:
        #print(key['name'],end='  ')
        result['name'] = key['name']
    if key['media_type'] == 'person':
        #print(key['profile_path'],end='  ')
        result['poster_url'] = 'https://image.tmdb.org/t/p/w300'+ key['profile_path']
    else:
        #print(key['poster_path'], end='  ')
        result['poster_url'] = 'https://image.tmdb.org/t/p/w300' + key['poster_path']
    #print("")
    results.append(result)
    counter+=1
print(results)



