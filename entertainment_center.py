import fresh_tomatoes
import media

"""Creating several Movie instances with data"""
interstellar = media.Movie("Interstellar",
                        "The story of a man and the starts",
                        "http://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                        "https://www.youtube.com/watch?v=zSWdZVtXT7E"
                        )

toy_story = media.Movie("Toy Story",
                        "A story of toys",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=Bj4gS1JQzjk"
                        )


avatar = media.Movie("Avatar",
                        "An American guy with lots of blue females",
                        "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=eUTtt14G31c"
                        )


"""Putting all Movie instances inside a list to be used by open_movies_page function"""
movies = [interstellar, toy_story, avatar]

fresh_tomatoes.open_movies_page(movies)
