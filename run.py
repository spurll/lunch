#!/usr/bin/env python


from argparse import ArgumentParser

from app import app, views


description = "Runs the Flask server for the Game/Lunch Day Voter."
parser = ArgumentParser(description=description)
parser.add_argument("-t", "--test", help="Changes host information to allow "
                    "access via localhost.", action="store_true")
parser.add_argument("-n", "--nodebug", help="Turns off server debug settings, "
                    "including the reloader.", action="store_true")
args = parser.parse_args()

# In case options have changed.
views.clear_vogts()
print "Reset vogts!"

if args.test:
    app.config["SERVER_NAME"] = app.config["TEST_SERVER_NAME"]
    app.config["HOST"] = app.config["TEST_HOST"]

app.run(app.config["HOST"], app.config["PORT"], debug=not args.nodebug)
