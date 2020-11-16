from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length


class SignUp(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=25)])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=25)])
    submit = SubmitField('Save')
