"""Server program for Tunt."""

from flask import Flask, Response
import os
import logging
import template
import mimetypes

app = Flask(__name__)


@app.route("/")
def render_home_page():
    """Return the HTML of the home page.

    Returns:
        The HTML of the home page.
    """
    with open("assets/home.yaml") as home_page:
        return template.compile_template(home_page)


@app.route("/asset/<asset_file_name>")
def send_asset(asset_file_name):
    """Return an asset.

    Args:
        asset_file_name: The path of the asset file relative to the assets folder.

    Returns:
        The asset specified in the URL.
    """
    with open(f"assets/{asset_file_name}") as asset_file:
        mime_type = mimetypes.guess_type(asset_file_name)
        return Response(asset_file.read(), mimetype=mime_type)


if os.getenv("GITHUB_ACTIONS") is not None:
    flask_logger = logging.getLogger("werkzeug")
    flask_logger.setLevel(logging.ERROR)
