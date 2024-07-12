from json import load, dumps
from robots.pose import Pose
from robots.joint import Joint


class MoveBank:

    __instance = None
    filepath = r"src\movebank\positions_kinova.json"

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(
                MoveBank,
                cls).__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        bankdict = self.__load_bank()
        self.__bankdict = bankdict

    def __load_bank(self) -> dict[str, dict[str, list[float]]]:
        with open(MoveBank.filepath, 'r') as file:
            json_object = load(file)
            return json_object

    def __update_bank(self) -> None:
        jsonstr = dumps(self.__bankdict, indent=4, sort_keys=True)
        with open(MoveBank.filepath, 'w') as outfile:
            outfile.write(jsonstr)
            print('File Updated')

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

    def _record_positions(
        self,
        pos_key: str,
        joint: Joint,
        pose: Pose,
    ) -> None:
        self.__bankdict[pos_key] = {
            'cartesian': str(pose.to_list),
            'joints': str(joint.to_list),
        }
        self.__update_bank()
