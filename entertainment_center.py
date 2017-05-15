import fresh_tomatoes
import media
# imports and provides access to media and fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://vignette3.wikia.nocookie.net/disney/images/1/13/Toy_Story.jpg/revision/latest?cb=20151003163558",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4",
                        "John Lasseter",
                        "https://en.wikipedia.org/wiki/John_Lasseter",
                        "Disney, Pixar",
                        "November, 1995")

avatar = media.Movie("Avatar",
                     "A Marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ",
                     "James Cameron",
                     "https://en.wikipedia.org/wiki/James_Cameron",
                     "Lightstorm, Dune, Ingenious",
                     "December, 2009")

batman = media.Movie("The LEGO Batman Movie",
                     """A cooler-than-ever Bruce Wayne must deal with the usual suspects as they plan to rule Gotham City, 
                     while discovering that he has accidentally adopted a teenage orphan who wishes to become his sidekick.""",
                     """https://images-na.ssl-images-amazon.com/images/M/MV5BMTcyNTEyOTY0M15BMl5BanBnXkFtZTgwOTA
                     yNzU3MDI@._V1_SY1000_CR0,0,674,1000_AL_.jpg""",
                     "https://www.youtube.com/watch?v=LZSQTVdF3QM",
                     "Chris McKay",
                     "https://en.wikipedia.org/wiki/Chris_McKay",
                     "Warner, DC",
                     "February, 2017")
                     

trolls = media.Movie("Trolls",
                     "After the Bergens invade Troll Village, Poppy, the happiest Troll ever born, and the overly-cautious, curmudgeonly Branch set off on a journey to rescue her friends.",
                     "https://upload.wikimedia.org/wikipedia/en/a/ad/Trolls_%28film%29_logo.png",
                     "https://www.youtube.com/watch?v=xyjm5VQ11TQ",
                     "Mike Mitchell",
                     "https://en.wikipedia.org/wiki/Mike_Mitchell_(director)",
                     "Dreamworks",
                     "November, 2016")

jungle_book = media.Movie("The Jungle Book",
                          "Raised by a family of wolves since birth, Mowgli must leave the only home he's ever known when the fearsome tiger Shere Khan unleashes his mighty roar. Guided by a no-nonsense panther and a free-spirited bear, the young boy meets an array of jungle animals, including a slithery python and a smooth-talking ape. Along the way, Mowgli learns valuable life lessons as his epic journey of self-discovery leads to fun and adventure.",
                          "https://upload.wikimedia.org/wikipedia/en/a/a4/The_Jungle_Book_%282016%29.jpg",
                          "https://www.youtube.com/watch?v=e8TPW6rFZpA",
                          "Jon Favreau",
                          "https://en.wikipedia.org/wiki/Jon_Favreau",
                          "Disney",
                          "April, 2016")

force_awakens = media.Movie("Star Wars: The Force Awakens",
                            "Three decades after the defeat of the Galactic Empire, a new threat arises. The First Order attempts to rule the galaxy and only a ragtag group of heroes can stop them, along with the help of the Resistance.",
                            "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
                            "https://www.youtube.com/watch?v=UitsQDWSlUg",
                            "J.J. Abrams",
                            "https://en.wikipedia.org/wiki/J._J._Abrams",
                            "Lucasfilm, Bad Robot",
                            "December, 2016")


movies = [toy_story, avatar, batman, trolls, jungle_book, force_awakens]
fresh_tomatoes.open_movies_page(movies)
