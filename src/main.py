from getopt import getopt
from sys import argv
from api.flask_app import FlaskApp
from robots.robot_enum import RobotEnum
from movebank.movebank import RobotTableEnum


if __name__ == "__main__":
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
                    robot_type = RobotEnum.KINOVA
            elif name in ['-t', '--table']:
                if value == '1':
                    robot_table = RobotTableEnum.KINOVA
                else:
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
