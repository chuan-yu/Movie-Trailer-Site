class Movie():
    """ 
            This is a Movie class.

            Instance Varaibles:
                    tilte (str): movie title
                    poster_image_url (str): the link to movie poster image
                    trailer_youtube_url (str): the Youtube link to movie trailer 
    """

    def __init__(self, movie_title, movie_tagline, movie_story_line, movie_release_date, movie_language, movie_review, poster_image, trailer_youtube):
        self.title = movie_title
        self.tagline = movie_tagline
        self.story_line = movie_story_line
        self.release_date = movie_release_date
        self.language = movie_language
        self.review = movie_review
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
