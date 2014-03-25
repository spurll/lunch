import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(basedir,'app.db'))
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Local Testing
HOST = "127.0.0.1"		# Must be 0.0.0.0 for external availability.

# Externally Accessible
#HOST = "0.0.0.0"		# Must be 0.0.0.0 for external availability.
#SERVER_NAME = "savage.startleddisbelief.com:{}".format(PORT)

PORT = 9999
DEBUG = True

CSRF_ENABLED = True
SECRET_KEY = "The lion walked backward down the stairs."

RUNNERS_UP = 4

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
                     "Ergo",
                     "Endeavor",
                     "Dominant Species",
                     "Pandemic",
                     "Dominion",
                     "Ascension",
                     "Midgard",
                     "Race for the Galaxy",
                     "Star Trek: Deck Building Game"],

           "lunch": {"Sushi":          ["Sushi Hon",
                                        "Sura Sushi",
                                        "Sushi California",
                                        "Sushi Jet",
                                        "Sushi King",
                                        "Blufish",
                                        "Kenko Niwa Japanese"],
                     "Indian":         ["Water Lily",
                                        "Clay Oven",
                                        "Famena's Roti and Curry",
                                        "Ivory",
                                        "East India Company",
                                        "Dhoom Indian Restaurant",
                                        "Sizzling Dhaba",
                                        "The Great Maharaja"],
                     "Pizza":          ["Panago",
                                        "Boston Pizza",
                                        "Diana's Gourmet Pizza",
                                        "Carbone Coal Fired Pizza",
                                        "Van Goes Pizza & Chicken",
                                        "Garbonzo's Pizza",
                                        "Desi Pizza & Curries"],
                     "Mediterranean":  ["A Taste of Mediterranean",
                                        "Olympia Diner",
                                        "Niko's Restaurant",
                                        "Pita Pit"],
                     "Mexican":        ["Burrito Splendido",
                                        "Carlos & Murphy's",
                                        "Modern Taco Company",
                                        "Casa Burrito"],
                     "Middle Eastern": ["Sultan's Shawarma",
                                        "Shawarma Khan",
                                        "Kabob Palace",
                                        "Falafel Place"],
                     "African":        ["Blue Nile",
                                        "Gohe Ethiopian"],
                     "Other Asian":    ["Saigon Jon's Vietnamese Kitchen",
                                        "Palatal Stir-Fry Express",
                                        "Pho Hoang",
                                        "Thida's Thai",
                                        "Lao Thai",
                                        "China City",
                                        "Kimchi Cafe",
                                        "North Garden",
                                        "Asia City",
                                        "Loha's Asian Restaurant",
                                        "Szechuan Restaurant",
                                        "Pasalubong Filipino Restaurant"],
                     "Burgers & Sandwiches":  ["Brogue Pubside",
                                        "Chaise Cafe",
                                        "Subway",
                                        "Garry's Deli",
                                        "Myer's Delicatessen",
                                        "Red Top Drive Inn",
                                        "Nook and Cranny"],
                     "Other":          ["Bodegoes",
                                        "Joey's Only Seafood",
                                        "Elements",
                                        "Chester Fried Chicken",
                                        "The Round Table",
                                        "Stella's Cafe and Bakery"]}}
