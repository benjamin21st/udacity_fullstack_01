import webbrowser
#
# class Video():
#     """ This is going to be some documentation """
#     def __init__(self, title, duration):
#         self.title = title
#         self.duration = duration


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # Video.__init__(self, )
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
