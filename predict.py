from yolo import YOLO
import numpy as np
from PIL import Image, ImageFont, ImageDraw

import cv2
yolo = YOLO()


'''
预测图片
'''


def Img():
    while True:
        img = input('Input image filename:')
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image)
            r_image.show()


'''
调用相机实时预测
'''


def View():

    yolo.detect_video("logs/1.mp4")

if __name__ == '__main__':
    Img()  # 图片预测
    # View()  # 相机预测
    yolo.close_session()
