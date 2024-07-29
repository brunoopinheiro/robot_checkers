from flask import Flask
from waitress import serve
from api.controllers.home_controller import home_controller
from api.controllers.robot_controller import robot_controller


class FlaskApp:

    def __init__(
        self,
        debug: bool = False,
    ) -> None:
        self.__app = Flask(__name__)
        # a lot of things here
        self.__register_template()
        self.__register_blueprints()
        if debug:
            self.debug_server()
        else:
            self.start_server()

    def __register_template(self) -> None:
        self.__app.static_folder = 'api/views/static'
        self.__app.template_folder = 'api/views/template'

    def __register_blueprints(self) -> None:
        self.__app.register_blueprint(
            robot_controller,
            url_prefix='/robot',
        )
        self.__app.register_blueprint(
            home_controller,
            url_prefix='/',
        )

    def debug_server(self) -> None:
        self.__app.run(
            debug=True,
            host='0.0.0.0',
            port='5000',
        )

    def start_server(self) -> None:
        serve(
            self.__app,
            host='0.0.0.0',
            port='5000',
        )


if __name__ == "__main__":
    app = FlaskApp(
        debug=True,
    )
