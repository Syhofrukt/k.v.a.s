from flask import Flask, render_template, request, redirect, url_for
from blueprints.api import api_blueprint
from blueprints.pages import pages_blueprint


app = Flask(__name__)
app.register_blueprint(api_blueprint)
app.register_blueprint(pages_blueprint)
app.secret_key = 'bebrivsekrutie99'


if __name__ == "__main__":
    app.run(debug=True)
