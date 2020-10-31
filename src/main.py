import flask

from routes import home


app = flask.Flask(__name__)

app.register_blueprint(home.blueprint)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
