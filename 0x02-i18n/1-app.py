#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask
from flask import render_template
from flask_babel import Babel


class Config(object):
    """
    class that has a LANGUAGES class attribute equal to ["en", "fr"].
    sets Babel’s default locale ("en") and timezone ("UTC").
    A config for the flask app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """Renders a basic html template"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
