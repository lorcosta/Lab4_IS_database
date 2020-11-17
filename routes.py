from form import SignUp
from run import app, db
from flask import render_template, redirect
from Models import User, Role


@app.before_first_request
def setup_db():
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
    sign_up = SignUp()
    if sign_up.validate_on_submit():
        return redirect('database_content')
    return render_template('signup.html', signUp=sign_up)


@app.route('/content')
def database_content():
    User.query.all()
    return render_template('databaseContent.html')
