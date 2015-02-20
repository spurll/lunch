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
                    "Asoyama Sushi*",
                    "Kenko Niwa Japanese*",
                    "Miso Japanese Restaurant*",
                    "Sushi Gozen*",
                    "Sushi Hon*",
                    "Sushi Jet*",
                    "Sura Suhi*",
                    "Umi Sushi*",
                    "Wasabi Sabi*",
                ]),
            ("Indian",
                [
                    "Tandoor House",
                    "Water Lily*",
                    "Clay Oven*",
                    "Karahi of India*",
                    "Dhoom Indian Restaurant*",
                    "Sizzling Dhaba*",
                ]),
            ("Chinese",
                [
                    "North Garden*",
                    "Asia City*",
                    "Szechuan Restaurant*",
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
                    "Vamos Tacos",
                    "Burrito Splendido",
                    "Carlos & Murphy's*",
                ]),
            ("Pizza",
                [
                    "Panago",
                    "Boston Pizza*",
                    "Carbone Coal Fired Pizza*",
                    "Van Goes Pizza & Chicken*",
                    "Garbonzo's Pizza*",
                ]),
            ("Burgers & Sandwiches",
                [
                    "Falafel Place",
                    "Pita Pit",
                    "The Fyxx",
                    "Junior's",
                    "Myer's Delicatessen",
                ]),
            ("Cafes, Chalets, and Miscellany",
                [
                    "Confusion Corner Bar & Grill",
                    "Desserts Plus",
                    "Good Eats",
                    "Saffron Restaurant",
                    "Prairie Ink Cafe*",
                    "Osborne Village Cafe",
                    "Booster Juice",
                    "Joey's Only Seafood",
                    "Swiss Chalet",
                    "Stella's Cafe and Bakery",
                    "Applebees*",
                    "Tony Roma's*",
                ]),
        ])
    }
