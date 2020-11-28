from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FileField
from wtforms.validators import DataRequired, Length, ValidationError, Email

from Models import User


class SignUp(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=25)])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    submit = SubmitField('Save')

    def validate_email(self, email):
        user_check = User.query.filter_by(email=self.email.data).first()
        if user_check:
            raise ValidationError('This email (%s) is already registered' % self.email.data)

    def validate_username(self, username):
        user_check = User.query.filter_by(username=self.username.data).first()
        if user_check:
            raise ValidationError('This username (%s) is not available' % self.username.data)


class SignIn(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField('Email address', validators=[DataRequired(), Email()])
    submit = SubmitField('Login')


class UploadForm(FlaskForm):
    file = FileField('File', validators=[DataRequired()])
    upload = SubmitField('Upload')
