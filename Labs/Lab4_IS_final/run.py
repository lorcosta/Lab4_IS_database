
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = 'qwertyuiopasdfghjklzxcvbnm'
app.config['MAIL_SERVER'] = 'smtp.mail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ['EMAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['EMAIL_PASSWORD']
mail = Mail(app)
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)


if __name__ == '__main__':
    from routes import apply_routing
    apply_routing(app).run(debug=True)
