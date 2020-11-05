from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.config['SECRET_KEY']='ASDFGHJKLPOIUYTREWQAZXCVBNHJUIOPIYTRDS'

from form import FormTest


@app.route('/registration', methods=['GET', 'POST'])
def index():
    name = None
    email = None
    surname = None
    form = FormTest()
    if form.validate_on_submit():
        name = form.name.data
        session['name'] = form.name.data
        email = form.email.data
        surname = form.surname.data
    return render_template('registration.html', formTest=form, name=name)


@app.route('/dashboard')
def dashboard():
    if session.get('name'):
        return render_template('dashboard.html')
    else:
        return redirect('registration')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('index')


if __name__ == '__main__':
    app.run()
