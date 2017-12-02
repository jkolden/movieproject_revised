import media
import fresh_tomatoes


# Creating movies to describe the instances of the Class Movie




avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://tinyurl.com/ydcvt8es",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie(
    "School of Rock",
    "A teacher forms a band with his students",
    "https://tinyurl.com/yclzd8xv",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

searching_for_sugarman = media.Movie(
    "Searching For Sugarman",
    "Academy Award winning documentary about a 1960's folk icon",
    "https://tinyurl.com/yc5xfhwm",
    "https://www.youtube.com/watch?v=QL5TffdOQ7g")

all_the_presidents_men = media.Movie(
    "All the President's Men",
    """Two reporters from the Washington Post uncover
    illegal activity at the highest levels of government""",
    "https://tinyurl.com/ydcj9pdc",
    "https://www.youtube.com/watch?v=vLt6djxhNe8")

moneyball = media.Movie(
    "Moneyball",
    "An unconventional general manager transforms the Oakland A's",
    "https://tinyurl.com/y7xoptwz",
    "https://www.youtube.com/watch?v=AiAHlZVgXjk")

# Movies array, contains the list of movies as input, which
# is passed to the function "open_movies_page". This function
# translates this list into a web page when we run the
# "entertainment_center.py" file.


movies = [toy_story,
          avatar,
          school_of_rock,
          searching_for_sugarman,
          all_the_presidents_men, moneyball]

fresh_tomatoes.open_movies_page(movies)
