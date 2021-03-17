"""Server program for Tunt."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def render_home_page():
    """Returns the HTML of the home page."""
    with open("assets/home.html") as home_page:
        return home_page.read()
