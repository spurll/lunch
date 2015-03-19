from slackutils import Slack
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import NumberRange
from sqlalchemy.sql import func

from lunch import app, db
from lunch.forms import VoteForm
from lunch.models import User, Vote, Favourite, History


PREMIUM = app.config["PREMIUM"]


def vote_totals(type=None):
    if type:
        totals = {option: {"total": sum, "ballots": count} for option, sum,
                  count in db.session.query(Vote.option, func.sum(Vote.score),
                  func.count(Vote.score)).filter_by(type=type)
                  .group_by(Vote.option).all()}
    else:
        totals = {option: {"total": sum, "ballots": count} for option, sum,
                  count in db.session.query(Vote.option, func.sum(Vote.score),
                  func.count(Vote.score)).group_by(Vote.option).all()}

    return totals


def determine_winner(type):
    totals = vote_totals(type)
    return max(totals, key=lambda x: totals[x]["total"])


def determine_winners(type, count):
    totals = vote_totals(type)
    winners = sorted(totals.keys(), key=lambda x: totals[x]["total"],
                     reverse=True)
    return winners[:count]


def weekly_winners(type):
    totals = vote_totals(type)
    winners = sorted(totals.keys(), key=lambda x: totals[x]["total"],
                     reverse=True)
    premium = [w for w in winners[:5] if w in PREMIUM[type]]

    while len(premium) > 2:
        # Remove premiums beyond 2.
        print('Too many premiums! Removing {}!'.format(premium[2]))
        winners.remove(premium[2])
        premium = [w for w in winners[:5] if w in PREMIUM[type]]

    return winners[:5]


def biweekly_winners(type):
    totals = vote_totals(type)
    winners = sorted(totals.keys(), key=lambda x: totals[x]["total"],
                     reverse=True)
    premium = [w for w in winners[:10] if w in PREMIUM[type]]

    while len(premium) > 4:
        # Remove premiums beyond 4.
        print('Too many premiums! Removing {}!'.format(premium[4]))
        winners.remove(premium[4])
        premium = [w for w in winners[:10] if w in PREMIUM[type]]

    return winners[:10]


def history(type, options):
    past = History.query.filter_by(type=type)                                 \
                        .filter(History.option.in_(options))

    return [(p.option, int(p.score())) for p in sorted(past,
            key=lambda x: x.score(), reverse=True)]


def create_ballot(type, options, user):
    class CurrentVoteForm(VoteForm):
        # Must be different form for games and lunch, otherwise it might be
        # populated with one, then if the user switches be populated with the
        # other, resulting in a bunch of hidden, invalid values that don't
        # validate.
        pass

    # Create the form element for each option.
    for option in options:
        ballot = User.query.get(user.id).votes.filter_by(type=type,
                 option=option).first()
        favourite = User.query.get(user.id).favourites.filter_by(type=type,
                 option=option).first()

        if ballot:
            # Initialize the element to the value of the ballot cast.
            value = ballot.score
        elif favourite:
            # Initialize the element to the saved value for this option.
            value = favourite.score
        else:
            # Initialize the element to the default score.
            value = 50

        field = IntegerRangeField(option, default=value,
                validators=[NumberRange(min=0, max=100)])

        setattr(CurrentVoteForm, option, field)

    return CurrentVoteForm()


def submit_vote(type, options, user, form):
    # Record the votes.
    for option in options:
        v = Vote(type=type, option=option, user_id=user.id,
                 score=form.__getattribute__(option).data)
        db.session.merge(v)

    # Delete existing favourites, then add each new favourite.
    if form.favourite.data:
        for option in options:
            f = Favourite(type=type, option=option, user_id=user.id,
                          score=form.__getattribute__(option).data)
            db.session.merge(f)

    db.session.commit()


def close_votes(type):
    totals = vote_totals(type)
    past = {option: {"total": total, "ballots": ballots} for option, total,
            ballots in db.session.query(History.option, History.total,
            History.ballots).filter_by(type=type).all()}

    # Update the vote history table.
    options = totals.keys() | past.keys()
    for o in options:
        t = totals.get(o, {"total": 0, "ballots": 0})
        p = past.get(o, {"total": 0, "ballots": 0})
        new = History(type=type, option=o, total=t["total"] + p["total"],
                      ballots=t["ballots"] + p["ballots"])
        db.session.merge(new)

    # Clear the existing votes in this category.
    Vote.query.filter_by(type=type).delete()
    db.session.commit()



def clear_votes(user=None):
    if user:
        print('User: {}'.format(user))
        User.query.get(user.id).votes.delete()
    else:
        print('No user.')
        Vote.query.delete()

    db.session.commit()


def clear_favourites(user=None):
    if user:
        User.query.get(user.id).favourites.delete()
    else:
        Favourites.query.delete()

    db.session.commit()


def slack_message(token, text, notify=False):
    s = Slack(token, name="LunchBot",
              icon="http://savage.startleddisbelief.com/LunchBot.png")
    return s.send("#lunch", text, notify=notify)


def slack_weekly_lunch(token):
    w = weekly_winners("lunch")

    if w:
        text = ("This week's lunches have been decided!\n\n{}\n\nPlease see "
                "that you have orders placed in the <https://docs.google.com/"
                "spreadsheets/d/1l-j4Gdn2-eO6bnHSLuF4GJxU1irYaPdUQpXKC3Cj7Cc/"
                "|standing orders document>.").format("\n".join(w))
        slack_message(token, text)
        close_votes("lunch")

    else:
        print('No votes to tally.')


def slack_biweekly_lunch(token):
    w = biweekly_winners("lunch")

    if w:
        text = ("The next two weeks' lunches have been decided!\n\n{}\n\n"
                "Please see that you have orders placed in the <https://docs."
                "google.com/spreadsheets/d/1l-j4Gdn2-eO6bnHSLuF4GJxU1irYaPdUQp"
                "XKC3Cj7Cc/|standing orders document>.").format("\n".join(w))
        slack_message(token, text)
        close_votes("lunch")

    else:
        print('No votes to tally.')


def slack_reminder(token, message=None):
    if not message: message = "Please vogt for next week's lunch selections!"
    text = "<http://savage.startleddisbelief.com/vote/lunch|" + message + ">"
    slack_message(token, text, notify=True)

