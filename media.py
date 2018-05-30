import webbrowser


class Movie():
    """ This class provides a way to store movie related information"""
    def __init__(self, movie_title, poster_image, trailer_url, rating, year):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url
        self.rating = rating
        self.year = year

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
