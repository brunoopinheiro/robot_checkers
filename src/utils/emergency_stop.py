import keyboard
from threading import Thread
from robots.irobot import IRobot


class EmergencyStop:
    """EmergencyStop class to add the option
    to apply a fault to the Kinova Robot in
    operation via terminal."""

    def __init__(
        self,
        robot_: IRobot,
    ) -> None:
        self.__robot = robot_
        self.__thread = None
        self.__stop = False

    def __run_thread(self):
        self.__thread = Thread(
            target=self.__emergency_stop,
        )
        self.__thread.start()

    def __emergency_stop(self):
        while not self.__stop:
            if keyboard.is_pressed('space'):
                self.__robot._apply_emergency_stop()
                self.__robot.fault_state = True
                print('Parada de Emergência Ativada!')
                self.__stop = True

    def initiate_emergency_stop(self):
        self.__run_thread()

    def stop_thread(self):
        self.__stop = True
