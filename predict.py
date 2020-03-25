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
    # vid = cv2.VideoCapture(0)
    # if not vid.isOpened():
    #     raise IOError("Couldn't open webcam or video")
    # while True:
    #     return_value, frame = vid.read()
    #     image = Image.fromarray(frame)
    #
    #     image = np.asarray(image)
    #     cv2.namedWindow("result", cv2.WINDOW_NORMAL)
    #     cv2.imshow("result", image)
    #     if cv2.waitKey(1) == 27:
    #         break
    yolo.detect_video("logs/1.mp4")

if __name__ == '__main__':
    # Img()  # 图片预测
    View()  # 相机预测
    yolo.close_session()
