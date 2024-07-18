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

path_origin = 'src/visao/extracted_frames'

path_save = "C:/Users/jlc/Documents/GitHub/equipe3-back/src/visao/cropped_pictures"
for img in os.listdir(path_origin):
    img_obj = Image.open(f"{path_origin}/{img}")
    img_obj_cropped = crop_max_square(img_obj)
    print(f'Saving cropped picture {img}_cropped.jpg at path {path_save}...')
    img_obj_cropped.save(f"{path_save}/{img}")

print('DONE!')
