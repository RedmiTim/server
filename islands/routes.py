from flask import Blueprint

blueprint = Blueprint('islands', __name__)


@blueprint.get('')
def get_user_islands():
    pass
