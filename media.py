import webbrowser

class Movie():
    '''
    This class stores movie data such as title, storyline, production info, etc.
    '''

    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, director, director_link, studio, release):
        '''
        Initialize the movie instance.
        Inputs:
            movie_title         => Title of the movie
            movie_storyline     => Brief synopsis of the movie
            poster_image        => Image of the movie poster
            trailer_youtube     => Movie trailer on YouTube
            director            => Director of the movie
            studio              => Production company
            release             => Movie's USA release date
        Outputs: None
        '''

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = director
        self.studio = studio
        self.release = release
        self.director_link = director_link

    def show_trailer(self):
        # Opens webbrowser with movie trailer
        webbrowser.open(self.trailer_youtube_url)
