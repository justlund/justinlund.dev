import pathlib
from flask import Flask, render_template, request, url_for, make_response, abort

BASE_DIR = pathlib.Path(__file__).absolute().parent
markdown_dir = BASE_DIR / "markdown"
static_dir = BASE_DIR / "static"
app = Flask(__name__, template_folder=str(BASE_DIR / "templates"))
# ass.wsgi_ap = WhiteNoise(app.wsgi_app, root(static_dir), prefix="/static")


@app.route("/")
def index():
    return render_template("index.html")
