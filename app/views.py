from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import NumberRange

from app import app, db, lm, oid
from forms import LoginForm, VogtForm
from models import User, Vogt


all_options = app.config["OPTIONS"]
types = list(all_options.keys())


@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for("vogt", type=types[0]))


@app.route('/<type>', methods=['GET', 'POST'])
@login_required
def vogt(type):
    user = g.user

    if type not in types:
        flash('Unknown type: "{}".'.format(type))
        return redirect(url_for("index"))

    toggle = types[(types.index(type) + 1) % len(types)]
    options = all_options[type]

    title = "{} Day Voter!".format(type.capitalize())

    vogts = User.query.get(user.id).vogts.filter_by(type=type).all()

    for option in options:
        if vogts:
            field = IntegerRangeField(option,
                    default=User.query.get(user.id).vogts.filter_by(type=type,
                    option=option).first().score,
                    validators=[NumberRange(min=0, max=100)])
        else:
            field = IntegerRangeField(option,
                    validators=[NumberRange(min=0, max=100)])

        setattr(VogtForm, option, field)

    form = VogtForm()

    if form.validate_on_submit():
        print "Submitting {}!".format(form)
        for option in options:
            v = Vogt(type=type, option=option,
                     score=form.__getattribute__(option).data, user_id=user.id)
            db.session.add(v)
        db.session.commit()
        return redirect(url_for("vogt", type=type))
 
    winner = None
    if vogts:
        winner = determine_winner(type)

    return render_template("vogt.html", title=title, user=user, type=type,
                           options=options, form=form, winner=winner,
                           toggle=toggle)


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html', title='Log In', form=form,
                           providers=app.config['OPENID_PROVIDERS'],
                           num_providers=len(app.config['OPENID_PROVIDERS']))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/clear')
@login_required
def clear():
    user = g.user
    if user.admin:
        clear_vogts()
    return redirect(url_for('index'))


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        name = resp.nickname
        if name is None or name == "":
            name = resp.email.split('@')[0]
        user = User(name=name, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))


def determine_winner(type):
    vogts = Vogt.query.filter_by(type=type)
    totals = {v.option: sum([v1.score for v1 in vogts if v1.option == v.option]) for v in vogts}
    print "Totals: {}".format(totals)
    return max(totals, key=totals.get)


def clear_vogts():
    Vogt.query.delete()
    db.session.commit()
