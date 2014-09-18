from requests import post
from slackutils import Slack

from lunch import db
from models import User, Vogt


def determine_winner(type):
    vogts = Vogt.query.filter_by(type=type)
    totals = {v.option: sum([v1.score for v1 in vogts if v1.option == v.option]) for v in vogts}
    print "Totals: {}".format(totals)
    return max(totals, key=totals.get)


def determine_winners(type, count):
    return vogt_totals(type)[:count]


def weekly_winners(type):
    winners = vogt_totals(type)
    premium = [w for w in winners[:5] if "*" in w]
    while len(premium) > 2:
        # Remove premiums beyond 2.
        print "Too many premiums! Removing {}!".format(premium[2])
        winners.remove(premium[2])
        premium = [w for w in winners[:5] if "*" in w]
    return winners[:5]


def vogt_totals(type):
    vogts = Vogt.query.filter_by(type=type)
    totals = {v.option: sum([v1.score for v1 in vogts if v1.option == v.option]) for v in vogts}
    print "Totals: {}".format(totals)
    winners = sorted(totals.keys(), key=totals.get, reverse=True)
    return winners


def slack_message(token, text, notify=False):
    s = Slack(token, name="LunchBot",
              icon="http://savage.startleddisbelief.com/LunchBot.png")
    return s.send("#food", text, notify=notify)


def slack_weekly_lunch(token):
    w = weekly_winners("lunch")
    if w:
        text = "This week's lunches have been decided!\n\n{}\n\nPlease see "  \
               "that you have orders placed in the <https://docs.google.com/" \
               "spreadsheets/d/1l-j4Gdn2-eO6bnHSLuF4GJxU1irYaPdUQpXKC3Cj7Cc/" \
               "|standing orders document>.".format("\n".join(w))
        slack_message(token, text)
    else:
        print "No vogts to tally."


def slack_reminder(token, message=None):
    if not message: message = "Please vogt for next week's lunch selections!"
    text = "<http://savage.startleddisbelief.com/lunch|" + message + ">"
    slack_message(token, text, notify=True)


def clear_vogts():
    Vogt.query.delete()
    db.session.commit()
