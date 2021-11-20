from flask import Flask
from flask_bootstrap import Bootstrap
from flask_simplemde import SimpleMDE
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import config_options
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_simplemde import SimpleMDE
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


bootstrap = Bootstrap()
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.session_protection = 'strong'
login_manager.login_message_category = 'info'
mail = Mail()
simple = SimpleMDE()
admin = Admin()
photos = UploadSet('photos', IMAGES)
bootstrap = Bootstrap()
bootstrap = Bootstrap()




def create_app(config_name):
     app = Flask(__name__)

     app.config.from_object(config_options[config_name])
     #Initializing Flask Extensions
     bootstrap.init_app(app)
     db.init_app(app)
     login_manager.init_app(app)
     mail.init_app(app)
     simple.init_app(app)
     admin.init_app(app)

     from app.auth.views import auth
     app.register_blueprint(auth)

     from app.main.views import main
     app.register_blueprint(main)

     # from .main import main as main_blueprint
     # app.register_blueprint(main_blueprint)

     # from .auth import auth as auth_blueprint
     # app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

     return app
