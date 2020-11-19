from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

from routes import apply_routing
app = apply_routing(app=Flask(__name__))
db = SQLAlchemy(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = 'qwertyuiopasdfghjklzxcvbnm'

# from routes import apply_routing
app = apply_routing(app)

if __name__ == '__main__':
    apply_routing(app).run(debug=True)