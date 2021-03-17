"""Server program for Tunt."""

from flask import Flask
import os, logging
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

if os.getenv("GITHUB_ACTIONS") is not None:
    flask_logger = logging.getLogger("werkzeug")
    flask_logger.setLevel(logging.ERROR)
