"""Server program for Tunt."""

from flask import Flask
import os
import logging
import template

app = Flask(__name__)


@app.route("/")
def render_home_page():
    """Return the HTML of the home page.

    Returns:
        The HTML of the home page.
    """
    with open("assets/home.yaml") as home_page:
        return template.compile_template(home_page)


@app.route("/css/<file>")
def send_css_file(file):
    """Return a CSS file.

    Args:
        file: The name of the CSS file.

    Returns:
        The CSS file specified in the URL.
    """
    with open(f"assets/css/{file}") as css_file:
        return css_file.read()


if os.getenv("GITHUB_ACTIONS") is not None:
    flask_logger = logging.getLogger("werkzeug")
    flask_logger.setLevel(logging.ERROR)
