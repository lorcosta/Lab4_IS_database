from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
from form import SignUp

@app.before_first_request
def setup_db():
    user_role = Role(name='User')
    user_susan = User(username='susan', role=user_role)
    db.session.add_all([user_susan])
    db.create_all()


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    signUp = SignUp()
    if signUp.validate_on_submit():
        return redirect('database_content')
    return render_template('signup.html')


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
    app.run()
