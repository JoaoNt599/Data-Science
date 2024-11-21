from flask import (
    Blueprint, render_template
)

bp = Blueprint('home', __name__)


@bp.route('/', methods=['GET'])
def index():
    return render_template("chart.html")

