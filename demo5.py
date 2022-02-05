# -*- coding: utf-8 -*-
# @File     : demo5.py
# @Author   : Leonard
# @Email    : leoleechn@hotmail.com
# @Software : PyCharm

# 说明： 人脸检测

# 导入第三方模块
import cv2 as cv


# 人脸检测函数
def detect():
    # 灰度转换
    imgGray = cv.cvtColor(imgRead, cv.COLOR_BGR2GRAY)
    faceDetect = cv.CascadeClassifier("C:/Program Files/opencv-4.x/data/haarcascades/haarcascade_frontalface_alt2.xml")
    face = faceDetect.detectMultiScale(imgGray, 1.05, 5, 0, (100, 100), (200, 200))
    for x, y, p, q in face:
        # 绘制矩形
        cv.rectangle(imgRead, (x, y, x + p, y + q), color=(0, 0, 255), thickness=1)
    # 图片展示
    cv.imshow("Result", imgRead)


# 读取图片
imgRead = cv.imread("pic1.jpg")

# 执行函数
detect()

# 退出
while True:
    if ord('q') == cv.waitKey(0):
        break

# 释放内存
cv.destroyAllWindows()
