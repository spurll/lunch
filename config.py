import os


basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
PORT = 9999

# Local Testing
#HOST = "127.0.0.1"		 # Must be 0.0.0.0 for external availability.
#SERVER_NAME = "localhost:{}".format(PORT)

# Externally Accessible
HOST = "0.0.0.0"		# Must be 0.0.0.0 for external availability.
SERVER_NAME = "savage.startleddisbelief.com:{}".format(PORT)

CSRF_ENABLED = True
SECRET_KEY = os.urandom(30)

RUNNERS_UP = 4
WEEKLY_MODE = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(basedir,'app.db'))

OPENID_PROVIDERS = [{'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
                    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
                    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'},
                    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
                    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'}]

OPTIONS = {"game": [ "Terra Mystica",
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
                     "Star Trek: Deck Building Game"],

           "lunch": {"Sushi":          ["Sushi Hon*",
                                        "Sushi California*",
                                        "Sushi King*",
                                        "Blufish*",
                                        "Kenko Niwa Japanese*"],
                     "Indian":         ["Water Lily*",
                                        "Clay Oven*",
                                        "Famena's Roti and Curry*",
                                        "Ivory*",
                                        "East India Company*",
                                        "Dhoom Indian Restaurant*",
                                        "Sizzling Dhaba*",
                                        "The Great Maharaja*"],
                     "Pizza":          ["Panago",
                                        "Boston Pizza*",
                                        "Carbone Coal Fired Pizza*",
                                        "Van Goes Pizza & Chicken*",
                                        "Garbonzo's Pizza*",
                                        "Desi Pizza & Curries*"],
                     "Mediterranean":  ["A Taste of Mediterranean",
                                        "Olympia Diner",
                                        "Niko's Restaurant",
                                        "Pita Pit"],
                     "Mexican":        ["Burrito Splendido",
                                        "Modern Taco Company",
                                        "Casa Burrito",
                                        "Carlos & Murphy's*"],
                     "Middle Eastern": ["Sultan's Shawarma",
                                        "Shawarma Khan",
                                        "Kabob Palace",
                                        "Falafel Place"],
                     "African":        ["Blue Nile",
                                        "Gohe Ethiopian"],
                     "Thai":           ["Siam Thai",
                                        "Thida's Thai"],
                     "Other Asian":    ["Saigon Jon's Vietnamese Kitchen",
                                        "Palatal Stir-Fry Express",
                                        "Pho Hoang",
                                        "China City",
                                        "Kimchi Cafe",
                                        "North Garden",
                                        "Asia City",
                                        "Loha's Asian Restaurant",
                                        "Szechuan Restaurant",
                                        "Pasalubong Filipino Restaurant"],
                     "Burgers & Sandwiches":
                                       ["Subway",
                                        "Garry's Deli",
                                        "Myer's Delicatessen",
                                        "Red Top Drive Inn",
                                        "Nook and Cranny",
                                        "Brogue Pubside*",
                                        "Chaise Cafe*"],
                     "Other":          ["Bodegoes",
                                        "Joey's Only Seafood",
                                        "Elements",
                                        "Chester Fried Chicken",
                                        "Stella's Cafe and Bakery",
                                        "The Round Table*"]}}
