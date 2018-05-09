import notflix
import media

toy_story_3 = media.Movie("Toy Story 3",
                          "Andy grew up and is going to college",
                          "resources/Toy_Stoy_3.png",
                          "https://www.youtube.com/watch?v=JcpWXaA2qeg")

lemony_snicket = media.Movie("Lemony Snicket's A Series of Unfortunate Events",
                             "3 orphans running away from an awful actor",
                             "resources/LSSUE.png",
                             "https://www.youtube.com/watch?v=fccho1IyX8Y")

treasure_planet = media.Movie("Treasure Planet",
                              "An adventure to find the treasure planet",
                              "resources/Treasure_Planet.jpg",
                              "https://www.youtube.com/watch?v=DJNT7C61NrE")


fantastic_mr_fox = media.Movie("Fantastic Mr Fox",
                               "A Fox steals food for his friends and family",
                               "resources/Fantastic_mr_fox.jpg",
                               "https://www.youtube.com/watch?v=1v6-T52zLO0")

pacific_rim = media.Movie("Pacific Rim",
                          "The world is invaded by gigant monsters",
                          "resources/Pacific_Rim.jpeg",
                          "https://www.youtube.com/watch?v=5guMumPFBag")

mulan = media.Movie("Mulan",
                    "A girl dressed as a man saves China",
                    "resources/Mulan.png",
                    "https://www.youtube.com/watch?v=MsAniqGowKE")

movies = [toy_story_3,
          lemony_snicket,
          treasure_planet,
          fantastic_mr_fox,
          pacific_rim,
          mulan]
notflix.open_movies_page(movies)
