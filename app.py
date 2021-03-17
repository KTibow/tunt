from flask import Flask

app = Flask(__name__)


@app.route("/")
def render_home_page():
    return "Hello."
