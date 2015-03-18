import fresh_tomatoes
import media

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


movies = [toy_story, avatar]

# fresh_tomatoes.open_movies_page(movies)
for i in movies:
    print(i.__doc__)