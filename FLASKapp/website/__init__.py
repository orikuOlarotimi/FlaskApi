# import mongoengine
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager

db = MongoEngine()
DB_URI = 'mongodb+srv://olarotimi:Dickfish1.@cluster0.elfv34i.mongodb.net/API?retryWrites=true&w=majority'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'timi1ka'
    app.config['MONGODB_HOST'] = DB_URI
    db.init_app(app)
    db.connect(host=DB_URI)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    from .models import User, Note

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.objects(pk=user_id).first()

    return app
