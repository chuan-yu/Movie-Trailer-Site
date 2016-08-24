import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        h2 {
            font-size: 20px;
            margin-bottom: 5px;
        }
        img {
            border-radius: 10px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
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
        .navbar {
            background: rgba(0, 0, 0, 0.2);
            border: 0px;
        }
        .navbar .navbar-brand {
            color: white;
            font-weight: bold;
            z-index: 50
        }
        .brochure {
            background: url(brochure.jpg) no-repeat center center;
            background-size: cover;
            position: relative;
            height: 400px;
            width: 100%;
            margin: 0;
            top: -80px
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            cursor: pointer;
        }
        .mvoie-tile:hover .movie-details {
            display: block;
        }
        .movie-details-wrapper {
            position: absolute;
            left: 33px;
            width: 220px;
            height: 342px;
            overflow: hidden;
            padding: 15px;
            vertical-align: top;
            z-index: 10;
            opacity: 0;
            background: rgba(0,0,0,0.8);
            -webkit-transition: opacity 1s ease;
            -moz-transition: opacity 1s ease;
            -o-transition: opacity 1s ease;
            transition: opacity 1s ease;
            color: white;
            text-align: left;
            border-radius: 10px;
        }
        .movie-details-wrapper:hover {
            opacity: 0.8;
        }
        .story-line {
            overflow: hidden;
            line-height: 18px;
            max-height: 144px;
        }
        .movie-title-wrapper {
            position: relative;
            top: -100px;
            color: white;
            width: 220px;
            height: 80px;
            margin-left: auto;
            margin-right: auto;
            border-radius: 0px 0px 10px 10px;
            background: -moz-linear-gradient(top, rgba(76,76,76,0.1) 0%, rgba(89,89,89,0.16) 12%, rgba(102,102,102,0.23) 25%, rgba(71,71,71,0.3) 39%, rgba(44,44,44,0.35) 50%, rgba(17,17,17,0.4) 60%, rgba(43,43,43,0.48) 76%, rgba(28,28,28,0.55) 91%, rgba(19,19,19,0.6) 100%);
            background: -webkit-linear-gradient(top, rgba(76,76,76,0.1) 0%,rgba(89,89,89,0.16) 12%,rgba(102,102,102,0.23) 25%,rgba(71,71,71,0.3) 39%,rgba(44,44,44,0.35) 50%,rgba(17,17,17,0.4) 60%,rgba(43,43,43,0.48) 76%,rgba(28,28,28,0.55) 91%,rgba(19,19,19,0.6) 100%);
            background: linear-gradient(to bottom, rgba(76,76,76,0.1) 0%,rgba(89,89,89,0.16) 12%,rgba(102,102,102,0.23) 25%,rgba(71,71,71,0.3) 39%,rgba(44,44,44,0.35) 50%,rgba(17,17,17,0.4) 60%,rgba(43,43,43,0.48) 76%,rgba(28,28,28,0.55) 91%,rgba(19,19,19,0.6) 100%);
            transition: opacity 1s ease;
        }
        .movie-tile:hover .movie-title-wrapper {
            opacity: 0;
        }
        .movie-title {
            overflow: hidden;
            line-height: 20px;
            max-height: 40px;
        }
        .tagline {
            overflow: hidden;
            line-height: 15px;
            max-height: 30px;
            padding: 0px 10px;
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
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
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

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">My Favourite Movies</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container brochure">
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-3 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <div class="movie-details-wrapper">
        <div class="movie-details">
            <h2 class="movie-title">{movie_title}</h2>
            <p class="release_date">Release Date: {release_date}</p>
            <p class="language">Language: {language}</p>
            <p class="review">Review: {review} / 10<p>
            <p class="story-line">Story Line: {story_line}</p>
        </div>
    </div>
    <img src="{poster_image_url}" width="220" height="342">
    <div class="movie-title-wrapper">
        <h2 class="movie-title">{movie_title}</h2>
        <p class="tagline">{tagline}</p>
    </div>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            tagline=movie.tagline,
            story_line=movie.story_line,
            release_date=movie.release_date,
            language=movie.language,
            review=movie.review,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
