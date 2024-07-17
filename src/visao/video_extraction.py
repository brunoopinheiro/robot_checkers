import cv2
import os
import time




path_video = 'C:/Users/jlc/Documents/Fabrica de Software 1 e 2/Projeto Damas/[Dataset] - Checkers-20240712T112016Z-001/[Dataset] - Checkers/pictures/WIN_20240711_15_50_56_Pro.mp4'

path_images = 'C:/Users/jlc/Documents/Fabrica de Software 1 e 2/Projeto Damas/[Dataset] - Checkers-20240712T112016Z-001/[Dataset] - Checkers/pictures'

video_capture = cv2.VideoCapture(path_video)

os.chdir('C:/Users/jlc/Documents/Fabrica de Software 1 e 2/Projeto Damas/[Dataset] - Checkers-20240712T112016Z-001/[Dataset] - Checkers/pictures')
f = 0
i = 1
while(video_capture.isOpened()):
    ret, frame = video_capture.read()
    if ret:
    
        cv2.imwrite(path_images+f'{i}.jpg'.format(f), frame)
        video_capture.set(1, f)
        i += 1
        f += 30
    else:
        video_capture.release()
        break


