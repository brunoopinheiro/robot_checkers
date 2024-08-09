from getopt import getopt
from sys import argv
from api.flask_app import FlaskApp
from robots.robot_enum import RobotEnum
from movebank.movebank import RobotTableEnum


if __name__ == "__main__":
    """Application entrypoint.
    Uses the getopt module to parse the options
    used to initiate the application.

    `--robot` or `-r`: determines the robot used
    in the system. The value `kinova` indicates
    that the physical robot should be used. Other
    values are treated as indication that the
    `Test` robot should be used. Defaults to `Test`

    `--table` or `-t`: determines which of the
    position references should be used for the robots,
    based on the table the physical robots are located.
    The values are `1` or `2`. `1` indicates the
    table next to entry door. Defaults to `2`.

    `--debug` or `-d`: determines the serving mode
    of the `Flask` app. If present, the `debug` mode
    for the Flask API is used, otherwise the `waitress`
    module is used to serve the application.
    """
    try:
        cli_args = argv[1:]
        debug_mode = False
        robot_type = RobotEnum.TEST
        robot_table = RobotTableEnum.KANOVA
        options, args = getopt(
            cli_args,
            'r:t:d',
            ['robot=', 'table=', 'debug'],
        )
        for name, value in options:
            if name in ['-r', '--robot']:
                if value.upper() == 'TEST':
                    robot_type = RobotEnum.TEST
                else:
                    print('Kinova Robot')
                    robot_type = RobotEnum.KINOVA
            elif name in ['-t', '--table']:
                if value == '1':
                    print('Table 1')
                    robot_table = RobotTableEnum.KINOVA
                else:
                    print('Table 2')
                    robot_table = RobotTableEnum.KANOVA
            elif name in ['-d', '--debug']:
                print('Running in Debug mode')
                debug_mode = True
    except Exception as e:
        print('Parsing Error: ', e)
    finally:
        app = FlaskApp(
            debug=debug_mode,
            robot_type=robot_type,
            table=robot_table,
        )
