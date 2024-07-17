from PIL import Image
import os



def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))
    
def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))

path_origin = "C:/Users/jlc/Documents/Fabrica de Software 1 e 2/Projeto Damas/[Dataset] - Checkers-20240712T112016Z-001/[Dataset] - Checkers/Extracted_Frames_[DATASET]_Checkers"

path_save = "C:/Users/jlc/Documents/Fabrica de Software 1 e 2/Projeto Damas/[Dataset] - Checkers-20240712T112016Z-001/[Dataset] - Checkers/Cropped_Images_[DATASET]_Checkers"

for img in os.listdir(path_origin):
    img_obj = Image.open(f"{path_origin}/{img}")
    img_obj_cropped = crop_max_square(img_obj)
    img_obj_cropped.save(f"{path_save}/{img}_cropped.jpg")
    