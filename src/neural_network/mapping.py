from neural_network.checkers_mapping_kanova import mapeadas
from yolo_test import main

class Mapping:

    @staticmethod
    def mapping_bounding_boxes(dict_yolo):
        coordinates_yolo = dict_yolo.values() # assuming that dict_yolo == {key': [x2', y1', x1', y2'], key'': [x2'', y1'', x1'', y2''], ...} 
        i1 = 0
        for coordinates in mapeadas.values():
            if all([([(coordinate_yolo[k] > coordinates[k]*0.8) or (coordinate_yolo[k] < coordinates[k]*1.2)] for coordinate_yolo in coordinates_yolo)] for k in range(4)):          
                return coordinates_yolo[i1]
            i1 += 1


# if __name__ == "__main__":
#     Mapping.mapping_bounding_boxes({main()})