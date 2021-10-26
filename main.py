import requests

api_key = '63af583a5faa849605808d646621afee'
url = 'https://api.themoviedb.org/3/search/movie'
parms = {
    "api_key": api_key,
    "query": 'ironman',
}


print("23123123")
response = requests.get(url, params=parms)
print(response.json())