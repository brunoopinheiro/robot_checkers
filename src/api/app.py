from flask import Flask, render_template
from waitress import serve


from controllers.home_controller import home_controller


app = Flask(__name__)
app.static_folder = 'views/static'
app.template_folder = 'views/template'
app.register_blueprint(home_controller, url_prefix='/')


@app.errorhandler(404)
def page_not_found(e):
    """Basic `Flask` template function to render a Not Found template
    when the API returns Status Code 404."""
    print(e)
    return render_template('notfound.html'), 404


def debug_server() -> None:
    return app.run(
        debug=True,
        host='0.0.0.0',
        port='5000',
    )


def start_server() -> None:
    serve(app, host='0.0.0.0', port='5000')


if __name__ == "__main__":
    debug_server()
