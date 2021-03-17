"""Server program for Tunt."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def render_home_page():
    """Returns the HTML of the home page."""
    with home_page as open("assets/home.html"):
        return home_page.read()
