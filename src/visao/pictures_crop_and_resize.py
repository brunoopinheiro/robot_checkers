from PIL import Image
import os
import cv2
import time


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))
    
def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))

path_origin = 'src/visao/dataset_week_2/from_pictures2'

lista_imagens = []
for i in os.listdir(path_origin):
    if os.path.isfile(os.path.join(path_origin, i).replace('\\', '/')):
        lista_imagens.append(i)

path_save1 = "C:/Users/jlc/Documents/GitHub/equipe3-back/src/visao/dataset_week_2/from_pictures2/final_cropped"
for img in lista_imagens:
    img_obj = Image.open(f"{path_origin}/{img}")
    img_obj_cropped = crop_max_square(img_obj)
    print(f'Saving cropped picture {img}_cropped.jpg at path {path_save1}...')
    img_obj_cropped.save(f"{path_save1}/{img}")
    

print('DONE!')

print('it will resize the pictures now...')
time.sleep(2)

path_save2 = "C:/Users/jlc/Documents/GitHub/equipe3-back/src/visao/dataset_week_2/from_pictures2/final_resized2"

for img in os.listdir(path_save1):
    image = cv2.imread(f"{path_save1}/{img}")
    imgResized = cv2.resize(image,(700, 700), interpolation=cv2.INTER_AREA)
    cv2.imwrite(f"{path_save2}/{img}", imgResized)

print('DONE!')
