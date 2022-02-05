# -*- coding: utf-8 -*-
# @File     : demo1.py
# @Author   : Leonard
# @Email    : leoleechn@hotmail.com
# @Software : PyCharm

# 说明： 读取图片

# 导入第三方模块
import cv2 as cv

# 读取图片
picRead = cv.imread("headPic.jpg")

# 展示图片
picShow = cv.imshow("show", picRead)

# 延时
cv.waitKey(0)
