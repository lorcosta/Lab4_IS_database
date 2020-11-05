from wtforms import SubmitField, StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length


class FormTest(FlaskForm):
    email = StringField('Email:', validators=[DataRequired()])
    surname = StringField('Surname:', validators=[DataRequired(), Length(min=3, max=20)])
    name = StringField('Name:', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password:', validators=[DataRequired(), Length(min=3, max=25)])
    submit = SubmitField('Send')
