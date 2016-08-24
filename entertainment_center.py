import media
import urllib
import json
import fresh_tomatoes

# The program uses TMDb (https://www.themoviedb.org) API to get movie details
API_KEY = "a8a55ee57c405e748329fde02518db1d"	# TMDb API key
YOUTUBE_URL_HEAD = "https://www.youtube.com/watch?v="
POSTER_IMAGE_URL_HEAD = "https://image.tmdb.org/t/p/w396"

movie_id_list = ["19995", "862", "1584", "597", "673", "557", "285", "157336"]  # The movie ID in TMDb databse

movie_list = []

for movie_id in movie_id_list:
	# Fetch movie data using TMDb API
	response = urllib.urlopen(
		"https://api.themoviedb.org/3/movie/" + movie_id + "?&api_key=" + API_KEY + "&append_to_response=trailers")
	# Decode the response from TMDb API which is in JSON format
	movie_data = json.load(response)

	movie_title = movie_data["title"]
	movie_tagline = movie_data["tagline"]
	movie_story_line = movie_data["overview"].encode("utf-8")
	movie_release_date = movie_data["release_date"]
	movie_language = movie_data["spoken_languages"][0]["name"]
	movie_review = movie_data["vote_average"]
	# Create full path of poster image
	poster_image_url = POSTER_IMAGE_URL_HEAD + movie_data["poster_path"]
	# Complete YouTube url = head + YouTube ID
	trailer_youtube_url = YOUTUBE_URL_HEAD + movie_data["trailers"]["youtube"][0]["source"] 
	# Create a Movie instance and add it to the movie list
	movie = media.Movie(movie_title, movie_tagline, 
		movie_story_line, movie_release_date, 
		movie_language, movie_review,
		poster_image_url, trailer_youtube_url)	
	movie_list.append(movie)

# Open the movies webpage
fresh_tomatoes.open_movies_page(movie_list)
