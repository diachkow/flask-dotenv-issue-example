import flask

import settings
from routes import home


app = flask.Flask(__name__)

app.register_blueprint(home.blueprint)


if __name__ == '__main__':
    app.run(
        host=settings.HOST,
        port=settings.PORT,
        debug=settings.DEBUG,
        load_dotenv=False
    )
