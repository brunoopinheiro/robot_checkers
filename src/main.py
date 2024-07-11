from robots.irobot import IRobot
from robots.kinova_robot import KinovaRobot
# add the robot controller
from utils.emergency_stop import EmergencyStop


def get_positions(robot: IRobot):
    doc_name = 'positions_kinova.txt'
    robot.connect()

    conditions = True
    try:
        doc_file = open(doc_name)
        doc_file.close()
    except FileNotFoundError:
        with open(doc_name, 'a+') as doc_file:
            doc_file.write('Position\tType\tJoints\n')

    while conditions:
        choice = input('Digite o nome da posição ou Q(q) para sair do programa:\n')
        if choice.upper() == "Q":
            conditions = False
        else:
            joint_pos = robot.get_joints()
            cart_pos = robot.get_cartesian()

            print(f'JOINTS: {joint_pos}')
            print(f'CART: {cart_pos}')
            with open(doc_name, 'a+') as doc_file_:
                doc_file_.write(f'{choice}\tjoints\t{joint_pos}')
                doc_file_.write(f'{choice}\cartesian\t{cart_pos}')


def robot_choice() -> IRobot:
    kinova = KinovaRobot()
    return kinova


def main():
    print('Projeto - Fábrica de Software 2')
    robot = robot_choice()
    # add the robot controller
    emergency_stop = EmergencyStop(robot)
    emergency_stop.initiate_emergency_stop()
    # THIS WILL BECOME A MENU LATER ON
    get_positions(robot)


if __name__ == '__main__':
    main()
