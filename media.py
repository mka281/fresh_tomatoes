import webbrowser

class Movie():
    """ This class provides a way to store movie related information"""
    def __init__(self, movie_title, moive_storyline, poster_image, trailer_url):
        self.title = movie_title
        self.storyline = moive_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
