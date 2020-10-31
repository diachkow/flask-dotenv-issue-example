import flask


blueprint = flask.Blueprint('home', __name__)


@blueprint.route('/', methods=['GET'])
def homepage():
    return 'Hello, world!', 200
