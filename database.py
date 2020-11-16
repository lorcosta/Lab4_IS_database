from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import os
from database import User, Role

app = Flask(__name__)
db = SQLAlchemy(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = 'qwertyuiopasdfghjklzxcvbnm'
from form import SignUp


@app.before_first_request
def setup_db():
    """user_role = Role(role='User')
    db.session.add(User(username='susan', role=user_role))"""

    user_instance = User(name='susan')
    user_from_db = User.query.filter_by(name='lorenzo').first()
    with app.push_context():
        db.session.add(user_instance)
        user_instance.role = Role(authorisation='moderator')
        user_from_db.Role(authorisation='admin')
        db.session.commit()
    for role in Role.query.filter_by(authorisation='admin').all():
        print(User.query.get(role.users.id))  # prints all the admins
    for role in Role.query.filter_by(authorisation='moderators').all():
        print(User.query.get(role.users.id))  # prints all the moderators
    db.create_all()


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    signUp = SignUp()
    if signUp.validate_on_submit():
        return redirect('database_content')
    return render_template('signup.html', signUp=signUp)


@app.route('/content')
def database_content():
    User.query.all()
    return render_template('databaseContent.html')


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(30))
    password = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


def __repr__(self):
    return '<User %r>' % self.username


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    users = db.relationship('User', backref='role')


if __name__ == '__main__':
    app.run(debug=True)
