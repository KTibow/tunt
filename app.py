"""Server program for Tunt."""

from flask import Flask
import os
import logging
import template
import mimetypes

# All range request imports
from datetime import datetime
from flask_rangerequest import RangeRequest

app = Flask(__name__)
server_boot_time = datetime.utcnow()


@app.route("/")
def render_home_page():
    """Return the HTML of the home page.

    Returns:
        The HTML of the home page.
    """
    with open("assets/home.yaml") as home_page:
        return template.compile_template(home_page)


@app.route("/new_game/")
def render_new_game_page():
    """Return the HTML of the game creation page.

    Returns:
        The HTML of the game creation page.
    """
    with open("assets/new_game.yaml") as new_game_page:
        return template.compile_template(new_game_page)


@app.route("/asset/<path:asset_file_name>")
def send_asset(asset_file_name):
    """Return an asset.

    Args:
        asset_file_name: The path of the asset file relative to the assets folder.

    Returns:
        The asset specified in the URL.
    """
    asset_path = f"assets/{asset_file_name}"
    asset_size = os.path.getsize(asset_path)
    with open(asset_path, "rb") as asset_file:
        asset_etag = RangeRequest.make_etag(asset_file)
    asset_response = RangeRequest(
        open(asset_path, "rb"),  # noqa: WPS515
        etag=asset_etag,
        last_modified=server_boot_time,
        size=asset_size,
    ).make_response()
    asset_response.mimetype = mimetypes.guess_type(asset_file_name)[0]
    return asset_response


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
