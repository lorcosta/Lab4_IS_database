import os

from email_validator import validate_email
from form import SignUp, SignIn, UploadForm
from flask import render_template, redirect, session
from flask_mail import Message
from Models import User, Role
from run import db, bcrypt, mail#, photos


def apply_routing(app):
    @app.before_first_request
    def setup_db():
        db.create_all()
        if not Role.query.filter_by(authorisation='admin').first() or not Role.query.filter_by(authorisation='user').first():
            role_teacher = Role(name='teacher', authorisation='admin')
            role_student = Role(name='student', authorisation='user')
            with app.app_context():
                db.session.add_all([role_teacher, role_student])
        db.session.commit()

    @app.route('/signup', methods=['POST', 'GET'])
    def signup():
        sign_up = SignUp()
        if sign_up.validate_on_submit():
            validate_email(sign_up.email.data)
            sign_up.validate_email(sign_up.email.data)
            sign_up.validate_username(sign_up.username.data)
            password_crypt = bcrypt.generate_password_hash(sign_up.password.data).encode('utf-8')
            new_user = User(username=sign_up.username.data, name=sign_up.name.data, email=sign_up.email.data,
                            password=password_crypt, role_id=2)
            db.session.add(new_user)
            session['name'] = new_user.name
            session['username'] = new_user.username
            session['email'] = new_user.email
            db.session.commit()
            send_mail(sign_up.email.data, 'You have successfully registered!', 'mail', user='lorenzo')
            return redirect('user')
        return render_template('signup.html', signUp=sign_up, title='Sign Up')

    @app.route('/sign_in', methods=['POST', 'GET'])
    def signin():
        sign_in = SignIn()
        # TODO seems the form is never valid
        print 'not validating'
        if sign_in.validate_on_submit():
            print 'validating'
            print sign_in.password.data
            print sign_in.email.data
            user_info = User.query.filter_by(email=sign_in.email.data).first()
            print user_info
            if user_info and bcrypt.check_password_hash(user_info.password, sign_in.password.data):
                print sign_in.password.data
                print sign_in.email.data
                session['name'] = user_info.name
                session['username'] = user_info.email
                session['email'] = user_info.email
                session['logged'] = True
                return redirect('user')
            else:
                # TODO error in logging in
                return True
        return render_template('sign_in.html', title='Sign In')

    @app.route('/home')
    def home():
        if not session.get('logged') is None and session.get('logged') is False:
            return redirect('user')
        else:
            return render_template('home.html', title='Homepage')

    @app.route('/user')
    def user():
        if session.get('logged') is True:
            if not session.get('name') is None and not session.get('username') is None and not session.get('email') is None:
                name = session.get('name')
                username = session.get('username')
                email = session.get('email')
                return render_template('user.html', title='Your data', name=name, username=username, email=email)
        else:
            return redirect('home')

    def send_mail(to, subject, template, **kwargs):
        msg = Message(subject,
                      recipients=[to],
                      sender=app.config['MAIL_USERNAME'])
        msg.body = render_template(template + '.txt', **kwargs)
        # msg.html = render_template(template + '.html', **kwargs)
        mail.send(msg)

    @app.route('/upload', methods=["POST", "GET"])
    def upload():
        if not os.path.exists('static/' + str(session.get('id'))):
            os.makedirs('static/' + str(session.get('id')))
        file_url = os.listdir('static/' + str(session.get('id')))
        file_url = [str(session.get('id')) + "/" + file for file in file_url]
        form_upload = UploadForm()
        print session.get('email')
        '''if form_upload.validate_on_submit():
            filename = photos.save(form_upload.file.data, name=str(session.get('id')) + '.jpg',
                                   folder=str(session.get('id')))
            file_url.append(filename)'''
        return render_template("upload.html", form_upload=form_upload, filelist=file_url)

    return app
