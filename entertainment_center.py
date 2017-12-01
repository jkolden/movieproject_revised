import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "https://orig00.deviantart.net/e2ad/f/2010/071/6/0/toy_story_3_poster_by_jihef03.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://pre00.deviantart.net/51e1/th/pre/f/2010/192/b/e/avatar_special_edition_poster_by_j_k_k_s.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School of Rock",
                             "A teacher forms a band with his students",
                             "https://tinyurl.com/yclzd8xv",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

searching_for_sugarman = media.Movie("Searching For Sugarman",
                                     "Academy Award winning documentary about a 1960's folk icon",
                                     "https://tinyurl.com/yc5xfhwm",
                                     "https://www.youtube.com/watch?v=QL5TffdOQ7g")

all_the_presidents_men = media.Movie("All the President's Men",
                                     "Two reporters from the Washington Post uncover illegal activity at the highest levels of government",
                                     "https://tinyurl.com/ydcj9pdc",
                                     "https://www.youtube.com/watch?v=vLt6djxhNe8")

moneyball = media.Movie("Moneyball",
                        "An unconventional general manager transforms the Oakland A's",
                        "https://tinyurl.com/y7xoptwz",
                        "https://www.youtube.com/watch?v=AiAHlZVgXjk")

movies = [toy_story, avatar, school_of_rock, searching_for_sugarman, all_the_presidents_men, moneyball]

fresh_tomatoes.open_movies_page(movies)

