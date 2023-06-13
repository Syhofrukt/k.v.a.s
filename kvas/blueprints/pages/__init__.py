from flask import Blueprint
from .main import main_blueprint
from .login import login_blueprint
from .core import core_blueprint

pages_blueprint = Blueprint("pages_blueprint", __name__, url_prefix="/")
pages_blueprint.register_blueprint(main_blueprint)
pages_blueprint.register_blueprint(login_blueprint)
pages_blueprint.register_blueprint(core_blueprint)