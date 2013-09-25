from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required, NumberRange


class LoginForm(Form):
    openid = TextField("openid", validators=[Required()])
    remember_me = BooleanField("remember_me", default=False)


class VogtForm(Form):
    pass
