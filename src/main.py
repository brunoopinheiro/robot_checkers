from getopt import getopt
from sys import argv
from api.flask_app import FlaskApp
from robots.robot_enum import RobotEnum
from movebank.movebank import RobotTableEnum


if __name__ == "__main__":
    try:
        cli_args = argv[1:]
        debug_mode = False
        robot_type = None
        robot_table = None
        options, args = getopt(
            cli_args,
            'd:r:t:',
            ['debug=', 'robot=', 'table='],
        )
        for name, value in options:
            if name in ['-d', '--debug']:
                if value.upper() == 'TRUE':
                    # -d True
                    # --debug True
                    print('Running in Debug Mode')
                    debug_mode = True
                else:
                    print('Running in Production Mode')
                    debug_mode = False
            elif name in ['-r', '--robot']:
                if value.upper() == 'TEST':
                    robot_type = RobotEnum.TEST
                else:
                    robot_type = RobotEnum.KINOVA
            elif name in ['-t', '--table']:
                if value == '1':
                    robot_table = RobotTableEnum.KINOVA
                else:
                    robot_table = RobotTableEnum.KANOVA
        # later should allow for selecting robot and table
    except Exception as e:
        print('Parsing Error: ', e)
    finally:
        app = FlaskApp(
            debug=debug_mode,
            robot_type=robot_type,
            robot_table=robot_table,
        )
