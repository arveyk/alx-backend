#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel
import pytz
from babel.dates import get_ti


app = Flask(__name__, template_folder='templates')
# babel = Babel(app, locale_selector=get_locale)
babel = Babel(app)

class Config:
    LANGUAGE = ["en", "fr"]
    utc = pytc.utc

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(config['LANGUAGES'])

@app.rounte('/')
def index():
    return render_template('1-index.html')
