from robots.irobot import IRobot
from robots.kinova_robot import KinovaRobot
from robots.test_robot import TestRobot
from controller.robot_controller import RobotController
from utils.emergency_stop import EmergencyStop
from movebank.movebank import MoveBank


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
        choice = input('Nome da posição ou Q(q) para sair do programa:\n')
        if choice.upper() == "Q":
            conditions = False
        else:
            joint_pos = robot.get_joints()
            cart_pos = robot.get_cartesian()

            print(f'JOINTS: {joint_pos}')
            print(f'CART: {cart_pos}')
            with open(doc_name, 'a+') as doc_file_:
                doc_file_.write(f'{choice}\tjoints\t{joint_pos}')
                doc_file_.write(f'{choice}\tcartesian\t{cart_pos}')


def update_bank(robotcontroller: RobotController) -> None:
    _stop = False
    robotcontroller.connect()
    while not _stop:
        choice = input('Dict Key or "EXIT" to quit.: ')
        if choice.upper() == "EXIT":
            _stop = True
        else:
            robotcontroller.record_position(
                pos_key=choice
            )
    robotcontroller.disconnect()


def test_positions(robotcontroller: RobotController) -> None:
    robotcontroller.connect()
    _stop = False
    print('Test Bank: "bank_key;[C|J]"')
    print('Type "EXIT" to leave.')
    while not _stop:
        try:
            pos = input('>> ')
            if pos.upper() == "EXIT":
                _stop = True
            else:
                key, movetype = pos.split(';')
                if movetype.upper() == 'C':
                    robotcontroller._to_custom_coords(key)
                else:
                    robotcontroller._to_custom_pose(key)
        except Exception as e:
            print('Error: ', e)
    robotcontroller.disconnect()


def robot_choice() -> IRobot:
    print('== Choose a Robot ==')
    print('[1] - Kinova')
    print('[2] - Test')
    robotchoice = None
    robot = None
    while robotchoice not in [1, 2]:
        try:
            robotchoice = int(input('>> '))
        except TypeError:
            print('Invalid Robot Type')
    if robotchoice == 1:
        robot = KinovaRobot()
    if robotchoice == 2:
        robot = TestRobot()
    return robot


def capture_pieces(robotcontroller: RobotController) -> None:
    robotcontroller.connect()
    print('Informe a posição de captura, e as posições de movimento.')
    print('Ex.: A1;C3;E5')
    print('Ou digite "EXIT" para sair.')
    _stop = False
    while not _stop:
        pos_str = input('>> ')
        if pos_str.upper() == 'EXIT':
            _stop = True
        else:
            try:
                pos_list = pos_str.lower().split(';')
                print(pos_list)
                valid = robotcontroller.check_valid_keys(*pos_list)
                if valid is False:
                    print('Apenas posições das casas brancas são válidas.')
                elif len(pos_list) > 1 and valid is True:
                    robotcontroller.capture_piece(
                        origin=pos_list[0],
                        targets=pos_list[1:]
                    )
                else:
                    print('Informe ao menos 2 posições separadas por ;')
                    print('Ex.: A1;C3')
            except Exception as e:
                print('Error: ', e)
    robotcontroller.disconnect()


def remove_pieces(robotcontroller: RobotController) -> None:
    robotcontroller.connect()
    print('Informe a posição da peça a ser removida.')
    print('Ex.: E5')
    print('Digite "EXIT" para sair.')
    _stop = False
    while not _stop:
        pos = input('>> ')
        if pos.upper() == 'EXIT':
            _stop = True
        else:
            try:
                robotcontroller.remove_piece_from_board(
                    piece_location=pos,
                )
            except KeyError as err:
                print(err)
    robotcontroller.disconnect()


def place_queen(robotcontroller: RobotController) -> None:
    robotcontroller.connect()
    _stop = False
    while not _stop:
        print('Informe a posição de colocação da Dama')
        print('EX.: E1')
        print('Digite "EXIT" para sair.')
        pos = input('>> ')
        if pos.upper() == 'EXIT':
            _stop = True
        else:
            try:
                print('Informe a Rainha a ser colocada.')
                rnum = int(input('>> '))
                robotcontroller.place_queen(
                    target_location=pos,
                    queen=rnum,
                )
            except KeyError as err:
                print(err)
    robotcontroller.disconnect()


def __print_menu() -> None:
    print('== Robot Operation ==')
    print('[1] - Test Positions')
    print('[2] - Get Positions')
    print('[3] - Capture Pieces')
    print('[4] - Remove Piece')
    print('[5] - Place Queen')
    print('[0] - EXIT')


def main():
    print('Projeto - Fábrica de Software 2')
    robot = robot_choice()

    # Might become a choice if positions are not compatible
    movebank = MoveBank()
    controller = RobotController(
        robot=robot,
        movebank=movebank,
    )
    emergency_stop = EmergencyStop(robot)
    emergency_stop.initiate_emergency_stop()

    __print_menu()
    _stop = False
    menuchoice = None
    while not _stop:
        try:
            menuchoice = int(input('>> '))
        except TypeError as err:
            print('Invalid Choice ', err)
        if menuchoice == 0:
            emergency_stop.stop_thread()
            _stop = True
        if menuchoice == 1:
            test_positions(controller)
        if menuchoice == 2:
            update_bank(controller)
        if menuchoice == 3:
            capture_pieces(controller)
        if menuchoice == 4:
            remove_pieces(controller)
        if menuchoice == 5:
            place_queen(controller)
        else:
            __print_menu()


if __name__ == '__main__':
    main()
