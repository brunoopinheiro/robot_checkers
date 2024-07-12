from json import load
from robots.pose import Pose
from robots.joint import Joint


class MoveBank:

    filepath = r"src\movebank\positions_kinova.json"

    def __init__(self) -> None:
        bankdict = self.__load_bank()
        self.__bankdict = bankdict

    def __load_bank(self) -> dict[str, dict[str, list[float]]]:
        with open(MoveBank.filepath, 'r') as file:
            json_object = load(file)
            return json_object

    def __str_to_floatlist(self, string: str) -> list[float]:
        values = string[1:-2].split(',')
        return [float(v) for v in values]

    def get_cartesian(self, key: str) -> Pose:
        if key in self.__bankdict:
            str_list = self.__bankdict[key]['cartesian']
            float_list = self.__str_to_floatlist(str_list)
            pose = Pose(*float_list)
            return pose
        else:
            raise KeyError('key not in MoveBank')

    def get_joints(self, key: str) -> Joint:
        if key in self.__bankdict:
            str_list = self.__bankdict[key]['joints']
            float_list = self.__str_to_floatlist(str_list)
            joint = Joint(*float_list)
            return joint
        else:
            raise KeyError('key not in MoveBank')
