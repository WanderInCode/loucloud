from flask import Flask
from .config import DefaultConfig
from .extension import login_manager, db, cache
from .frontend import frontend
from .user import User, user
from .host import host
from .image import image
from .template import template
from .vm import vm
# from .image import image
# from .template import template
# from .vm import vm
app = Flask(__name__)
app.config.from_object(DefaultConfig)
# register blueprints
app.register_blueprint(frontend)
app.register_blueprint(host)
app.register_blueprint(user)
app.register_blueprint(image)
app.register_blueprint(template)
app.register_blueprint(vm)
# app.register_blueprint(image)
# app.register_blueprint(template)
# app.register_blueprint(vm)
# Config SQLAlchemy object
# flask-sqlalchemy
db.init_app(app)
# Update Flask-Login config
cache.init_app(app)
login_manager.login_view = 'frontend.login'

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

login_manager.setup_app(app)
