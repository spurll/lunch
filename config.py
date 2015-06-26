from os import urandom, path
from collections import OrderedDict


CSRF_ENABLED = True
SECRET_KEY = urandom(30)
PROPAGATE_EXCEPTIONS = True
REMEMBER_COOKIE_NAME = 'lunch_token'    # Needs to be unique server-wide.

basedir = path.abspath(path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(path.join(basedir, "app.db"))

LDAP_URI = "ldap://ec2-23-23-226-137.compute-1.amazonaws.com"
LDAP_SEARCH_BASE = "ou=People,dc=invenia,dc=ca"

ADMIN_USERS = ["gem.newman"]

RUNNERS_UP = 4
WEEKLY_MODE = True
BIWEEKLY = True

TYPES = ["lunch", "game"]

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
                    "Asoyama Sushi",
                    "Kenko Niwa Japanese",
                    "Miso Japanese Restaurant",
                    "Sushi Gozen",
                    "Sushi Hon",
                    "Sushi Jet",
                    "Sura Suhi",
                    "Umi Sushi",
                    "Wasabi Sabi",
                ]),
            ("Indian",
                [
                    "Tandoor House",
                    "Water Lily",
                    "Clay Oven",
                    "Karahi of India",
                    "Dhoom Indian Restaurant",
                    "Sizzling Dhaba",
                ]),
            ("Chinese",
                [
                    "North Garden",
                    "Asia City",
                    "Szechuan Restaurant",
                ]),
            ("Other Asian",
                [
                    "Palatal Stir-Fry Express",
                    "Saigon Jon's Vietnamese Kitchen",
                    "Siam Thai",
                    "BIMI Korean/Japanese",
                    "Loha's Asian Restaurant",
                ]),
            ("Mexican",
                [
                    "Burrito Splendido",
                    "Taco del Mar",
                    "Vamos Tacos",
                    "Carlos & Murphy's",
                ]),
            ("Pizza & Italian",
                [
                    "Panago",
                    "Buccaccino's",
                    "Niccolinos",
                    "Boston Pizza",
                    "Carbone Coal Fired Pizza",
                    "Van Goes Pizza & Chicken",
                    "Garbonzo's Pizza",
                ]),
            ("Burgers & Sandwiches",
                [
                    "Nick's on Broadway",
                    "Flat Land Wrap",
                    "Falafel Place",
                    "Pita Pit",
                    "The Fyxx",
                    "Junior's",
                    "Myer's Delicatessen",
                    "Barley Brothers",
                ]),
            ("Cafes, Chalets, and Miscellany",
                [
                    "Desserts Plus",
                    "Good Eats",
                    "Saffron Restaurant",
                    "Osborne Village Cafe",
                    "Booster Juice",
                    "Joey's Only Seafood",
                    "Swiss Chalet",
                    "Stella's Cafe and Bakery",
                    "Prairie Ink Cafe",
                    "Confusion Corner Bar & Grill",
                    "Applebees",
                    "Tony Roma's",
                ]),
        ])
}

PREMIUM = {
    "game": {},
    "lunch": {
        "Asoyama Sushi",
        "Kenko Niwa Japanese",
        "Miso Japanese Restaurant",
        "Sushi Gozen",
        "Sushi Hon",
        "Sushi Jet",
        "Sura Suhi",
        "Umi Sushi",
        "Wasabi Sabi",
        "Water Lily",
        "Clay Oven",
        "Karahi of India",
        "Dhoom Indian Restaurant",
        "Sizzling Dhaba",
        "North Garden",
        "Asia City",
        "Szechuan Restaurant",
        "Carlos & Murphy's",
        "Boston Pizza",
        "Carbone Coal Fired Pizza",
        "Van Goes Pizza & Chicken",
        "Garbonzo's Pizza",
        "Prairie Ink Cafe",
        "Buccaccino's",
        "Niccolinos",
        "Barley Brothers",
        "Confusion Corner Bar & Grill",
        "Applebees",
        "Tony Roma's",
    }
}
