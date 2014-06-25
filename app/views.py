from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import NumberRange
import ldap

from app import app, db, lm
from forms import LoginForm, VogtForm
from models import User, Vogt
from authenticate import authenticate


RUNNERS_UP = app.config["RUNNERS_UP"]
WEEKLY_MODE = app.config["WEEKLY_MODE"]
OPTIONS = app.config["OPTIONS"]
TYPES = list(OPTIONS.keys())


@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for("vogt", type=TYPES[0]))


@app.route('/<type>', methods=['GET', 'POST'])
@login_required
def vogt(type):
    user = g.user

    if type not in TYPES:
        flash('Unknown type: "{}".'.format(type))
        return redirect(url_for("index"))

    toggle = TYPES[(TYPES.index(type) + 1) % len(TYPES)]
    options = OPTIONS[type]

    title = "{} Day Voter!".format(type.capitalize())

    vogts = User.query.get(user.id).vogts.filter_by(type=type).all()

    class CurrentVogtForm(VogtForm):
		# Must be different form for games and lunch, otherwise it might be
		# populated with one, then if the user switches be populated with the
		# other, resulting in a bunch of hidden, invalid values that don't
		# validate.
        pass

    categories = None
    if isinstance(options, dict):
        categories = options
        options = [item for cat in categories for item in categories[cat]]

    for option in options:
        if vogts:
            field = IntegerRangeField(option,
                    default=User.query.get(user.id).vogts.filter_by( \
                    type=type, option=option).first().score,
                    validators=[NumberRange(min=0, max=100)])
        else:
            field = IntegerRangeField(option, default=50,
                    validators=[NumberRange(min=0, max=100)])

        setattr(CurrentVogtForm, option, field)

    form = CurrentVogtForm()

    if form.is_submitted():
        print "Form submitted. Validating..."

        if form.validate_on_submit():
            print "Submitting {}!".format(form)

            for option in options:
                v = Vogt(type=type, option=option, user_id=user.id,
                         score=form.__getattribute__(option).data)
                db.session.add(v)

            db.session.commit()
            return redirect(url_for("vogt", type=type))
        else:
            print "Unable to validate."
            print "Errors: {}".format(form.errors)
 
    winners = []
    if vogts:
		if WEEKLY_MODE:
			winners = weekly_winners(type)
		else:
			winners = determine_winners(type, RUNNERS_UP + 1)

    if categories:
        template = "complex_ballot.html"
        options = categories
    else:
        template = "simple_ballot.html"

    return render_template(template, title=title, user=user, type=type,
                           options=options, form=form, winner=winners,
                           weekly=WEEKLY_MODE, toggle=toggle)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/clear')
@login_required
def clear():
    user = g.user
    if user.is_admin():
        clear_vogts()
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))

    form = LoginForm()

    if request.method == 'GET':
        return render_template('login.html', title="Log In", form=form)

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        try:
            print "Logging in..."
            user = authenticate(username, password)
        except ldap.INVALID_CREDENTIALS:
            user = None

        if not user:
            print "Login failed."
            flash("Login failed.")
            return render_template('login.html', title="Log In", form=form)

        if user and user.is_authenticated():
            db_user = User.query.get(user.id)
            if db_user is None:
                db.session.add(user)
                db.session.commit()

            login_user(user, remember=form.remember.data)

            return redirect(request.args.get('next') or url_for('index'))

    return render_template('login.html', title="Log In", form=form)


@lm.user_loader
def load_user(id):
    return User.query.get(id)


@app.before_request
def before_request():
    g.user = current_user


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

def clear_vogts():
    Vogt.query.delete()
    db.session.commit()
