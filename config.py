from os import urandom, path
from collections import OrderedDict


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
BIWEEKLY = True

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
    "lunch": OrderedDict(
        [
            ("Japanese",
                [
                    "Dwarf no Cachette*",
                    "Samurai Japanese*",
                    "Sushi Hon*",
                    "Sushi California*",
                    "Blufish*",
                    "Kenko Niwa Japanese*"
                ]),
            ("Indian & African",
                [
                    "Water Lily*",
                    "Clay Oven*",
                    "Karahi of India*",
                    "Ivory*",
                    "East India Company*",
                    "Dhoom Indian Restaurant*",
                    "Sizzling Dhaba*",
                    "The Great Maharaja*",
                    "Blue Nile Ethiopian",
                ]),
            ("Mexican",
                [
                    "Vamos Tacos",
                    "Burrito Splendido",
                    "Casa Burrito",
                    "Carlos & Murphy's*",
                ]),
            ("Mediterranean",
                [
                    "Flavour Fusion",
                    "Shawarma House",
                    "A Taste of Mediterranean",
                    "Niko's Restaurant",
                    "Pita Pit",
                    "Bombolini*",
                ]),
            ("Pizza",
                [
                    "Panago",
                    "Boston Pizza*",
                    "Carbone Coal Fired Pizza*",
                    "Van Goes Pizza & Chicken*",
                    "Garbonzo's Pizza*",
                ]),
            ("Thai",
                [
                    "Siam Thai",
                    "Thida's Thai",
                ]),
            ("Chinese",
                [
                    "North Garden*",
                    "Asia City*",
                    "Azalea*",
                    "Szechuan Restaurant*",
                ]),
            ("Other Asian",
                [
                    "Palatal Stir-Fry Express",
                    "Saigon Jon's Vietnamese Kitchen",
                    "BIMI Korean/Japanese",
                    "Loha's Asian Restaurant",
                    "Kimchi Cafe*",
                ]),
            ("Burgers & Sandwiches",
                [
                    "Boon Burger",
                    "Garry's Deli",
                    "Myer's Delicatessen",
                    "Fox and Fiddle*",
                    "Chaise Cafe*",
                ]),
            ("Cafes, Chalets, and Miscellany",
                [
                    "Prairie Ink Cafe",
                    "Osborne Village Cafe",
                    "Booster Juice",
                    "Bodegoes",
                    "Joey's Only Seafood",
                    "Swiss Chalet",
                    "Chester Fried Chicken",
                    "Stella's Cafe and Bakery",
                ]),
        ])
    }
