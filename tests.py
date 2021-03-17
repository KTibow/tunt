"""The test program for Tunt."""

import requests


def test_homepage_content():
    """Verifies the content of the homepage.

    Get the content of the home page, and make sure it includes "Tunt".
    This helps guard against general errors, 404, 500, and more errors.
    """
    home = requests.get("http://127.0.0.1:5000/")
    assert "Tunt" in home.text
