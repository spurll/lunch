#!/usr/bin/env python

import web, json, os, re, base64


try:
    filename = "data/options.json"
    file = open(filename, "r")
    options = json.load(file)
    file.close()
except IOError:
    options = {"game": {}, "lunch": {}}
    print "Unable to read {}. Weird.".format(filename)


try:
    filename = "data/allowed.json"
    file = open(filename, "r")
    allowed = json.load(file)["users"]
    file.close()
except IOError:
    allowed = ()
    print "Unable to read {}. Weird.".format(filename)


DEFAULT_SCORE = 50


urls = ("/game", "Index", "/lunch", "Index", "/login", "Login")


render = web.template.render("templates/")


class Index(object):
    def GET(self):
        print "GET"
        print "path: {}".format(web.ctx.path)
        type = web.ctx.path[1:]
        print "type: {}".format(type)

        auth = web.ctx.env.get("HTTP_AUTHORIZATION")
        if auth is not None:
            # Check to see if a .vogt file for the user exists. If so, populate
            # with that information and set "voted" to true.
            auth = re.sub("^Basic ", "", auth)
            user, password = base64.decodestring(auth).split(":")
            try:
                filename = "data/{}/{}.vogt".format(type, user)

                file = open(filename, "r")
                form = json.load(file)
                file.close()

                voted=True

                # Output debug info to server console.
                print "Loaded: {}".format(form)

            except IOError:
                # Initial setup.
                form = {g: DEFAULT_SCORE for g in options[type]}

                voted = False

                # Output debug info to server console.
                print "Unable to read {}. User probably hasn't voted.".format(filename)

            winner = determine_winner(type)

            toggle = "lunch" if type == "game" else "game"
            return render.index(form=form, voted=voted, type=type,
                                winner=winner, toggle=toggle)

        else:
            raise web.seeother("/login")

    def POST(self):
        print "POST"
        print "path: {}".format(web.ctx.path)
        type = web.ctx.path[1:]
        print "type: {}".format(type)

        auth = web.ctx.env.get("HTTP_AUTHORIZATION")
        if auth is not None:
            # Check to see if a .vogt file for the user exists. If so, populate
            # with that information and set "voted" to true.
            auth = re.sub("^Basic ", "", auth)
            user, password = base64.decodestring(auth).split(":")

            # Retrieve input.
            form = web.input()

            # Output debug info to server console.
            print "Received: {}".format(form)

            # Save to .vogt file.
            try:
                filename = "data/{}/{}.vogt".format(type, user)

                file = open(filename, "w+")
                json.dump(form, file)
                file.close()

            except IOError:
                print "Unable to write to {}. Weird.".format(filename)

            winner = determine_winner(type)

            # Announce winner.
            print "Winner: {}".format(winner)

            toggle = "lunch" if type == "game" else "game"
            return render.index(form=form, voted=True, type=type,
                                winner=winner, toggle=toggle)

        else:
            raise web.seeother("/login")


class Login:
    def GET(self):
        auth = web.ctx.env.get("HTTP_AUTHORIZATION")
        authreq = False

        if auth is None:
            authreq = True
        else:
            auth = re.sub("^Basic ", "", auth)
            username, password = base64.decodestring(auth).split(":")
            if username in allowed.keys() and allowed[username] == password:
                raise web.seeother("/game")
            else:
                authreq = True

        if authreq:
            web.header("WWW-Authenticate", "Basic realm='Authentication'")
            web.ctx.status = "401 Unauthorized"
            return


def determine_winner(type):
    # Load all .vogt files.
    path = os.path.join("data", type)
    files = os.listdir(path)

    # Remove directories and files that don't match the pattern, if any.
    files = [os.path.join(path, f) for f in files
             if os.path.isfile(os.path.join(path, f))
             and extension(f).lower() == ".vogt"]

    # Sum scores for all options.
    totals = {k: 0 for k in options[type]}
    for f in files:
        try:
            file = open(f, "r")
            votes = json.load(file)
            file.close()

            totals = {k: totals[k] + int(votes[k]) if k in votes.keys() else 0
                      for k in options[type]}

        except IOError:
            print "Unable to read {}. Weird.".format(f)

    print "Totals: {}".format(totals)

    return max(totals, key=totals.get)


def extension(f):
    ext = re.search(r"\.[^\.]+$", f)
    if ext: ext = ext.group(0)
    return ext


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
