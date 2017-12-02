import media
import fresh_tomatoes


# Creating movies to describe the instances of the Class Movie


toy_story = media.Movie(
    "Toy Story",
    "A Story of a boy and his toys that come to life",
    "https://tinyurl.com/y8jrdmex",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

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
    "https://tinyurl.com/al4r7gu")

all_the_presidents_men = media.Movie(
    "All the President's Men",
    """Two reporters from the Washington Post uncover
    illegal activity at the highest levels of government""",
    "https://tinyurl.com/ydcj9pdc",
    "https://tinyurl.com/lgl4e79")

moneyball = media.Movie(
    "Moneyball",
    "An unconventional general manager transforms the Oakland A's",
    "https://tinyurl.com/y7xoptwz",
    "https://www.youtube.com/watch?v=AiAHlZVgXjk")

movies = [toy_story,
          avatar,
          school_of_rock,
          searching_for_sugarman,
          all_the_presidents_men, moneyball]

fresh_tomatoes.open_movies_page(movies)
