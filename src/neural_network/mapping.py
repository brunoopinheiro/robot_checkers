from checkers_mapping import mapeadas
from yolo_test import main
class Mapping:

    @staticmethod
    def mapping_bounding_boxes(dict_yolo):
        for casa in mapeadas.values():
            for coordanada in casa:
                for coordanadas_yolo in dict_yolo.values():
                    for coordenada_yolo in coordanadas_yolo:
                        if coordanada >= coordenada_yolo*0.9 and coordanada <= coordanadas_yolo*1.1:
                            return coordanadas_yolo


# Mapping.mapping_bounding_boxes({main()})
# TypeError: unhashable type: 'list'  
    
# if __name__ == "__main__":
#     Mapping.mapping_bounding_boxes({main()})