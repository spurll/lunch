from os import urandom, path


CSRF_ENABLED = True
SECRET_KEY = urandom(30)
PROPAGATE_EXCEPTIONS = True

basedir = path.abspath(path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(path.join(basedir, "app.db"))

LDAP_URI = "ldap://ec2-23-23-226-137.compute-1.amazonaws.com"
LDAP_SEARCH_BASE = "ou=People,dc=invenia,dc=ca"

ADMIN_USERS = ["gem.newman"]

RUNNERS_UP = 4
WEEKLY_MODE = True

OPTIONS = {
    "game":
        [
            "Terra Mystica",
             "Star Cluster",
             "Agricola",
             "Ora & Labora",
             "Dune",
             "Tales of the Arabian Nights",
             "Dungeon Lords",
             "Magic: the Gathering",
             "Cosmic Encounter",
             "Power Grid",
             "Mansions of Madness",
             "Small World",
             "Endeavor",
             "Dominant Species",
             "Pandemic",
             "Dominion",
             "Ascension",
             "Midgard",
             "Race for the Galaxy",
             "Star Trek: Deck Building Game",
         ],
    "lunch":
        {
            "Japanese":
                [
                    "Dwarf no Cachette*",
                    "Samurai Japanese*",
                    "Sushi Hon*",
                    "Sushi California*",
                    "Sushi King*",
                    "Blufish*",
                    "Kenko Niwa Japanese*"
                ],
            "Indian":
                [
                    "Water Lily*",
                    "Clay Oven*",
                    "Karahi of India*",
                    "Famena's Roti and Curry*",
                    "Ivory*",
                    "East India Company*",
                    "Dhoom Indian Restaurant*",
                    "Sizzling Dhaba*",
                    "The Great Maharaja*",
                ],
            "Pizza":
                [
                    "Panago",
                    "Boston Pizza*",
                    "Carbone Coal Fired Pizza*",
                    "Van Goes Pizza & Chicken*",
                    "Garbonzo's Pizza*",
                    "Doughboys Pizzeria*",
                ],
            "Mediterranean":
                [
                    "A Taste of Mediterranean",
                    "Olympia Diner",
                    "Niko's Restaurant",
                    "Pita Pit",
                    "Bombolini*",
                    "Brooklyn's Bistro*",
                ],
            "Mexican":
                [
                    "Burrito Splendido",
                    "Modern Taco Company",
                    "Casa Burrito",
                    "Carlos & Murphy's*",
                ],
            "Middle Eastern":
                [
                    "Sultan's Shawarma",
                    "Shawarma Khan",
                    "Kabob Palace",
                    "Falafel Place",
                ],
            "African":
                [
                    "Blue Nile",
                    "Gohe Ethiopian"
                ],
            "Thai":
                [
                    "Siam Thai",
                    "Thida's Thai",
                ],
            "Chinese":
                [
                    "North Garden*",
                    "Asia City*",
                    "Azalea*",
                    "Szechuan Restaurant*",
                ],
            "Other Asian":
                [
                    "Saigon Jon's Vietnamese Kitchen",
                    "Palatal Stir-Fry Express",
                    "Pho Hoang",
                    "Loha's Asian Restaurant",
                    "Pasalubong Filipino Restaurant",
                    "Kimchi Cafe*",
                ],
            "Burgers & Sandwiches":
                [
                    "Subway",
                    "Boon Burger",
                    "Garry's Deli",
                    "Myer's Delicatessen",
                    "Red Top Drive Inn",
                    "Nook and Cranny",
                    "Wendy's",
                    "Brogue Pubside*",
                    "Fox and Fiddle*",
                    "Chaise Cafe*",
                ],
            "Other":
                [
                    "Booster Juice",
                    "Bodegoes",
                    "Joey's Only Seafood",
                    "Elements",
                    "Applebee's",
                    "Swiss Chalet",
                    "Chester Fried Chicken",
                    "Stella's Cafe and Bakery",
                    "The Round Table*",
                    "Bistro 7 1/4*",
                ],
        }
    }
