import webbrowser


class Movie():
    """This class provides a way to store movie related information.
    It can only receive string attributes
    Attributes

    attr1 (self, str): The first attribute its the attribute `self` it helps
    to declare the instance variable that you need to use the class in
    other documents

    attr2(movie_title,str): Its the movie title

    attr3(movie_storyline, str): Its a little resume of the plot of the movie

    attr4(poster_image, str): Is the url or localization of the poster image of
    the movie

    attr5(trailer_youtube, str): Its the url of the movie trailer in youtube
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    # This function initializes the class Movie when its called

    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):

        # Assign the value of the argument

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # This function opens the movie trailer in a new browser window
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
