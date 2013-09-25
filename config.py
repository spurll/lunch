import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(basedir,'app.db'))
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = "The lion walked backward down the stairs."

OPENID_PROVIDERS = [{'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
                    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
                    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'},
                    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
                    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'}]

OPTIONS = {"game":  ["Agricola",
                     "Ora & Labora",
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
                     "Dune",
                     "Star Trek: Deck Building Game"],
           "lunch": ["Sushi Hon",
                     "Boston Pizza",
                     "Saigon Jon's Vietnamese Kitchen",
                     "Desi Pizza & Curries",
                     "Sura Sushi",
                     "Water Lily East Indian Restaurant",
                     "Carbone Coal Fired Pizza",
                     "Joey's Only Seafood",
                     "Clubhouse Pizza",
                     "Falafel Place",
                     "Saffron Restaurant",
                     "Kenko Niwa Japanese",
                     "Sushi California",
                     "Boon Burger Cafe",
                     "Thida's Thai",
                     "East India Company",
                     "Dhoom Restaurant",
                     "China City",
                     "Sultan's Shawarma",
                     "Ivory",
                     "New Asia",
                     "Kimchi Cafe",
                     "Pasalubong Filipino Restaurant",
                     "Pho Hoang",
                     "Yuki Sushi",
                     "Watta Sushi",
                     "Ingko Sushi",
                     "JC's Tacos and More",
                     "Lao Thai"]}
