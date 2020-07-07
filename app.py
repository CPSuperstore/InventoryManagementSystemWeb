from flask import Flask, render_template

from InventoryManagementSystemWeb.api import app as api
from InventoryManagementSystemWeb.filters import app as filters
from InventoryManagementSystemWeb.security import SECRET_KEY

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(filters)

@app.context_processor
def inject_dict_for_all_templates():
    return {
        "development": False
    }


@app.route("/")
def index():
    return render_template("index.twig")

