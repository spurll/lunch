import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(basedir,'app.db'))
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#HOST = "127.0.0.1"		# Must be 0.0.0.0 for external availability.
HOST = "0.0.0.0"		# Must be 0.0.0.0 for external availability.
PORT = 9999
SERVER_NAME = "savage.startleddisbelief.com:{}".format(PORT)
DEBUG = True

CSRF_ENABLED = True
SECRET_KEY = "The lion walked backward down the stairs."

OPENID_PROVIDERS = [{'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
                    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
                    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'},
                    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
                    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'}]

OPTIONS = {"game": [ "Terra Mystica",
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
                                        "Kenko Niwa Japanese"],
                     "Indian":         ["Water Lily",
                                        "Clay Oven",
                                        "Famena's Roti and Curry",
                                        "Ivory",
                                        "East India Company",
                                        "Dhoom Indian Restaurant",
                                        "Desi Pizza & Curries"],
                     "Pizza":          ["Boston Pizza",
                                        "Diana's Gourmet Pizza",
                                        "Carbone Coal Fired Pizza",
                                        "Clubhouse Pizza"],
                     "Mediterranean":  ["A Taste of Mediterranean",
                                        "Olympia Diner",
                                        "Niko's Restaurant",
                                        "Pita Pit"],
                     "Mexican":        ["Modern Taco Company"],
                     "Middle Eastern": ["Sultan's Shawarma",
                                        "Kabob Palace",
                                        "Falafel Place"],
                     "Other Asian":    ["Saigon Jon's Vietnamese Kitchen",
                                        "Pho Hoang",
                                        "Thida's Thai",
                                        "Lao Thai",
                                        "China City",
                                        "Kimchi Cafe",
                                        "North Garden",
                                        "Asia City",
                                        "Pasalubong Filipino Restaurant"],
                     "Burgers":        ["Boon Burger",
                                        "Brogue Pubside",
                                        "Nook and Cranny"],
                     "Other":          ["Joey's Only Seafood",
                                        "Elements",
                                        "Gohe Ethiopian",
                                        "The Round Table",
                                        "Saffron Restaurant"]}}
