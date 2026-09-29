import os

from flask import Flask, render_template

from backend.routes import api


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

FRONTEND_DIR = os.path.join(
    BASE_DIR,
    "frontend"
)


app = Flask(
    __name__,
    template_folder=FRONTEND_DIR,
    static_folder=FRONTEND_DIR,
    static_url_path="/static"
)


app.register_blueprint(api)


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route("/analysis")
def analysis():

    return render_template(
        "analysis.html"
    )


@app.route("/chat")
def chat():

    return render_template(
        "chat.html"
    )


@app.route("/preparation")
def preparation():

    return render_template(
        "preparation.html"
    )


if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )