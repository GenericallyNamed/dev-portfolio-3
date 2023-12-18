"""Builds the landing page for the portfolio app."""

from flask import render_template
import portfolio

@portfolio.app.route('/')
def show_landing():
    """Builds the landing page."""
    return render_template('landing.html')