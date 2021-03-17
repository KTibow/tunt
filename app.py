"""Server program for Tunt."""

from flask import Flask, Response
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


@app.route("/css/<css_file_name>")
def send_css_file(css_file_name):
    """Return a CSS file.

    Args:
        css_file_name: The name of the CSS file.

    Returns:
        The CSS file specified in the URL.
    """
    with open(f"assets/css/{css_file_name}") as css_file:
        return Response(css_file.read(), mimetype="text/css")


if os.getenv("GITHUB_ACTIONS") is not None:
    flask_logger = logging.getLogger("werkzeug")
    flask_logger.setLevel(logging.ERROR)
