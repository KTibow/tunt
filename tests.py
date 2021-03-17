"""The test program for Tunt."""

import requests


def test_homepage_content():
    """
    Get the content of the home page, and compare it with the actual HTML file.
    This helps guard against general errors, 404, 500, and more errors.
    """
    with open("assets/home.html") as original_page:
        home = requests.get("http://127.0.0.1:5000/")
        assert home.text == original_page.read()
