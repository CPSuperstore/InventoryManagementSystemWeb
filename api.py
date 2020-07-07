from flask import Blueprint

from InventoryManagementSystemWeb.database import conn, c, d, get_table_id

app = Blueprint('api', __name__, template_folder='templates')

@app.route("/")
def index():
    return "API Not Implemented."

