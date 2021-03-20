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


@app.route("/asset/<path:asset_file_name>")
def send_asset(asset_file_name):
    """Return an asset.

    Args:
        asset_file_name: The path of the asset file relative to the assets folder.

    Returns:
        The asset specified in the URL.
    """
    with open(f"assets/{asset_file_name}") as asset_file:
        mime_type = mimetypes.guess_type(asset_file_name)[0]
        return Response(asset_file.read(), mimetype=mime_type)


http_internal_server_error = 500
http_not_found_error = 404


@app.errorhandler(http_internal_server_error)
def render_server_error(_):
    """Return the HTML of the 500 error page.

    Returns:
        The HTML of the 500 error page.
    """
    with open("assets/500.yaml") as error500_page:
        return template.compile_template(error500_page), 500


@app.errorhandler(http_not_found_error)
def render_not_found_error(_):
    """Return the HTML of the 404 error page.

    Returns:
        The HTML of the 404 error page.
    """
    with open("assets/404.yaml") as error404_page:
        return template.compile_template(error404_page), 404


if os.getenv("GITHUB_ACTIONS") is not None:
    flask_logger = logging.getLogger("werkzeug")
    flask_logger.setLevel(logging.ERROR)
