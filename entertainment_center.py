import fresh_tomatoes
import media
import http.client
import json


# Info for API requests
conn = http.client.HTTPSConnection("api.themoviedb.org")
payload = "{}"
api_key = ""


# Get youtube trailer url of a movie with its id
def get_trailer_link(movie_id):
    conn.request(
        "GET",
        f"/3/movie/{movie_id}/videos?language=en-US&api_key={api_key}",
        payload
    )
    res = conn.getresponse()
    data = res.read()
    data_json = json.loads(data.decode("utf-8"))

    key = data_json["results"][0]["key"]
    youtube_url = "https://www.youtube.com/watch?v="+key
    return youtube_url


# Get movies from a list & Create movie instaces with their info
def get_movies_list(list_id):
    conn.request(
        "GET",
        f"/3/list/{list_id}?api_key={api_key}&language=en-US",
        payload
    )
    res = conn.getresponse()
    data = res.read()
    data_json = json.loads(data.decode("utf-8"))
    movies_list = data_json["items"]

    for i in movies_list:
        # Get required info for Movie class
        title = i["title"]
        storyline = i["overview"]
        tmdb_poster_link = "https://image.tmdb.org/t/p/w600_and_h900_bestv2"
        poster_image_url = tmdb_poster_link + i['poster_path']
        youtube_url = get_trailer_link(i["id"])

        # Create new movie instance and add it to my_list
        movie = media.Movie(title, storyline, poster_image_url, youtube_url, rating, year)
        my_list.append(movie)

# List to store movie instances
my_list = []

# Run the get_movies_list method with given list_id
list_id = 79011
get_movies_list(list_id)

# Generate Fresh Tomatoes page
fresh_tomatoes.open_movies_page(my_list)
