from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, PasswordField, FileField
from wtforms.validators import DataRequired, Length, ValidationError, Email

from Models import User
from run import photos


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
    email = StringField('E-mail', validators=[DataRequired(), Email()])


class UploadForm(FlaskForm):
    file = FileField('file', validators=[DataRequired(), FileAllowed(photos, u'Images only!')])
    upload = SubmitField('Upload')
