"""Initializer for the Flask server."""
#import flask
from flask import Flask

# Path: src/__init__.py
app = Flask(__name__)

# Tell the app about the views.
import portfolio.views # noqa: E402  pylint: disable=wrong-import-position
