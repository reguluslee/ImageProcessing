# -*- coding: utf-8 -*-
# @File     : demo7.py
# @Author   : Leonard
# @Email    : leoleechn@hotmail.com
# @Software : PyCharm

# 说明： 视频检测

# 导入第三方模块
import cv2 as cv


# 人脸检测函数
def detect(value):
    # 灰度转换
    imgGray = cv.cvtColor(value, cv.COLOR_BGR2GRAY)
    faceDetect = cv.CascadeClassifier(
        "C:/Program Files/opencv-4.x/data/haarcascades/haarcascade_frontalface_default.xml")
    face = faceDetect.detectMultiScale(imgGray, 1.01, 5, 0, (10, 10), (100, 100))
    for x, y, p, q in face:
        # 绘制矩形
        cv.rectangle(value, (x, y, x + p, y + q), color=(0, 0, 255), thickness=1)
    # 内容展示
    cv.imshow("Result", value)


# 读取摄像头
# videoRead = cv.VideoCapture(0 + cv.CAP_DSHOW)

# 视频导入
videoRead = cv.VideoCapture("video1.mp4")

# 退出
while True:
    flag, frame = videoRead.read()
    if not flag:
        break
    # 执行函数
    detect(frame)
    # 退出
    if ord('q') == cv.waitKey(0):
        break

# 释放内存
cv.destroyAllWindows()

# 释放摄像头
# videoRead.release()
