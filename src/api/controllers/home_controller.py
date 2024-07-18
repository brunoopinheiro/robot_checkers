from flask import Blueprint, render_template


home_controller = Blueprint('home_controller', __name__)


@home_controller.route('/', methods=['GET'])
def index():
    return render_template('index.html')
