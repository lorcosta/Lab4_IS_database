from flask import Flask, render_template

app = Flask(__name__)

names = ['Andrea', 'Elena', 'Edoardo', 'Francesco']

@app.route('/user/<id>')
def name(id):
    id=int(id)
    if id > len(names):
        return render_template('404.html'), 404
    return render_template('student.html', id=id, name=names[id])


if __name__ == '__main__':
    app.run(debug=True)
