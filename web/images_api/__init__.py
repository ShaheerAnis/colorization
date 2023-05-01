from flask import Blueprint

images_blueprint = Blueprint('images_blueprint', __name__)

from . import images_api
