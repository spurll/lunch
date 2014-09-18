from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import NumberRange
import ldap

from lunch import app, db, lm
from forms import LoginForm, VogtForm
from models import User, Vogt
from authenticate import authenticate
from util import determine_winner, determine_winners, weekly_winners, vogt_totals, clear_vogts


RUNNERS_UP = app.config["RUNNERS_UP"]
WEEKLY_MODE = app.config["WEEKLY_MODE"]
OPTIONS = app.config["OPTIONS"]
TYPES = list(OPTIONS.keys())


@app.route('/')
@app.route('/index')
def index():
    print "Blah!"
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
        default = 50
        ballot = User.query.get(user.id).vogts.filter_by(type=type,
                 option=option).first()
        if ballot: default = ballot.score

        field = IntegerRangeField(option, default=default,
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

    vogters = filter(lambda u: u.vogts.all(), User.query.all())
    return render_template(template, title=title, user=user, type=type,
                           options=options, form=form, winner=winners,
                           weekly=WEEKLY_MODE, vogters=vogters, toggle=toggle)


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

