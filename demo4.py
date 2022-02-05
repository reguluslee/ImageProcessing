# -*- coding: utf-8 -*-
# @File     : demo4.py
# @Author   : Leonard
# @Email    : leoleechn@hotmail.com
# @Software : PyCharm

# 说明： 绘制矩形和圆形

# 导入第三方模块
import cv2 as cv

# 读取图片
picRead = cv.imread("headpic.jpg")

# 确定坐标
x, y, p, q = 100, 100, 100, 100

# 绘制矩形
cv.rectangle(picRead, (x, y, x + p, y + q), color=(0, 0, 255), thickness=1)

# 绘制圆形
cv.circle(picRead, center=(x + p, y + q), radius=100, color=(0, 0, 255), thickness=1)

# 展示图形
cv.imshow("show", picRead)

# 退出
while True:
    if ord('q') == cv.waitKey(0):
        break

# 释放内存
cv.destroyAllWindows()
