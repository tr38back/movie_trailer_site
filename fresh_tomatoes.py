import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Trailers for Holden & Pen!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 10%;
            width: 80%;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .img, .movie-name:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .wrapper:after {
        display: block;
        height: 0;
        clear: both;
        }

        .storyline, a {
            color: #0645AD;
        }
        .storyline:hover {
            color: #0B0080;
            text-decoration: underline;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.img, .movie-name', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- end Trailer Video Modal -->
    <div class="alert alert-success" style="width: 70%; margin: auto;" >
     <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
      <h2 style="font-size: 1.5em; margin: 0px;"><strong>Holden & Pen!</strong></h2>
          I know that Toy Story and Avatar weren't actually on the
            list of your favorite movies, but I'm using them for filler in this project <3
    </div><br>

<div class="alert alert-info" style="width: 70%; margin: auto;" >
 <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
  <h2 style="font-size: 1.5em; margin: 0px;"><strong>Also:</strong></h2>
 You can interact here! Just click on the image of the movie poster or the name of the movie to watch its trailer -
 or click on the director's name to read about the director. :)
</div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Some Favorite Movies for Holden and Penlope</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container" style="display: flex; flex-wrap: wrap;">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center">
    <img class="img" src="{poster_image_url}" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer" width="220" height="342">

    <h2 class="movie-name" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer" >{movie_title}</h2>

    <h5 class="storyline" data-toggle="collapse" data-target="#{safe_title}">Storyline</h5>
  <div id="{safe_title}" class="collapse">
    {movie_storyline}
  </div>

    <h4>Production Info</h2>

    <p>
    Director: <a href="{director_link}" target="_blank">{director}</a><br>
    Production Studio: {studio}<br>
    Release Date: {release}
    </p>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+',
                                                         movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title= movie.title,
            poster_image_url= movie.poster_image_url,
            trailer_youtube_id= trailer_youtube_id,
            director= movie.director,
            studio= movie.studio,
            release= movie.release,
            director_link = movie.director_link,
            movie_storyline = movie.storyline,
            safe_title = movie.safe_title

        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
