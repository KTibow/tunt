import requests


def test_homepage_content():
    home = requests.get("http://127.0.0.1:5000/")
    original_page = open("assets/home.html")
    assert home.text == original_page.read()
    original_page.close()
