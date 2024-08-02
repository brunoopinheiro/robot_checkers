from flask import Blueprint, render_template


def construct_home_blueprint() -> Blueprint:

    home_controller = Blueprint('home_controller', __name__)

    @home_controller.errorhandler(404)
    def not_found():
        return render_template('notfound.html')

    @home_controller.route('/', methods=['GET'])
    def index():
        return render_template('index.html')

    @home_controller.route('/docs', methods=['GET'])
    def api_docs():
        return render_template('api_doc.html')

    return home_controller
