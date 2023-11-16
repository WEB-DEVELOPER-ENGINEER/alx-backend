#!/usr/bin/env python3
"""Mock logging in"""
from typing import (
    Dict, Union
)
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """App configuration class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@babel.localeselector
def get_locale() -> str:
    """Gets locale from request object"""
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[Dict[str, Union[str, None]], None]:
    """
    Validate user login details
    Args:
        id (str): user id
    Returns:
        (Dict): user dictionary or None if the ID not found or
                if login_as was not passed.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request():
    """use get_user to find a user if any,
    and set it as a global on flask.g.user"""
    setattr(g, 'user', get_user())


@app.route('/', strict_slashes=False)
def index() -> str:
    """Renders a basic html template"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
