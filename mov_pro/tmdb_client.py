import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MDZiZDM0NmFhZDVjYjFhZWU0YjI0MTM4MmE5M2M4NSIsIm5iZiI6MTc2MTY1NTQ3Mi4xMTEsInN1YiI6IjY5MDBiYWIwNzMyZDRmZjdmYmEzMTcyMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Ow43tXNQqezdiMo-W-qc3nYCqKJQHhqRdnUEmFISLgc'
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size = 'w342'):
    base_url = "https://image.tmdb.org/t/p/"
    return f'{base_url}{size}/{poster_api_path}'

'''def get_movie(how_many, list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    api_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MDZiZDM0NmFhZDVjYjFhZWU0YjI0MTM4MmE5M2M4NSIsIm5iZiI6MTc2MTY1NTQ3Mi4xMTEsInN1YiI6IjY5MDBiYWIwNzMyZDRmZjdmYmEzMTcyMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Ow43tXNQqezdiMo-W-qc3nYCqKJQHhqRdnUEmFISLgc'
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data["results"][:how_many]'''

def get_movie(how_many, list_type):
    api_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MDZiZDM0NmFhZDVjYjFhZWU0YjI0MTM4MmE5M2M4NSIsIm5iZiI6MTc2MTY1NTQ3Mi4xMTEsInN1YiI6IjY5MDBiYWIwNzMyZDRmZjdmYmEzMTcyMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Ow43tXNQqezdiMo-W-qc3nYCqKJQHhqRdnUEmFISLgc'
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "accept": "application/json"
    }
    print("🔗 endpoint:", endpoint)
    response = requests.get(endpoint, headers=headers)
    print("status:", response.status_code)
    data = response.json()
    print("results:", len(data.get("results", [])))
    return data["results"][:how_many]


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    api_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MDZiZDM0NmFhZDVjYjFhZWU0YjI0MTM4MmE5M2M4NSIsIm5iZiI6MTc2MTY1NTQ3Mi4xMTEsInN1YiI6IjY5MDBiYWIwNzMyZDRmZjdmYmEzMTcyMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Ow43tXNQqezdiMo-W-qc3nYCqKJQHhqRdnUEmFISLgc'
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    api_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MDZiZDM0NmFhZDVjYjFhZWU0YjI0MTM4MmE5M2M4NSIsIm5iZiI6MTc2MTY1NTQ3Mi4xMTEsInN1YiI6IjY5MDBiYWIwNzMyZDRmZjdmYmEzMTcyMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Ow43tXNQqezdiMo-W-qc3nYCqKJQHhqRdnUEmFISLgc'
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()['cast']

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    api_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MDZiZDM0NmFhZDVjYjFhZWU0YjI0MTM4MmE5M2M4NSIsIm5iZiI6MTc2MTY1NTQ3Mi4xMTEsInN1YiI6IjY5MDBiYWIwNzMyZDRmZjdmYmEzMTcyMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Ow43tXNQqezdiMo-W-qc3nYCqKJQHhqRdnUEmFISLgc'
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()